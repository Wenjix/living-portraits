# PLAYER_INTEGRATION.md — wiring `behavior_select` into the player

How `runtime/behavior_select.py` plugs into the live player loop, so a portrait
picks a **new personality-true idle behaviour each cycle**, re-weighted by the
director's mood. This is the consume path for `phineas.json`'s `dynamic` block
(`motion.idle_behaviors` + `dynamic.mood_reweights`).

> **Do not edit `player.py` to try this — the show is running.** This doc is the
> integration contract for whoever next swaps the player's render mode from the
> text/rig dev-view to the `ClipPlayer` (clip + rig) mode. The selector module
> is finished, import-safe, and self-tested; it waits for that swap.

---

## TL;DR (the one call)

Once per **loop boundary** per panel — i.e. the moment a panel's current idle
loop finishes and nothing is queued — ask the selector what to play next:

```python
import behavior_select  # already on sys.path: player.py does sys.path.insert(0, ROOT/"runtime")

pick = behavior_select.pick_behavior(slug, behavior_clips)   # mood read from data/mood.json
if pick is not None:
    clip, behavior_id = pick
    clip_player.play_clip(clip)        # ClipPlayer from runtime/clip_player.py
# else: leave the current loop running (library not baked yet) — never goes black
```

`slug` is the panel's character (`"phineas"` for Panel A, `"seraphina"` for B).
`behavior_clips` is the list of that character's behaviour-loop clips (see
[§ What to pass](#what-to-pass-as-the-clip-source)). `pick_behavior` returns
`(clip, behavior_id)` or `None`.

---

## Where in the loop — the exact call-site

`player.py`'s main loop (today) renders each panel directly via `draw_stage`
(player.py:338–340). That is the **text/rig dev-view**; it does not yet drive
`ClipPlayer`. `behavior_select` belongs to the **clip-mode** render path that
`runtime/clip_player.py` already documents (its module docstring + `ClipPlayer`
usage block). The integration therefore lands when the player adopts a
per-panel `ClipPlayer`. Concretely:

### Step 1 — one `ClipPlayer` per panel, created once before the loop

Right after the fonts/clock are set up (around player.py:314, before
`while running:`), build a player per panel and load the character's behaviour
clips once:

```python
from clip_player import ClipPlayer
from clip_graph  import ClipGraph
import behavior_select

PANEL_CHAR = {"A": "phineas", "B": "seraphina"}   # which portrait lives where

clip_players = {nm: ClipPlayer(nm, rect=pygame.Rect(*PANELS[nm]["rect"]))
                for nm in PANELS}

# The behaviour-loop clips for each character, collected from the baked library
# (see § What to pass). Refresh on manifest mtime, exactly like load_state does
# for stage_state.json — a freshly-baked behaviour appears without a restart.
behavior_clips = {nm: load_behavior_clips(PANEL_CHAR[nm]) for nm in PANELS}
```

### Step 2 — at the loop boundary, pick + play

`ClipPlayer` already exposes the loop boundary as **`ClipPlayer.idle`**
(clip_player.py:505) — `True` when its queue is drained and the active clip
(if any) has finished and is **not** a hold loop. That is the *only* correct
moment to switch behaviours: never mid-clip (the loop contract is
anchor→behaviour→anchor, so a switch mid-loop would tear the seam).

Replace the per-panel render block (player.py:338–340) with:

```python
now = time.monotonic()
dt = min(0.25, max(0.0, now - last_tick)); last_tick = now
screen.fill((0, 0, 0))

if not draw_move(screen, beat, frame, fonts, dt):     # cross-frame walk wins, unchanged
    for nm, panel in PANELS.items():
        cp = clip_players[nm]
        # LOOP BOUNDARY: current behaviour finished -> choose the next one.
        if cp.idle:
            pick = behavior_select.pick_behavior(PANEL_CHAR[nm], behavior_clips[nm])
            if pick is not None:
                clip, behavior_id = pick
                cp.play_clip(clip)
                # (optional) record behavior_id for the liveness/telemetry overlay
        sub = screen.subsurface(pygame.Rect(*panel["rect"]))
        cp.tick(sub)                                  # advances one frame + blits
```

Key points:

- **`if cp.idle:`** is the loop boundary. Because a behaviour clip is `loopable`,
  a freshly-played behaviour keeps `idle == False` until it finishes one full
  loop — so you get exactly one pick per cycle, not one per frame.
- **`pick is None` ⇒ do nothing.** The panel's `ClipPlayer` keeps holding its
  current frame/loop (clip_player.py `_next_frame` never goes black). That is the
  correct degrade when the character's behaviour loops aren't baked yet — the
  portrait holds its anchor instead of erroring. On a *cold* start (no clip ever
  played) `cp.idle` is `True` and `pick` is `None`; seed a hold first (below).
- **Cold-start seed (optional but tidy):** before the loop, give each panel a
  hold so frame 0 isn't blank:
  `cp.play_clip(graph.hold_clip(BASE_POSE))` if you have a base hold, or just let
  the first non-`None` pick populate it.

> Do **not** call `pick_behavior` every frame unconditionally. It is cheap
> (cached JSON read by mtime, a tiny weighted draw) but the *semantics* require
> picking only at a boundary, or the portrait would re-roll its behaviour every
> 1/30 s and never actually play one.

---

## What to pass as the clip source

`pick_behavior(slug, available_clips_or_graph, …)` accepts **any** of:

| You pass… | Selector does… | Use when |
|---|---|---|
| a **list of clips** (the behaviour loops for one character) | filters to that character's behaviour self-loops, keys by tag | **recommended** — see the ClipGraph caveat below |
| a single **clip** | wraps it in a one-element list | one behaviour baked so far |
| a **`ClipGraph`** | reads `.edges()`, filters to behaviour self-loops | only if behaviours live as distinct self-loop edges |
| `None` / empty | → returns `None` | library not baked |

### ClipGraph caveat (why a *list* is recommended)

`runtime/clip_graph.py` stores **one clip per ordered `(from_node, to_node)`
pair** (`add_clip` is last-write-wins). Per `phineas.json`'s
`render_pseudocode`, every idle behaviour is an **anchor self-loop**
(`idle → idle`). Those collide: a single `ClipGraph` can hold only ONE
`idle→idle` edge, so it cannot carry all four of Phineas's behaviours as
`idle→idle`.

So the bake should hand the player the **list** of a character's behaviour-loop
clips (collected as it bakes them), not rely on them all fitting the graph's
`idle→idle` slot. `pick_behavior` is built for exactly this — that is why the
arg is `available_clips_or_graph` and the recommended call passes
`behavior_clips[nm]` (a list). (If a future design instead gives each behaviour
its own pose node, passing the `ClipGraph` works unchanged — the selector
filters `.edges()` by tag either way.)

### How behaviour clips are recognised (the tag contract)

A clip counts as "behaviour *B* for character *C*" when:

1. it is a **held loop** — `from_node == to_node` (an anchor self-loop), or
   failing explicit nodes, `loopable` is truthy; **and**
2. its `tags` identify behaviour *B* — either the **bare id** (`"declaim"`) or a
   namespaced form (`"behavior:declaim"` / `"behaviour:declaim"`); **and**
3. its `tags` either name character *C* via `"character:<slug>"`, or carry **no**
   `character:` tag at all (untagged ⇒ belongs to everyone, fine for a
   single-character clip list). A clip tagged for a *different* slug is rejected.

This matches what `pipeline/orchestrate.py` already stamps
(`["hold", "synthetic", "character:<slug>", …]`); the bake just needs to add the
behaviour id as a tag when it registers each behaviour loop (the
`render_pseudocode` `tags=[behavior.id]`).

### `load_behavior_clips(slug)` — sketch for the player

```python
from clip_graph import ClipGraph, CLIPS_DIR

def load_behavior_clips(slug):
    """Behaviour-loop clips for one character, from the baked manifest.
    Returns a list[Clip]; [] when nothing is baked (pick_behavior -> None)."""
    graph = ClipGraph.load()                  # data/clips/manifest.json
    want = {f"character:{slug}"}
    return [c for c in graph.edges()
            if getattr(c, "from_node", None) == getattr(c, "to_node", None)  # a loop
            and (want & set(c.tags) or not any(t.startswith("character:") for t in c.tags))]
```

(You don't strictly need to pre-filter — `pick_behavior` filters again — but
narrowing to one character keeps the list small and the intent clear. Cache the
result and reload on `manifest.json` mtime, mirroring `load_state`.)

---

## How mood flows in

- The director writes `data/mood.json` → `{"mood": "<word>"}`.
- `pick_behavior` calls `behavior_select.current_mood()` **for you** when you
  don't pass `mood=`. It re-reads the file each call (cheap) and falls back to
  `DEFAULT_MOOD` (`"neutral"`) if the file is missing/malformed — so a mood you
  pick up mid-show changes the *next* behaviour pick, no restart.
- The character's `dynamic.mood_reweights[mood]` multiplies the matching
  behaviours' base weights (`side_eye_rival: 2.5` under `"conspiratorial"`, etc).
  A mood with **no** rule for this character (e.g. the current `data/mood.json` =
  `"bored"`, which Phineas has no entry for) leaves base weights untouched.
- If you already have the mood in hand (e.g. the beat carries it), pass it
  explicitly to skip the file read: `pick_behavior(slug, clips, mood=beat_mood)`.

Observed reweighting on the **real** `phineas.json` (from
`python runtime/behavior_select.py --show phineas`):

```
mood=neutral         declaim=40% wounded_sulk=30% side_eye_rival=20% appraise_viewer=10%
mood=grand           declaim=62% wounded_sulk=19% side_eye_rival=12% appraise_viewer=6%
mood=wounded         declaim=28% wounded_sulk=52% side_eye_rival=14% appraise_viewer=7%
mood=conspiratorial  declaim=31% wounded_sulk=23% side_eye_rival=38% appraise_viewer=8%
mood=vain            declaim=35% wounded_sulk=26% side_eye_rival=17% appraise_viewer=22%
```

Each mood pushes the matching behaviour to the top while keeping the others
present — the portrait's body language shifts with mood without ever becoming a
one-note loop.

---

## Minimal diff sketch (against current `player.py`)

The current loop (player.py:338–340):

```python
        if not draw_move(screen, beat, frame, fonts, dt):
            for nm, panel in PANELS.items():
                draw_stage(screen, nm, panel, beat, frame, fonts)
```

becomes (clip-mode):

```python
        if not draw_move(screen, beat, frame, fonts, dt):
            for nm, panel in PANELS.items():
                cp = clip_players[nm]
                if cp.idle:                                    # loop boundary
                    pick = behavior_select.pick_behavior(PANEL_CHAR[nm], behavior_clips[nm])
                    if pick is not None:
                        cp.play_clip(pick[0])
                cp.tick(screen.subsurface(pygame.Rect(*panel["rect"])))
```

plus the one-time setup from Step 1 (the `clip_players` + `behavior_clips`
dicts + `PANEL_CHAR`) before `while running:`.

`draw_move` (the cross-frame walk) is **untouched** — when a beat carries a
`move`, it still owns the whole frame; behaviour selection only governs the
normal per-panel idle render, exactly where `draw_stage` runs today.

### What stays the same

- `load_state` / the 15-frame mtime poll of `stage_state.json` — unchanged.
- `draw_move` and the cross-frame walk — unchanged.
- The text dev-view (`draw_stage_text`) remains the fallback renderer; you can
  keep `draw_stage` as the cold-start/no-clip path and only switch a panel to
  `ClipPlayer` once `behavior_clips[nm]` is non-empty.

---

## Contract recap (what the module guarantees)

- **Import-safe** with neither `pygame`, `torch`, `numpy`, nor `cv2` installed
  (verified by import-blocking those four and importing the module). No file
  I/O, no clock, no RNG seeding at import. The only hard dep is the stdlib;
  `clip_graph`/`Clip` are duck-typed, never imported at module top level.
- **Never raises** on a missing/malformed character JSON or `data/mood.json` —
  returns `None` / safe defaults so a render frame can't crash on it.
- **`pick_behavior(...) is None`** ⇒ "no behaviour to play this cycle" ⇒ the
  player keeps its current loop. This is the not-yet-baked degrade.
- **Mood** is read from `data/mood.json` each call (or pass `mood=`); falls back
  to `"neutral"` (no reweight) when absent/unknown.
- Pass a `random.Random` via `rng=` for a reproducible/seeded show; otherwise the
  module's own RNG varies picks across cycles.

Verify any time: `python runtime/behavior_select.py --selftest` (synthetic math,
no deps) and `python runtime/behavior_select.py --show phineas` (real JSON).

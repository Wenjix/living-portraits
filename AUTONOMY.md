# Living Portraits — Autonomy Layer

Giving the portraits a **heartbeat**: an LLM (GLM-4.5-air, via the IC z.ai gateway)
that lets each character lead its own life — by day it decides *where it wants to go*
in the video graph, and the body walks there step by step; later it will *grow its own
map*, writing Midjourney prompts to generate new poses it wishes it had.

This is the Track-1 (a "stage manager" brain) ↔ Track-2 (the MJ video graph) fusion.
It does **not** replace anything: it layers on top of the existing random walk and the
circadian bedtime routine, and degrades back to them whenever the brain is absent.

---

## The core idea

The walker is already a **goal-seeking state machine**. `runtime/circadian.py:decide()`
is a hardcoded goal-seeker: at night it picks the goal "sleep" and forces the walker one
transition at a time toward it. The autonomy layer adds a **second, smarter goal-setter**
with the *same contract* — an LLM that picks an arbitrary goal pose by day — plus a
**pathfinder** so the walk can reach any pose, not just a scripted chain.

### Precedence (who drives the body)

```
circadian (the clock)   >   mind (the LLM's intent)   >   random walk (fallback)
   night → go to bed          day → pursue the goal        no goal / stale / brain off
```

`_preview_graph.py:_pick()` consults them in that order. The mind only ever *forces* a
step or says *"none"* (hand back). It never strands the walk.

---

## Components

| Piece | File | Role | Runs in |
|---|---|---|---|
| **Pathfinder** | `runtime/pathfind.py` | BFS over transition edges → the next hop toward a goal | walker (per pick) |
| **Mind** | `runtime/mind.py` | `decide()` sibling of circadian; reads intent, forces steps toward the goal, pins idles at it | walker (per pick) |
| **LLM client** | `director/llm.py` | GLM via the IC z.ai gateway (Anthropic Messages shape, stdlib urllib) | heartbeat |
| **Heartbeat** | `director/heartbeat.py` | the slow brain: sense → think (GLM) → write intent + journal | `lp-mind` task |
| **Walker hook** | `_preview_graph.py` | consults the mind by day; publishes its pose; `--mind` flag | `lp-preview` task |

Everything in `runtime/` is pure + stdlib + import-safe (it's imported by the 10 fps render
loop). All network / LLM lives in `director/`.

### Data flow & file contracts (single-writer, no races)

```
 lp-mind (heartbeat, ~4 min)                 lp-preview (walker, 10 fps)
 ───────────────────────────                 ───────────────────────────
 read  data/mind/pose/<char>.json  ◄──────── write (on pose change, atomic)
 read  data/mind/journal/<char>.jsonl
 GLM → choose goal
 write data/mind/intent.json       ────────► read (mtime-cached, per pick)
 append journal/<char>.jsonl                 mind.decide() → pathfind → force next step
```

- `data/mind/intent.json` — **heartbeat is the sole writer**; walker only reads.
  `{ "characters": { "phineas": { "goal": "phineas:glower", "set_at": <epoch> }, ... } }`
- `data/mind/pose/<char>.json` — **each panel's walker is the sole writer** (per-character
  path → no cross-panel race); heartbeat reads. `{ node, dwell, last_label, updated }`
- `data/mind/journal/<char>.jsonl` — heartbeat appends one line per decision (the character's
  inner monologue, fed back as context next tick — this is what makes it read as a *life*).
- All writes are atomic (tmp + `os.replace`). All of `data/` is gitignored.

**Staleness guard:** a goal older than `mind.DEFAULT_MAX_AGE` (30 min) is ignored. So if the
heartbeat dies or gets blocked, the portraits fall back to the lively random walk — never
frozen at a stale goal.

---

## How a "want" becomes motion

GLM says `goal = phineas:glower`. The heartbeat writes it to `intent.json`. On the walker's
next pick: circadian says daytime → hand off; `mind.decide()` runs
`pathfind.next_step(anchor → glower)` → forces the `a2g` transition; it plays once (~6 s) and
lands on `glower`; next pick forces the next hop if any, else (at the goal) **pins** on
`glower`'s idle loops. The character has visibly *walked there* and now *dwells* on what it
wanted — until the heartbeat picks a new goal. The graph's `validate()` already guarantees
every pose is reachable and can return, so the walk never strands.

---

## The self — the generic system prompt

Every portrait carries one base prompt (`heartbeat.BASE_SYSTEM`) so it **always knows what it
is, who it is, and what it does**: a self-aware living painting on an LED panel at Immersive
Commons (Floor 10, Frontier Tower SF); it knows people watch it; it hangs beside other
portraits it has opinions about; its existence is a graph of poses joined by transitions; each
tick it chooses a pose to walk to and dwell in; it has moods, boredom, whims, and a life
between glances. The per-character identity (name, essence, personality, catchphrases) is read
from `prompts/characters/<char>.json` and appended under a `## Who you are` heading. So Phineas
chooses melodrama, MAXX chooses flexing — in character.

---

## The brain — z.ai / GLM

- **Model:** `glm-4.5-air` (fast + cheap, right for a per-tick decision; `glm-4.6` available
  for richer prose like Phase-2 generation prompts).
- **Path:** `director/llm.py` → `POST https://immersivecommons13.tail5da903.ts.net/v1/messages`
  (Anthropic Messages shape) with an IC-minted `agt_` proxy key. The gateway holds the real
  Z.ai org key and meters a weekly token budget; our key carries **zero IC tool scopes**, so
  it's safe on hil. See memory `project_zai_gateway`.
- **Key:** minted via IC MCP (`ic_request_zai_key` → `ic_admin_approve_key_request`), **5×
  tier = 50 M tokens/week, resets Mondays, never expires.** Resolved at runtime from, in order:
  `$ZAI_AGENT_KEY` / `$ANTHROPIC_AUTH_TOKEN` → `~/.config/living-portraits/zai_key.txt` →
  `<project>/data/mind/zai_key.txt`. Never committed.
- **Reachability:** validated live from a `tag:personal` host. hil is also `tag:personal`, so
  it reaches the tailnet `serve` endpoint. (If the gateway later moves to public Funnel-only,
  nothing changes — same URL.)

---

## Runbook

**Heartbeat (dev / test):**
```
python director/heartbeat.py --once --dry-run            # one decision, printed, writes nothing
python director/heartbeat.py --once --chars phineas,maxx # one real tick (writes intent + journal)
python director/heartbeat.py --chars phineas,maxx        # the live loop (~4 min cadence)
```

**Walker with the mind on:**
```
pythonw _preview_graph.py --a phineas --b maxx --mind    # consult intent.json by day
```
Without `--mind` the walker is the current pure random walk (production default, unchanged).

**On hil (Phase 0 deploy — not yet done):**
1. Put the key at `C:\living-portraits\data\mind\zai_key.txt` (gitignored; avoids S4U profile
   ambiguity for `~/.config`).
2. Confirm reachability: `python director/heartbeat.py --once --dry-run` should print a GLM
   decision (proves hil → ic13 over the tailnet).
3. New task **`lp-mind`** → `pythonw director\heartbeat.py --chars phineas,maxx --quiet`,
   `WorkingDirectory=C:\living-portraits`, S4U (no window needed), AtLogon + RestartCount.
   **Watch the `Set-ScheduledTask -Action` WorkingDirectory-wipe trap** (memory
   `project_living_portraits`).
4. Re-point **`lp-preview`** to pass `--mind` (same `Set-ScheduledTask` care).
5. Screenshot via `lp-shot` to confirm the panels follow chosen goals.

---

## Phases

- **Phase 0 — capability on hil.** MJ session + deps (`midjourney/` client, `curl_cffi`,
  `ffmpeg`) and the z.ai key on hil; confirm hil→ic13 reachability; stand up `lp-mind`; enable
  `--mind`. *(MJ deps only strictly needed for Phase 2.)*
- **Phase 1 — the brain over existing poses.** ✅ **BUILT** (this doc). pathfind + mind +
  heartbeat + walker hook + 14 tests + live-validated LLM. GLM picks among existing poses; the
  graph walks there. No MJ, no moderation risk.
- **Phase 2 — autonomous pose growth.** The mind may request a NEW pose (a label + `/imagine`
  still prompt + motion prompts, the `NODE_SPECS`/`EDGE_SPECS` shape). An `lp-gen` worker runs
  the existing MJ pipeline (imagine → pick → video → gif → `video_graph.py build`), then the
  walker hot-reloads the graph. Start human-gated, then full-auto behind a daily budget.
- **Phase 3 — the life.** Persistent moods, character relationships (Phineas glowers when
  Seraphina's panel is bright), the GodComplex F5 floor-context seam (riff on who's in the
  room), eventually F4 voice.

---

## Honest risks (carry into Phase 2)

1. **MJ moderation in an unattended loop = the #1 risk.** An LLM-written prompt with a
   body/clothing word trips MJ's filter → temp block, and *retrying during a block extends it*.
   `lp-gen` MUST lint prompts (strip body/garment terms, MJ-safe negatives) and respect the
   block's `until` timestamp. Fail safe = stop generating, keep walking existing poses.
   (Memory `project_living_portraits` MJ-moderation gotcha; `feedback_mj_oref_ow_suppresses_wardrobe`.)
2. **Identity drift.** Generating a pose from a generated still repeatedly morphs the face.
   Anchor every `--oref` to the *original canonical* still, never the latest.
3. **Graph hot-reload.** The walker loads `video_graph.json` once at startup. Phase 2 needs
   mtime-watch reload (don't reload mid-transition). `video_graph.save()` must become atomic.
4. **Budgets = the "set logic."** Cap new poses/day/character; rate-step the heartbeat by state
   (fast awake, slow asleep — already implemented). Log what's dropped; no silent caps.
5. **hil task gotchas.** S4U vs session-1, the pythonw shim-pair, the `Set-ScheduledTask
   -Action` WorkingDirectory wipe.
6. **Coherence.** Without the journal, LLM picks read as dressed-up randomness. The persistent
   journal is what makes it a continuous *life*.

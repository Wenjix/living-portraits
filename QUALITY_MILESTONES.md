# Living Portraits — Quality Milestones (recursive-loop backlog)

A FINITE, curated list of small genuine quality improvements to what we already have. No new
features, no new deps, no new systems.

**Loop rule.** Each iteration: do ONLY the next unchecked milestone — the smallest change that
genuinely improves quality, minimal code, no bloat. Verify on hil (deploy the changed file(s) +
a concrete check) and **confirm the panels still paint**; if a change breaks the player, revert
it. Commit one atomic commit. Check the item off with a one-line result. **Exactly one milestone
per iteration.** When every box is checked, **STOP — do not invent new milestones** (that is the
bloat we are avoiding).

---

- [x] **M1 — Atomic graph save.** `runtime/video_graph.py:save()` writes the JSON directly. Phase 2
  rebuilds the graph every ~20 min while the player hot-reloads it on mtime change → a torn read is
  possible (and more likely the bigger the graph gets). Make `save()` write tmp + `os.replace`, like
  the other atomic writers in the project. **Done when:** save uses temp+rename; `video_graph.py build`
  still works; player healthy after deploy.
  **✓ 2026-06-07:** `save()` writes `.tmp` then `Path.replace` (atomic; no new import). hil build clean —
  20 nodes/344 edges walk-safe, valid JSON readback, no `.tmp` leftover; player kept painting (`_preview.log` 33s).

- [x] **M2 — The brain can tell how long it has lingered.** The walker publishes `pose/<char>.json`
  only on a pose CHANGE, so `dwell` is ~always 0 and the heartbeat's "you have lingered N moments"
  is dead — the brain can't decide "I've been here a while, move on." Publish the live dwell (or a
  timestamp the heartbeat turns into elapsed). **Done when:** `dwell` advances while a character
  idles; the heartbeat prompt shows a real lingered count.
  **✓ 2026-06-07:** `_publish_pose` now re-publishes on node OR dwell change (added `_pub_dwell` tracker;
  ~1 tiny atomic write per ~6s idle). Heartbeat already reads `dwell` (sole consumer) — no change there.
  Proven headless on hil (SDL dummy, isolated pose dir): published dwell series `[0,1,…,14]` while the
  node held at `maxx:idle`; old code published `[0]` only. NOTE: live-display confirm was blocked by a
  fullscreen Steam game clean-exiting the player on sight (pre-existing crash-loop, environmental — NOT
  this change; watchdog shows DOWN every 3 min since 20:28, before deploy). Surfaced to Ray separately.

- [x] **M3 — Keep the pose vocabulary clean (anti-bloat).** Phase 2 can add up to 15 poses/char/day;
  near-duplicate poses would dilute the walk and bloat the graph. In `propose_pose`, reject a proposal
  whose label/still is too close to an existing pose (cheap token-overlap check). **Done when:** a
  near-duplicate proposal is skipped + logged; no redundant node enters the graph.
  **✓ 2026-06-07:** added `_is_duplicate` (word-token subset OR Jaccard>=0.5 vs existing + pending pose
  labels); `propose_pose` skips + logs `anti-dup` before the queue. Proven on hil: 5/5 unit cases +
  integration (dup skipped, 0 written with writes ON; genuinely-new label still accepted) = PROOF PASS.
  Live in lp-mind (`--propose-every 8`) after restart; player kept painting throughout.

- [x] **M4 — Resilient player (survives display theft).** Verifying M2 revealed the REAL dark-panel
  cause: a fullscreen Steam game DESTROYS the player's window -> pygame QUIT -> the player *clean-exited*
  (so the original "re-assert topmost" couldn't help — you can't keep an exited process on top). Ray's
  call (2026-06-07): make the player resilient instead. Now (1) QUIT is ignored — only the operator's
  ESC exits; (2) a lost display (`pygame.error`) is recovered in-loop — drop gif caches, wait, rebuild
  the window -> panels return the instant the screen is free, same process persists (watchdog sees it UP,
  no restart churn); (3) topmost re-asserted every ~10s with `SWP_NOACTIVATE` (folds in the original M4
  intent without stealing focus from the game). **Done when:** player ignores QUIT + recovers a lost
  display + re-pins topmost; panels paint after deploy.
  **✓ 2026-06-07:** shipped. Live on hil: PID alive 2m+ painting + walking, dwell advancing, ZERO error
  noise. Recovery mechanics proven headless (quit->init->set_mode->flip + gif reload = RECOVERY-CYCLE-OK);
  QUIT-ignore by construction. (Real game-theft survival not exercisable while the display is free; the
  3-min watchdog remains the backstop.)

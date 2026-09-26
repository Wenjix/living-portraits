# Living Portraits — the model stack, and why most of it should not be upgraded

**Verified as of 2026-09-10.** Every version claim below was checked against primary sources on that
date; the claims that could *not* be confirmed are listed in §6 and must not be quoted as fact. Model
versions move fast — re-run §7 before acting on anything here.

This file exists because "it's an older project, let's update the models" is the obvious conclusion
and it is mostly **wrong** for this system. Three of the tempting upgrades are actively harmful, one
was already attempted and broke production, and the highest-value changes on the list are bug fixes
rather than version bumps.

---

## 1. What we actually run

### Live path — a change here shows up on the wall

| Model | Pinned at | Role |
|---|---|---|
| **glm-5.1** | `director/llm.py:58` `DEFAULT_MODEL` | per-tick goal decisions. The IC gateway remaps 5.1 → 5.2-class |
| **glm-5.1** | `director/heartbeat.py:82` `PROSE_MODEL` | creative authorship (Phase-2 pose proposals) |
| **glm-4.5-air** | `director/voice_eval.py:47` `JUDGE_MODEL` | cheap judge, `max_tokens=8` |
| **qwen3:8b** | `director/llm.py:71` `OLLAMA_MODEL` | local fallback brain (Ollama) |
| **qwen3:8b** | `director/stage_manager.py:25` `MODEL` | stage manager / dialogue beats — **always local** |
| **qwen2.5vl:7b** | `pipeline/verify.py:63` `OLLAMA_VL_MODEL` | vision register check (soft gate) |
| **qwen3:8b** | `pipeline/verify.py:64` `OLLAMA_TEXT_MODEL` | text register check |
| **Midjourney V7** | `pipeline/autogen.py:82` `IMAGINE_VERSION`, `:78` `OREF_WEIGHT=160` | every pose still and every transition clip |
| **Piper** / **Kokoro** | `pipeline/tts.py` | speech. Import-guarded; **neither installed**, `ENGINE is None` |

The brain is z.ai-first with automatic failover to local Ollama, plus `LP_LLM_LOCAL_FIRST=1` (local
primary) and `LP_LLM_LOCAL_ONLY=1` (fully air-gapped). See `director/llm.py:75-80`.

### Dormant path — has never executed in production

SDXL 1.0 + InstantID + IP-Adapter + InsightFace (`pipeline/_gen_anchor_sdxl.py`) · AnimateDiff · SVD ·
LTX-Video 0.9.7-dev · LivePortrait (`pipeline/_bake*.py`) · SAM 3.1 (`pipeline/segment.py`).

The shipped 59-node / 500-edge graph is **Midjourney footage**, not local. These three parallel
local-generation stacks were superseded and none of them has ever produced a frame that reached the wall.

### Hardware, because it decides most of this

The GPU is an **RTX 2080 Ti, 11 GB, on supercommons2** (`MIGRATION.md:10`, `pipeline/generate.py:7`) —
shared with the Ollama models and the catalog. "hil" is the unattended *deploy* host
(`research/FACTS.md` `[LP-DEPLOY]`); confirm which box before any `ollama pull`.

Turing (sm_75) has **no BF16 compute**. Every 2026 open-weight DiT ships BF16 weights, and FP16
inference on them produces black frames (NaN latents). That is a numerical wall, not a capacity
wall — no quantization fixes it.

---

## 2. The upgrade that was already tried, and broke

`pipeline/autogen.py:79-81` records it verbatim:

> `--oref` (omni-reference) requires MJ v7. The account default moved to v8.1, which rejects `--oref`
> (``--oref` is not compatible with `--version 8.1``) → every still submit failed
> (**166 dead proposals, 2026-06-17**). Pin v7 so `--oref` works again.

**`IMAGINE_VERSION = "7"` is a fix for a production outage, not staleness.** Midjourney is on V8.2
(default since 2026-07-24), and `--oref` / `--ow` remain V7-only — the Omni Reference docs carry an
explicit "not supported in V8.2" flag.

Two further consequences:

- `IMAGINE_MODE = "relax"` (`autogen.py:86`) is a **hard requirement of the identity lock**, not a cost
  optimization. `--oref` is documented as incompatible with Fast Mode, Draft Mode, Conversational Mode
  and `--q 4`. A plan change or timeout tweak that silently flips it breaks identity.
- Keep the explicit `--v 7` in the prompt string at `:323`. Never rely on the account default; that is
  exactly how the June outage happened.

`--ow 160` needs no adjustment (documented range 1–1000, default 100, guidance "keep below 400").

---

## 3. Worth doing

Ranked. Note that #1 and #4 are **bugs**, not upgrades.

### 3.1 The `tts.py` landmine — 5 minutes, zero behaviour change today

`pipeline/tts.py:171` calls the **piper-tts 1.2.0 (2023)** signature:

```python
voice.synthesize(text, wf, length_scale=1.0 / max(rate, 0.1))
```

Current piper is 1.8.0, where that signature is gone. The import guard at `tts.py:38` still *succeeds*,
so the day anyone `pip install`s piper, `ENGINE` flips to `"piper"`, **bypasses the safe fallback**, and
raises `TypeError` on the first aside — on the wall. Replace with `synthesize_wav(...,
syn_config=SynthesisConfig(length_scale=...))`; `PiperVoice.load` at `:169` is still valid.

### 3.2 Local brain `qwen3:8b` → `qwen3.5:9b` — the highest real value

6.6 GB Q4_K_M, 9.65B params, 256K context, Apache 2.0. The newest *official* Qwen with a tier that fits
11 GB (qwen3.6 ships 27b/35b only). This outranks the GLM question because **the stage manager is always
local** — every dialogue beat comes from this model whether or not z.ai is up.

Three things must ride along in the same commit:

1. `director/stage_manager.py:48` — `/no_think` is glued directly onto the JSON contract string
   (`'"bridge":"<short note or null>"}\n/no_think'`). Qwen3.5 does not support that soft switch, so it
   becomes literal prompt garbage attached to the schema spec. Also at `director/llm.py:171`.
   `"think": False` (already set) is the correct model-agnostic lever.
2. `director/stage_manager.py:25` — `MODEL` is **hardcoded with no env read**, unlike `llm.py:71`.
   Make both track one variable.
3. **`grep -rn num_ctx director/ pipeline/` returns zero hits.** Going from qwen3's 40K window to
   qwen3.5's 256K unpinned is a KV-cache blowup on a shared card. Add `"num_ctx": 4096`.

**Gate:** the incumbent was verified in-character on the box (Phineas/MAXX/Seraphina distinct + valid
JSON, ~9–14s warm). The replacement gets the same verification or it does not ship. Watch
`LP_OLLAMA_KEEP_ALIVE=30m` pinning a bigger model's VRAM.

### 3.3 Real lip-sync — the actual prize

Today the mouth timing is **fabricated**: `_phonemize()` maps *letters* to visemes via `_CHAR_VISEME`,
and `SECS_PER_PHONEME = 0.085` (`tts.py:100`) spaces them evenly. Even the "real" Piper path rescales
that fake even track to the wav duration.

Piper ≥1.5 returns actual alignments: `synthesize_wav(..., include_alignments=True)` → per-phoneme
`num_samples`. For a mouth rig on a public wall this is the biggest quality win available, with no GPU
and no new vendor. Keep `_phonemize()` / `synthetic_visemes()` as the no-engine fallback.

**The gotcha:** `_hash()` at `tts.py:103` keys on `sha256(text + "|" + voice)` only — not the engine, not
the track format. Old fabricated tracks and new real ones are indistinguishable by filename and will be
served side by side. Add the engine + a format version to the hash, or wipe `data/tts/` **before** the
first real-alignment synth.

License note: `piper-tts` is now GPL-3.0-or-later (archived `rhasspy/piper` was MIT). This repo is MIT
and takes it as an optional, non-redistributed runtime dep. `rhasspy/piper-voices` is MIT, so
`sherpa-onnx` (Apache-2.0) runs the identical `.onnx` voices with no GPL in the tree — but see §6, we did
not confirm sherpa-onnx exposes per-phoneme durations.

### 3.4 Vision verifier `qwen2.5vl:7b` → `qwen3.5:4b` — one line

`pipeline/verify.py:63`. **Take the 4b, not the 9b:** MMMU 77.6 vs 78.4 (0.8 points) for half the
weights (3.4 GB vs 6.6 GB). Against Qwen2.5-VL-7B's 58.6 either is a ~19-point jump. `register()` is a
*soft* gate that already degrades open by design (`pipeline/VERIFY_CONTRACT.md:79-90`), on a card the
repo documents as contended — 3.2 GB for 0.8 points is a bad trade there. Bonus: `OLLAMA_TIMEOUT = 20`
(`verify.py:65`) surfaces a slow VLM as `register: SKIPPED (ollama unreachable)`, a timeout wearing a
dead-daemon costume; the 4b reduces that exposure.

Do **not** bundle this with collapsing the text model — `qwen3:8b` is pinned in three code files plus
~10 docs, and collapsing them puts the heartbeat's strict-JSON contract on an untested model.

### 3.5 `segment.py` dtype bug — 3 lines

`pipeline/segment.py:168` unconditionally enters `torch.autocast(device_type="cuda",
dtype=torch.bfloat16)` whenever CUDA is present. Turing has no native BF16. Gate on capability:

```python
_dt = torch.bfloat16 if torch.cuda.get_device_capability()[0] >= 8 else torch.float16
```

An explicit capability check is the documented workaround precisely because
`torch.cuda.is_bf16_supported()` now reports Turing as compatible — so on current PyTorch this does not
raise, it runs emulated and slow. Also: the per-prompt `except Exception: continue` discards its
exception, making a dtype error, a missing HF credential (`facebook/sam3.1` is gated) and a genuinely
empty mask indistinguishable. Log it.

Diagnose first: `python pipeline/segment.py` already prints `SAM available: <bool> (<err>)` and
`backend=<sam|grabcut>`.

---

## 4. Do not do this

- **Do not migrate Midjourney V7 → V8.2.** See §2. It changes the base model *and* the identity
  mechanism at once (one anchor + a numeric `--ow` becomes up to four references with no documented
  identity-weight parameter), against 59 nodes and 500 edges of shipped footage. `AUTONOMY.md:170-171`
  cannot save you: anchoring to the canonical still defends against drift *within* one model; the same
  anchor reconstructed by a different model through a different mechanism resolves to a different face.
  And because every edge is a real clip between a start and an end frame, a V7-still → V8.2-still
  transition renders the face change **as visible morphing, in motion, on a public wall.**
- **Do not ship glm-5.1 → glm-5.3.** The gateway already resolves 5.1 to 5.2-class. GLM-5.3 shipped
  *without retraining the base model* — same base as 5.2, gains entirely from post-training RL, and the
  measured delta is agentic coding and exploit discovery (Terminal-Bench 3.0 4.6 → 28.3). The heartbeat
  reads 5 journal lines and emits 4 fields; none of that delta applies. Cost goes **up**: identical
  per-token price but reasoning cannot be disabled and `reasoning_effort` defaults to max, billed as
  output at $4.40/M across ~360 ticks/character/day. If it is ever swapped, the migration notice is
  mandatory in the same commit — `director/llm.py:110-116` currently sends no `thinking` field, and
  `heartbeat.py:365`'s `max_tokens=300` guarantees an empty-text return once reasoning tokens count.
- **Leave `director/voice_eval.py:47` alone.** `JUDGE_MODEL = "glm-4.5-air"` at `max_tokens=8` is not
  the default model and moving it to 5.3 would break it instantly.
- **Do not self-host `glm-5.3-flash`.** MIT weights, yes — and ~328 GB FP8 across 62 shards (~643 GB
  BF16). Three orders of magnitude off an 11 GB card. On Ollama it exists only as `:cloud`.
- **Do not revive SDXL + InstantID on this box.** The blocker is numerical, not capacity. Do not let a
  GGUF quant defeat the "13 GB > 11 GB" argument and then ship black frames.
- **Do not start a 2026 local-video migration.** LTX-2.5 official minimum 32 GB; Wan 14B wants 80 GB;
  FramePack states "GTX 10XX/20XX are not tested"; SageAttention needs Ampere. FlashPortrait's ~10 GB
  offload figure technically fits and still leaves nothing for the Ollama brains.
- **Do not adopt anything without a license.** `ornith-1.5:9b` (fits, newer, Ollama page names no
  license and no lab) and EditaLive ("academic research only") are both disqualified for an open-source
  engine on a permanent public installation.
- **Do not `pip install chatterbox-tts` expecting nano or flash.** The 0.1.7 wheel contains zero
  references to either, and its pins (`torch==2.6.0`, `transformers==5.2.0`) will fight the gen stack.
- **SAM needs no upgrade.** `download_ckpt_from_hf(version="sam3.1")` is already current; no SAM 3.2 or
  4 exists. There is only the dtype bug in §3.5.

---

## 5. One-way doors

1. **The art generator.** The only genuinely irreversible decision here. The moment a pose rendered by
   a different generator lands in `video_graph.json`, the graph is hybrid and the face is inconsistent
   *in motion*. There is no partial migration. If it ever becomes necessary: re-render the canonical
   anchors offline → human A/B against the originals → if the face moved, stop → otherwise re-render
   **all** 59 nodes and **all** 500 edges → cut over atomically. Before estimating that, resolve the
   blocker: the `midjourney` Python client used at `autogen.py:315-340` is third-party, **not vendored,
   not in any requirements file**, and whether it supports multi-image reference submission is unknown.
   Treat V7 + `--oref` as **supported-but-terminal**: `--cref`/`--cw` (the mechanism `--oref` replaced)
   is already in Legacy Features, and `--ow` has quietly dropped out of the current Parameter List.
2. **The TTS cache.** Wipe or version `data/tts/` before the first real-alignment synth, not after.
3. **SVD 1.1's gated repo.** Accepting Stability's terms is an account-level action with a $1M revenue
   threshold attached. The path is dormant — just don't.
4. **Mixed mattes.** Re-segmenting part of the graph is irreversible without a full re-bake, because you
   cannot tell from the artifact which backend produced it. Do not re-bake a subset to "upgrade"
   segmentation.

Everything in §3 is a `git revert` plus at most one `ollama pull`. `qwen3:8b` and `qwen2.5vl:7b` are both
still published with no deprecation notice.

---

## 6. What we could NOT verify — do not quote as fact

**Blocking the GLM decision:**

- **Whether `glm-5.3` works over the Anthropic Messages shape.** Direct first-party contradiction: the
  official glm-5.3 overview page lists "Anthropic Message Protocol" among its three protocols, while
  GitHub issue `can1357/oh-my-pi#10539` (closed) states z.ai's docs describe the Anthropic-compat proxy
  as supporting models only *through GLM-5.1*. z.ai's own Claude Code guide still maps OPUS/SONNET →
  GLM-4.7, naming no GLM-5.x id. **Unresolved. Settle with one curl to `{gateway}/v1/messages`.**
- **`glm-5.3-flash` over Messages** — its official page lists only Chat Completions. Confirmed-negative-ish.
- Native `json_object` mode is **not** a provider guarantee on the Messages API (it relies on prompt
  conventions there). Mild impact — `complete_json()` never sends `response_format` and `_extract_json()`
  already handles fences — but the strict `{goal, mood, urgency, reason}` contract rests on prompting
  plus that parser, not on the vendor.
- IC's `agt_` key carries a **model allow-list** (`llm.py:5`) and `base_url()` points at the IC tailnet
  host, not `api.z.ai`. Whatever z.ai supports, IC must also allow. That is an ask, not a code change.

**Affecting the local-brain swap:**

- **Qwen3.5-9B's thinking default** — the HF card says on, Unsloth's docs say off for the 9B. Both cannot
  be right. `"think": false` should override either way; confirm before quoting a latency number.
- **Ollama throughput on the qwen3.5 architecture** — `ollama/ollama#14579` reports 15–20 tok/s vs ~100
  on llama.cpp, but **specifically for the 35B-A3B MoE**. Whether the dense 9B shares that gap is
  untested. Minutes of latency tolerance absorbs it either way; don't publish an unmeasured number.
- **Qwen3-VL-8B vs Qwen3.5-9B per-size on MMMU** — no head-to-head found. Vendor evidence is
  flagship-only. Do not repeat it as a small-model claim.
- **Gemma 4 12B's release date and Apache-2.0 terms** — the "3 Jun 2026" date is not on Google's card,
  and Apache 2.0 would be a departure from Gemma's historical custom terms. Verify before relying on it.

**Frequently misquoted, affects nothing here:**

- **The Midjourney video model version.** The official Video article names no version anywhere; the last
  officially named video model is V1 (2025-06-18). Do not record "video is V1" as fact. It happens not to
  matter — video identity comes entirely from the input frames — but there is no way to pin it, so if
  Midjourney silently reships it, transition motion quality could shift with no version string changing.
- **SAM 3.1's parameter count / weight size.** The ~848M / ~3.4 GB figures are secondary-source only;
  Meta's release notes, blog and HF card all state no parameter count. Also, the 16–24 GB "comfort floor"
  that circulates for SAM describes the **video tracking** path — `segment.py` only uses single-image.
- **Which PyTorch branch this box is on** for the bf16 autocast (§3.5). Undeterminable — there is no
  `requirements.txt` and no torch pin anywhere in the repo.
- **LTX-2.5's exact release date** (2026-08-11) rests on third-party coverage. The model, the 22B size
  and the license are first-party. (The HF org lists `LTX-2.5-Diffusers` at 19B; quote 22B.)
- **"Qwen-Image 2.0, 7B, February 2026"** appears confidently on SEO sites. The official README announces
  2.0 with no weights and the Qwen HF org has no such repo. That 7B figure has no primary source.
- **"Wan 3.0 open weights, April 2026"** traces to a single LinkedIn post. Wan 3.0 is real but API-only
  public beta since 2026-08-06, with no weights anywhere.
- **`sherpa-onnx` per-phoneme alignment support** — unverified, and it decides whether the GPL-avoidance
  route can also deliver real lip-sync (§3.3).

---

## 7. How to re-verify

This file is a snapshot. Before acting on any version claim:

```
ollama show qwen3.5:9b            # local brain candidate: does the tag exist, what size
ollama show qwen3.5:4b            # VLM candidate
curl {ZAI_GATEWAY}/v1/messages -d '{"model":"glm-5.3","max_tokens":50,...}'   # §6 blocker
python pipeline/segment.py        # prints SAM availability + backend
grep -rn num_ctx director/ pipeline/                                          # still zero?
```

Midjourney's current version and `--oref` compatibility must be read off the official Parameter List
and the Omni Reference article — not off a changelog summary, and not off this file.

---

*Researched 2026-09-10 by a verified multi-agent sweep (8 model families, each version claim
independently checked by a second pass hunting hallucinated version numbers). Repo line numbers and the
graph statistics in this file were confirmed against the working tree on the same date.*

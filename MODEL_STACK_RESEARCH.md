# Living Portraits — the Midjourney exit, and the open model questions

**Researched 2026-09-23 to 2026-09-24.** This is the follow-up to `MODEL_STACK.md` (2026-09-10). It answers the questions that file left open in §5 and §6, plus the Midjourney exit strategy. Nothing here re-opens what `MODEL_STACK.md` already settled:
- MJ V7 → V8.2 on the live pin
- glm-5.1 → 5.3
- the dormant local generation stacks
- SAM

**How to read it.**
- Every claim traces to a primary source that was re-opened and checked on the dates above.
- Confidence levels:
  - **high**: several first-party sources agree and were re-checked.
  - **medium**: one first-party source.
  - **low**: inference or partial support.
  - **unknown**: could not be established.
- Where two first-party sources contradict each other, both are reported and the contradiction is left **unresolved**.
- The full per-track answers, every numbered source (with first-party or secondary status and dates) and the verifier output are in [`research/MODEL_STACK_EVIDENCE.md`](research/MODEL_STACK_EVIDENCE.md).
- Everything that must not be repeated as fact is in §9, **DO NOT QUOTE**.

---

## 0. Read this first: the premise may already be out of date

The brief assumes Midjourney V7 + `--oref` is the live art pipeline and that its retirement is the future risk. The project's own upstream says that risk has **already happened**, for a different reason.

**This fork and upstream are different repos.**
- This repo is `Wenjix/living-portraits`, MIT, a fork of `RayyanZahid/living-portraits`.
- `Immersive-commons/living-portraits` is Apache-2.0 and **not** a fork. It was last pushed 2026-09-12.
- Both facts were checked with `gh repo view`.

**Upstream's `CHANGELOG.md`, 0.2.0, dated 2026-08-09 (read directly):**
- "**Generation moved from Midjourney to Higgsfield** (`pipeline/hf_gen.py`)."
- "**The Midjourney path had been failing silently for weeks** (`MidjourneyAPIAuthError: POST /api/storage-upload-file -> 403`), which is the 905 failed proposals in the queue."
- "Midjourney code is retained as reference and fallback, but its session is dead."
- A later entry says the published code "still documents a Midjourney path that has returned 403 on every call since 2026-07-02."

**Upstream `pipeline/autogen.py`:**
- `BACKEND = os.environ.get("LP_GEN_BACKEND", "hf")`, described as "the default since 2026-08-09".
- The MJ path is "RETIRED but deliberately kept intact … MJ remains the fallback if the HF session or plan ever goes away".
- Upstream's `ARCHITECTURE.md` gives the switch date as 2026-08-08.

**Upstream `pipeline/hf_gen.py`** (commit `5efea6c`, 2026-09-09):
- Stills: `gpt_image_2 @ 1k = 0.5 credits`.
- Clips: `kling3_0 @ 1:1/5s = 7.5 credits with sound OFF`.
- "Credits are a MONTHLY pool (3000, granted on the 23rd, and NOT rolled over)".
- The Higgsfield session has a single owner. "a second host running `hf` steals and kills the first's session", so everything goes through a proxy on another host.

**What this changes:**
1. **The existential event may already be behind us.** On the upstream deployment, MJ generation has been dead since 2026-07-02, 84 days ago. The cause was an **account/session failure (a 403)**, not a model deprecation. The cause of the 403 is undetermined. Neither "V7 retired" nor "`--oref` retired" was needed to stop the pipeline.
2. **The one-way door may already be crossed.** If hil runs upstream code with `LP_GEN_BACKEND=hf`, the wall may already play a graph that mixes MJ faces with `gpt_image_2`/`kling3_0` faces. `MODEL_STACK.md` §5 says there is no partial migration.
3. **`MODEL_STACK.md` does not prove MJ is live.** Its "Verified as of 2026-09-10" covers *version claims*. Its "Live path" table describes what this fork's code pins, not jobs succeeding. No local source shows an MJ job succeeding after 2026-07-02. The only first-party evidence on MJ account health is negative.
4. **Upstream's stated reason for leaving is itself contested (unresolved).**
   - Upstream says "Midjourney could only animate forward from a single still" and that the old path "faked the return by playing the forward clip backwards".
   - Midjourney's Video doc documents `--end` (uploaded end frame, shipped 2025-07-24). This fork's `autogen.py` already renders a real reverse clip with `end_image`.
   - Both are first-party. Only an owner inspection of hil can say which code ran there.

**Gate 0 — owner, this week, all read-only. It decides which branch of §1.7 applies:**
```
REM on hil
findstr /n "BACKEND = " C:\living-portraits\pipeline\autogen.py
echo %LP_GEN_BACKEND%
dir C:\living-portraits\pipeline\hf_gen.py
type C:\living-portraits\DEPLOYED.json
powershell -NoProfile -Command "Get-Content C:\living-portraits\data\mind\gen_events.jsonl -Tail 50"
REM then count nodes/edges in the live data\clips\video_graph.json and check whether any node came from gpt_image_2 / kling3_0
```
Also check the MJ account: status, plan tier, whether it is suspended, and the cause of the 403.

---

## 1. Primary mission — the Midjourney exit strategy

### 1.1 How much warning would we get? — **none guaranteed; plan on 0 days**

**Confidence.** High that nothing is guaranteed. High that written notice was 0 days for 3 of 5 default switches. Low for any positive number.

**Stated policy.** The ToS (Version Effective Date May 27, 2026) says:
- "Please do not create any dependencies on any attributes of the Services or the Assets."
- "We reserve the right to modify or discontinue any aspect of the Service, including pricing and features, at any time."

Midjourney's only advance-notice promise anywhere covers **Privacy Policy** changes. A help-center search for "retire", "sunset" or "unavailable" returns 0 articles.
- https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service (accessed 2026-09-24)

**Track record.** Written channels checked: docs, updates.midjourney.com and X. Discord `#announcements` and Office Hours were **not** checked: they need a login, and the Office Hours Spaces are deleted.

| Change | Date | Written warning before it | Source |
|---|---|---|---|
| V5.2 → V6 default | 2024-02-14 | None found. Docs still said "--v 5.2 is the current default" on 2024-02-15. X for that window is not archived. | web.archive.org/web/20240215190735/https://docs.midjourney.com/docs/model-versions |
| V6 → V6.1 default | 2024-07-30 | 0 days ("as of today") | https://updates.midjourney.com/version-6-1/ |
| V7 weights changed in place under the same `--v 7` | 2025-04-30 / 05-02 | 0 days ("you don't need to change anything") | https://updates.midjourney.com/v7-update-editor-and-exp/ |
| `--cref` unavailable on V7 | by 2025-04-17 | none | web.archive.org/web/20250417124822/…/32162917505293-Character-Reference |
| V6.1 → V7 default | 2025-06-17 | About 24 days of hints with no date. Updates site only (2025-05-23: "getting ready to make our V7 model the 'default' model"). Docs and X gave 0 days. | https://updates.midjourney.com/rank-images-from-all-time/ |
| **V7 → V8.1 account default** (the June outage behind this repo's 166 dead proposals) | 2026-06-10/11 | **0 days.** Announced *after* the switch: the Version doc showed V8.1 as default at 2026-06-11T02:33Z, before the X post (04:02Z) and the updates post (04:08Z). | web.archive.org/web/20260611023347/…/32199405667853-Version; https://x.com/midjourney/status/2064921117618557292 |
| V8.2 default | 2026-07-24 | 0 days | https://x.com/midjourney/status/2080781271043911807 |
| Character Reference article deleted | between 2026-06-11 and 2026-09-23 | none | docs.midjourney.com/api/v2/help_center/en-us/articles/32162917505293.json (RecordNotFound) |
| Omni callout reworded to V8.2 wording | between 2026-08-28 and 2026-09-01 | none | https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference |
| **V8.0 alpha retired.** The only numbered model *documented as unavailable*. | removed 2026-07-24 | Written signals from 2026-03-21 ("we will likely remove the 'present' version of V8"). A formal "in two weeks" came on 2026-06-11; the actual removal was 43 days later. | https://updates.midjourney.com/v8-1-is-now-the-default-model/ and G5 in the evidence file |

**Where V7 and `--oref` stand today (2026-09-24).**
- **Still documented.** The Omni Reference doc says "Omni Reference can only be used with Midjourney version 7". The page carries `data-title="This feature is not supported in V8.2"` (Zendesk JSON, `edited_at` 2026-09-01). This confirms `MODEL_STACK.md:62-63`.
- **Still wired into the web client.** The client forces version 7 when character references are attached on 8.1/8.2 (`forcedV7ForOref`, bundle captured 2026-09-19/21). This is UI code, not documentation.
- **Signs of pressure:**
  - 2026-06-11: "V7 omni-reference is available to use while we finish training the improved version for V8".
  - 2026-08-27: the V8 Edit Model launched "(replacing omni-reference)", so that condition has arguably been met.
  - 2026-09-10 on X: "we replaced omni with the new edit model" and "can you show any examples where omni works better than the new edit model?"
- **No V7 or `--oref` retirement notice** had appeared in any updates post up to 2026-09-24T01:59Z, or on X up to 2026-09-16.
- **Informal and present-tense only** (X, 2026-09-09): "right now almost every old visual model is still available".

**The other zero-warning channels.**
- **Account.** Midjourney may "suspend or ban Your access to the Services at any time, and for any reason". The ToS imposes no duty to warn. Its automation clause, "You may not use automated tools to access, interact with, or generate Assets through the Services", applies to any unattended client that submits jobs. Upstream's 403 shows what a zero-warning loss looks like, whatever its cause.
- **Model drift.** Pinning `--v 7` does not freeze the weights: V7 was changed in place twice in 2025. Video has **no** version pin at all. The client's video identifier `vid_1.1_*` has not changed from 2025-06-17 to 2026-09-19, so a retrain would be invisible.

**Corrections to `MODEL_STACK.md` from this track.**
- `--ow` was **never** in the Parameter List. It is documented only in the Omni Reference article ("between 1 and 1,000, with the default being --ow 100"), confirmed across Wayback CDX captures. So "`--ow` has quietly dropped out of the current Parameter List" (`MODEL_STACK.md:213`) is wrong.
- The Legacy Features page still says "For information on the current default version (V7)…", while the Version doc says V8.2. Both were edited 2026-09-01. This is a first-party contradiction and is unresolved. It does not matter while `--v 7` is explicit.

**The alternatives' warning, for comparison.** No vendor promises the permanence this project needs.

| Vendor | Pinnable ID? | Stated minimum notice | In practice |
|---|---|---|---|
| Midjourney | No; labels change in place | none | 0 days, except one alpha model |
| OpenAI | Dated snapshots (`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst-2026-09-08`) | ≥6 months for *GA* models; ≥3 months for *specialized variants*; safety exception | The tier of the gpt-image-2 and 2.5 models is **not stated**. One 2026 deprecation gave 20 days (gpt-5.4-cyber). A snapshot gained a feature on Aug 20, so behaviour is pinned but features are not. |
| Kling | Version names (`kling-v2-1`, `kling-v3`) | "at least 30 days" (Paid Service Terms 4.1) | Effects discontinued with 0, 19 and 43 days' notice. No model deprecations yet. |
| BFL | `flux-2-pro` is a "fixed snapshot … This endpoint will not change" | ToS: "may not provide you with any notice beforehand" | flux-pro-1.0 endpoints were deprecated 28 days after the announcement |
| Higgsfield | None: may "substitute, deprecate, retire, or remove any model, model version … at any time" | none (a 15-day clause in the July 23 draft was dropped on July 26) | Web: "Higgsfield uses the latest available version" |
| Google Vertex | `-001` GA IDs | "at least 12 months after release". The same page lists veo-3.0 lasting 336 days, a first-party inconsistency. | `veo-3.1-generate-001`: "Retirement date: November 17, 2026 or later" |
| Luma / MiniMax / Alibaba | Luma `ray-3.2`; MiniMax undated names; Alibaba dated snapshots only | Luma: 30 days of "commercially reasonable efforts"; MiniMax: "in advance", no number; Alibaba: 30 days for snapshots, 3 months for mainline models | Alibaba retired two batches with "No dedicated announcement" |

Sources for this table: G3 in the evidence file, including https://developers.openai.com/api/docs/deprecations.md, https://kling.ai/document-api/guides/protocols/paid-service.md, https://docs.bfl.ml/flux_2/flux2_overview.md, https://higgsfield.ai/terms-of-use-agreement, https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions, https://lumalabs.ai/legal/api-terms-of-use and https://www.alibabacloud.com/help/en/model-studio/model-depreciation.

### 1.2 The closest identity mechanism on V8.x — **the Edit Model: single anchor yes, tunable weight no**

**Confidence:** high.

**The mechanism.**
- The **Edit Model** is written `--edit <url> [url…]` in a prompt, or "Attach to prompt" on the web.
- It runs on V8.1 and V8.2 only.
- It can "Generate new images using up to 4 reference images (replacing Omni Reference and Character Reference)".
- Source: https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model

**Single anchor: yes.**

**Tunable weight: none documented, and none in the production client.**
- The Version chart marks Omni Reference Weight ✗ for V8.1 and V8.2.
- The web client's Edit slot ships `disableWeights:!0` with strength fixed at 100 and a setter that does nothing.
- An undocumented `--ev` accepts only 1 or 2, so it is a switch, not a weight.
- `--raw` is the only documented balance control.
- Midjourney makes no claim about face fidelity.

**Other facts:**
- The V8.2 edit model was "updated … for better image quality" **in place** on 2026-08-29.
- Edit creations are public unless Stealth is on (Pro/Mega).
- The alpha "Use Subject" role is not a V8 identity route. On V8.x it silently submits a **V7** job ("Submitted with v7 — omni references are v7-only").

**Client angle (inference).** The web client submits `--edit` as a *separate job type*, `t:"edit_diffusion"`, not `t:"imagine"`. A client that only sends imagine jobs may not be able to reach the Edit Model at all.

**Verdict.** V8.x offers no drop-in replacement for `--oref --ow 160`. Moving to it is the V8 migration the brief already closed.

### 1.3 What actually stops when V7 or `--oref` goes

| Work item | Stops? | Why | What is still open |
|---|---|---|---|
| New pose stills (`--oref <anchor> --ow 160 --v 7`) | **Yes** | Omni is V7-only; the Edit Model is 8.1/8.2-only; there is no other documented identity path | — |
| Edges into a new pose | **Yes** | They need the new still | — |
| New edges, takes or idle loops **between existing stills** | **No documented rule stops it** | Video accepts only `--motion`, `--raw`, `--loop`, `--end`, `--bs`. It animates images "regardless of what version they were made in". The client sends no image version. | (a) **Uploads 403 on the upstream account.** This blocks it in practice in every branch until the account is fixed. (b) Whether video is tied to V8 is **unresolved** (below). (c) Drift in the frames between the endpoints can't be detected. (d) Relax video needs Pro or Mega, is SD only, and allows 3 at a time. |
| Re-rendering an existing edge | Same as the row above | Same | The new take comes from whatever video model is served *today*, not the one that rendered its sibling takes |
| Playing the existing footage | **No** | The clips are local files. "you own all the images and videos you create, even if you decide to cancel your subscription" | Whether you keep the rights after a **ban** is undocumented |

**Unresolved first-party contradiction on video.**
- Midjourney's EU "Public Summary of Training Content" lists the "Image and Video family of models" with "Model dependencies: Midjourney V8, V8.1, and V8.2". The EC template defines that field as "a modification, including fine-tuning, of one or more general-purpose AI models already placed on the Union market". The same page is dated "Last update: March 17, 2026", yet lists V8.2, which was released 2026-07-24.
- Against it: the Video doc and the unchanged `vid_1.1_*` identifier.
- An unchanged identifier does not prove the weights are unchanged.
- Sources: https://docs.midjourney.com/hc/en-us/articles/48067080311309-Public-Summary-of-Training-Content ; https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video

**The graph (counted in this repo's `data/clips/video_graph.json` on 2026-09-24).**
- 59 nodes and 500 edge rows: 204 transitions and 296 idles. The idles are **inside** the 500.
- Every idle has `start_frame == end_frame` and `loop: true`.
- The rows collapse to **251 unique clips**: 114 transitions and 137 idles. 83 clips carry 4 takes and 168 carry 1 (83×4 + 168 = 500).
- A full re-render is therefore 251 clips minimum, or 500 renders to reproduce every take.

### 1.4 Could a non-Midjourney generator do it? — **on paper yes; for this painted face, unproven**

**Confidence:** medium.

**Stills from one anchor with a tunable identity weight.**
- **Kling Image 2.1** is the only one found with a documented *continuous* identity weight. It takes `image_reference: subject` with `human_fidelity` ∈ [0,1], default 0.45, described as "Facial reference intensity".
  - "Only kling-v2-1 supports this parameter".
  - It has no seed.
  - Price: $0.028 per image.
  - https://kling.ai/document-api/api/image/2-1/image-generation.md
- **Other vendors' knobs control something else.**
  - Ideogram `image_weight`, Recraft `strength`, Firefly and Stability `fidelity` weight resemblance or style, not identity.
  - Leonardo's character guidance is LOW/MID/HIGH.
  - For OpenAI `gpt-image-2`: "omit this parameter [input_fidelity]".
  - BFL `flux-2-pro` takes up to 8 references with no weight but is a fixed snapshot.
- **No vendor documents drift on painted faces.** The only still-image drift measurement found is BFL's FLUX.1 Kontext paper, on a photo: https://arxiv.org/html/2506.15742v2

**Video between an explicit start and end frame** (API reference pages):
- Google Veo 3.1 `lastFrame`
- Kling 3.0 / 3.0 Omni `last_frame`
- Luma Ray 3.2 `end_frame`
- MiniMax H3 / H3-Max `role: last_frame`
- Vidu Q2/Q3
- Alibaba `wan2.2-kf2v-flash` `last_frame_url`
- LTX-2.5 `last_frame_uri`
- xAI `grok-imagine-video-1.5`
- PixVerse
- Adobe Firefly v3 keyframes
- Runway resells several of these; its own Gen-4.5 is first-frame only.

**The closest analogue to today's `--oref` plus end-frame recipe is Kling 3.0.** It accepts `element` + `first_frame` + `last_frame` in **one** request ("Up to 3 Elements"; the docs include an example headed "First_frame & last_frame & element").
- Building an element needs a `frontal_image` plus 1–3 more reference images, not a single anchor.
- The element has no weight.
- Loops (start == end) and the output aspect for square input are undocumented for Kling 3.0 image-to-video.
- https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md ; https://kling.ai/document-api/api/video/3-0-omni/elements.md

**Disqualified or blocked:**
- **Seedance via BytePlus:** "not available in the United States". Upstream rendered Seedance through Higgsfield anyway; that reseller path was not cleared.
- **MiniMax H3 open weights:** the US is an Excluded Territory, and the exclusion covers Outputs.
- **Wan 3.0 direct:** one first-party page says "preview" and another says "launched". Preview terms allow only internal testing.
- **Non-commercial weights:** FLUX.2 [dev] and FLUX.1 Kontext [dev], Qwen-Image-2.1, InsightFace-based pipelines (InstantID), InfiniteYou, StyleID, EdgeFace HF weights.
- **No end frame:** Kling O1 with element+first+last, Kling 2.6 elements, Kling 3.0 Turbo, Higgsfield `kling3_0_turbo`, `grok_video_v15`.

**Higgsfield, the path upstream actually deployed:**
- **Tooling.** The official CLI `github.com/higgsfield-ai/cli`: the repo is MIT, v1.1.26 (2026-09-18); the licence of the distributed binary is unconfirmed.
- **Models.** `gpt_image_2` takes repeatable image references with no weight. `kling3_0` takes a first and last frame.
- **Terms (last updated July 26, 2026)** are clear but unfavourable for a permanent wall:
  - Higgsfield may **train on "Your Content, Inputs, and Outputs"**, and reference images count as Inputs. Only Enterprise excludes training.
  - The terms before July 26 granted a perpetual, transferable licence over Inputs.
  - It may substitute models at any time.
  - Account sharing is banned.
  - Provenance markers must not be removed.
- https://higgsfield.ai/terms-of-use-agreement

**The identity gate every pilot needs is itself a licensing problem, and so is this repo's current QA code.**
- `pipeline/verify.py:204` loads InsightFace `FaceAnalysis(name="buffalo_l")` (threshold 0.55, `VERIFY_CONTRACT.md:61`).
- InsightFace says "all open source models from our repo are for non-commercial research purposes only". That was its answer to a question about internal use: https://github.com/deepinsight/insightface/issues/2486
- The installer also pulls InsightFace files from third-party mirrors.
- **No clean replacement was found.** AuraFace (Apache-2.0) has unanswered provenance questions and a different embedding space, so 0.55 does not transfer. SFace, YuNet and dlib each have training-data licence problems.
- Face recognition is weak on paintings anyway: in ArtFace, AntelopeV2 had an EER of 14.0% on painted portraits.
- **So in any pilot, human review on the panel is the gate of record, and an embedder is only triage.**

### 1.5 The client — **not public; unidentifiable from outside hil**

**Confidence:** medium.

**What is known:**
- `from midjourney.api import MidjourneyAPIClient   # lazy: only present on hil` (`autogen.py:211`).
- Upstream's release script leaves it out on purpose: `"midjourney",  # vendored client`. hil's host `.gitignore` excludes `midjourney/` and `sessions/`.
- It authenticates through Firebase from `sessions/midjourney.json`, raises `MidjourneyAPIAuthError`, depends on `curl_cffi`, and calls midjourney.com's **web** endpoints.
- **Nothing public matches its fingerprint.**
  - GitHub code search finds these names only in living-portraits itself.
  - PyPI `midjourney` 0.0.1 is an empty placeholder (a 0-byte `__init__.py`).
  - `midjourney-py` 1.0.4 has no `api` module.
  - A private repository can't be ruled out.
- **Wording conflict, unresolved:** `MODEL_STACK.md:210` says "not vendored"; upstream says "vendored client".

**Multi-image reference submission: unconfirmed, and irrelevant under the V7 pin.**
- `autogen.py` passes the reference only inside the prompt string (`--oref %s --ow %d --v %s`).
- The Omni doc says "You can only use one image with Omni Reference".
- V8.x multi-reference goes through the separate `edit_diffusion` job type (§1.2).

**How it was identified: owner, read-only on hil, no live MJ call.**
```
REM 1. which python runs lp-gen
schtasks /query /tn lp-gen /v /fo list
REM 2. the client's files
powershell -NoProfile -Command "Get-ChildItem C:\living-portraits\midjourney -Recurse | Select FullName,Length,LastWriteTime"
REM 3. print its source without constructing a client  (<PY> = the interpreter from step 1)
<PY> -c "import sys,inspect; sys.path.insert(0,r'C:\living-portraits'); import midjourney, midjourney.api as a; print(midjourney.__file__); [print(inspect.getsource(getattr(a.MidjourneyAPIClient,m))) for m in ('__init__','submit_imagine','submit_video','upload_image','job_status')]"
REM 4. wire-format strings
powershell -NoProfile -Command "Get-ChildItem C:\living-portraits\midjourney -Recurse -Filter *.py | Select-String -Pattern 'submit-jobs','imagePrompts','videoType','--end','relaxed','firebase','edit_diffusion'"
REM 5. provenance
<PY> -m pip show -f midjourney midjourney-py curl_cffi
```
Also ask whoever maintains the private monorepo for `git log --follow -- <project>/midjourney/api.py`.

**Midjourney's official API.** There is none. The only first-party trace is a 2025-07-16 enterprise API survey: https://updates.midjourney.com/enterprise-api-survey/

### 1.6 Migration options

**Two rules apply to every row:**
- **No hybrid graphs.** `MODEL_STACK.md:205-209` says: "There is no partial migration … re-render **all** 59 nodes and **all** 500 edges → cut over atomically". Any option that adds non-V7 nodes or edges beside existing MJ footage is therefore **disqualified**, however cheap it looks.
- **Prices** below come only from published price pages; the arithmetic is shown. "251" means the unique clips and "500" means every take.

| Option | What changes | Identity mechanism | Start+end-frame video | Re-render scope | Licensing / ToS | Cost (published prices only) | Reversibility | Key unknowns |
|---|---|---|---|---|---|---|---|---|
| **O5 — Freeze** | No new art. The wall keeps playing the local footage. | None needed | — | 0 / 0 | None new. Rights after a ban are undocumented. | $0 | Fully reversible; the face is untouched | None, beyond the ban question |
| **O0 — Stay on V7 + tripwires** | Nothing in `autogen.py` (IMAGINE_VERSION and IMAGINE_MODE untouched); add §1.8 | `--oref` single anchor, `--ow` 1–1,000 | MJ `--end`, `--loop` | 0 / 0 | **Unattended submission falls under the ToS "automated tools" clause.** Bans come "at any time, and for any reason". | Existing plan | Reversible; the face is untouched. Pinning does not freeze the weights. | **Is the account alive (403 since 2026-07-02)?** Does V7 `--oref` still run? Plan tier? |
| **O1 — Stockpile now** (bounded, manual) | Pre-render reserve V7 poses and their edges while V7 still runs | Same as O0 | Same as O0 | Adds within the V7 lineage only | Same ToS exposure as O0, and more of it. Relax: 3 concurrent, waits of 0–30 min or longer. | Existing plan; $ price not in the sources | Reversible; same face recipe | Account health; how many poses to bank |
| **O2 — V8.x Edit Model, full re-render** | Every still via `--edit`, every edge re-rendered | Single anchor, **no weight** | MJ video | 59 / 251–500 | MJ ToS + Stealth | Not in the sources | One-way door | **CLOSED by the brief** (V7→V8.2). Listed for completeness. |
| **O3a / O3b / O3c / O6 — any hybrid** (MJ Edit Model on the canonical for new poses; external stills + MJ edges; external new poses beside MJ footage; frames pulled from MJ video) | New nodes beside the existing MJ graph | varies | varies | Additive | varies | varies | **Creates a hybrid graph** | **DISQUALIFIED** by the atomic-cutover rule. (O3a also re-opens the closed V8 question.) |
| **O4a — Kling API direct, full atomic re-render** | Stills: Kling Image 2.1 `subject` + `human_fidelity`, or an Image 3.0 element. Clips: Kling 3.0 `first_frame` + `last_frame` (+ `element`). | 2.1 stills: weight [0,1]. Element: frontal + 1–3 references, no weight. | **Yes, documented.** Loop and square output undocumented. | 59 / 251–500 | **STOP until Kling answers in writing:** consumer ToS 4.6 ("without our written permission, you may not use … the Output for any commercial purposes") conflicts with API terms 6.4 ("not restricted"); ToS 4.5 "Kling AI" labelling; ToS 4.7.1 licence to "publicly display" Input and Output; US sign-up eligibility (Singapore entity, one endpoint). | Clips at $0.084/s (720P, no audio): 5 s → $0.42 × 251 = **$105.42**, × 500 = **$210.00**. At 6 s (MJ clips are ~6 s) → $0.504 × 251 = **$126.50**, × 500 = **$252.00**. Stills: $0.028 × 59 = **$1.65**. Element creation: API price unpublished. | One-way door | Painted faces; whether elements expire; loops; aspect; US eligibility |
| **O4b — Higgsfield** (upstream's path: `gpt_image_2` + `kling3_0`) | Upstream's backend, through the `hf` CLI or API | `gpt_image_2`: references, no weight. CLI `kling3_0`: no element flag. | `kling3_0`: yes | 59 / 251–500, **unless hil has already mixed it in** | Trains on Inputs (the anchors) except on Enterprise; model substitution at any time; single-owner session | No per-model credit table published. Upstream **measured** 7.5 credits per 5 s `kling3_0` clip (a measurement, not a price): 251 × 7.5 = 1,882.5 credits against a 3,000-credit monthly pool | One-way door; **may already be crossed** | Which ToS version covered the anchor uploads; whether `gpt_image_2` equals OpenAI's snapshot; silent model substitution |
| **O4c — pinned stills, no Kling anywhere** | Stills: BFL `flux-2-pro` or an OpenAI dated snapshot. Clips: MiniMax H3-Max (`role: last_frame`), or self-hosted Wan2.1 FLF2V / VACE on rented GPUs. | No weight | Yes | 59 / 251–500 | OpenAI: customer owns output, no training without opt-in. BFL: may train on **and publicly display** Inputs and Outputs, no notice. MiniMax: "you retain your ownership rights". | `flux-2-pro`: $0.045 per edit with a 1 MP anchor → **$2.66** for 59; with the full 2048² anchor ≈ $0.09 → **$5.31**. MiniMax H3-Max 480P: $0.25 × 251 = **$62.75**. | One-way door; the only **hosted** option with pinned still endpoints | Drift on painted faces; OpenAI tier; MiniMax quality at 480P |
| **O4d — frozen open weights on a rented GPU** (not on supercommons2 or hil) | Stills: Qwen-Image-Edit-2511 (Apache-2.0) or FLUX.2 [klein] 4B + LoRA. Clips: Wan2.1-FLF2V-14B / VACE-14B (Apache-2.0). | No anchor weight | Yes (FLF2V has no square size) | 59 / 251–500 | Weights OK. Whether MJ's "may not reverse engineer … the Assets" reaches a LoRA trained on V7 stills is unresolved. | No published per-clip price | One-way door, but **no vendor can ever retire it** | Quality; square output |
| **O4e — Google Veo 3.1 / Gemini 3 Pro Image** (demoted) | Veo `lastFrame` clips | No weight | Yes, but **16:9 / 9:16 only** against square stills | 59 / 251–500 | "Google won't claim ownership"; SynthID on every image | Veo 3.1 Lite $0.30 per 6 s × 251 = **$75.30** | One-way door | `veo-3.1-generate-001` retires "November 17, 2026 or later" |

### 1.7 Recommendation

**Default posture until Gate 0 (§0) says otherwise: O5, freeze.**
- The only first-party evidence on MJ account health is negative.
- O5 is face-neutral and carries no automation exposure.
- Nothing is lost by freezing while the owner checks.

**Branch A — this fork drives the wall, the graph is all-MJ, and the account is healthy:**
1. **O0 with tripwires, only after the owner has reviewed the ToS "automated tools" clause (§1.1) and accepted the account risk.** Otherwise stay on O5. Keep IMAGINE_VERSION and IMAGINE_MODE as they are.
2. **O1, optional, under the same acceptance.** A bounded, manual reserve of V7 poses. Stop at the first submit error; June burned 166 proposals.
3. **Prepare the exit without uploading the canonical anywhere yet.**
   - Send Kling the written questions from the O4a row, including ToS 4.7.1 on Inputs, *before* any anchor upload.
   - Run the first pilot on a **non-canonical test character**: about 10 transitions and 10 idles, Kling 3.0 first/last frame, with and without an element.
   - Pilot cost: 40 renders × $0.42 = **$16.80** at 5 s, or $20.16 at 6 s, plus stills at $0.028 each.
   - Download pilot results promptly: Kling clears generated results after 30 days.
4. **Second exit target: O4c without Kling.**

**Branch B — hil runs Higgsfield and the live graph already mixes faces (the door is crossed):**
1. **Stop adding nodes.**
2. **Audit the mixed graph by eye on the panel.**
3. **Choose one of two exits; there is no "re-render only if it looks bad" middle path:**
   - (i) **A full atomic re-render** of the whole live graph on **one** generator. Higgsfield Enterprise is its only no-training tier. The alternative is O4a direct, once Kling's STOP clears.
   - (ii) **Roll back to the all-MJ 59/500 graph and freeze.**
4. **Find out which Higgsfield ToS governed the anchor uploads.** Accounts registered before July 26 stayed on the Aug 30, 2025 terms until 2026-08-27, unless they accepted the new terms earlier. Those terms granted an "irrevocable, perpetual … transferable" licence over Inputs and Outputs. Accounts registered July 23–25 got the July 23 terms, stated as "Effective: immediately".

**Branch C — MJ account dead or banned, or V7/`--oref` retired:**
1. **O5 immediately.**
2. **Pilot as in Branch A.**
3. **Then decide:** a full atomic re-render on O4a if Kling clears, otherwise O4c without Kling, or stay frozen.

**What would change this ranking:**
- **Kling confirms commercial use, labelling and US eligibility in writing:** O4a becomes the primary exit.
- **Kling refuses or answers ambiguously:** O4c.
- **The pilot shows no vendor holds the painted face:** O5 becomes the long-term plan.
- **Midjourney grants an automation exception or ships an enterprise API:** O0 and O1 get stronger.
- **The EU-summary question resolves toward V8-derived video, or `vid_1.1_*` changes:** pause all MJ video until an A/B comparison against archived takes is done.

### 1.8 Tripwires (only meaningful in Branch A)

| Signal | How | How often | Trigger → action |
|---|---|---|---|
| Omni Reference article | `https://docs.midjourney.com/api/v2/help_center/en-us/articles/36285124473997.json` (`edited_at`, body) | daily | RecordNotFound, "version 7" wording removed, or the article moved to Legacy → **halt new poses, O5** |
| Version article | `…/articles/32199405667853.json` | daily | V7 dropped from the chart, or any "no longer available" naming V7 → **halt, O5** |
| Legacy Features / Parameter List | `…/33329788681101.json`, `…/32859204029709.json` | daily | Omni or `--oref` added to Legacy/Deprecated → **alert and prepare the exit** |
| Updates feed | `https://updates.midjourney.com/sitemap-posts.xml`, grep `retire|deprecat|decommission|discontinu|sunset|omni|oref|v7|video model` | daily | V7 or oref named → halt; other hits → alert |
| Pipeline telemetry on hil | `data/mind/gen_events.jsonl` | every job | Any 403 on `/api/storage-upload-file`, `MidjourneyAPIAuthError`, or "not compatible with `--version`" → **autogen halts on the first error and pages the owner** |
| EU training summary | `…/articles/48067080311309.json` | monthly | Any edit → pause MJ video and re-check whether it is tied to V8 |
| ToS and Community Guidelines | `…/32083055291277.json`, `…/32013696484109.json` | weekly | Effective-date or automation wording changes → owner legal review |
| Web client bundle | Newest `clientSideEntry-*.js` via Wayback CDX. Key on **stable i18n strings** (`info.prompt.orefForcedV7`, `imagePrompts.omniStrength`, `error.promptParser.unknownVideoVersion`), not minified identifiers. | weekly | Oref-forcing gone → halt. A new video identifier → pause video. **A missing capture means "unknown", not "no change".** |
| Manual canary (owner) | One `--oref --ow 160 --v 7` relax job, plus one start/end video between two existing stills | monthly | Fails → halt. Face differs from the canonical by eye → pause (V7 changed in place). |
| Discord `#announcements` and Office Hours | Owner, logged in (agents can't reach these) | weekly | Any V7, oref or video-model statement → alert |

---

## 2. Secondary A — does `sherpa-onnx` expose per-phoneme durations? — **No** (high confidence)

**The answer.**
- sherpa-onnx **v1.13.8** (latest, 2026-09-10; no v2 tag) returns only audio: `struct GeneratedAudio { std::vector<float> samples; int32_t sample_rate; … }`.
- The Python binding exposes only `samples` and `sample_rate`.
- The only timing hook is a per-sentence progress callback.
- The VITS/Piper and Kokoro code runs every graph output and then `return std::move(out[0])`, so a durations output is computed and thrown away.
- The maintainer, 2026-07-07: "We don't currently have plans to support this. Instead, we are focusing on an HMM/GMM-based approach".
- Sources:
  - https://github.com/k2-fsa/sherpa-onnx/releases/tag/v1.13.8
  - https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/csrc/offline-tts.h
  - https://github.com/k2-fsa/sherpa-onnx/issues/3727

**Two findings that change the plan in `MODEL_STACK.md` §3.3.**

**1. sherpa-onnx is not GPL-free for Piper voices today.**
- TTS is on by default and links `piper_phonemize` and espeak-ng (GPL-3.0-or-later) into the core. The macOS 1.13.8 wheel exports 50 `espeak_*` symbols while declaring Apache.
- The maintainer calls espeak-ng's GPL "incompatible with the Apache-2.0 license of sherpa-onnx", with a fix planned for 2.0.0 (issue #3731, open, no milestone).
- Sources:
  - https://github.com/k2-fsa/sherpa-onnx/issues/3731
  - https://github.com/k2-fsa/sherpa-onnx/blob/040afe360a38e25daaa325ce8889abf93ea02609/CMakeLists.txt

**2. The two Piper voices `tts.py` names are in a licensing contradiction (unresolved).**
- `en_GB-alan-medium` and `en_GB-jenny_dioco-medium` are both "Finetuned from U.S. English lessac voice".
- The lessac licence is "Research Purposes only" and excludes "the development … of voice synthesis … products or services".
- The piper-voices README says `license: mit`.
- Both are first-party. Standard 5 may disqualify these voices, and that is an owner decision.
- Sources:
  - https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_US/lessac/medium/MODEL_CARD
  - https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_GB/jenny_dioco/medium/MODEL_CARD
  - https://huggingface.co/rhasspy/piper-voices/blob/main/README.md

**Durations do exist, just not through sherpa-onnx.** Both were reproduced by an agent on 2026-09-23.

| Route | What you get | Licence notes |
|---|---|---|
| **A.** Stock Piper `.onnx`, with `/Ceil_output_0` (w_ceil) exposed as an output, run with onnxruntime | Frames per phoneme × 256 samples, exact. Deterministic only with `noise_w=0`. | onnx is Apache and onnxruntime is MIT; write the patch yourself (piper1-gpl's patch script is GPL). Needs espeak `en-gb-x-rp` IPA, which means espeak-ng as a separate process, or pre-computed IPA. **Blocked for alan and jenny by the lessac contradiction.** |
| **B.** Kokoro Python `KPipeline` | Per-word `start_ts`/`end_ts` and `pred_dur`, from kokoro 0.7.0 | Apache-2.0, but loads GPL espeak-ng **in-process** |
| **C. (best supported)** sherpa's Kokoro int8 graph run directly with onnxruntime plus the bundled `lexicon-gb-en.txt` | A per-token duration output (`onnx::Shape_3411`). `hello world` → 72 frames × 600 = 43,200 samples, exact. | Apache-2.0 weights. **No GPL code in the process.** Words not in the lexicon have no fallback. Kokoro grades these voices **C** (`bm_george`) and **B-** (`bf_emma`). |
| **D.** Forced alignment of the finished wav (MFA 3.4.2, MIT) | Phone intervals, 10 ms frames | The toolchain has no non-commercial parts (kalpy MIT, Kaldi/OpenFst Apache; pin `ffmpeg=*=lgpl*`; sox and mad stay installed, uncalled). **Use `english_us_arpa`** (LibriSpeech-only, CC BY 4.0; US ARPAbet phones). **`english_mfa` is BLOCKED:** 4 of its 10 training corpora are non-commercial (208.68 of 3,614.20 h). For HF v3.3.0 models the command is `mfa align_one_hf`, not `align_one`. |

Also see https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/docs/ALIGNMENTS.md: piper-tts itself gets alignments by *patching* w_ceil into the graph, and "all of the existing voices need to be patched".

**What was not confirmed:**
- How well `english_us_arpa` aligns synthetic British speech.
- Whether training-corpus NC terms bind a CC BY 4.0 model (a legal question).

---

## 3. Secondary B — local expressive TTS for the two registers — **medium; the two research angles disagree**

**Hard constraint:** nothing was benchmarked on the 2080 Ti or the i9-9900K. Every pick below needs an ear test on the box before it ships.

| | Pick (B2: cloning angle) | Pick (B1: voice-design angle) |
|---|---|---|
| **Phineas** — "dry patrician baritone, grandiloquent, self-pitying" | **Chatterbox EN 500M** (MIT/MIT), cloned from CC0 Voice-Zero `simon_evers.flac` ("Public School (Received Pronunciation)"). Vendor's dramatic recipe: `cfg ≈ 0.3`, `exaggeration ≥ 0.7`. | **VoxCPM2** (Apache-2.0/Apache-2.0): a voice from a description, then clone plus `(style)` direction. Alternate: **Qwen3-TTS-12Hz-1.7B-VoiceDesign**, FP32 only ("we strongly recommend using `float32` … on machines that do not support `bfloat16`"). |
| **Seraphina** — "quick dry mezzo, complicit and amused" | **Chatterbox EN 500M**, cloned from CC0 `ruth_golding.flac` (RP) | **VoxCPM2**. Alternate: **Maya1** (Apache-2.0; British voices and `<sarcastic>`/`<chuckle>` tags, but 3.3B BF16, "16GB+ VRAM", no cloning). |

**What decides between them:**
- **VRAM.** Nothing fits in the ~3–4 GB left beside Ollama at a precision known to be safe on Turing. Run offline: on CPU in FP32 (VoxCPM2 needs a `config.json` dtype edit), or on the whole card with Ollama unloaded (`keep_alive: 0`).
- **Dependency pins.** Chatterbox 0.1.7 (2026-03-26, still current) pins `torch==2.6.0` and `transformers==5.2.0`, so give each engine its own venv. The repo's default branch is `master`; Nano and Multilingual V3 exist only there; Flash is a separate package.
- **Timings.** Neither pick emits phoneme timings. Pair either with MFA `english_us_arpa` (§2, route D) or use Kokoro route C for lip-sync.
- **Voice rights (an owner and legal call).** CC0 covers copyright in the LibriVox recordings, not the question of cloning a real person's voice for a permanent public display. The clean alternative: design a voice with Qwen3-TTS VoiceDesign (Apache), then clone *that*.
- **Operations.** Every Chatterbox output carries the Perth watermark. A secondary report says Chatterbox can "babble … scream … randomly shouts curse words", so generate every aside offline and review it before it can play.

**Disqualified by licence:**
- F5-TTS (weights CC-BY-NC)
- XTTS-v2 (CPML, non-commercial including outputs)
- Fish S2 Pro
- Higgs TTS 3
- Breeze TTS 2
- OmniVoice (CC-BY-NC)
- AuK (needs non-commercial Qwen2.5-Omni-3B)
- VoiceSculptor (base model CC-BY-NC)
- StyleTTS2 (weights unlicensed)
- Step-Audio-EditX (no weights licence)

**Conditional on legal review:** IndexTTS-2/2.5. Its bilibili licence reaches "model outputs".

**Key sources:**
- https://huggingface.co/ResembleAI/chatterbox
- https://github.com/resemble-ai/chatterbox/blob/master/pyproject.toml
- https://pypi.org/project/chatterbox-tts/0.1.7/
- https://huggingface.co/openbmb/VoxCPM2
- https://github.com/OpenBMB/VoxCPM/blob/main/README.md
- https://github.com/QwenLM/Qwen3-TTS/issues/43
- https://huggingface.co/maya-research/maya1
- https://github.com/OwenTyme/voice-zero/blob/main/voices/README.md

---

## 4. Secondary C — Qwen3.5-9B thinking default, and ollama#14579 — **high confidence**

**C1: thinking is ON by default.** The "both can't be right" puzzle resolves once you separate the files each source describes; it is not a real contradiction.

| Artifact | Default when unset |
|---|---|
| Official `Qwen/Qwen3.5-9B` `chat_template.jinja` | **ON**: `{%- if enable_thinking is defined and enable_thinking is false %} … {%- else %} {{- '<think>\n' }}` |
| Official card | **ON**: "Qwen3.5 models operate in thinking mode by default" |
| Unsloth's doc | "For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default". True of **Unsloth's own GGUFs**, whose embedded template inverts the condition. |
| Ollama `qwen3.5:9b` | **ON**: renderer `Qwen35Renderer{isThinking: true, …}` |

**What this means for the repo's calls:**
- **`"think": false` works for qwen3.5 on `/api/chat`.** It writes the same empty-think prefill that Qwen's template uses.
- **`/no_think` is not supported by Qwen3.5.** Nothing in Ollama's qwen3.5 renderer handles it, so on 3.5 the `/no_think` at `director/llm.py:172` and `director/stage_manager.py:48` reaches the model as **literal text**.
- **Sampler mismatch.** Ollama ships the *thinking* preset `{"presence_penalty":1.5,"temperature":1,"top_k":20,"top_p":0.95}`, and the repo overrides only temperature. The card's non-thinking general preset is 0.7 / 0.8 / 20 / 1.5.

**Sources:**
- https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/chat_template.jinja
- https://huggingface.co/Qwen/Qwen3.5-9B
- https://unsloth.ai/docs/models/qwen3.5 (page last updated 2026-08-13)
- https://huggingface.co/unsloth/Qwen3.5-9B-GGUF
- https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/qwen35.go

**C2: #14579 is not MoE-only, but nobody has reported the dense 9B.**
- The body is about Qwen3.5-35B-A3B. Comments add the **dense** `qwen3.5:27b`. None of the 12 comments mentions 9B.
- The issue is **open** and no release note cites it.
- The engine that was measured was replaced: llama-server became Ollama's sole GGUF engine in **v0.30.0** (PR #16031).
- The more relevant risk for this card is a separate llama.cpp **Turing** regression on the qwen35 architecture (#25162: "24-42% performance regression on Turing GPUs (RTX 2080 Ti, SM75)"). Ollama vendored the regressing commit from **v0.30.4 through v0.32.5**.
- No dense-9B throughput has been measured on CUDA or Turing. **Do not publish a number; measure on supercommons2.**
- **Sources:**
  - https://github.com/ollama/ollama/issues/14579
  - https://github.com/ollama/ollama/pull/16031
  - https://github.com/ggml-org/llama.cpp/issues/25162
  - https://github.com/ollama/ollama/blob/v0.34.4/LLAMA_CPP_VERSION

**Ollama version floor (combining C and D):**
- **≥ v0.31.2** is needed for `think:false` + `format` on qwen3.5; below that the format is silently ignored.
- **Avoid v0.30.4–v0.32.5 on the 2080 Ti.**
- **Net: ≥ v0.32.6.** v0.34.4 (2026-09-23) is the latest.
- The v0.32.6 floor is inferred: it is the first tag containing the reporter's recovered build, and the actual fix commit is unidentified.

---

## 5. Secondary D — local-brain bake-off shortlist under 7 GB — **high confidence**

Every tag, size, context, licence and lab below was read off `ollama.com/library/<name>` and cross-checked against the lab's own model card on 2026-09-23.

| Tag | Size | Ctx | Licence | Lab | Thinking | Verdict |
|---|---|---|---|---|---|---|
| `qwen3:8b` | 5.2 GB Q4_K_M | 40K | Apache-2.0 | Qwen / Alibaba Cloud | ON by default; send `think:false` | **baseline** |
| `qwen3.5:9b` | 6.6 GB Q4_K_M, 9.65B | 256K | Apache-2.0 | Qwen (the Ollama page shows only the brand) | ON by default; `think:false` works; `/no_think` unsupported | **lead** |
| `qwen3.5:4b` | 3.4 GB Q4_K_M | 256K | Apache-2.0 | Qwen | same as the 9B | include |
| `qwen3:4b-instruct-2507-q4_K_M` | 2.5 GB | 256K | Apache-2.0 | Qwen / Alibaba Cloud | Non-thinking only. Pin the **exact** tag: bare `qwen3:4b` is the thinking variant. | include |
| `gemma4:e4b-it-qat` | 6.1 GB (5.2 GB model + 992 MB projector) | 128K | **Apache-2.0** | Google DeepMind | Effectively ON on local Ollama; send `think:false` | include; **not** `gemma4:e4b` (9.6 GB) |
| `granite4.2:8b` | 5.3 GB Q4_K_M | 128K | Apache-2.0 | IBM | ON by default. `think` must be **top-level**; the page's `options.think` example is ignored. | include; test first; re-pull (a bad `num_ctx` was removed 2026-09-04) |
| `ministral-3:8b` | 6.0 GB Q4_K_M | 256K | Apache-2.0 | Mistral AI (the Ollama page shows only the brand) | none | include; ships temperature 0.15 |

**Settled from `MODEL_STACK.md` §6:**
- **Gemma 4 is Apache 2.0**, not the custom Gemma Terms. The Gemma Terms page itself says "For Gemma 4 terms, see the Gemma 4 license".
- **Gemma 4 12B was released June 3, 2026.** But `gemma4:12b` is 7.6 GB and `:12b-it-qat` is 7.2 GB, so it fails the size cap.
- Sources:
  - https://ai.google.dev/gemma/docs/gemma_4_license (last updated 2026-04-01)
  - https://ai.google.dev/gemma/terms
  - https://ai.google.dev/gemma/docs/releases

**Reserves, HOLD and excluded:**
- **Reserves:** `granite4.1:8b`, `phi4-mini:3.8b-q4_K_M` (MIT), `gemma4:e2b-it-qat`, `llama3.1:8b` (Llama licence: "Built with Llama" display duty).
- **HOLD:**
  - `olmo-3:7b-instruct`: its card says "intended for research and educational use", and the Ollama page names no lab.
  - `nemotron-3-nano:4b`: two first-party licence names disagree.
- **Excluded:**
  - `ornith-1.5:9b`: no licence.
  - `exaone3.5`: NC.
  - `glm4:9b`: commercial use needs registration.
  - `lfm2.5`: over a $10M revenue threshold. A judgment call, not a rule-5 disqualification.
  - Everything over 7 GB.

**Mechanics that apply to every candidate:**
- Pin one shared `num_ctx`. The default is 4096 below 23 GiB of VRAM; the Modelfile doc still says 2048, a first-party inconsistency.
- Send top-level `think:false`.
- Consider a JSON **schema** in `format` instead of `"json"`, to enforce the four keys.
- Host Ollama ≥ v0.32.6 (§4).
- File size is not runtime VRAM. The qwen3.5 GGUFs carry vision weights, and whether those load on text-only calls is unknown.
- Sources:
  - https://ollama.com/library/qwen3.5/tags
  - https://ollama.com/library/gemma4/tags
  - https://huggingface.co/ibm-granite/granite-4.2-8b
  - https://mistral.ai/news/mistral-3/
  - https://docs.ollama.com/capabilities/structured-outputs
  - https://github.com/ollama/ollama/releases/tag/v0.31.2

---

## 6. Corrections this research makes to `MODEL_STACK.md`

1. **§1 and §2 treat MJ V7 as the live art path.** Upstream says MJ has returned 403 since 2026-07-02 and Higgsfield has been the default since 2026-08-08/09. Unverified for hil until Gate 0.
2. **§5.1 says `--ow` "dropped out of the current Parameter List".** It was never in it; it is documented only in the Omni article.
3. **§5.1 says the client is "not vendored".** Upstream's release script calls it a "vendored client". Unresolved.
4. **§3.3's sherpa-onnx route.** It gives no durations, and its shipped wheels link GPL espeak-ng.
5. **§3.3's Piper voices** (`en_GB-alan-medium`, `en_GB-jenny_dioco-medium`) are lessac-derived, and lessac is research-only. This conflicts with the MIT label. Unresolved.
6. **§6, Gemma 4 12B.** Date (June 3, 2026) and Apache-2.0 are both confirmed first-party. It is still over the size cap.
7. **§6, Qwen3.5-9B thinking default.** Resolved: ON. Unsloth describes its own GGUFs.
8. **§3.2's "`think: False` is the correct lever".** Confirmed, and it additionally needs Ollama ≥ v0.31.2 (≥ v0.32.6 on the 2080 Ti).
9. **New: the identity gate.** `pipeline/verify.py:204` uses InsightFace `buffalo_l`, whose models InsightFace restricts to non-commercial research. That affects the *current* QA path, not just a migration.

---

## 7. Owner actions: what research cannot close

1. **Gate 0 (§0).** Which repo drives the wall, `LP_GEN_BACKEND` on hil, whether the live graph is mixed, and MJ account health and the cause of the 403.
2. **The client inspection commands on hil (§1.5).**
3. **A review of the ToS "automated tools" clause** (§1.1), before O0 or O1.
4. **Written questions to Kling:** ToS 4.6 vs API 6.4, 4.5 labelling, 4.7.1 display licence over Inputs, US eligibility. Send them before any canonical anchor is uploaded to any vendor.
5. **Ask Immersive Commons:**
   - Annual revenue over $1M? MJ Pro/Mega is required to own Assets above that.
   - Over $10M? This matters for LTX-2.x and LFM licences.
   - Any Enterprise agreement with Higgsfield, Kling or BFL?
6. **Legal calls:**
   - lessac-derived Piper voices
   - espeak-ng as a subprocess vs in-process
   - the IndexTTS output licence
   - InsightFace `buffalo_l` in `verify.py`
   - cloning real LibriVox readers' voices
7. **Measurements on the box:**
   - The Ollama version on supercommons2 and hil.
   - `qwen3.5:9b` VRAM and tok/s beside the TTS load.
   - What the literal `/no_think` does on qwen3.5 with `think:false`.
   - An ear test of Chatterbox EN 500M vs VoxCPM2 for both registers.
8. **Read Discord `#announcements`** for any V7, oref or video-model statement. Agents cannot reach it.

---

## 8. Method

- **Phase 1–3: research, verification, reconcile.** 11 research tracks.
  - Midjourney tracks MJ1–MJ6 each had 3 independent verifiers: one re-opened every cited URL, one hunted for invented versions and first-party contradictions, and one re-derived the answer from scratch.
  - Secondary tracks A, B1, B2, C and D each had 1 combined verifier.
  - A reconciler per track dropped every claim a verifier refuted unless it re-verified the claim itself.
- **Phase 4–6: critique, gap-fill, synthesis.**
  - A completeness critic read all 11 answers and spot-checked sources. It is what surfaced the upstream Higgsfield migration, which no research track had looked at.
  - 8 gap-fill tracks followed, each with its own verifier.
  - Then a synthesis of the Midjourney exit, and a red-team that raised 8 major and 20 minor objections. All of them are applied in §1.
- **Checked directly, not left to agents:**
  - The upstream repo identities, commit `5efea6c`, `hf_gen.py`, `autogen.py`'s backend default and the 0.2.0 CHANGELOG entries.
  - The graph counts in `data/clips/video_graph.json`.
  - The `/no_think` line numbers.
  - The InsightFace use in `verify.py`.
- **About 64 agents in total.** Phases 4–6 were re-run from saved per-track files after a workflow cache miss; no verified research was regenerated.

---

## 9. DO NOT QUOTE

Everything below is low confidence or unknown. **None of it may be repeated as fact.** Each list below is generated from that track's reconciled answer, plus the gap-fill items that could not be confirmed and the gap verifiers' flags.

**The load-bearing ones:**
- **Any positive number of days' warning before V7 or `--oref` is retired.** That includes "two weeks", "43 days", "125 days" and any day-count analogy with V8.0.
- **"257 nodes / 1462 edges" as hil's *current* graph.** Upstream wrote that figure on 2026-08-09.
- **That the wall's live graph is, or is not, mixed MJ/Higgsfield.** Unknown until Gate 0.
- **The cause of the MJ 403 since 2026-07-02.** Expired session, plan change, endpoint change and ban are all possible.
- **That MJ video is, or is not, derived from V8.** An unresolved first-party contradiction.
- **Any video model version name for MJ**, including "V1" as the version served today.
- **That the Edit Model, or any vendor, preserves this painted face.** Untested everywhere.
- **Any MJ plan price, or a relax-mode cost for `--oref`.** The "2 minutes" figure is a Fast-mode GPU accounting row.
- **Higgsfield per-clip prices.** The 7.5 credits is upstream's *measurement*.
- **Kling commercial-use status.** First-party documents conflict.
- **The licence of the distributed `hf` CLI binary.**
- **Which Higgsfield ToS version covered any anchor upload.**
- **Any dense Qwen3.5-9B throughput on Ollama or Turing**, and that v0.32.6 actually recovers Turing throughput.
- **The licence status of `en_GB-alan-medium` and `en_GB-jenny_dioco-medium`.**
- **That `sherpa-onnx` is GPL-free.**
- **Alignment accuracy of `english_us_arpa` on British TTS**, and whether training-corpus NC terms bind a CC BY 4.0 aligner model.
- **Any British-accent quality claim for any TTS model**, and **any TTS model's VRAM or speed on the 2080 Ti.**
- **Who wrote the `midjourney.api` client, its licence, and whether it can send `edit_diffusion` jobs.**
- **The OpenAI notice tier for `gpt-image-2` or `gpt-image-2.5-*`.**

### The complete list, by track

### MJ1 — Midjourney deprecation track record, stated policy, and notice given
- **[low]** 'V8.1 default was pre-signalled in the 2026-06-03 office hours, about 7 days ahead' (Medium recap: 'The v8.1 model will become the default model on the main site and in Discord before that occurs.') — *Secondary only (third-party recap of spoken office hours at medium.com/enthusiastically-midjourney); the first-party audio was not accessible; another secondary recap (geekycuriosity.substack.com) was reported as carrying no such pre-signal.*
- **[low]** 'V6 was pre-signalled in office hours as default by end of January 2024' (uxdesign.cc / medium design-bootcamp recap) — *Secondary only; stated target slipped to 2024-02-14 per the first-party Version doc.*
- **[low]** 'On August 29, 2026, Midjourney made V8.1 (not V8.2) the new default' — *Hallucinated secondary search summary; contradicted by the Version doc and the 2026-07-24 X post (V8.2 default since 2026-07-24).*
- **[low]** 'V6, V6.1, V7, V8.1, V8.2 and Niji 4 through 7 all still run as of August 2026; --v 5.2 is selectable' — *SEO/secondary search summary; no first-party test or statement covers all of these.*
- **[low]** Any specific positive notice period for a V7 or --oref retirement (e.g. 'two weeks', '43 days') — *Rests on a single precedent (V8.0), which was an alpha-site-only model; no stated policy exists.*
- **[low]** 'V7 / --oref will stay callable for many months after being relabelled Legacy' — *Inference from the --cref and Niji 6 precedents; not a stated policy; --upbeta shows Legacy items can later be marked 'may not function reliably'.*
- **[low]** Character Reference added to Legacy Features on 2026-09-01T17:12Z; Retexture on 2026-08-28T21:35Z — *Inferred from Zendesk heading-ID (ULID) timestamps; heading IDs can be reused (Niji 6 heading carries a 2025-01-14 ID although it moved to Legacy between 2025-10-16 and 2026-03-15). Hard bound is 2026-03-15..2026-09-01.*
- **[low]** Remix doc's '--version 3 ... --version 4' example as evidence old versions still run — *It is a hypothetical error example about stylize limits, not a statement of availability.*
- **[low]** 'Midjourney docs promised a V7 fallback that the prompt path did not honour' (doc vs behaviour contradiction) — *The doc fallback text covered adding an image to the web Imagine bar; the project's error was a text --oref under the v8.1 account default. Different paths; not shown to conflict.*
- **[unknown]** Whether --v 7 + --oref works today on the project's path — *Documented as supported; not tested against the live service.*
- **[unknown]** Whether older versions (--v 5.2/6/6.1, --niji 6, --test/--testp, legacy --hd, legacy upscalers) are accepted today — *Documentation-only evidence; no live test.*
- **[unknown]** When the June 2026 outage began relative to the 2026-06-10 default switch — *Repo only dates the 166-proposal count (2026-06-17).*
- **[unknown]** Existence of an automation exception or enterprise API access for this project — *Only a 2025-07-16 survey post exists; no launch or grant found.*
- **[unknown]** Whether the web Imagine bar still has an Omni Reference slot — *Current Omni doc is internally inconsistent: its reference-type list omits Omni Reference but its body still describes the Omni Reference section.*
- **[low]** GPU Speed table row 'Omni Reference Prompt (V7) 2 minutes' as evidence that oref runs in Fast Mode — *The table does not say it is Fast-only; the Omni doc says oref is 'currently not compatible with Fast Mode'. Low stakes because the project runs relax.*
- **[unknown · gap G5]** Any first-party written advance notice of the 2024-02-14 V5.2->V6 default switch. Discord #announcements was not accessible; no @midjourney X post from 2024-02-09 to 2024-03-06 is archived in Wayback, so absence on X is unproven; the docs said nothing until after the switch; the updates page did not exist yet.
- **[unknown · gap G5]** Exact time on 2024-02-14 that V6 became default.
- **[unknown · gap G5]** Office-hours statements (spoken X Spaces) for Jan–Feb 2024 and 2025-05-21/05-29/06-04/06-11. The Spaces posts were deleted, the Hivemind room pages are dynamic and not archived (live 404), and third-party recaps are secondary (Medium returned 403 and is not in Wayback).
- **[unknown · gap G5]** Discord #announcements content for the V6 and V7 default switches (needs login; not attempted).
- **[unknown · gap G5]** Completeness of the X record: only Wayback-captured status IDs could be enumerated (1,519 @midjourney posts), and uncaptured posts are unknown. The archive.md capture of twitter.com/midjourney from 2024-01-31 was blocked (HTTP 429).
- **[unknown · gap G5]** Which 'old visual model(s)' are not available, given 'almost every' (2026-09-09); V8.0 is the only one documented.
- **[unknown · gap G5]** Whether --v 1–5.2, --niji 4/5, --test/--testp or legacy --hd actually accept jobs today. Not tested; the latest positive first-party statement is 2026-03-01 ('everything back to midjourney v1').
- **[unknown · gap G5]** Any formal first-party model-retention or deprecation-notice policy: none exists in docs, updates posts or recovered X posts.
- **[low · gap G5 verifier flag]** '20 @midjourney posts were recovered for 2025-05-15 to 2025-06-16': the actual count is 28 readable plus 8 author-deleted (the researcher's own mj_tweets.json has 28).
- **[low · gap G5 verifier flag]** 'The Version article across 24 captures': CDX shows 26 captures with status 200 (21 canonical plus 5 utm variants).
- **[low · gap G5 verifier flag]** 'updates: about 25 days of undated hints': the hints are dated posts (2025-05-23T23:15:17Z, 24.2 days before the switch; 2025-05-29T23:03:25Z, 18.2 days before). They are 'undated' only in that neither gives a switch date.
- **[low · gap G5 verifier flag]** 'X Spaces sessions were held on 05-21': no 05-21 Spaces post or title was seen. This is inferred from a deleted Hivemind reply whose parent is deleted and uncaptured.
- **[low · gap G5 verifier flag]** 'the target slipped about 2 weeks' (V6 default): rests only on unreadable secondary Medium recap titles.
- **[low · gap G5 verifier flag]** 'V8.0 alpha retirement: informal from 2026-03-21': the 2026-03-21 item is a written updates.midjourney.com post, and a written 2026-04-14 decommission notice was omitted. The 57/100-day analogy is anchored on the X reply, not on the first written notice.
- **[low · gap G5 verifier flag]** '1,709 status IDs': a fresh CDX run today gives 1,710 (drift, not an error).

### MJ2 — Midjourney V8.x identity-preservation mechanism
- **[low]** Edit Model character consistency is 'a significant upgrade compared to OREF in V7' — *Only a third-party blog says this (woollyferncreative.com). No first-party claim exists.*
- **[low]** Edit Model output is 1472 x 816 at 16:9 — *A single third-party X user report (@cfryant, 2026-08-28). There is no first-party figure.*
- **[low]** The Editor erase/layers route keeps the V7 face 'pixel-exact' or 'exactly' — *MJ says only 'will remain unchanged', in the Layers section. The fill is V6.1 or the Edit Model, never V7. HD inputs are downscaled to SD, and an unmasked submit re-renders the whole image.*
- **[low]** Retexture 'cannot change pose' — *This is an inference. The doc says only that it keeps 'the structure of the original image—like a template'.*
- **[unknown]** The Edit Model has no weight parameter at all — *The only supportable claim is that no weight is documented. The live UI was not inspected.*
- **[unknown]** Attaching the anchor as Image Prompt + Edit reference and raising --iw strengthens identity — *Combining them is documented. Any effect on identity is not documented, and MJ says references are 'not to copy them exactly'.*
- **[unknown]** '--edit <url>' works through the web prompt bar or the third-party midjourney.api client — *The how-to is documented only for Discord. Web and API behaviour is unverified.*
- **[unknown]** Edit Model jobs run in Relax mode — *The docs do not say either way. The V8.x chart's Relax ✓ is general, not specific to the Edit Model.*
- **[unknown]** Edit Model works with Draft or Conversational mode — *Not documented. The Draft status on V8.x is itself contradictory between first-party docs.*
- **[unknown]** Draft Mode is (or is not) available on V8.1/V8.2 — *First-party contradiction: the Version chart says ✗, the Draft doc says 'A single Draft mode prompt in V8.1 or V8.2 will generate a big batch of 24 images'.*
- **[unknown]** Conversational Mode on V8.2 — *First-party contradiction: the Version chart says ✓ for 'V8.1 & V8.2', the Draft/Conversational doc says 'version 7 and 8.1'.*
- **[low]** --iw range 0–3 applies to V8.2 — *The Image Prompts table labels the column 'Version 8.1' only. The Version chart marks Image Weight ✓ for V8.1 & V8.2 but gives no range.*
- **[low]** --ow minimum is 0 (or 1) — *First-party contradiction: the doc says 'between 1 and 1,000', the launch post says '0 to 100 to 1000'. Not load-bearing for --ow 160.*
- **[unknown]** Upload size limit (10MB vs 20MB) — *First-party contradiction between Creating on Web (10MB) and web-updates-5 (20 MB).*
- **[unknown]** Any date or plan for retiring V7, --oref or --ow — *No first-party statement was found. The only pointer is precedent: V8.0 was pre-announced 'in two weeks' but lasted until 2026-07-24.*
- **[low]** MODEL_STACK.md:213 '--ow has quietly dropped out of the current Parameter List' — *Unsupported. --ow is absent from every Parameter List capture checked, 2025-05-12 through 2026-09-05, so it never 'dropped out'.*
- **[low]** Discord Vary Region on V8.2 uses V6.1 — *The Vary Region doc (2026-07-27) predates the Edit Model launch and may be stale compared with the Version chart's 'Using Edit Model'.*
- **[unknown]** The meaning of the alpha 'Use Subject' action — *It is mentioned only in the 8/20 changelog, with no description.*
- **[unknown]** Edit Model availability on Niji — *Not stated. The V8.x chart column marks Niji ✗ in general.*
- **[unknown]** The Edit Model preserves the canonical's face under perspective or pose edits — *MJ documents perspective changes but makes no claim about face or identity fidelity.*
- **[unknown · gap G6]** What the alpha 'Use subject' toggle does after the Edit Model launch (2026-08-27). The only archived alpha bundle is from 2026-08-23, where subject means Omni (V7/8.1/8.2) or Character Reference (V6/6.1/niji 6). The bundle the alpha home page loaded on 2026-09-06 (clientSideEntry-y2kswza0.js) is not in Wayback, and the live site returns 403.
- **[unknown · gap G6]** How the 8/23 alpha actually routed an Omni 'subject' on V8.1/V8.2: its V8.x parsers do not accept --oref, and the effectiveVersion override was not traced.
- **[unknown · gap G6]** The meaning of the undocumented --ev ('Edit Variation', values 1|2). It may be the 'v8.1 and v8.2 edit types' from the 9/23 alpha changelog, or something else; no first-party text explains it and the UI never sets it.
- **[unknown · gap G6]** Whether the server accepts '--edit <url>' typed as prompt text. The UI code shows the web client parses it and serializes to it, but no live submission was made.
- **[unknown · gap G6]** Whether '--edit' works inside a plain 'imagine' job, as the repo's third-party midjourney.api client would likely send it. The web client uses a separate 'edit_diffusion' job type.
- **[unknown · gap G6]** Whether Edit Model jobs run in Relax mode on the server. Docs are silent; the client code does not downgrade Relax for edit jobs.
- **[unknown · gap G6]** Edit Model output pixel dimensions at non-1:1 aspect ratios, and whether edit outputs match the generic V8.2 SD/HD sizes. No first-party figure exists.
- **[unknown · gap G6]** Any first-party measurement or claim of face or identity fidelity for the Edit Model.
- **[unknown · gap G6]** Discord #alpha-news and #announcements were not read (they require auth).

### MJ3 — Midjourney video: end frames, versioning, coupling to the image model
- **[unknown]** 'The V2 video model is on the post-V8 roadmap, with a new compute cluster enabled in March' (attributed to the pixverse.ai blog) — *Not present on the cited pixverse page when fetched on 2026-09-23. It exists only in a search-engine summary. No first-party source mentions a video V2.*
- **[low]** 'Midjourney shipped its first video model in April 2026' (aimagicx.com and search summaries) — *Secondary SEO claim, contradicted by first-party V1 launch sources dated 2025-06-18.*
- **[unknown]** GenIArt_Fr recap of the 2026-03-25 Office Hours ('V8 Roadmap') — *Secondary, seen only truncated, not re-verified.*
- **[unknown]** 'The currently served video model is V1' — *V1 is the last named version, but no source says which weights are served now, and the EU summary hints at V8 dependencies.*
- **[unknown]** 'The video model was retrained on / is built on V8.x' — *Rests only on the EU summary's 'Model dependencies' line, and that document's own dates are inconsistent.*
- **[unknown]** 'A silent video-model change has shipped' OR 'the video model has never changed' — *Neither is documented. There is no pin or version string for video.*
- **[unknown]** Upload limit stated as a single number (10MB or 20 MB) — *Two first-party sources conflict: Creating on Web says 10MB, web-updates-5 says 20 MB.*
- **[low]** '--ow recently dropped out of the Parameter List' (prior sweep) — *--ow is absent from every Parameter List snapshot checked, 2025-05-03 through today. It was never listed there.*
- **[unknown]** '--end can be combined with Extend / Extend Manual' — *Undocumented.*
- **[unknown]** 'Identity is preserved in the intermediate frames of a start/end clip' — *Undocumented. The docs promise nothing between the endpoints.*
- **[unknown]** 'A frame extracted from an MJ video can serve as a new pose still' — *Documented only step by step, never as a workflow. Frames are 480p/720p-class against 2048px upscaled V7 stills, and fidelity is untested.*
- **[unknown]** Any V7 or --oref retirement date — *None is published anywhere first-party.*
- **[unknown]** 'The midjourney.api client sends / does not send a video version field' — *The client is not vendored or available locally, and MJ publishes no API.*
- **[unknown]** 'The account is on Pro/Mega' — *Not verified. Relax video requires Pro or Mega per the docs.*
- **[unknown]** 'The alpha Animate breakage (fixed 2026-09-16) affected production' — *The changelog is scoped to alpha.midjourney.com only.*
- **[unknown]** Pixel size of the cdn_variant_url grid variant — *Undocumented.*
- **[low]** EU summary dates ('Last update: March 17, 2026', 'placed March 17, 2026') used to date the video model — *These dates conflict with the Version doc's V8.1 (2026-04-14) and V8.2 (2026-07-24) release dates.*
- **[low]** 'Current default version is V7' (Legacy Features) — *Contradicted by the Version doc ('The current default Midjourney version is V8.2'). Both were updated 2026-09-01. Not adjudicated.*
- **[unknown]** Whether --oref runs in Fast Mode — *First-party sources are ambiguous: the Omni doc says it is not compatible with Fast Mode, while the GPU Speed Fast-cost table and the fast-mode-for-v7 post describe --oref Fast costs. Out of scope (IMAGINE_MODE is closed).*
- **[low]** --ow lower bound (0 vs 1) — *The launch post says 0–1000 and the doc says 1–1,000. Irrelevant at --ow 160.*
- **[low]** HD video launch date given as '2025-08-06' without a timezone — *The post was published 2025-08-07T01:29:13Z, which is Aug 6 only in US Pacific. Give the date in UTC or state the timezone.*
- **[low]** 'autogen's payload matches MJ's documented API exactly' — *MJ documents only the web UI and Discord, and 'does not provide an API'. The field names belong to a third-party client. The features match; the interface does not.*
- **[low]** 'V8.0 retirement is the precedent for how V7 will be retired' — *V8.0 was an alpha-only model retired after two weeks' notice. Applying that to V7 is an inference from a single case.*
- **[low]** '--oref first appears in the Parameter List from 2025-12-02' (independent verifier) — *Re-check found --oref already present in the 2025-09-05 snapshot.*
- **[unknown · gap G4]** Whether the EU summary's 'Model dependencies' or 'Last update' text was ever different. There are no Wayback captures, and Zendesk exposes no public revision history. Zendesk metadata only shows the body unchanged since 2026-08-11T21:29:00Z; the first 9 minutes after creation (21:20:22Z to 21:29:00Z) are unobservable.
- **[unknown · gap G4]** Whether the weights served under vid_1.1 / 'video 1' have ever been retrained, on V8.x or otherwise. The client-side identifier has not changed since 2025-06-17, and MJ has changed image weights under unchanged version strings before, so the client cannot reveal this.
- **[unknown · gap G4]** What the '.1' in 'vid_1.1' means. It predates the public V1 launch (2025-06-17 bundle), and no first-party text explains it.
- **[unknown · gap G4]** How the server routes video jobs, and whether routing depends on the image model or the start image's provenance. Only the client payload is visible, and it carries no image version.
- **[unknown · gap G4]** The live 2026-09-24 web bundle. midjourney.com returns a Cloudflare 403. The latest verified bundle is 2026-09-19 (clientSideEntry-rx83xj3k.js), which the 2026-09-21 homepage capture still loads.
- **[unknown · gap G4]** The Discord bot's video job type and version handling. Not accessible.
- **[unknown · gap G4]** What autogen's third-party midjourney.api client (only on hil) sends as videoType. Secondary reverse-engineered clients send 'vid_1.1_i2v_start_end_480' for start/end jobs, but that client itself is not verified.
- **[unknown · gap G4]** Semantics of the undocumented '--length 2.5|5' video flag, and whether it affects the server-side model.
- **[unknown · gap G4]** Whether a V7-era or video-V1-specific EU training summary exists outside docs.midjourney.com. None is in the help center. Under EC point 33, models placed before 2 August 2025 have until 2 August 2027.
- **[unknown · gap G4]** What the NA() helper (parent-image version 7/8/8.1/8.2/niji 6/niji 7 plus personalization or sref) gates in the UI. It was seen only in feed and rendering code, not on the submission path.
- **[low · gap G4 verifier flag]** c18/answer: the params list 'keeps only --raw, --motion, --length and --end ... skips every other flag, including --v' is inaccurate. The first-party Video doc lists '--motion low, --motion high, --raw, --loop, --end, and --bs #'. The bundle's shared parser honors --bs and the speed/visibility flags, and R2 strips --v before parsing. This is a mechanism error, not a fabricated number.
- **[low · gap G4 verifier flag]** No fabricated version numbers, dates, sizes or hashes found. Every date and version in the answer (2025-06-17/18, 2025-07-02/26/30, 2025-08-07, 2026-03-17, 2026-04-14, 2026-06-11, 2026-07-15/24, 2026-08-11/17/23, 2026-09-16/19/21, 105 articles, 92 posts, 139 JS captures, sha256 prefixes) was re-confirmed this session.

### MJ4 — Non-Midjourney stills: single identity anchor, tunable weight, or edit-from-anchor
- **[unknown]** That Kling Image 2.1 human_fidelity will hold the painted Old-Master face or its brushwork across 59 poses — *No first-party evidence on painted faces; the parameter's existence is documented, its fitness for this character is not*
- **[unknown]** Kling Image 2.1 release date or remaining service lifetime — *Not seen in a first-party source this session; the default model is now kling-v3*
- **[low]** Reproducibility of Kling or Seedream renders — *Neither request body exposes a seed; exact re-render behaviour is undocumented*
- **[low]** 'Edit-from-anchor avoids re-rendering the graph' — *Inference: true only if edited stills are added as new nodes; replacing nodes forces edge re-renders*
- **[low]** The hybrid (non-MJ stills as new nodes, MJ video renders the edges) looking seamless — *MJ docs confirm external start/end frames, but the V7-to-non-MJ face morph along each edge is untested*
- **[low]** 'Derive every node in one hop from the anchor' as best practice — *Inference; Google's first-party doc recommends chaining previous generations instead; neither is measured*
- **[low]** FLUX.2 'maintains character consistency even after multiple sequential edits' — *Vendor claim with no metric; the only measurement is for FLUX.1 Kontext (2025, photo input)*
- **[low]** Qwen-Image-Edit-2511 'mitigate image drift' as evidence about repeated edits — *The README never defines 'image drift'*
- **[low]** LongCat-Image-Edit multi-turn identity consistency — *Vendor claim, no metric*
- **[low]** HiDream-O1-Image 'preserve identity / IP across new scenes' — *Vendor README caption, no metric; the optional prompt agent uses Gemma weights under a separate licence*
- **[low]** Kontext drift result applied to FLUX.2 — *The measured model is FLUX.1 Kontext; no FLUX.2 drift metric exists*
- **[unknown]** Kontext drift result applied to painted faces — *The paper's input was a photo*
- **[unknown]** input_fidelity working on gpt-image-2.5-sunburst / -flare — *The API reference lists it generically; the guide scopes input-fidelity notes to earlier models*
- **[unknown]** A per-image OpenAI price for GPT Image 2.5 — *Only token rates are published; Runway's resale credits are not OpenAI's price*
- **[unknown]** FLUX.2 [flex] price ($0.05 vs $0.06/MP) — *First-party BFL pages contradict each other*
- **[unknown]** FLUX.2 [max] single-anchor edit price ($0.07 vs about $0.10) — *docs pricing.md and bfl.ai/pricing disagree*
- **[unknown]** Whether klein Base 4B/9B LoRA endpoints are on the public API — *The BFL overview and LoRA pages contradict each other*
- **[low]** BFL finetune_strength range, and the stability of the -finetuned endpoint names and prices — *No range documented; public beta, and 'may change before general availability'*
- **[unknown]** Ideogram custom-training minimum (10 vs 15 images) — *Ideogram's tutorial and OpenAPI contradict each other*
- **[unknown]** Ideogram API per-image prices — *The pricing tab is JS-rendered; not seen*
- **[unknown]** Ideogram §2.3.1 / Runway 'Powered by Runway' applying to this offline render — *The clauses are tied to end-user-facing apps; applicability is not stated*
- **[low]** Ideogram image_weight as an identity control — *Documented as resemblance to the input image, not identity*
- **[low]** Recraft strength as an identity control; Recraft V4.1 image-to-image price — *strength is a general similarity knob; only the V3 price is published*
- **[unknown]** Leonardo LOW/MID/HIGH strength on resold Nano Banana Pro / FLUX.2 / Seedream — *The upstream APIs have no such parameter; Leonardo does not document the mechanism*
- **[unknown]** Leonardo price and output terms — *Not retrieved*
- **[unknown]** Adobe Firefly price and output terms — *Not retrieved*
- **[unknown]** Seedream / BytePlus output ownership — *The clause was not found in the BytePlus legal pages fetched*
- **[unknown]** Alibaba Model Studio output ownership — *Not retrieved*
- **[unknown]** Luma uni-1 output terms; Photon weight range — *Not retrieved or not documented*
- **[unknown]** xAI and MiniMax output terms; MiniMax price — *Not retrieved*
- **[unknown]** Training a LoRA on the 59 MJ V7 stills being permitted — *MJ ToS bars reverse engineering 'the Assets' and says nothing about training; unresolved*
- **[unknown]** How the ToS 'automated tools' clause applies to an unattended third-party client — *MJ ToS says 'You may not use automated tools to access ... the Services'; reported, not adjudicated*
- **[unknown]** AuraFace as a valid identity metric on painted faces — *Licence confirmed (Apache-2.0); accuracy on paintings unverified*
- **[unknown]** Gemini 3 Pro Image style references preserving Old-Master brushwork — *The capability exists; there is no evidence on this style*
- **[unknown]** BFL commercial-licence price for the FLUX.2 [dev] / klein 9B weights — *Not published in static pages*
- **[unknown]** FLUX 3 image editing availability date — *Release notes say 'phased', with no date*
- **[unknown]** USO / UNO licence status — *A verifier asserted they are FLUX.1-dev based; not re-checked this session*
- **[unknown]** Runway muse_image provenance — *Not researched*
- **[unknown]** Pixel-exact preservation of unedited regions by any hosted editor — *OpenAI explicitly disclaims it; the others are silent*
- **[low]** Hosted FLUX.2 klein 9B outputs being commercially usable — *Inferred from BFL Developer Terms covering API Outputs generally; no klein-9B-specific statement*
- **[unknown · gap G3]** OpenAI: which policy tier (GA at ≥6 months, or specialized variant at ≥3 months) covers gpt-image-2.5-sunburst/-flare. The model pages do not state a launch stage. The name has no 'preview', which the policy uses to mark preview models.
- **[unknown · gap G3]** OpenAI: whether a dated snapshot guarantees identical weights. The docs say only 'performance and behavior remain consistent'.
- **[unknown · gap G3]** Gemini API: any numeric minimum notice for stable models. None is stated, and stable Veo 3.0 -001 models on the Gemini API got 15 days.
- **[unknown · gap G3]** Gemini: whether the GA gemini-3-pro-image (released May 28, 2026) has the same weights as the Nov 2025 preview. The model page says 'Latest update November 2025'.
- **[unknown · gap G3]** Google: whether GCP Terms §1.4(e) (12 months) applies to retiring an Agent Platform generative model that has a replacement. The clause excepts cases where a 'materially similar' replacement exists.
- **[unknown · gap G3]** BFL: any retirement date or minimum-notice policy for the flux-2-pro / flux-2-klein-9b fixed snapshots. None was found in the docs, release notes or legal pages.
- **[unknown · gap G3]** BFL: when FLUX 3 image synthesis/editing will ship, and when the first dated pinnable FLUX 3 version tag will be published.
- **[unknown · gap G3]** Kling: whether a model_name (kling-v2-1, kling-v3, kling-v3-omni, kling-video-o1) is immutable or can be upgraded in place. The '12/16/2025 V2.6 model upgraded' and '09/15/2026 Virtual Try-On 3.0' entries are ambiguous.
- **[unknown · gap G3]** Kling: any retirement date for kling-v2-1, the only version with human_fidelity. None was announced on the updates page.
- **[unknown · gap G3]** Kling: whether the 30-day clause in §4.1 is meant to cover retiring a model.
- **[unknown · gap G3]** Luma: an explicit GA or preview label for ray-3.2. Only the pricing caveat 'ahead of general availability' was found.
- **[unknown · gap G3]** Luma: how long the X-API-Version deprecation window lasts.
- **[unknown · gap G3]** Luma: the retirement dates for legacy Ray models, which are sent only in per-account notices.
- **[unknown · gap G3]** MiniMax: a numeric notice period, and any snapshot or version-pinning policy for MiniMax-H3 / MiniMax-H3-Max.
- **[unknown · gap G3]** MiniMax: whether the fal.ai post-training of H3-Max creates a separate lifecycle dependency.
- **[unknown · gap G3]** Alibaba: whether wan2.2-kf2v-flash counts as a 'mainline' model (3 months' notice) or some other class, and what the 'legacy' filing in the docs means. The page never defines it.
- **[unknown · gap G3]** Alibaba: the Chinese-language notices linked from the policy page (zh/notice/detail?id=1841, 2009, 1950, 1949, 1938, 1934) render client-side and could not be read. kf2v's absence from the Oct 10, 2026 batch is confirmed only for the six English notices I fetched.
- **[unknown · gap G3]** Higgsfield: any ToS clause on discontinuation. higgsfield.ai/terms-of-service, /terms, /api-terms and cloud.higgsfield.ai/terms all returned 404.
- **[unknown · gap G3]** Change history (Wayback) was not checked for the BFL, Kling, Luma, MiniMax or Alibaba policy pages. Only OpenAI's was bracketed in time.
- **[low · gap G3 verifier flag]** 'Alibaba: 36 days for snapshots' (Notice-actually-given section): no claim ID or URL. Not reproducible today from any English notice. The Jun 08, 2026 snapshot notice gives 124 days.
- **[low · gap G3 verifier flag]** '92–124 days for the Oct 10 batches' is incomplete: the Apr 13, 2026 notice (_731) for the same Oct 10 date gives 180 days.
- **[low · gap G3 verifier flag]** c57 source list names notices '_717/_718 Apr 03' and bare slug suffixes '_7d4/_79e/_7d0'. Slugs built from the base name model_studio_notice_of_retirement_for_selected_legacy_models_<suffix> return 'not found' for 7d4/79e/7d0. The real slugs are ..._legacy_longtail_models_7d4, ..._legacy_mainline_models_79e/_79d and ..._postponed_retirement_of_selected_legacy_models_7d0. '_717/_718' not located.
- **[low · gap G3 verifier flag]** Higgsfield 'None stated' / 'terms URLs all 404': a search miss, not a fabrication. The ToU exists at https://higgsfield.ai/terms-of-use-agreement (Last updated July 26, 2026) and has an explicit model-retirement clause.
- **[unknown · gap G7]** Accuracy of AuraFace-v1, SFace or dlib on paintings, Old-Master-style or other non-photographic faces: no first-party or peer-reviewed evaluation found. The AuraFace card and blog say nothing on it.
- **[unknown · gap G7]** Any evaluation of a face metric on this project's actual case: re-render drift of one generator-made character from a single anchor. All painting studies measure cross-artist sitter identity or diffusion stylization.
- **[unknown · gap G7]** Provenance and training data of AuraFace glintr100.onnx: fal has not answered HF discussion #8 (opened 2025-09-29) or #9.
- **[unknown · gap G7]** Training dataset of the OpenCV Zoo SFace 2021dec weights: opencv_zoo issue #313 has no maintainer answer. Upstream zhongyy/SFace has no licence.
- **[unknown · gap G7]** A cosine threshold for AuraFace: none is published. verify.py's 0.55 is buffalo_l-specific and does not transfer (different latent space).
- **[unknown · gap G7]** InsightFace commercial licence price for buffalo_l: listed only as 'Custom'.
- **[unknown · gap G7]** Numeric results of Huber et al. ICPR 2022: the IEEE/CSDL pages would not render and Semantic Scholar returned 429. Only the dataset description was confirmed.
- **[unknown · gap G7]** The weight licence for timesler/facenet-pytorch: the repo is MIT, but no separate weight licence was found and the VGGFace2 / CASIA-WebFace terms were not checked. Not recommended.
- **[unknown · gap G7]** Whether YuNet (trained on WIDER Face photos) reliably detects faces in painted portraits: not evaluated in any source found. This matters because verify.py fails a clip when no face is detected.
- **[low · gap G7 verifier flag]** c22 source_date 'last commit 2022-01-10' is wrong: the latest commit touching opencv/doc/tutorials/dnn/dnn_face/dnn_face.markdown is 899b4d14 at 2022-02-22T19:55:26Z.
- **[low · gap G7 verifier flag]** Answer's EdgeFace line ('code is BSD-3 but the HF weights are cc-by-nc-sa-4.0') implies the weights exist only on HF. The GitHub repo also ships the weights under BSD-3. The claim is incomplete, though nothing in it is invented.
- **[low · gap G7 verifier flag]** c20 implies the HF mirror is licence-tagged Apache. The HF metadata has no licence tag; only the LICENSE file and README line say Apache 2.0.
- **[low · gap G7 verifier flag]** Overall 'confidence: high' and 'Licence side: closed' are not supported. Training-data licences for YuNet (WIDER FACE CC BY-NC-ND) and dlib (VGG Face CC BY-NC 4.0) were not checked, and SFace and AuraFace provenance is unresolved.

### MJ5 — Non-Midjourney image-to-video with explicit start AND end frames
- **[unknown]** Any ranking of vendors by identity drift or face fidelity — *No first-party drift metrics exist for any vendor; only a pilot can establish it.*
- **[unknown]** Claims that Veo, Kling, MiniMax, Vidu, Wan, LTX, BFL, xAI, PixVerse or Pika produce seamless loops from identical first/last frames — *Undocumented; only Luma (loop flag), Gemini Omni Flash (same-image recipe) and Seedance (identical frames allowed, but disqualified in the US) document it.*
- **[unknown]** Luma `loop` + `start_frame` returns exactly to the start frame — *The doc says 'seamlessly looping' but does not say the loop point equals start_frame.*
- **[unknown]** Luma API output is cleared for commercial public display — *Governing base terms for API PAYG are unstated; the individual ToS has a paid-subscription condition and a Trials clause; pricing is pre-GA.*
- **[unknown]** Wan 3.0 (direct Model Studio) is usable for a permanent public display — *First-party preview-vs-launched contradiction; Preview terms are internal-testing only.*
- **[low]** Gemini Omni Flash per-clip cost of about $0.50 for 5 s — *Token-billed at 'approximately $0.10 per second'; the Gemini API documents no duration parameter; derived arithmetic only.*
- **[unknown]** Vertex AI Veo 3.1 prices — *The pricing unit is printed as '/ 1 count' and is undefined; Vertex 3.1 GA lists pay-as-you-go 'Not supported'.*
- **[low]** Vidu Q2-turbo 540P 5 s exact price ($0.07 vs $0.08) — *'Starts at $0.03, +$0.01/sec' is ambiguous about whether the base includes the first second.*
- **[low]** BFL two-keyframe (ii2v) price equals the i2v rate ($0.17/s hd) — *The pricing page lists t2v/i2v/v2v only; ii2v is inferred.*
- **[unknown]** BFL FLUX 3 aspect ratios (1:1, 9:16) and resolution range — *Not verified in this session.*
- **[unknown]** Pika's own Pikaframes / 'Pika 2.5 Keyframe' API price — *Only the fal reseller price ($0.04/s, 5 s minimum) was captured; the Pika model page is login-walled.*
- **[unknown]** xAI grok-imagine-video-1.5 output ownership / commercial terms — *The x.ai legal pages returned a Cloudflare block.*
- **[unknown]** PixVerse output terms — *Not checked.*
- **[unknown]** Adobe Firefly v3 video price and output terms — *No published per-clip price found; terms not checked.*
- **[unknown]** Kling output aspect ratio for square input — *Only an input-image constraint (1:2.5–2.5:1) is documented; the i2v doc has no aspect setting.*
- **[low]** Canonical MJ stills are exactly 1:1 — *Only the character framing spec says 1:1; data/gen/*.png is not in the repo and autogen.py passes no --ar flag.*
- **[unknown]** Kling minimum prepaid Resource Package spend — *Not captured; per-second $ values are unit conversions.*
- **[unknown]** Rented-GPU cost to self-host Wan2.1-FLF2V, VACE, OmniWeaving or LTX-2.5 — *No published per-clip price gathered.*
- **[unknown]** MiniMax Open Platform ToS effective date (e.g. 'March 30, 2026') — *Not visible on the first-party page; the only date seen was from a secondary source.*
- **[unknown]** Wan 3.0 'public beta since 2026-08-06' — *From a prior sweep; not re-confirmed; current first-party pages say 'Currently in preview' / 'officially launched Aug 24 2026'.*
- **[unknown]** US availability of Kling, Vidu, PixVerse, xAI APIs — *Not checked; only BytePlus was confirmed to exclude the US.*
- **[unknown]** Whether Runway's `wan3` route avoids Alibaba's Preview Product Terms — *Runway's ToS governs Runway outputs, but pass-through obligations were not checked.*
- **[unknown]** Whether Seedance 2.x face moderation would flag painted portrait faces — *Moot for direct use (US-excluded), but unverified for reseller routes.*
- **[low]** Effective Wan 3.0 price after the 'Limited-time 30% off' — *Only list prices were quoted; the discount's duration and base are unclear.*
- **[unknown · gap G1]** Individual subscription tiers: plan names, prices, monthly credit counts and per-tier concurrency. The pricing page https://higgsfield.ai/pricing renders client-side, the r.jina.ai renderer was blocked (403), and Wayback snapshots are empty shells. '3000 credits on the 23rd' and '8 concurrent jobs' come only from upstream's own account measurements.
- **[unknown · gap G1]** Whether any Higgsfield model ID pins weights, either a CLI job_set_type such as kling3_0 or an API endpoint ID such as kling-video/v3.0/std/image-to-video. No first-party pinning or version-freeze statement exists, and ToS §1.7 reserves the right to substitute models.
- **[unknown · gap G1]** Any model deprecation notice period for Developer Access. None exists in the current ToS; the 15-day notice appears only in the July 23 draft that never took effect.
- **[unknown · gap G1]** Whether upstream vendor output or ownership terms (OpenAI, Kuaishou, ByteDance) pass through Higgsfield. Only acceptable-use and prohibited-use policies pass through (ToS §8). Higgsfield publishes no per-vendor terms page.
- **[unknown · gap G1]** US availability of standard (non-Draft) Seedance 2.0 and 2.5 for US subscription, CLI or API users. No explicit first-party statement was found.
- **[unknown · gap G1]** Whether wan3_0 is still a valid CLI job_set_type. It is absent from every CLI doc revision checked; confirming it needs an authenticated `higgsfield model list`.
- **[unknown · gap G1]** The seedance_2_5 CLI flag schema. MODELS.md has no entry; only the skills docs list start_image and end_image.
- **[unknown · gap G1]** Whether Kling O3 image-reference actually honours first_frame_url + last_frame_url + elements together. Only the schema was seen, and upstream found that accepted parameters are not always honoured.
- **[unknown · gap G1]** Output aspect for a square input on API Kling 3.0 image-to-video. The schema has no aspect_ratio field.
- **[unknown · gap G1]** Mapping of Higgsfield API names ('Kling Omni', released 2025-12-01; 'Kling O3', released 2026-02-01) to Kuaishou's names ('Kling 3.0 Omni', 'O1').
- **[unknown · gap G1]** Upstream's claim that the CLI session uses one-time-use refresh tokens. The first-party README says only 'tokens are short-lived. Re-run `higgsfield auth login`.'
- **[unknown · gap G1]** Whether the MIT licence covers the distributed hf binary. The repo holds only docs and an installer; the binary comes from the non-public module github.com/higgsfield-ai/cli-src.
- **[unknown · gap G1]** Which ToS version governed upstream's August 2026 anchor uploads. The 2025 perpetual/irrevocable licence applied to pre-July-26 accounts until 2026-08-27 unless the user accepted the new terms earlier; the account's registration date and acceptance date are unknown.
- **[unknown · gap G1]** Subscription credit prices per model and configuration (for example, 7.5 credits for kling3_0 at 1:1, 5 s, sound off). Higgsfield publishes no credit table; cost appears only on the Generate button or through `hf generate cost`. Upstream measured those numbers.
- **[unknown · gap G1]** The sound-off API price per 5 s clip for Kling 3.0 image-to-video or O3 first-last-frame. The first-party descriptions are ambiguous ('for 1 second clips... 3 or 15 second clips'), and the promo discount has no stated expiry.
- **[unknown · gap G1]** Whether the pipeline's mp4→gif center-crop transcode counts as removing provenance markers under ToS §5.5/§6.4. It is also unknown whether Higgsfield embeds such markers in CLI outputs at all.
- **[unknown · gap G1]** The remainder of the X post's replies. The Community Note (secondary) described the July 23 draft's perpetual licence.
- **[low · gap G1 verifier flag]** API Kling 3.0 std image-to-video 'standard rate starts at $0.084/s' (answer §e, c56): taken from a related_models_description field whose text differs per page (O3 page gives $0.056/$0.112 for the same field). The same page also shows overview price 0.0840/second and says 'Public pricing information is not available'. Not confirmed as this endpoint's price.
- **[low · gap G1 verifier flag]** 'Kling 3.0 Omni element is exposed on the web' and 'kling-video/o3/image-reference' = Kling 3.0 Omni: no first-party page seen equates API 'Kling O3' with 'Kling 3.0 Omni', and the web help article ties Elements to the generic Kling multi-shot flow.
- **[low · gap G1 verifier flag]** 'Higgsfield API launched 2026-09-16': true only for the standalone product announced in the changelog. higgsfield-client 0.1.0 ('Higgsfield API Python SDK', 2025-11-17, cloud.higgsfield.ai) shows an earlier API existed.
- **[low · gap G1 verifier flag]** 'Per-tier numbers for individual plans could not be confirmed' and 'Higgsfield publishes no credit table': Higgsfield's own blog (Sep 15, 2026 / Jun 26, 2026) publishes Starter/Plus/Ultra credits (200/1,000/3,000), Ultra concurrency (8 video + 8 image), and sample per-clip credit costs.
- **[low · gap G1 verifier flag]** 'The July 23 version is marked did not take effect': the banner says only the scheduled Aug 7 effect for existing users did not happen. That version said it was effective immediately for users registering on or after July 23, 2026.
- **[low · gap G1 verifier flag]** Process counts in commands_run ('all 67 help-center articles', '13 snapshots') were not reproduced. The creator-hub sitemap lists 95 non-changelog URLs, including category pages.
- **[unknown · gap G2]** Positive confirmation that US-resident customers can sign up, pay and call the Kling API. No first-party list of supported countries or payment regions was found, and no US exclusion was found either. The only secondary result (videoai.me, milvus.io) is not usable as evidence.
- **[unknown · gap G2]** Whether a painted or Old-Master (non-photographic) face is accepted as an image_refer element and passes content moderation. Only realistic-only for video_refer is documented; the consumer guide lists anime/CG/fantasy characters.
- **[unknown · gap G2]** Whether elements expire, count against an API-account quota, or fall under the 30-day purge of generated results. Only consumer-app quotas (30–500 elements by membership tier) are documented.
- **[unknown · gap G2]** API price of creating an element (final_unit_deduction exists in the response; no row in the pricing tables). 'Free' is stated only for the consumer app.
- **[unknown · gap G2]** Whether attaching an element changes per-second video billing beyond what the pricing table shows; the table has no element dimension.
- **[unknown · gap G2]** Output aspect ratio for a 1:1 first/last frame on /image-to-video/kling-3.0 (no aspect setting), and whether the 3.0 Omni aspect_ratio 1:1 is honoured when a first frame is given.
- **[unknown · gap G2]** Any first-party measurement that an element reduces face drift between the endpoints; only qualitative marketing claims exist ('effectively solves the pain point of subjects losing their shape').
- **[unknown · gap G2]** Whether the legacy (model_name-style) image2video API offers element + image_tail for kling-v3. The legacy docs are not in llms.txt and were not fetched.
- **[unknown · gap G2]** Meaning of 'kling-video-o3' in the elements page ('Video-customized elements are only supported for kling-video-o3 and later models'). No other first-party page defines that model id.
- **[unknown · gap G2]** Wayback dating of when the 'First_frame & last_frame & element' examples were added: the Wayback CDX returned 'Temporarily Offline'.
- **[low · gap G2 verifier flag]** None of the version numbers, model IDs, prices, dates or limits in the answer is fabricated. Each was re-seen on a first-party kling.ai page on 2026-09-24.
- **[low · gap G2 verifier flag]** Inference presented as documentation: 'multi_shot defaults to true, so it must be set to false for a single shot'. The doc says only 'When set to false, multi-shot prompts will not produce multi-shot output.'
- **[low · gap G2 verifier flag]** Overstatement: 'The only billing axes are audio, video input, motion control and resolution'. The table also has a Voice Control axis.
- **[low · gap G2 verifier flag]** '$0.42' for a 5 s, 720p clip is the researcher's own arithmetic (0.084 x 5). It is labelled as such and is correct against the table.

### MJ6 — The third-party midjourney client + official API + ToS on automation
- **[unknown]** Any identity, repo URL, author, license or commit date for the midjourney.api client — *Not found in any public or local source. It is private and vendored.*
- **[unknown]** 'midjourney.api passes the prompt string to Midjourney unchanged', or 'passes any reference flag, including several URLs, through' — *The only first-party evidence is that autogen.py puts --oref/--ow/--v into the prompt argument. The client's own code is unreadable.*
- **[low]** 'The v8.1 error proves Midjourney's server parsed --oref from the prompt text' (researcher claim c27) — *The error named --version 8.1 while the version came from the account default, not the prompt. The error could also come from client-side validation.*
- **[unknown]** 'Midjourney's web API accepts several image-prompt, --sref or --edit URLs as prompt text' — *Midjourney documents that syntax only 'in Discord'. The web uses UI slots.*
- **[low]** Web wire format: POST /api/submit-jobs; metadata counters imagePrompts/imageReferences/characterReferences/depthReferences; t:'imagine'/'video'; newPrompt; bucketPathname; /api/job-status — *Secondary reverse engineering only (egaki, WilliamJizh, bucagdas, JuyeongYi). Midjourney does not document it.*
- **[low]** videoType value 'vid_1.1_i2v_start_end_480' (or 'vid_1.1_i2v_480') — *Secondary only, and the secondary sources disagree with each other.*
- **[low]** 'Metadata reference counters are cosmetic when the reference is a URL' — *A single secondary claim (bucagdas), not confirmed first-party.*
- **[low]** 'cdn.midjourney.com / midjourney.com sit behind Cloudflare bot protection, which is why curl_cffi is needed' — *Secondary (egaki AGENTS.md) plus one verifier's curl observation, which the reconciler did not re-check.*
- **[low]** 'Midjourney's wire value for relax mode is "relaxed"' — *Only the project's own comment (autogen.py L90-92) supports it. A secondary client sends 'relax'. No Midjourney source.*
- **[low]** 'The client comes from kernel/midjourney in the private monorepo' — *Inferred from one prompt note, 'kernel.midjourney.generate_video'.*
- **[low]** 'deploy_hil.py ships midjourney/ to hil' — *Inferred from 'midjourney' missing from EXCLUDE_DIRS. Only the host .gitignore entry is explicit.*
- **[unknown]** 'hil runs Midjourney V7 today' or 'hil runs Higgsfield today' — *First-party sources contradict each other (contradiction #1).*
- **[unknown]** 'hil's graph is 257 nodes / 1462 edges' presented as current — *From an upstream doc headed 'Written 2026-08-09'. It contradicts local MODEL_STACK.md and is not re-checked on hil.*
- **[unknown]** '4 Higgsfield successes since the cutover' presented as a current count — *The count is as of about 2026-08-09, not today.*
- **[unknown]** Cause of the 403s since 2026-07-02, including 'the account was banned' — *Upstream says it did not determine the cause.*
- **[unknown]** 'lp-gen runs C:\living-portraits\.venv\Scripts\python.exe' — *Upstream lists bare 'pythonw' (as of 2026-08-09). The interpreter must be resolved on hil.*
- **[low]** 'A site-packages midjourney on hil must be the empty PyPI placeholder' — *midjourney-py 1.0.4 also installs a top-level midjourney package.*
- **[low]** '--ow is deprecated or removed' — *It is missing from the Parameter List but still documented in the Omni Reference article (1–1,000, default 100).*
- **[low]** Prior-sweep wording that the Omni Reference doc says 'not supported in V8.2' — *That phrase is not in the current article (updated 2026-09-01). Today's text reads 'can only be used with Midjourney version 7' and 'When using V8.X, use the Edit Model instead'.*
- **[low]** Upstream CHANGELOG claims 'Midjourney could only animate forward from a single still' / 'the old path faked the return' — *Contradicted by the Midjourney Video doc (--end) and by the project's own 2026-07-11 code (contradiction #2).*
- **[low]** 'API keys are restricted to the Midjourney Enterprise dashboard' (WebSearch/SEO summaries) — *No first-party source. Midjourney's only API post is the 2025-07-16 survey.*
- **[unknown]** Any claim that Midjourney granted this project an API or automation exception — *No evidence either way.*
- **[unknown]** 'The web UI's multi-image picker equals multi-reference support in the web API' — *The UI statement does not establish API behaviour.*
- **[low]** web-updates-4 'strip irrelevant parameters (--cw/--ow)' presented as proof of the web API wire format — *It only hints that the web app handles these as prompt parameters.*
- **[unknown]** 'No private repo holds the client' — *GitHub code search indexes public default branches only.*

### A — sherpa-onnx per-phoneme durations / alignments (lip-sync without GPL)
- **[low]** Researcher's exact Piper figures '28 phoneme IDs / 91 frames / 23296 samples' — *Not reproducible: the input was not recorded and VITS durations are stochastic at noise_w=0.8. Use the reconciler's recorded run instead (31 ids; noise_w=0 gives 96 frames / 24576 samples).*
- **[low]** Researcher's callback chunk sizes (25344, 0.5), (29952, 1.0) — *Input text not recorded; the verifier got different sizes. Only the structural result (one chunk per sentence) is reproducible.*
- **[low]** 'export via kokoro-onnx (MIT)' for sherpa's Kokoro int8 v1.0 graph — *Contradicted by sherpa's run.sh (its own export, then add_meta_data, then quantize). The kokoro-onnx model_url is a hard-coded metadata string.*
- **[unknown]** Calling alan-medium / jenny_dioco-medium 'MIT voices' — *Only the repo-level HF tag says MIT. The per-voice MODEL_CARD chain leads to the lessac research-only licence, and for alan also to an 'All Rights Reserved' dataset. This is an unresolved first-party contradiction.*
- **[unknown]** Legal status of espeak-ng as a subprocess vs in-process (ctypes/static), and of sherpa-onnx wheels labelled Apache while embedding espeak-ng — *These are linking facts, not legal conclusions; no counsel or authoritative ruling was consulted.*
- **[low]** Hop length 256 applies to all Piper voices — *It is the piper1-gpl default, but it was measured on alan-medium only.*
- **[unknown]** w_ceil / Kokoro durations are 'lip-sync accurate' — *Totals are exact by construction, but per-phoneme timing was not compared with a forced aligner or checked perceptually.*
- **[unknown]** sherpa-onnx 2.0.0 timing or feature set — *Issue #3731 is open with no milestone and no v2 tag.*
- **[unknown]** OpenPhonemizer suitability for en-gb-x-rp voices — *The project is archived, alpha, and unmaintained; British RP accuracy was not tested.*
- **[unknown]** Durations output in fp32 Kokoro v1_0 / v1_1 sherpa graphs, and in the kokoro-onnx library runtime — *Only the int8 v1_0 graph was inspected.*
- **[unknown]** Licence and provenance of misaki gb_gold/gb_silver dictionaries (the source of lexicon-gb-en.txt) — *Only the repo-level Apache-2.0 was checked.*
- **[unknown]** MFA transitive dependency and model licences — *Only the repo-level licences (MIT, CC-BY-4.0) were checked.*
- **[unknown]** Kokoro-82M training data including synthetic audio from closed commercial TTS — *Stated on the model card; any downstream terms-of-service effect is unassessed.*
- **[unknown · gap G8]** Licence of CORAAL v2021.07, the version MFA lists, from a page for that version. The current first-party page covers v2023.06 (CC BY-NC-SA 4.0). The Wayback Machine went offline mid-session and lingtools.uoregon.edu was unreachable.
- **[unknown · gap G8]** Whether non-commercial or share-alike terms on training corpora bind the CC BY 4.0 english_mfa model. This is a legal question and was not resolved.
- **[unknown · gap G8]** Provenance of Gentle's kaldi-models-0.04 acoustic model. The folder name matches Kaldi's ASpIRE tdnn_7b recipe (Fisher English, LDC), but nothing first-party names it.
- **[unknown · gap G8]** Whether english_uk_mfa / english_mfa v3.1.0 dictionaries (GitHub) come from WikiPron. Only the HF v3.3.0 card states 'Source: wikipron'; the v3.1.0 README is silent.
- **[unknown · gap G8]** A runtime trace that MFA 3.4.2 never calls sox or ffmpeg on wav input. This is based on grep of the MFA and kalpy source only.
- **[unknown · gap G8]** MFA was not run end to end, and alignment accuracy on synthetic British TTS audio (VoxCPM2, Chatterbox, Kokoro) was not measured, for either english_us_arpa (US ARPAbet) or english_mfa.
- **[unknown · gap G8]** Pretraining data licence of wav2vec2-lv-60 checkpoints (Libri-Light), and training data of NVIDIA parakeet CTC models (only HF licence tags checked).
- **[unknown · gap G8]** Licences of MFA English G2P models beyond the HF card metadata. They are needed only for words missing from the dictionary.
- **[unknown · gap G8]** Whether the deploy host 'hil' is Windows. A win-64 solve was run in case it is; its GPL set matches linux-64.
- **[low · gap G8 verifier flag]** Practical chain says 'english_us_arpa v3.3.0 acoustic model, dictionary and G2P': there is no v3.3.0 G2P. Tag v3.3.0 contains no g2p/; the G2P on main is version 3.2.0 (meta.json).
- **[low · gap G8 verifier flag]** Practical chain says 'mfa align_one' for the HF v3.3.0 model. In MFA 3.4.2 HF models load through 'align_one_hf'; 'align_one' takes legacy files (GitHub v3.0.0).
- **[low · gap G8 verifier flag]** c5: 'gst-plugin, whose file declares LGPL'. The file header is Apache-2.0; only a GStreamer registration string says "LGPL".
- **[low · gap G8 verifier flag]** c17: the quote is attributed to config.py, but 'sqlite:///' is in abc.py:378 and 'SOX = 2' is in data.py:360.
- **[low · gap G8 verifier flag]** c34: 'dictionary source is wikipron, 266,823 words' holds only for the HF main card. GitHub v3.0.0 cites Prosodylab-aligner (199,858 words). The tag v3.3.0 card also gives different LibriSpeech hours (976.90 vs 982.10).

### B1 — Local expressive TTS — description/instruction-controlled voice design
- **[low]** FP32 weight footprints: VoxCPM2 about 9.5 GB, Qwen3-TTS-VD about 8.4 GB — *My arithmetic (params x 4 bytes + codec files as stored). Excludes activations. The speech_tokenizer's stored dtype was not checked.*
- **[low]** VoxCPM2 FP16 'should work' by editing config.json — *Guess by a GitHub CONTRIBUTOR (not a verified maintainer). The reporter saw no speedup. VoxCPM's own code says fp16/bf16 drift glitches output on MPS.*
- **[low]** VoxCPM2 ~13 GB peak on a 2080 Ti 22G — *One user's anecdote with a 3-minute reference clip; dtype unknown.*
- **[low]** VoxCPM2 CPU speed (1.56 it/s, or any 'x-times realtime' derived from it) — *One user log on a Core Ultra 7 255H; not the i9-9900K; the realtime ratio would be a derivation.*
- **[low]** VoxCPM2 GGUF via llama.cpp-omni fits ~3.55 GB and runs on Turing CUDA — *File sizes are real, but the GGUF is a third-party conversion. F16/Q8_0 correctness on sm_75 is untested, and the RTF 1.76 figure is for Apple M4 Pro/Metal only.*
- **[low]** Community Qwen3-TTS VoiceDesign GGUF (cstr) and its 'slight British accent' example — *Third-party, unverified. Qwen warns its code predictor is 'extremely sensitive to precision'.*
- **[unknown]** Any claim that Qwen's docs show a 'British English accent' example — *Came from a web-search summary; no British example appears in any Qwen first-party file.*
- **[low]** Maya1 is derived from Llama 3.2 3B (Llama license obligations) — *Inferred from config shape and a secondary (unsloth) mirror comparison; the card says 'pretrained' and declares no base_model.*
- **[low]** A fixed seed keeps Maya1's voice constant across lines — *Only a one-word org-member reply ('seed.'); no documentation or test.*
- **[low]** MOSS '1.7B needs 12 GB' applied to MOSS-VoiceGenerator specifically — *The collaborator's figure is for a generic '1.7B' model (incl. tokenizer, on L20), not stated for VoiceGenerator.*
- **[low]** FireRedTTS3-Instruct ~2.1B parameters — *Derived from file size; no first-party figure.*
- **[unknown]** FireRedTTS3 acoustic edits are template-only (or free-form) — *The first-party card says both.*
- **[low]** Cross-report InstructTTSEval numbers for Qwen3-TTS-VD (78.4/78.8/72.0 from MOSS; 76.4/81.4/64.2 from FireRed) — *Secondary for Qwen; Gemini-judged; they disagree with Qwen's own 82.9/82.4/68.4.*
- **[unknown]** Relative British-accent quality of VoxCPM2 vs Qwen VD vs Maya1 — *No first-party or independent measurement exists; must be A/B listened.*
- **[low]** Qwen3-TTS OpenVINO CPU path as a shipping option — *Only on optimum-intel main (merged 2026-09-16); not in the v2.2.0 release; speed unknown.*
- **[unknown]** Qwen3-TTS-VD FP32 fits on the 11 GB card with activations — *VRAM not documented; only weight arithmetic available.*
- **[unknown]** Parler-TTS can render a British accent from a description — *Not documented on the model cards.*
- **[unknown]** VoiceSculptor-VD is Apache-2.0 clean — *Its declared base Llasa-3B is CC-BY-NC-4.0; unresolved first-party conflict (moot: Chinese-only).*
- **[low]** IndexTTS-2.5 as a clone partner with text-described emotion for designed voices — *An untested combination proposed by the verifier; no source documents it for this use.*
- **[unknown]** MFA English v3.1.0 gives accurate phone timings on synthetic theatrical British speech — *Not measured anywhere.*

### B2 — Local expressive TTS — reference cloning + emotion/style controls
- **[low]** Chatterbox runs FP32 on Turing by default — *Inferred from source (no dtype cast in tts.py/t3.py), not documented; not run on a 2080 Ti.*
- **[low]** Chatterbox will reproduce a British/RP accent from simon_evers or ruth_golding — *Vendor documents accent inheritance only for cross-language transfer; not tested.*
- **[unknown]** Chatterbox (any variant) fits alongside ~7 GB Ollama in 11 GB — *Only checkpoint sizes seen (~3.2 GB fp32 files); runtime VRAM not measured.*
- **[unknown]** Turbo/Nano [sarcastic]/[dramatic]/[narration]/[whispering] tags produce the intended delivery — *Tokens exist in added_tokens.json; behaviour undocumented.*
- **[unknown]** chatterbox-flash has a '520M decoder' — *Only a config label 'Llama_520M' was seen by the verifier; no first-party parameter count. Dropped.*
- **[unknown]** chatterbox-flash works on Turing with --dtype fp16/fp32 — *Override is documented; Turing behaviour untested.*
- **[unknown]** Chatterbox Nano is 3x realtime on the i9-9900K — *Vendor figure is for an unspecified 8-core CPU.*
- **[low]** Chatterbox Multilingual V3 improves British accent retention in English — *Card claim is about accent preservation 'across languages'; English-to-English not addressed.*
- **[unknown]** Zonos v0.1-transformer runs on the RTX 2080 Ti — *bf16 hard-coded in model.py; HF card and GitHub README contradict each other on GPU support.*
- **[unknown]** ZONOS1-GGUF F16 as a Turing workaround — *Its runtime repo zonos1.cpp returns 404.*
- **[unknown]** IndexTTS-2/2.5 is licensable for a permanent public MIT installation — *Custom bilibili license reaches outputs, allows revocation; README routes commercial use to bilibili. Needs legal read.*
- **[unknown]** Qwen3-TTS VoiceDesign can produce a convincing British RP reference on Turing — *No British preset; examples use bf16 + FA2; untested.*
- **[unknown]** VoxCPM2 runs cleanly in fp16 on CUDA Turing — *Vendor code says bf16/fp16 drift glitches output on MPS; CUDA Turing untested; fp32 memory unknown.*
- **[low]** karen_savage2 is RP — *Not from the Celebration of Dialects volumes; Voice-Zero says such labels are 'often based on guesswork'.*
- **[unknown]** simon_evers is a baritone / ruth_golding and karen_savage2 are mezzos — *No listening done.*
- **[low]** Chatterbox 'randomly shouts curse words' — *Secondary field report from the Voice-Zero maintainer, not a vendor statement; use only as a reason to review output.*
- **[unknown]** Orpheus presets are American — *First-party README lists English presets without saying 'American'. Dropped.*
- **[unknown]** Higgs TTS 3 inference code is Apache-2.0 — *No first-party source ties Higgs TTS 3 code to the Apache-2.0 higgs-audio repo. Dropped.*
- **[low]** MOSS-VoiceGenerator is 1.7B — *Card table says 1.7B; verifier saw HF safetensors 2,114,118,656 params; not re-checked here.*
- **[low]** ~4 GB free VRAM beside Ollama — *Arithmetic from the brief, not measured on supercommons2.*
- **[unknown]** Orpheus weights are purely Apache-2.0 — *base_model is Llama-3.2-3B-Instruct; whether Llama license terms attach is unresolved.*
- **[unknown]** Dia2 usable for a permanent public installation — *Apache-2.0 license vs 'intended for research and educational use' disclaimer on the same card.*
- **[unknown]** VibeVoice usable commercially — *MIT tag vs 'limited to research purpose use'.*
- **[unknown]** pocket-tts-timestamped fork license — *Not checked.*
- **[unknown]** kyutai voice-donations include usable British voices — *Not enumerated.*
- **[unknown]** GPL espeak-ng runtime dependency (Kokoro British path, Zonos) is acceptable — *Policy call, same as piper-tts in MODEL_STACK.*
- **[unknown]** Any ranking of models by quality on the Phineas/Seraphina registers — *No listening comparison done.*

### C — Qwen3.5-9B thinking default + ollama#14579 throughput scope
- **[low]** TsengSR's #14579 figures (17 tok/s at 32k, 25 at 16k, 40 at 8k context for qwen3.5-27b) — *No GPU model or quant named; only '24 GB VRAM' implied. Violates the attribute-every-number rule.*
- **[low]** '12tk/s vs 35tk/s' (Ollama vs llama.cpp, Qwen3.5-27B) from the #14579 author — *From a different comment than the matched-16k-context claim; the author's llama.cpp 35-40 tk/s was stated at 60-120k context; GPU not restated. Not a matched measurement.*
- **[low]** 'Qwen3.5-35B quant runs at 140tk/s' on llama.cpp (#14579 author, 2026-03-26) — *No hardware, quant, or version stated.*
- **[low]** rick-github's #14861 tps table (qwen3.5:35b 89.27 vs unsloth UD on llama.cpp engine 218.86) — *No hardware stated; MoE; pre-v0.30.0 engine.*
- **[low]** '40~50 tokens/sec (for 35b:a3b, 9b, and 4b)' on M3 Ultra (#14662) — *The only 9B tok/s seen: Apple Silicon, quant and Ollama version not stated, compared with qwen3-vl:8b rather than llama.cpp; irrelevant to CUDA/Turing.*
- **[low]** '0b14b87d7 give: 27.47 tok/s' (#25162 close comment) — *The close comment does not restate model or GPU. 0b14b87d7 is a master tip, not the fix. Measured on upstream llama-server, not Ollama.*
- **[unknown]** llama.cpp #25185 as 'the fix' for the Turing qwen35 regression — *Suggested by users (#25162, #14861 comment); no Turing test result posted; the PR title scopes it to FA kernels while the regression names SSM kernels.*
- **[unknown]** Any claim that Ollama >= v0.32.6 restores qwen35 throughput on the 2080 Ti — *Only build containment is verified; recovery through Ollama's qwen35 blob path is unmeasured.*
- **[low]** /api/show thinking output for qwen3.5:9b ({false,true}, default true) — *Read from source (qwen35.go, model_thinking.go); not executed.*
- **[low]** Behaviour of '/no_think' text on qwen3.5:9b ('will still start with thinking' per #14716) — *Single user report; the card only says the soft switch is 'not officially supported'.*
- **[low]** Unsloth HF GGUF in Ollama defaulting thinking OFF via llama-server chat_template — *Inference from a code comment in llm/llama_server.go; untested; Unsloth doc says no Qwen3.5 GGUF works in Ollama (possibly stale).*
- **[low]** Unsloth doc 'reasoning is disabled by default' for 4B/9B as a statement about the Qwen model — *Contradicted for the Qwen model by Qwen's card and template; true only of Unsloth's inverted GGUF templates.*
- **[low]** #14715 qwen3.5:9b Xid 43/31 crash on RTX 2080 Ti — *Single report on a modified 22GB card, Ollama 0.17.5, placeholder driver/log fields, closed NOT_PLANNED without logs.*
- **[low]** #17434 JSON-schema + think:false CUDA crash (qwen3.6:35b, 0.32.5, DGX Spark GB10) — *User report, different model/hardware; the repo uses format 'json', not a schema.*
- **[low]** #14850 2026-07-17 comment that qwen3.5:27b with think=False still ignores a complex format — *User comment, Ollama version not stated, issue closed as duplicate.*
- **[low]** #18152 Windows TDR crash on 0.33.x with qwen3:8b — *Single user report; hil's OS not confirmed here.*
- **[low]** #16685 qwen3.5:9b long-form collapse with think=false — *Single user report on Vulkan/CPU at ~3-4k generated tokens; the brain emits short JSON.*
- **[low]** #17218 qwen3.5:4b figures (321.6 s -> 617.2 s; 81.4% -> 64.2%) — *Single user report; image-heavy VQA on an RTX 3070 Laptop; not text throughput and not the 9B.*
- **[low]** #15771 Qwen3.6-35B-A3B Ollama 0.21.0 vs llama-cli numbers on RX 7900 XTX — *AMD ROCm, MoE, pre-v0.30.0 engine; quant not re-verified; irrelevant to the 9B on Turing.*
- **[unknown]** Ollama 'released on' dates for v0.30.0, v0.31.2, v0.34.4 — *GitHub publishedAt predates the contained merges and tag commits (e.g. v0.31.2 publishedAt 2026-07-06 vs PR #15901 merged 2026-07-07; v0.34.4 publishedAt 02:24Z vs tag commit 23:36Z the same day). Tag containment is reliable; dates are not.*
- **[low]** Ollama version '0.7.15' in #14579 body — *Verbatim but implausible; likely a typo.*
- **[low]** phreer/ollama 82516fd as a fix for #14579 — *Fork-only memory-estimation change; never found upstream; not a throughput fix.*

### D — Local-brain bake-off shortlist under 7 GB (Ollama)
- **[low]** 'The director holds ~8GB' of VRAM with qwen3:8b — *An internal repo note (pipeline/_bake.py:24), not a measurement, and not a first-party vendor source.*
- **[unknown]** Any runtime VRAM figure for any candidate on the 2080 Ti — *Not measured; the file size is not the footprint.*
- **[unknown]** Tokens/sec or latency on Turing, including whether the dense qwen3.5:9b shares the throughput gap in ollama/ollama#14579 — *No primary measurement was found or run.*
- **[low]** 'Ollama structured outputs are model-agnostic' as a literal Ollama statement — *The docs state no model restriction and exclude only Ollama Cloud. 'Model-agnostic' is an inference, and per-model version bugs existed (qwen3.5 until 0.31.2, gemma4 until 0.21.1).*
- **[unknown]** Unsloth's claim that Qwen3.5-9B does not think by default — *No Unsloth URL was seen this session; it appears only via MODEL_STACK.md:245. All first-party sources say thinking is on by default.*
- **[low]** Ministral-3-8B 'released 2025-10-31' — *That is the HF repo createdAt. The first-party announcement date is December 2, 2025.*
- **[low]** Granite 4.2 'shipped with num_ctx 131072' — *Issue #18074 never quotes the removed PARAMETER num_ctx value; 131072 is the GGUF context_length.*
- **[low]** Stage-manager prompt of about 600 tokens — *A verifier estimate from file byte counts, not re-measured and not tokenised.*
- **[unknown]** The minimum Ollama version for granite4.2:8b — *The tag declares no 'requires'. v0.30.0 is only the first release whose source contains the llama-server chat-template path.*
- **[low]** Excluding lfm2.5:8b-a1b — *A judgment call on a revenue-threshold licence, not a non-commercial licence; not a rule-5 disqualification.*
- **[unknown]** The OLMo 3 HOLD rationale that it is 'research-only' — *The licence is Apache 2.0. The 'intended for research and educational use' sentence needs a legal reading.*
- **[low]** Ollama page 'Updated N weeks/months ago' ages — *Relative dates that change daily; not usable as release dates.*
- **[unknown]** Byte-identity of Ollama GGUFs with the official HF checkpoints — *Not checked. The GGUF headers for qwen3.5 carry no organization field.*
- **[unknown]** In-character voice quality and JSON-adherence rankings of the candidates — *Only the bake-off can establish these.*

---

*Generated 2026-09-24. The per-track evidence, including every source with its first-party or secondary status and date, is in `research/MODEL_STACK_EVIDENCE.md`. Re-verify before acting: vendor pages move, and Midjourney in particular changes in place without notice.*

# Model-stack research — evidence appendix (2026-09-23/24)

Companion to `MODEL_STACK_RESEARCH.md`. This file is generated, not hand-written: it holds the full reconciled answer, the numbered source list (FIRST-PARTY / secondary, with dates), unresolved contradictions, could-not-confirm items and dropped claims for each of the 11 research tracks, followed by the 8 gap-fill results and their verification. Numbered citations like [12] inside a track refer to that track's own source list.

Pipeline: research → verification (3 independent lenses for MJ1–MJ6; one combined lens for A–D) → reconcile (refuted claims dropped) → completeness critic → gap-fill + verification → synthesis → red-team. Sources were accessed 2026-09-23 (tracks) and 2026-09-24 (gaps).

---

# Track MJ1 — Midjourney deprecation track record, stated policy, and notice given
Primary mission track: yes · Final confidence: medium

## Answer
## Direct answer: how much warning before V7 or --oref stops working?

**Guaranteed warning: 0 days (high confidence).** No Midjourney source promises that an old version will stay available for any length of time.
- The ToS says: "Please do not create any dependencies on any attributes of the Services" and "We reserve the right to modify or discontinue any aspect of the Service, including pricing and features, at any time." [1]
- The only advance-notice promise anywhere in MJ's docs covers changes to the Privacy Policy, not models ("prior to the change becoming effective") [3].

**Written warning seen before default or behaviour changes: 0 days (high confidence for docs, updates.midjourney.com and X).**
- V6.1 became the default the same day it was released [11].
- V7 had about 25 days of undated hints before it became the default [13][14][12].
- V8.1 was announced after the switch. The Version doc already showed V8.1 as default at 2026-06-11T02:33Z [20]. The X post (04:02Z) [9] and the updates post (04:08Z) [8] came later. The only updates post between 2026-04-30 and the switch is from 2026-05-27 and says nothing about a default change [18][60].
- V8.2 became the default the same day it was released [10].

**Retirement of a numbered model: seen once, and only for an alpha model.**
- V8.0 got informal warnings from 2026-03-21 [15][16] and a formal "in two weeks" notice on 2026-06-11 [8][9].
- It was actually removed on 2026-07-24 [4], 43 days after the formal notice. The docs still called it "still available for a limited time" on 2026-07-20 [22].
- No production version from V1 to V7 is documented as unavailable. The only "no longer available for use" line is about V8.0 [4].

**Where V7 / --oref stand today (2026-09-23):**
- Both are still documented as working. The Omni Reference doc says "Omni Reference is compatible with Midjourney version 7" [7], and the Version chart marks Omni Reference as supported on V7 [4].
- No retirement announcement was found in updates posts up to 2026-09-24T01:59Z [65][18] or on the @midjourney X timeline up to 2026-09-16 [64].
- --oref is now at its most exposed point:
  - The Edit Model is described as "(replacing omni-reference)" [26] and "replaces Omni Reference, Character Reference, and the Retexture tool" [4].
  - The Parameter List now reads "(replaced by the Edit Model in V8.X) --oref" [6].
  - The documented fallback from V8 to V7 for oref ("will automatically run the prompt in V7" [29]; "(Uses V7)" in the chart [21]) is gone from today's docs [4][7].
  - The web "Image Reference Types" list on the Omni page no longer includes Omni Reference [7] (it did on 2026-06-11 [29]). The Discord `--oref` path is still documented [7].

**Most likely retirement path, based on precedent (low confidence):**
1. --oref gets relabelled into Legacy Features with no notice and stays callable on V7. --cref is still documented as usable on V6 / Niji 6 [5], about 14.5 months after V7 became the default on 2025-06-17 [4].
2. An actual shutdown, if it follows the V8.0 case, would get a written post on updates.midjourney.com and X, possibly stating "two weeks". That is one precedent, for an alpha model, and nothing guarantees it.

**Separate risks that come with no notice:**
- **The model behind the same version label can change.** MJ changed V7 in place on 2025-04-30 ("This applies to all images made with --v 7. you don't need to change anything") [48]. On 2025-05-02 the old model became reachable only via `--q 2` [49]. On 2025-06-16 the V7 style-reference model was swapped [50].
  - No in-place V7 change was announced after 2025-06-17 (all updates posts scanned) [18].
  - The Seeds doc warns: "your seed may no longer work as expected" [52].
  - So pinning `--v 7` protects against default switches but does not freeze the rendered face.
- **Account risk (outside this track).** The ToS says "You may not use automated tools…" and allows a ban "at any time, and for any reason" [1]. The Community Guidelines say "automating interactions… is strictly prohibited" except "explicitly granted" cases [2]. It applies to any unattended third-party client [70].

**Planning figure: 0 days.** The existing explicit `--v 7` pin is the right defence against default switches, which have never come with dated written notice. Early-warning signals to watch:
- The Omni Reference article (36285124473997) disappearing (RecordNotFound, as happened to Character Reference [37]) or turning up as a Legacy Features section.
- The V7 column leaving the Version chart [4].
- Any "deprecat…" post on updates.midjourney.com or @midjourney.
- The weekly Office Hours X Spaces [63] (spoken, not transcribed here).

## Timeline

| Event | Date | Notice given | Source |
|---|---|---|---|
| V5.2 → V6 default | 2024-02-14 | first-party notice not found (updates page started 2024-03-21) | [4][5][62] |
| Free-GPU rating rewards halted | 2024-03-13 | 0 days ("until further notice") | [47] |
| V6 → V6.1 default | 2024-07-30 | 0 days ("as of today") | [11][4] |
| V7 released | 2025-04-03 | — | [4] |
| Old grid-movie `--video` disappears from Parameter List | between 2025-04-14 and 2025-04-24 | none; never listed as Deprecated; token reused for the video model by 2025-09-05 | [42][43][44][45] |
| --cref: "not currently available" on V7 → "not compatible… use Omni Reference" | by 2025-04-17 → by 2025-06-08 | none | [34][35] |
| V7 model changed in place (same `--v 7`) | 2025-04-30; 2025-05-02 (old via `--q 2`); style-ref model 2025-06-16 (old via `--sv 4`) | 0 days | [48][49][50] |
| --cref leaves Parameter List; --oref takes its place | between 2025-05-12 and 2025-07-02 | none | [30][31] |
| V6.1 → V7 default | 2025-06-17 | ~25 days of undated hints (2025-05-23, 2025-05-29) | [13][14][12][4] |
| /tune stops working (doc change) | between 2025-09-14 and 2025-10-16 | none found | [40][41] |
| Niji 6 moved under "Legacy Versions" (chart still marks `--niji 6` as supported) | between 2025-10-16 and 2026-03-15 | none | [41][39][4][5] |
| Rooms removed | 2026-02-26 | 0 days | [46][72] |
| V8.0 alpha launched; first "likely remove" warning | 2026-03-17; 2026-03-21 | informal | [4][15] |
| V8.1 alpha ("Things will change! Perhaps without notice!") | 2026-04-14 | — | [16] |
| V8.1 on Discord + midjourney.com; V8.1 quality updated in place | 2026-04-30 | same day | [17] |
| **V7 → V8.1 account default** | **2026-06-10** | **0 days; docs changed first, announced after the fact** | [4][19][20][9][8][18][60] |
| V8.0 deprecation notice | 2026-06-11 | "in two weeks" | [8][9] |
| "(Uses V7)" oref fallback added to Version chart | between 2026-06-11 and 2026-06-18 | added after the switch | [20][21] |
| `--preview`; V8.2 preview | 2026-06-16; 2026-06-25 | "not guaranteed to run consistently over time" | [25][24] |
| Project: 166 dead proposals (the repo dates the count, not the onset) | 2026-06-17 | — | [70] |
| V8.2 released and made default; V8.0 removed | 2026-07-24 | 0 days (default); 43 days after the "two weeks" notice (V8.0) | [10][4][22][23] |
| Parameter List --oref note → "(replaced by the Edit Model in V8.X)" | between 2026-07-09 and 2026-09-01 | none | [32][33][6] |
| Edit Model test ("replacing omni-reference"); doc page; in-place update | 2026-08-27; 2026-08-28; 2026-08-29 | 0 days | [26][27][51] |
| Omni callout → "not supported in V8.2… use the Edit Model"; V7 fallback text removed | between 2026-08-28 and 2026-09-01 | none | [7][27][29][69] |
| Retexture → Legacy ("versions 7 and earlier") | by 2026-09-01 | none | [5][54] |
| Character Reference → Legacy Parameters (`--cref --cw`); standalone article deleted | added between 2026-03-15 and 2026-09-01; article live 2026-06-11, gone now | none | [5][39][36][37][38] |
| --upbeta: Legacy → Deprecated ("may not function reliably") | between 2026-03-15 and 2026-09-01 | none | [39][5] |
| Alpha site adds per-account "Your defaults" for parameters | 2026-09-24T01:59Z | alpha only | [65] |
| V7 / --oref retirement notice | none found through 2026-09-24T01:59Z | — | [65][64][18] |

## a) What "Legacy" means in practice

There is no general rule; each item gets its own statement.
- **Character Reference:** "set your default version to Midjourney or Niji 6… In Discord, use the `--cref` parameter" [5].
- **Style Tuner:** "The /tune command no longer works… existing `--style code` parameters can still be used" [5].
- **Retexture:** "set your default version to V7 or earlier" [54].
- **--upbeta:** moved from Legacy to Deprecated, with "may not function reliably" [39][5]. So Legacy status does not guarantee an item keeps working.
- **Deprecated lists:** Legacy Features has an undated Deprecated Parameters list [5]. The Discord Command List has its own undated "Deprecated Commands" list [58].
- **Tokens silently reused for new meanings:**
  - `--video`: grid movie → video model [45][44]
  - `--hd`: early model → V8.1 2048px [5][6]
  - `--fast`: deprecated → Fast Mode [5][6]
  - `--w`: width → weird [5][6]

## c) Stated retention policy

None exists. The only relevant text is the ToS disclaimers [1], the alpha caveat [16], the `--preview` caveat [25], "Turbo Mode… might change anytime" [57], and the Seeds warning [52].

## d) Are old versions still callable? Documented yes; not tested.

- The Version chart has V6 and V7 columns with Relax and Fast marked as supported, and marks "--niji 6" as supported [4].
- The V6.1 model still does the work for V7 Pan, Zoom Out and Editor ("Using V6.1") [4], and for Vary Region on V8.2 SD images [55].
- Remaster "remixes your prompt into version 5.2" [5].
- Style Reference: "add `--sv 4`… or switch to V6" [53].
- Earlier default-switch posts told users how to stay on the old version with `--v`: "--v 6.1" [12] and "--v 6" [11]. The V8.1 post gives no such line, only the V7 oref note [8].

## Corrections to the prior sweep and MODEL_STACK.md

- **MODEL_STACK.md:213** says "--ow has quietly dropped out of the current Parameter List" [71]. That is wrong: `--ow` never appeared in any of the 28 archived Parameter List captures from 2025-02-14 to 2026-09-05 [68][30][31][32][33][42][43][44], or in the live page [6]. It is documented only in the Omni Reference article ("between 1 and 1,000… default… --ow 100") [7].
- **"Not supported in V8.2"** is confirmed [7].
- **--cref** moved into Legacy Features only by 2026-09-01. It had its own article until at least 2026-06-11 [36].

## Sources
[1] FIRST-PARTY · Version Effective Date: May 27, 2026 (edited_at 2026-05-27, updated_at 2026-08-17); accessed 2026-09-23 via Zendesk API · https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — 'Please do not create any dependencies on any attributes of the Services or the Assets.' / 'We reserve the right to modify or discontinue any aspect of the Service, including pricing and features, at any time.' / 'Midjourney reserves the right to suspend or ban Your access to the Services at any time, and for any reason.' / 'You may not use automated tools to access, interact with, or generate Assets through the Services.'
[2] FIRST-PARTY · edited_at 2025-12-05; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines — 'With a few rare exceptions that are explicitly granted, Midjourney does not provide an API... automating interactions with Midjourney service is strictly prohibited... Accounts who do not comply with these rules may be blocked.'
[3] FIRST-PARTY · edited_at 2026-09-03; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32083472637453-Privacy-Policy — The only advance-notice promise in MJ docs, and it covers the policy itself: 'We will let You know via email and/or a prominent notice on Our Service, prior to the change becoming effective'
[4] FIRST-PARTY · edited_at 2026-09-01T17:26:08Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'The current default Midjourney version is V8.2.' / 'V8.2 released as the default version on July 24, 2026' / 'Edit Model, which replaces Omni Reference, Character Reference, and the Retexture tool' / 'V8.1 released on April 14, 2026, and was the default version from June 10 to July 23, 2026' / 'V8.0 ... was available on the Midjourney Alpha website until July 24, 2026 ... no longer available for use' / 'V7 was released on April 3, 2025, and was the default version from June 17, 2025 to June 9, 2026' / V6.1 and V6 default ranges / chart columns 'V6 | V7 | V8.1 & V8.2', Omni Reference supported on V7 only, no '(Uses V7)', Pan/Zoom/Editor on V7 'Using V6.1', '--niji 6' supported / Niji 7 'launched on January 9, 2026'
[5] FIRST-PARTY · edited_at 2026-09-01T17:19:52Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — Legacy Versions (Niji 6, V5.2 'default model from June 22, 2023 to February 14, 2024', ...); Legacy Parameters list incl. 'Character Reference --cref --cw'; 'To use a Character Reference on the website, set your default version to Midjourney or Niji 6 ... In Discord, use the --cref parameter'; Deprecated Parameters '--width and --w ... --fast (replaced with Quality) ... --upbeta'; 'Note: The --upbeta parameter is deprecated, and Beta Upscale may not function reliably.'; 'The /tune command no longer works ... existing --style code parameters can still be used'; 'It automatically remixes your prompt into version 5.2'; 'The Retexture tool within the Editor is compatible with versions 7 and earlier'; '--hd is an early alternative model'; 'For information on the current default version (V7)'
[6] FIRST-PARTY · edited_at 2026-09-01T17:18:30Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'You can provide Midjourney with an Omni Reference! (replaced by the Edit Model in V8.X) --oref'; no --ow entry; 'Generate videos in Discord using --video'; 'Generate V8.1 images at higher resolution (2048px) using --hd'; '--weird or --w'; 'Fast Mode Switch your GPU speed to Fast Mode --fast'; '--edit'
[7] FIRST-PARTY · edited_at 2026-09-01T16:30:42Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — callout 'This feature is not supported in V8.2' + 'When using V8.X, use the Edit Model instead'; 'Omni Reference is compatible with Midjourney version 7.'; 'Omni Reference can only be used with Midjourney version 7.'; '--ow ... any value between 1 and 1,000, with the default being --ow 100'; 'Omni Reference is currently not compatible with Fast Mode, Draft Mode & Conversational Mode, or --q 4'; Image Reference Types list is 'Animate / Edit Model Reference (Attach to prompt) / Style Reference / Image Prompt' (no Omni Reference); 'To use an Omni Reference in Discord, start by adding the --oref parameter'
[8] FIRST-PARTY · 2026-06-11T04:08:51Z · https://updates.midjourney.com/v8-1-is-now-the-default-model/ — 'we've updated the default model from V7 to V8.1!' / 'Note: V7 omni-reference is available to use while we finish training the improved version for V8' / 'we will be deprecating our V8.0 alpha model in two weeks'
[9] FIRST-PARTY · 2026-06-11T04:02:13Z (read via cdn.syndication.twimg.com) · https://x.com/midjourney/status/2064921117618557292 — 'We've made V8.1 the new default model for all users on Midjourney. V8 will now be deprecated in 2 weeks. V8.2 will start testing extremely soon.'
[10] FIRST-PARTY · 2026-07-24T22:24:48Z · https://x.com/midjourney/status/2080781271043911807 — 'We're releasing V8.2 today and making it the default model on Midjourney.'
[11] FIRST-PARTY · 2024-07-30T17:46:11Z · https://updates.midjourney.com/version-6-1/ — 'So as of today we're making V6.1 the default model on Midjourney for all users.' / 'type --v 6 after your job'
[12] FIRST-PARTY · 2025-06-17T04:46:33Z · https://updates.midjourney.com/v7-is-now-the-default-model/ — 'we're officially updating the default model to V7! This means if you haven't tried V7 yet, your model will be automatically switched to V7.' / '(or type --v 6.1 after your prompt)'
[13] FIRST-PARTY · 2025-05-23T23:15:17Z · https://updates.midjourney.com/rank-images-from-all-time/ — 'We're getting ready to make our V7 model the 'default' model' (undated heads-up, 25 days before switch)
[14] FIRST-PARTY · 2025-05-29T23:03:25Z · https://updates.midjourney.com/faster-v7-ideas-ranking-party-and-better-moderation/ — 'This is part of our ‘final optimization’ pass before making V7 default for the whole community' / 'Note: Omni-reference jobs remain the same.'
[15] FIRST-PARTY · 2026-03-21T00:27:47Z · https://updates.midjourney.com/relax-mode-for-v8-alpha/ — 'When the next V8 comes out, we will likely remove the 'present' version of V8. So remember everything you're using now is Alpha and temporary.'
[16] FIRST-PARTY · 2026-04-14T20:33:37Z · https://updates.midjourney.com/v8-1-alpha/ — 'Things will change! Perhaps without notice!' / 'It is likely that we will decommission our V8.0 model after V8.1 has been out for a few weeks.' (caveat scoped to alpha V8 series)
[17] FIRST-PARTY · 2026-04-30T20:47:41Z · https://updates.midjourney.com/v8-1-updates/ — 'V8.1 is now available on Discord as well as midjourney.com' / 'We've improved sharpness and image quality for V8.1!'
[18] FIRST-PARTY · accessed 2026-09-23 · https://updates.midjourney.com/sitemap-posts.xml — 92 posts; only web-updates-5 (2026-05-27) between v8-1-updates (2026-04-30) and the V8.1-default post (2026-06-11); newest post alpha-changelog-9-23-26 (2026-09-24T01:59Z); scan of all 46 posts since 2025-06-17 finds no V7/oref retirement and no in-place V7 model update
[19] FIRST-PARTY · snapshot 2026-05-18 · https://web.archive.org/web/20260518101550/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'The current default Midjourney version is V7.' / 'V8.1 released on midjourney.com on April 30, 2026' / 'The V8.0 Alpha ... is still available for a limited time.'
[20] FIRST-PARTY · snapshot 2026-06-11T02:33:47Z · https://web.archive.org/web/20260611023347/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'The current default Midjourney version is V8.1.' / 'became the default version on June 10, 2026' (before the X and updates announcements); chart Omni Reference row has no '(Uses V7)'
[21] FIRST-PARTY · snapshot 2026-06-18 · https://web.archive.org/web/20260618022947/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — chart Omni Reference row under V8.1: '(Uses V7)'
[22] FIRST-PARTY · snapshot 2026-07-20 · https://web.archive.org/web/20260720001156/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — V8.0 Alpha 'is still available for a limited time' (i.e., not removed at two weeks)
[23] FIRST-PARTY · snapshot 2026-07-31 · https://web.archive.org/web/20260731111048/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'The current default Midjourney version is V8.2.' / V8.0 'no longer available for use'; chart still shows '(Uses V7)'
[24] FIRST-PARTY · 2026-06-25T19:11:05Z · https://x.com/midjourney/status/2070223272072065228 — 'Try adding --preview to your prompt for a early peak at V8.2 aesthetics & personalization.'
[25] FIRST-PARTY · 2026-06-16T22:04:29Z · https://updates.midjourney.com/draft-mode-for-v8-1-and-new-feature-previews/ — 'Images that you create with --preview might be a little unpolished and the jobs are not guaranteed to run consistently over time.'
[26] FIRST-PARTY · 2026-08-27T23:32:15Z · https://updates.midjourney.com/edit-model-for-v8/ — 'Today we’re gonna start letting everyone test our first V8.2 image edit model!' / 'Generating images with other images (replacing omni-reference) with up to 4 image references at once' / 'Drag images into the prompt bar under "attach to prompt”' / 'Type --edit url... on Discord'
[27] FIRST-PARTY · created_at 2026-08-28T20:52:18Z · https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model — Lower bound for the current Omni Reference callout wording (which links this article)
[28] FIRST-PARTY · snapshot 2026-04-04 · https://web.archive.org/web/20260404144227/https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — callout 'This feature is not currently supported in V8 Alpha.'
[29] FIRST-PARTY · snapshot 2026-06-11 · https://web.archive.org/web/20260611023543/https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — callout 'This feature is not currently supported in V8.1' + 'Adding an Omni Reference image to the Imagine bar will automatically run the prompt in V7.'; Image Reference Types list includes 'Omni Reference (replaces Character Reference)'
[30] FIRST-PARTY · snapshot 2025-05-12 · https://web.archive.org/web/20250512033313/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'You can provide Midjourney with a Character Reference! --cref'; no --ow
[31] FIRST-PARTY · snapshot 2025-07-02 · https://web.archive.org/web/20250702124452/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'You can provide Midjourney with an Omni Reference! (replaces Character Reference in V7) --oref'; no --ow
[32] FIRST-PARTY · snapshot 2026-07-09 · https://web.archive.org/web/20260709023826/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — '(replaces Character Reference in V7) --oref'; no --ow
[33] FIRST-PARTY · snapshot 2026-09-05 · https://web.archive.org/web/20260905023030/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — '(replaced by the Edit Model in V8.X) --oref'; no --ow
[34] FIRST-PARTY · snapshot 2025-04-17 · https://web.archive.org/web/20250417124822/https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference — 'Character References are not currently available when using version 7.'
[35] FIRST-PARTY · snapshot 2025-06-08 · https://web.archive.org/web/20250608034223/https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference — 'Character Reference is not compatible with version 7, use Omni Reference instead.'
[36] FIRST-PARTY · snapshot 2026-06-11 (last CDX capture) · https://web.archive.org/web/20260611023543/https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference — callout 'This feature is not supported in V7 or V8.1' + 'When using V7, use Omni Reference instead.' (standalone article still live)
[37] FIRST-PARTY · accessed 2026-09-23 · https://docs.midjourney.com/api/v2/help_center/en-us/articles/32162917505293.json — {"error":"RecordNotFound","description":"Not found"} — standalone Character Reference article deleted
[38] FIRST-PARTY · accessed 2026-09-23 · https://docs.midjourney.com/api/v2/help_center/en-us/articles/33329788681101.json — Heading IDs h_01M1EZAC51QPWT0Z23XS6K9GA2 (Character Reference) and h_01M154RRDHJBB8KDNZ40VJPVNX (Retexture) decode to 2026-09-01T17:12Z and 2026-08-28T21:35Z (inference only; the Niji 6 heading carries a reused 2025-01-14 ID)
[39] FIRST-PARTY · snapshot 2026-03-15 · https://web.archive.org/web/20260315172656/https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — 'Legacy Parameters High Definition Model --hd Test Models --test --testp ... Uplight --uplight Upbeta --upbeta Stop --stop Style Tuner Codes --style code'; Deprecated list ends '--old'; no Character Reference section; 'Legacy Versions Niji 6' present; 'current default version (V7)'
[40] FIRST-PARTY · snapshot 2025-09-14 · https://web.archive.org/web/20250914032819/https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — 'With this tool, you can use the /tune command along with a prompt to generate a variety of sample images.'
[41] FIRST-PARTY · snapshot 2025-10-16 · https://web.archive.org/web/20251016191047/https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — 'The /tune command no longer works, and new Style Tuners cannot be created.'; 'Legacy Versions' begins with Version 5.2 (no Niji 6 yet)
[42] FIRST-PARTY · snapshot 2025-04-14 · https://web.archive.org/web/20250414145207/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'Video Create a short clip of your image generating in Discord using the video parameter --video'
[43] FIRST-PARTY · snapshot 2025-04-24 · https://web.archive.org/web/20250424175623/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — no --video entry
[44] FIRST-PARTY · snapshot 2025-09-05 · https://web.archive.org/web/20250905120803/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'Video Generate videos in Discord using --video' (token reused)
[45] FIRST-PARTY · snapshot 2025-01-15 · https://web.archive.org/web/20250115180656/https://docs.midjourney.com/docs/video — 'Use the --video parameter to create a short movie of your initial image grid being generated.' / '--video works with Model Versions 5.2 6 niji 5 and niji 6'
[46] FIRST-PARTY · 2026-02-26T20:13:48Z · https://updates.midjourney.com/an-update-on-rooms/ — 'Today we are removing the Rooms feature from the website.'
[47] FIRST-PARTY · 2024-03-13 · https://updates.midjourney.com/halting-free-gpu-rewards/ — 'we need to halt our free-gpu rewards for image-ranking until further notice'
[48] FIRST-PARTY · 2025-04-30T22:59:14Z · https://updates.midjourney.com/v7-update-editor-and-exp/ — 'New V7 image model update ... This applies to all images made with --v 7. you don't need to change anything'
[49] FIRST-PARTY · 2025-05-02T21:05:47Z · https://updates.midjourney.com/fast-mode-for-v7/ — 'We're launching V7 model speedups today' / 'if you want the old version you can still get it via --q 2' / '--oref jobs are still 2x the cost of a normal --fast mode job'
[50] FIRST-PARTY · 2025-06-16T19:48:37Z · https://updates.midjourney.com/style-references-for-v7/ — 'It is now default and live for all V7 jobs.' / 'you can either use V6, or you'll need to specify --sv 4 to fall back to the old model'
[51] FIRST-PARTY · 2026-08-29 · https://updates.midjourney.com/edit-image-quality-update/ — 'we've updated our V8.2 edit model for better image quality' (same-day in-place update)
[52] FIRST-PARTY · edited_at 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds — 'Seeds may behave unexpectedly, so they shouldn't be relied on for the same results over different prompting sessions. Assume that if you take a break and come back later, your seed may no longer work as expected.'
[53] FIRST-PARTY · edited_at 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference — '--sv 4 is the old V7 sref model (prior to June 16, 2025).' / 'To use old codes, add --sv 4 to your prompt (uses the old V7 model) or switch to V6.'
[54] FIRST-PARTY · edited_at 2026-09-02 · https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor — 'To access the old Retexture feature, set your default version to V7 or earlier.'
[55] FIRST-PARTY · edited_at 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32794723105549-Vary-Region — 'Vary Region is available on V8.2 SD images in Discord. Note that Vary Region currently uses V6.1.'
[56] FIRST-PARTY · edited_at 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32570788043405-Pan — 'when using V7 and V8.1, Pan still utilizes V6.1' (conflicts with Version chart 'Using Edit Model' for V8.1 & V8.2)
[57] FIRST-PARTY · edited_at 2026-08-28 · https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo — 'If the Turbo GPUs aren’t available or you're on an older version, your job will switch automatically to Fast Mode. Remember, Turbo Mode is experimental, so its availability and costs might change anytime.'
[58] FIRST-PARTY · edited_at 2026-03-24 · https://docs.midjourney.com/hc/en-us/articles/32894521590669-Discord-Command-List — 'Deprecated Commands /private (replaced with /stealth) /pixels /idea'
[59] FIRST-PARTY · 2026-01-20 · https://updates.midjourney.com/web-updates-4/ — 'Automatically strip irrelevant parameters (--cw/--ow) when cref/oref not present' (web layer rewrites prompts)
[60] FIRST-PARTY · 2026-05-27T18:44:53Z · https://updates.midjourney.com/web-updates-5/ — Only post between 2026-04-30 and the V8.1 switch; mentions 'Rerun as HD' for V8.1 but no default change
[61] FIRST-PARTY · accessed 2026-09-23 · https://updates.midjourney.com/sitemap-tags.xml — Only tags: alpha, feature, hotfix, announcement, changelog (no office-hours posts)
[62] FIRST-PARTY · 2024-03-21 · https://updates.midjourney.com/new-updates-page/ — 'Added the /updates page to stay appraised of the latest announcements, gallery changes and Office Hours directly on the website.'
[63] FIRST-PARTY · 2026-09-16T19:13:17Z · https://x.com/midjourney/status/2100302017004777515 — 'Midjourney Weekly Office Hours - 9/16' (office hours are X Spaces; not transcribed)
[64] FIRST-PARTY · accessed 2026-09-23 (covers 2026-06-11 to 2026-09-16) · https://syndication.twitter.com/srv/timeline-profile/screen-name/midjourney — No @midjourney tweet in that window mentions retiring V7 or omni-reference; includes 2026-08-28 edit-model test and 2026-08-29 edit-model update tweets
[65] FIRST-PARTY · 2026-09-24T01:59:23Z · https://updates.midjourney.com/alpha-changelog-9-23-26/ — 'DEFAULT PARAMETERS ... Go to Settings → Advanced → Your defaults, or just click "Set current pills as default"' / 'Pasted prompts keep their image prompts instead of turning into edit references.'; no V7/oref retirement
[66] FIRST-PARTY · 2025-05-01T23:03:26Z · https://updates.midjourney.com/omni-reference-oref/ — 'This parameter goes from 0 to 100 to 1000 (100 is default)' (conflicts with doc's 1–1,000)
[67] FIRST-PARTY · 2025-07-16 · https://updates.midjourney.com/enterprise-api-survey/ — 'We're starting to investigate opening up an Enterprise API' (survey only; no launch post found)
[68] FIRST-PARTY · accessed 2026-09-23 · https://web.archive.org/cdx/search/cdx?url=docs.midjourney.com/hc/en-us/articles/32859204029709*&output=txt&fl=timestamp&filter=statuscode:200&collapse=digest — 28 unique-digest Parameter List captures, 2025-02-14 to 2026-09-05; --ow absent from every capture checked (verifiers: all 28; reconciler: 7 + live page)
[69] FIRST-PARTY · accessed 2026-09-23 · https://web.archive.org/cdx/search/cdx?url=docs.midjourney.com/hc/en-us/articles/36285124473997*&output=txt&filter=statuscode:200 — Last Omni Reference capture is 20260611023543; no capture of the V8.2 wording
[70] secondary · local repo lines 79-81, 86, 90-92; accessed 2026-09-23 · https://github.com/Wenjix/living-portraits/blob/master/pipeline/autogen.py — Project record (not MJ): 'The account default moved to v8.1, which rejects --oref ("`--oref` is not compatible with `--version 8.1`") -> every still submit failed (166 dead proposals, 2026-06-17).' / IMAGINE_VERSION = "7" / 'midjourney.api now normalizes relax->relaxed (captured from MJ web UI 2026-06-18)'
[71] secondary · local repo line 212-213; accessed 2026-09-23 · https://github.com/Wenjix/living-portraits/blob/master/MODEL_STACK.md — Project claim being corrected: '`--ow` has quietly dropped out of the current Parameter List.'
[72] FIRST-PARTY · 2026-02-26T19:34:43Z · https://updates.midjourney.com/personalization-and-web-updates/ — 'We're sunsetting rooms on web' (same day as removal)

## Contradictions (first-party vs first-party — unresolved)
- Current default version: Version doc 'The current default Midjourney version is V8.2.' (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version, edited 2026-09-01) vs Legacy Features 'For information on the current default version (V7), please visit our Version article.' (https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features, edited 2026-09-01). Not resolved.
- --ow range: Omni Reference doc 'any value between 1 and 1,000, with the default being --ow 100' (https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference) vs launch post 'This parameter goes from 0 to 100 to 1000 (100 is default)' (https://updates.midjourney.com/omni-reference-oref/, 2025-05-01). Not resolved; irrelevant at --ow 160.
- Pan backend under V8.x: Pan doc 'when using V7 and V8.1, Pan still utilizes V6.1' (https://docs.midjourney.com/hc/en-us/articles/32570788043405-Pan, edited 2026-07-27) vs Version chart 'Pan ... V8.1 & V8.2: Using Edit Model' (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version, edited 2026-09-01). Not resolved.
- Oref and Fast Mode: Omni doc 'Omni Reference is currently not compatible with Fast Mode' (https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference) vs 'Please Note: --oref jobs are still 2x the cost of a normal --fast mode job' (https://updates.midjourney.com/fast-mode-for-v7/, 2025-05-02). Different dates; not resolved; project runs relax.
- Omni Reference doc internal inconsistency (same page, edited 2026-09-01): 'Image Reference Types: Animate / Edit Model Reference (Attach to prompt) / Style Reference / Image Prompt' (no Omni Reference; the 2026-06-11 snapshot listed 'Omni Reference (replaces Character Reference)') vs 'Drag and drop your image from the uploads library into the Omni Reference section.' Not resolved.
- Token reuse (not strictly contradictions, both first-party and current): '--fast (replaced with Quality)' in Legacy Features Deprecated list vs '--fast Switch your GPU speed to Fast Mode' in Parameter List; '--hd is an early alternative model' (Legacy Features) vs 'Generate V8.1 images at higher resolution (2048px) using --hd' (Parameter List); '--width and --w' deprecated (Legacy Features) vs '--weird or --w' (Parameter List).
- Not a contradiction (explained): V8.1 release date 'April 14, 2026' (current Version doc) vs 'released on midjourney.com on April 30, 2026' (Version doc snapshot 2026-05-18); April 14 = alpha site (https://updates.midjourney.com/v8-1-alpha/), April 30 = Discord + midjourney.com (https://updates.midjourney.com/v8-1-updates/).
- Secondary-only conflict (not decided): one office-hours recap (medium.com, 2026-06-04) reports a V8.1-default pre-signal on 2026-06-03; a verifier reported a substack recap with no such pre-signal. Neither is first-party.

## Could not confirm
- Any Discord #announcements message or spoken office-hours statement before 2026-06-10 announcing the V8.1 default switch (Discord and Office Hours X Spaces audio not accessible; 'no notice' findings are scoped to docs, updates.midjourney.com and X posts).
- First-party notice preceding the V6 default switch (2024-02-14); predates the updates page (2024-03-21).
- Whether --v 5.2, --v 6, --v 6.1, --niji 6, --v 1-4, --test/--testp, --uplight, legacy upscalers or the legacy --hd model are accepted today (docs only; not tested against the service).
- Whether --v 7 + --oref + --ow 160 in relax mode works on 2026-09-23 (docs say V7 oref is supported; not tested).
- Whether the midjourney.com web Imagine bar still exposes an Omni Reference slot: the current Omni doc's 'Image Reference Types' list omits it while the same page still says 'Drag and drop your image ... into the Omni Reference section'. Matters because the project's third-party client mimics the web UI.
- When the project's --oref failures actually began (repo dates only the 166-proposal count, 2026-06-17; first public commit is 2026-07-11).
- Exact date the Omni Reference callout changed to the V8.2 wording (bounded 2026-08-28..2026-09-01; no Wayback capture after 2026-06-11).
- Exact dates for: --upbeta Legacy->Deprecated, legacy --hd leaving the Legacy Parameters list, Character Reference section added to Legacy Features (bounded 2026-03-15..2026-09-01; heading-ID inference says 2026-09-01), /tune stopping (bounded 2025-09-14..2025-10-16 by doc change only).
- Whether Immersive Commons / the project holds an 'explicitly granted' automation exception or any enterprise agreement.
- Whether midjourney.com/tos matches the docs.midjourney.com ToS article (midjourney.com/tos returns HTTP 403 to curl).
- Source and endpoints of the third-party 'midjourney' Python client (not public; only installed on host 'hil').
- Any first-party statement of a planned V7 or --oref retirement date: none found through the 2026-09-24T01:59Z alpha changelog and the X timeline through 2026-09-16.
- Which first-party source is current on Pan under V8.x (Pan doc: V6.1; Version chart: Edit Model).
- Office-hours content for 2026-06-03, 2026-06-10 and 2026-09-16 (only secondary recaps, which conflict with each other).

## Dropped claims (refuted or unsupported in verification)
- 'The updates site published nothing between 2026-04-30 and the switch': false. web-updates-5 was published 2026-05-27; it has no default notice.
- 'No official @midjourney X post about the V8.1 default switch was found': false. https://x.com/midjourney/status/2064921117618557292 exists (2026-06-11T04:02:13Z), posted after the switch.
- '--video: still current, not removed': wrong for the legacy grid-movie --video. It left the Parameter List between 2025-04-14 and 2025-04-24, was never marked Deprecated, and the token was reused for the video model by 2025-09-05.
- 'Legacy --hd model dropped': overstated. It was dropped only from the Legacy Parameters list; Legacy Features still describes '--hd is an early alternative model', and the upscaler tables still have 'hd' rows.
- 'Midjourney framed V7 oref as temporary': overreach. The source says only 'V7 omni-reference is available to use while we finish training the improved version for V8'.
- 'The Edit Model replacement shipped on 2026-08-27': overstated. The post says 'start letting everyone test our first V8.2 image edit model'.
- 'The project's outage came 7 days after the switch': not established. The repo dates the 166-proposal count, not when the failures began.
- 'V7 default: accounts were switched automatically': missing a qualifier. The source says 'if you haven't tried V7 yet, your model will be automatically switched'.
- 'Docs do not reliably predict how the prompt-parameter path behaves': not shown. The doc fallback covered adding an image to the web Imagine bar, not a text --oref under the v8.1 account default.
- 'The Remix doc uses V3 -> V4 as a working example': it is an error example and does not show that those versions still run.
- 'Legacy in operation = still usable on its version' as a general rule: the docs give no general rule, and --upbeta moved from Legacy to Deprecated with 'may not function reliably'.
- Prior sweep / MODEL_STACK.md:213 '--ow has quietly dropped out of the current Parameter List': false. --ow is absent from all 28 archived Parameter List captures (2025-02-14 to 2026-09-05); it is documented only in the Omni Reference article.
- 'Style Tuner removed before 2025-10-16 (exact date not found)': refined, not dropped. The doc change falls between 2025-09-14 and 2025-10-16.
- '--ow absent from 13 Wayback snapshots': the count understates the archive. There are 28 unique-digest captures; the conclusion is unchanged.

## DO NOT QUOTE (low/unknown)
- [low] 'V8.1 default was pre-signalled in the 2026-06-03 office hours, about 7 days ahead' (Medium recap: 'The v8.1 model will become the default model on the main site and in Discord before that occurs.') — Secondary only (third-party recap of spoken office hours at medium.com/enthusiastically-midjourney); the first-party audio was not accessible; another secondary recap (geekycuriosity.substack.com) was reported as carrying no such pre-signal.
- [low] 'V6 was pre-signalled in office hours as default by end of January 2024' (uxdesign.cc / medium design-bootcamp recap) — Secondary only; stated target slipped to 2024-02-14 per the first-party Version doc.
- [low] 'On August 29, 2026, Midjourney made V8.1 (not V8.2) the new default' — Hallucinated secondary search summary; contradicted by the Version doc and the 2026-07-24 X post (V8.2 default since 2026-07-24).
- [low] 'V6, V6.1, V7, V8.1, V8.2 and Niji 4 through 7 all still run as of August 2026; --v 5.2 is selectable' — SEO/secondary search summary; no first-party test or statement covers all of these.
- [low] Any specific positive notice period for a V7 or --oref retirement (e.g. 'two weeks', '43 days') — Rests on a single precedent (V8.0), which was an alpha-site-only model; no stated policy exists.
- [low] 'V7 / --oref will stay callable for many months after being relabelled Legacy' — Inference from the --cref and Niji 6 precedents; not a stated policy; --upbeta shows Legacy items can later be marked 'may not function reliably'.
- [low] Character Reference added to Legacy Features on 2026-09-01T17:12Z; Retexture on 2026-08-28T21:35Z — Inferred from Zendesk heading-ID (ULID) timestamps; heading IDs can be reused (Niji 6 heading carries a 2025-01-14 ID although it moved to Legacy between 2025-10-16 and 2026-03-15). Hard bound is 2026-03-15..2026-09-01.
- [low] Remix doc's '--version 3 ... --version 4' example as evidence old versions still run — It is a hypothetical error example about stylize limits, not a statement of availability.
- [low] 'Midjourney docs promised a V7 fallback that the prompt path did not honour' (doc vs behaviour contradiction) — The doc fallback text covered adding an image to the web Imagine bar; the project's error was a text --oref under the v8.1 account default. Different paths; not shown to conflict.
- [unknown] Whether --v 7 + --oref works today on the project's path — Documented as supported; not tested against the live service.
- [unknown] Whether older versions (--v 5.2/6/6.1, --niji 6, --test/--testp, legacy --hd, legacy upscalers) are accepted today — Documentation-only evidence; no live test.
- [unknown] When the June 2026 outage began relative to the 2026-06-10 default switch — Repo only dates the 166-proposal count (2026-06-17).
- [unknown] Existence of an automation exception or enterprise API access for this project — Only a 2025-07-16 survey post exists; no launch or grant found.
- [unknown] Whether the web Imagine bar still has an Omni Reference slot — Current Omni doc is internally inconsistent: its reference-type list omits Omni Reference but its body still describes the Omni Reference section.
- [low] GPU Speed table row 'Omni Reference Prompt (V7) 2 minutes' as evidence that oref runs in Fast Mode — The table does not say it is Fast-only; the Omni doc says oref is 'currently not compatible with Fast Mode'. Low stakes because the project runs relax.


---

# Track MJ2 — Midjourney V8.x identity-preservation mechanism
Primary mission track: yes · Final confidence: high

## Answer
## MJ2: Midjourney V8.x identity preservation (reconciled 2026-09-23; every quote re-fetched today)

**Current version.** V8.2 is the default according to three first-party sources:
- The Version doc: "The current default Midjourney version is V8.2" and "V8.2 released as the default version on July 24, 2026" [1].
- The V8.2 launch post [2].
- The official @midjourney X post of 2026-07-24: "We're releasing V8.2 today and making it the default model" [3].

One first-party page disagrees. Legacy Features still says "For information on the current default version (V7)…" [4]. This is logged under contradictions and not resolved here. V7 is still documented and selectable [1][8].

**The V8.x mechanism is the Edit Model.** On the web it is the "Edit Model Reference (Attach to prompt)" slot; in prompt syntax it is `--edit <url> [url…]`. The Version doc says it "replaces Omni Reference, Character Reference, and the Retexture tool" [1][5][6].

### Direct answer: single anchor + tunable weight on V8.x = **PARTIAL**
- **Single anchor: YES.** The Edit Model can "Generate new images using up to 4 reference images (replacing Omni Reference and Character Reference)" [5]. The web docs describe the slot as a way to "maintain character/object consistency" [18][19].
- **Tunable weight: NONE DOCUMENTED.** This does not prove no weight exists.
  - The Edit Model article has no weight, strength or slider. Its only balance control is `--raw`, "allowing your prompt text to have more influence" [5].
  - None of the 105 help-center articles mentions an edit or reference weight for the Edit Model.
  - The Version chart marks **Omni Reference Weight ✗ for V8.1 & V8.2** [1].
  - The Parameter List gives `--edit` no weight companion [10].
  - No post up to the 9/23 changelog adds one [6][7][25].
  - `::` per-reference weights are documented only for `--sref` [13]. Text multi-prompt weights are documented only through V6.1 [28].
- **What V8.x lacks compared with V7 `--oref <url> --ow 160 --v 7`:**
  1. **A numeric reference-strength dial.** `--ow` takes "any value between 1 and 1,000, with the default being --ow 100", and the web has an "Omni Strength slider" [8].
  2. **First-party face guidance tied to that dial:** "If you want to make sure that a character's face is extremely visible … try something higher like –-ow 400" [9].
  3. **Compatibility with the V7 pin.** The Edit Model "is compatible with Midjourney versions 8.1 and 8.2" [5] and is ✗ on V7 [1]. Using it means V8.x renders the face, which is the one-way door.
  4. **Any first-party claim about face fidelity.** Even the V7 doc warns that "intricate details like specific freckles … may not perfectly match your reference" [8].
  5. **A documented Relax/Draft/Conversational status for the Edit Model itself.** The docs say nothing either way [5][21]. The V8.x chart column says Relax ✓, Conversational ✓ and Draft ✗ [1], but the Draft ✗ contradicts the Draft doc [22].
- **Not a real V7-vs-V8 difference:** web prompt-text syntax. Both `--oref` [8] and `--edit` [5] have text syntax documented only "in Discord". The Parameter List lists both with no platform restriction: "Parameters always go at the end of your text prompt" [10]. The repo already submits `--oref … --ow … --v 7` as web prompt text (autogen.py:327) [40]. Whether `--edit` works this way on the web, the API or the third-party client is unverified.
- **Only documented knob that can be stacked on the anchor (effect on identity undocumented):**
  - One image can be an Image Prompt, a Style Reference and an Edit Model reference at once: "even use it as all three!" [17]. The Edit Model "can also be used with Image Prompts" [5].
  - `--iw` runs 0–3 with default 1, from a column labelled "Version 8.1" [11].
  - But "Image Prompts and references" are "inspiration … not to copy them exactly" [11].

### Mechanism table
| mechanism | V8.x status | syntax | weight param + range | prompt-expressible? | incompatibilities | source |
|---|---|---|---|---|---|---|
| **Edit Model** | ✓ V8.1 & V8.2 only; ✗ V6/V7 | `… --edit URL [URL…]` (1–4, space-separated; Discord how-to); web "Attach to prompt" / Quick Edit / Editor | **none documented**; `--raw` only | Discord yes; web text undocumented (the Parameter List does list `--edit`) | `--tile`; results not Remix-able; not a video reference; V8.x `--q` ✗, Turbo ✗; AR follows the first image unless `--ar` ("default aspect ratio settings will not automatically apply"); GPU 1 min SD / 2.3 min HD | [1][5][6][10][20][21] |
| Omni Reference | ✗ on V8.x: rendered badge "This feature is not supported in V8.2"; "can only be used with Midjourney version 7" | `--oref URL --ow N`, one image only | `--ow` 1–1,000, default 100, "keep your weight below 400" | yes | "not compatible with Fast Mode, Draft Mode & Conversational Mode, or --q 4"; not compatible with V6.1 inpaint/outpaint; results ✗ Vary Region/Pan/Zoom Out; 2× GPU | [1][8][9][29][39] |
| Character Reference | Legacy; MJ/Niji 6 only; "replaced by Omni Reference in V7, and the Edit Model in V8.X" | `--cref URL --cw N` | `--cw` "from 100 to 0", default 100; at `--cw 0` "it'll just focus on face" | yes (V6) | not V7/V8 | [4][23] |
| Image Prompt | ✓ V8.1 & V8.2 | URL at start of prompt | `--iw` 0–3, default 1 ("Version 8.1" column) | yes | needs text or 2+ images | [1][11][12] |
| Style Reference | ✓ | `--sref URL/code`; Discord `URL1::2 URL2::1` | `--sw` 0–1000, default 100 | yes | "doesn't copy objects or people"; `--sw` ✗ with Moodboards | [13] |
| Personalization | ✓ (V7 global profile works in V8.1/8.2; V8 profiles ✗ on V7) | `--p` / `--p ID` | `--stylize` 0–1000, default 100 | yes | aesthetic only; no identity claim | [14] |
| Moodboards | ✓ (V6+) | `--p mID` | via `--stylize` | yes | ✗ `--sv`/`--sw` | [15] |
| Editor (erase/layers inpaint, outpaint) | ✓; V8.x "Using Edit Model"; V7 "Using V6.1" | UI only (web Edit tab; upload or paste URL) | none | no (web only) | V8.x edits public unless Stealth; HD→SD downscale | [1][16][17] |
| Retexture | V7 and earlier; "a built-in functionality of the Edit Model for V8.X" | UI | none | no | keeps "the structure of the original image—like a template" | [4][16] |
| Other character-specific V8.x feature | none found (105 help-center articles; updates sitemap) | — | — | — | — | — |

### Editing the existing V7 canonical still instead of regenerating
- **Edit Model route.** It edits uploaded or external images from written instructions, including perspective changes ("let's see this image from the front / … from behind") [5][16]. But it is V8.x-only [5], so the output is rendered by V8.x. There is no first-party claim about face preservation.
- **Editor erase/layers route.**
  - The docs say: "only the areas of your image with visible transparency will be regenerated … any visible parts will remain unchanged" (Layers section) [16]. Vary Region/Erase allows "precise alterations without changing the rest of the image" [19].
  - Pixel-exactness is **not** stated.
  - The erased area is filled by V6.1 when V7 is selected, or by the Edit Model on V8.x. It is never filled by V7 [1].
  - A submit "without erasing or making any selections … will apply to the entire image" [16].
  - Inpainting or outpainting an HD image "will downscale the resulting images to SD" [1].
  - This only helps when the head does not move.
- **Omni-made stills (all 59 pose stills used `--oref`).** They "can only be opened in the Edit tab. You will need to remove the Omni Reference and --ow parameter before submitting your edits" [16]. They are also ✗ with Vary Region, Pan and Zoom Out [8].
- **Privacy.** Edit-model creations "will appear on midjourney.com for other members to see unless you have Stealth mode enabled. This applies to … external images" [16]. "Stealth mode is available only to Pro and Mega Plan members" [26].

### Published plans (first-party only)
- 2026-06-11: "V7 omni-reference is available to use while we finish training the improved version for V8" [24].
- 2026-08-27: the Edit Model test launched as "replacing omni-reference" [6]. 2026-08-29: quality update [7].
- **No first-party plan to port `--oref`/`--ow` to V8.x, and no retirement date for V7 or `--oref`,** in the help center, the updates sitemap or the ToS.
- Precedent: on 2026-06-11 MJ said "we will be deprecating our V8.0 alpha model in two weeks" [24]. V8.0 actually stayed "available … until July 24, 2026" [1]. Watch updates.midjourney.com for a similar notice.
- ToS: "Please do not create any dependencies on any attributes of the Services or the Assets" [27].

### Corrections to MODEL_STACK.md and the researcher
1. **MODEL_STACK.md:62-63 is CORRECT.** It says the Omni docs carry an "explicit 'not supported in V8.2' flag". The researcher said otherwise, and that is wrong.
   - The Omni article contains `<p class="custom_incompatible" data-title="This feature is not supported in V8.2">` [8].
   - The theme CSS renders that attribute as visible red text: `.custom_incompatible::before { content: attr(data-title); color: #f2330d; }` [39].
   - Badge history: 2026-04-04 "not currently supported in V8 Alpha." [33]; 2026-06-11 "not currently supported in V8.1", plus "will automatically run the prompt in V7" [34]; today's wording since then.
2. **MODEL_STACK.md:213 is unsupported.** It says "`--ow` has quietly dropped out of the current Parameter List". `--ow` is absent from every Parameter List capture checked (2025-05-12 through 2026-09-05) and from today's page. It is documented only in the Omni article [10][37][38].
3. **The "(Uses V7)" note is older than the researcher dated it.** The Omni-on-V8.x note appears in the Version chart captures of 2026-06-18 and 2026-07-31 [35][36]. It is absent from the 2026-06-11 capture and from today's chart.
4. **Out of scope:** the ToS says "You may not use automated tools to access, interact with, or generate Assets through the Services" [27]. This bears on any unattended third-party client.

## Sources
[1] FIRST-PARTY · updated 2026-09-01 (Zendesk updated_at 2026-09-01T17:26:08Z); accessed 2026-09-23 via docs.midjourney.com/api/v2/help_center · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'The current default Midjourney version is V8.2.' / 'V8.2 released as the default version on July 24, 2026.' / Edit Model 'replaces Omni Reference, Character Reference, and the Retexture tool.' Chart (V6|V7|V8.1 & V8.2): Edit Model ✗/✗/✓; Omni Reference ✗/✓/✗; Omni Reference Weight ✗/✓/✗; Image Prompts, Image Weight, Style Reference, Style Weight ✓ on V8; Editor/Pan/Zoom Out on V7 'Using V6.1', on V8 'Using Edit Model'; V8 Quality ✗, Draft ✗, Conversational ✓, Relax ✓, Turbo ✗, Niji ✗. 'Using any of our inpainting or outpainting tools (Pan, Zoom Out, Edit/Vary Region) on HD images will downscale the resulting images to SD.' 'V7 was released on April 3, 2025, and was the default version from June 17, 2025 to June 9, 2026.' 'V8.0 … was available on the Midjourney Alpha website until July 24, 2026.'
[2] FIRST-PARTY · 2026-07-24 (article:published_time 2026-07-24T22:18:48Z) · https://updates.midjourney.com/version-8-2/ — 'We are launching our V8.2 image model today.' It does not mention the Edit Model.
[3] FIRST-PARTY · 2026-07-24T22:24:48Z (fetched via cdn.syndication.twimg.com/tweet-result) · https://x.com/midjourney/status/2080781271043911807 — Official @midjourney: 'We're releasing V8.2 today and making it the default model on Midjourney.'
[4] FIRST-PARTY · updated 2026-09-01T17:19:52Z · https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — 'Character Reference is a feature compatible with Midjourney and Niji version 6 … was replaced by Omni Reference in V7, and the Edit Model in V8.X.' '--cw … default value is 100 (the maximum), but you can lower the value to narrow the details to just the face of your character.' 'The Retexture tool within the Editor is compatible with versions 7 and earlier … keeping the structure of the original image—like a template.' Contradiction: 'For information on the current default version (V7), please visit our Version article.'
[5] FIRST-PARTY · created 2026-08-28T20:52:18Z, updated 2026-09-04T18:46:32Z · https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model — 'Generate new images using up to 4 reference images (replacing Omni Reference and Character Reference).' 'The Edit model is compatible with Midjourney versions 8.1 and 8.2. It can also be used with Image Prompts, Style References, Moodboards, Personalization, and --hd.' 'not currently compatible with --tile' / 'Edit model image results are not currently compatible with Remix.' 'To use the Edit model in Discord, start by adding the --edit parameter to the end of your prompt, then pasting your image URL. If you want to use multiple images, separate each URL with a space.' 'The Edit model will automatically try to match the aspect ratio of the first image you upload … Your default aspect ratio settings will not automatically apply.' 'includes the functionality of previous features like Omni Reference and Character Reference, but with the ability to include up to four reference images.' 'let's see this image from the front / let's see this image from behind'. '--raw … allowing your prompt text to have more influence on the outcome.' A keyword scan finds 'weight' only in CSS font-weight, with no strength or slider.
[6] FIRST-PARTY · 2026-08-27 (published 2026-08-27T23:32:15Z) · https://updates.midjourney.com/edit-model-for-v8/ — 'Today we're gonna start letting everyone test our first V8.2 image edit model!' / 'Generating images with other images (replacing omni-reference) with up to 4 image references at once' / 'Type --edit url... on Discord'. No weight is mentioned.
[7] FIRST-PARTY · 2026-08-29 (published 2026-08-29T00:35:46Z) · https://updates.midjourney.com/edit-image-quality-update/ — 'we've updated our V8.2 edit model for better image quality'
[8] FIRST-PARTY · updated 2026-09-01T16:30:42Z · https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — Badge HTML: <p class="custom_incompatible" data-title="This feature is not supported in V8.2">When using V8.X, use the Edit Model instead… 'Omni Reference can only be used with Midjourney version 7.' '--ow … any value between 1 and 1,000, with the default being --ow 100 … keep your weight below 400' / 'Omni Strength slider in the Imagine bar'. 'You can only use one image with Omni Reference.' 'not compatible with Fast Mode, Draft Mode & Conversational Mode, or --q 4.' 'not compatible with features like inpainting or outpainting that still use V6.1.' 'results currently are not compatible with Vary Region, Pan, or Zoom Out.' 'intricate details like specific freckles or logos on clothing may not perfectly match your reference.'
[9] FIRST-PARTY · 2025-05-01 (published 2025-05-01T23:03:26Z) · https://updates.midjourney.com/omni-reference-oref/ — 'This parameter goes from 0 to 100 to 1000 (100 is default)'; 'If you want to make sure that a character's face is extremely visible (or that their clothes are preserved) you should try something higher like –-ow 400'; 'there's a slider in the web ui'
[10] FIRST-PARTY · updated 2026-09-01T17:18:30Z · https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'Omni Reference … (replaced by the Edit Model in V8.X) --oref'; 'Edit Model Create and modify images using written instructions and up to four reference images using --edit'; 'Image Weight Control the impact of image prompts --iw'; 'Parameters always go at the end of your text prompt'. There is no --ow entry.
[11] FIRST-PARTY · updated 2026-08-31T19:20:10Z · https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts — Table 'Version 8.1 | Version 7 | Niji 7': 'Image Weight Default 1 | 1 | 1', 'Image Weight Range 0 - 3 | 0 - 3 | 0 - 2'. 'Midjourney uses Image Prompts and references as inspiration to guide new creations, not to copy them exactly.' 'paste your image URL at the beginning of your text prompt.' Needs 'either multiple Image Prompts or a combination of one Image Prompt and a text prompt.'
[12] FIRST-PARTY · 2026-04-14 · https://updates.midjourney.com/v8-1-alpha/ — 'Image prompts and even image weights are now available in V8.1'
[13] FIRST-PARTY · updated 2026-09-01T17:28:05Z · https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference — 'It doesn't copy objects or people, just the overall style'; '--sw … any value between 0 and 1000, with the default being --sw 100'; '--sw is not compatible with Moodboards'; '--sref URL1::2 URL2::1 URL3::1'; 'Style Reference can be combined with Edit Model references and Image Prompts.'
[14] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32433330574221-Personalization — 'Your V7 Global Personalization Profile is compatible with V8.2.' 'V8 profiles are currently not compatible with V7.' 'The stylize parameter accepts values from 0 to 1000. The default is 100.'
[15] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/39193335040013-Moodboards — 'compatible with Midjourney versions 6 and later, but cannot be used with Style Reference Version (--sv) or Style Weight (--sw).' '(example: --p mID)'
[16] FIRST-PARTY · updated 2026-09-02T22:15:51Z · https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor — 'Inpainting and outpainting now use the new Edit Model for V8.X.' External images: 'upload an image directly from your device, or paste an image URL.' 'When you submit an edit using layers, only the areas of your image with visible transparency will be regenerated … any visible parts will remain unchanged.' 'without erasing or making any selections … This new edit will apply to the entire image.' 'images from your gallery made using Omni Reference can only be opened in the Edit tab. You will need to remove the Omni Reference and --ow parameter before submitting your edits.' Edit-model creations 'will appear on midjourney.com for other members to see unless you have Stealth mode enabled. This applies to Midjourney-generated images and external images.' 'Retexturing is now a built-in functionality of the Edit Model for V8.X.' 'To access the old Retexture feature, set your default version to V7 or earlier.'
[17] FIRST-PARTY · updated 2026-09-01T17:35:13Z · https://docs.midjourney.com/hc/en-us/articles/33329300781837-Web-vs-Discord — Editor row: ✓ midjourney.com, ✗ Discord. 'designate your image as an Image Prompt, Style Reference, or Edit Model reference—even use it as all three!'
[18] FIRST-PARTY · updated 2026-08-31T19:42:17Z · https://docs.midjourney.com/hc/en-us/articles/33390732264589-Creating-on-Web — 'Use the image as an Edit Model reference to make edits or maintain character/object consistency.' 'The maximum image file size you can upload to Midjourney is 10MB.'
[19] FIRST-PARTY · updated 2026-09-01T17:21:15Z · https://docs.midjourney.com/hc/en-us/articles/33329329805581-Modifying-Your-Creations — 'use reference images to achieve things like character consistency (it replaces Omni Reference and Character Reference in V8.X)'; 'Vary Region / Erase … precise alterations without changing the rest of the image.'
[20] FIRST-PARTY · updated 2026-08-31T18:48:32Z · https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — 'Other Image Reference Types (not compatible with video generations): Edit Model Reference (Attach to prompt)'
[21] FIRST-PARTY · updated 2026-08-28T23:10:23Z · https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo — 'Edit Model SD Prompt 1 minute / Edit Model HD Prompt 2.3 minutes / Omni Reference Prompt (V7) 2 minutes'. The Relax limitations list ('Permutation prompts, the repeat parameter, HD resolution videos, and Max Upscale') does not mention the Edit Model.
[22] FIRST-PARTY · updated 2026-07-27T16:06:57Z · https://docs.midjourney.com/hc/en-us/articles/35577175650957-Draft-Conversational-Modes — 'Draft mode is compatible with Midjourney versions 7 and 8.1'; 'A single Draft mode prompt in V8.1 or V8.2 will generate a big batch of 24 images.'; 'Conversational mode is compatible with Midjourney version 7 and 8.1.'
[23] FIRST-PARTY · 2024-03-12 · https://updates.midjourney.com/character-refs/ — 'You can use --cw to modify reference strength from 100 to 0 … At strength 0 (--cw 0) it'll just focus on face'
[24] FIRST-PARTY · 2026-06-11 (published 2026-06-11T04:08:51Z) · https://updates.midjourney.com/v8-1-is-now-the-default-model/ — 'V7 omni-reference is available to use while we finish training the improved version for V8'; 'we will be deprecating our V8.0 alpha model in two weeks'
[25] FIRST-PARTY · published 2026-09-24T01:59:23Z (9/23 changelog) · https://updates.midjourney.com/alpha-changelog-9-23-26/ — 'The editor now supports v8.1 and v8.2 edit types, and edit canvases can run in HD.' 'Pasted prompts keep their image prompts instead of turning into edit references.' (alpha site). No edit weight is mentioned.
[26] FIRST-PARTY · updated 2026-03-25 · https://docs.midjourney.com/hc/en-us/articles/32019750070669-Stealth-Mode — 'Stealth mode is available only to Pro and Mega Plan members.'
[27] FIRST-PARTY · Version Effective Date: May 27, 2026 (Zendesk updated 2026-08-17) · https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — 'Please do not create any dependencies on any attributes of the Services or the Assets.' 'You may not use automated tools to access, interact with, or generate Assets through the Services.'
[28] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights — 'Multi-prompts work with Midjourney versions 1, 2, 3, 4, Niji 4, 5, Niji 5, 6, Niji 6, and 6.1.'
[29] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32176522101773-Quality — '--q 4 is not compatible with Omni Reference.'
[30] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds — 'For consistency in your images, we recommend style references, omni references, and personalization.' (stale relative to V8.x)
[31] FIRST-PARTY · updated 2026-07-27 · https://docs.midjourney.com/hc/en-us/articles/32794723105549-Vary-Region — 'Vary Region is available on V8.2 SD images in Discord. Note that Vary Region currently uses V6.1. To edit HD images, you can use the Edit tools on midjourney.com, but the results will be SD resolution'
[32] FIRST-PARTY · 2026-05-27 · https://updates.midjourney.com/web-updates-5/ — 'Upload error message now shows the correct 20 MB limit.' (contradicts the 10MB in [18])
[33] FIRST-PARTY · Wayback capture 2026-04-04 · https://web.archive.org/web/20260404144227id_/https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — Badge data-title="This feature is not currently supported in V8 Alpha."
[34] FIRST-PARTY · Wayback capture 2026-06-11 · https://web.archive.org/web/20260611023543id_/https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — Badge data-title="This feature is not currently supported in V8.1"; 'Adding an Omni Reference image to the Imagine bar will automatically run the prompt in V7.' This is the last capture before today.
[35] FIRST-PARTY · Wayback capture 2026-06-18 · https://web.archive.org/web/20260618022947id_/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — The Version chart shows '(Uses V7)' on Omni Reference and Omni Reference Weight for V8.x. The 20260611023347 capture has no such note.
[36] FIRST-PARTY · Wayback capture 2026-07-31 · https://web.archive.org/web/20260731111048id_/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — '(Uses V7)' is still present on Omni and Omni Weight for V8.x. It is absent from today's chart.
[37] FIRST-PARTY · Wayback capture 2025-05-12 · https://web.archive.org/web/20250512033313id_/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — The Parameter List has '--cref' and no --oref, --ow or --cw. The 20250702124452 capture adds --oref, still with no --ow.
[38] FIRST-PARTY · Wayback capture 2026-07-09 · https://web.archive.org/web/20260709023826id_/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — 'Omni Reference … (replaces Character Reference in V7) --oref', with no --ow. The 20260905023030 capture has --oref and --edit, with no --ow.
[39] FIRST-PARTY · Wayback capture 2026-09-01 · https://web.archive.org/web/20260901221421id_/https://docs.midjourney.com/hc/theming_assets/17091846/15004028046605/style.css?digest=48590226229645 — '.custom_incompatible::before { content: attr(data-title); color: #f2330d; … }'. The badge text is rendered visibly on the page.
[40] secondary · repo HEAD 7d9cc26, read 2026-09-23 · pipeline/autogen.py — Repo evidence, not an MJ doc. Line 327: prompt = still_prompt + ' --oref %s --ow %d --v %s'. Lines 79-82: MJ rejected --oref on v8.1 ('`--oref` is not compatible with `--version 8.1`'). MODEL_STACK.md:62-63 and :213 hold the prior claims corrected above.
[41] secondary · Sep 2 (2026) · https://www.woollyferncreative.com/blog/midjourney-aug-2026-update-edit-model — SECONDARY opinion only: 'I think it's a significant upgrade compared to OREF in V7.' Not used as fact.
[42] secondary · 2026-08-28T23:21:45Z (via syndication) · https://x.com/cfryant/status/2093479178704445933 — SECONDARY third-party user report: 'Low resolution output (1472 x 816 at 16:9)'. Not used as fact.

## Contradictions (first-party vs first-party — unresolved)
- Current default version. The Version doc says 'The current default Midjourney version is V8.2.' (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version, updated 2026-09-01). The V8.2 post (https://updates.midjourney.com/version-8-2/, 2026-07-24) and the official X post (https://x.com/midjourney/status/2080781271043911807, 2026-07-24) agree. Legacy Features says 'For information on the current default version (V7), please visit our Version article.' (https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features, updated 2026-09-01). Reported, not resolved.
- Draft Mode on V8.x. The Version chart marks Draft Mode ✗ in the V8.1 & V8.2 column (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version, updated 2026-09-01). The Draft doc says 'A single Draft mode prompt in V8.1 or V8.2 will generate a big batch of 24 images.' and 'Draft mode is compatible with Midjourney versions 7 and 8.1' (https://docs.midjourney.com/hc/en-us/articles/35577175650957-Draft-Conversational-Modes, updated 2026-07-27).
- Conversational Mode on V8.2. The Version chart marks Conversational ✓ for 'V8.1 & V8.2' (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version). The Draft & Conversational doc says 'Conversational mode is compatible with Midjourney version 7 and 8.1.' (https://docs.midjourney.com/hc/en-us/articles/35577175650957-Draft-Conversational-Modes).
- --ow lower bound. The Omni doc says 'any value between 1 and 1,000, with the default being --ow 100' (https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference, updated 2026-09-01). The launch post says 'This parameter goes from 0 to 100 to 1000 (100 is default)' (https://updates.midjourney.com/omni-reference-oref/, 2025-05-01).
- Upload size limit. Creating on Web says 'The maximum image file size you can upload to Midjourney is 10MB.' (https://docs.midjourney.com/hc/en-us/articles/33390732264589-Creating-on-Web, updated 2026-08-31). web-updates-5 says 'Upload error message now shows the correct 20 MB limit.' (https://updates.midjourney.com/web-updates-5/, 2026-05-27).
- Stale-doc drift, not a strict contradiction. The Seeds doc still recommends 'omni references' for consistency (https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds, updated 2026-07-27), while the V8.x docs say the Edit Model replaced Omni. Vary Region says 'Vary Region currently uses V6.1' on V8.2 in Discord (https://docs.midjourney.com/hc/en-us/articles/32794723105549-Vary-Region, updated 2026-07-27), while the Version chart says the V8.x Editor, Pan and Zoom Out are 'Using Edit Model'.

## Could not confirm
- Whether any weight, strength or slider for Edit Model references exists in the live midjourney.com UI. None appears in any of the 105 help-center articles or in the updates posts up to the 9/23 changelog. The live UI could not be inspected: Cloudflare returns 403 and browser automation is not permitted.
- Whether '--edit <url>' works as prompt text on the midjourney.com web Imagine bar, a web or API submission, or the third-party midjourney.api client. The how-to is Discord-only, although the Parameter List lists --edit.
- Whether Edit Model jobs can run in Relax mode. Neither the Edit Model doc nor the GPU Speed doc says so either way.
- Whether the Edit Model works with Draft or Conversational mode.
- Whether --iw or --stylize changes how strongly an Edit Model reference preserves identity, and what happens when the same anchor is attached as both Image Prompt and Edit reference.
- The --iw range for V8.2 specifically. The table column is labelled only 'Version 8.1'.
- Any first-party measurement of face or identity fidelity for the Edit Model versus V7 --oref.
- The Edit Model's output resolution. There is no first-party figure.
- Any first-party plan or date to retire V7, --oref or --ow, or to port them to V8.x. Discord #announcements was not read (requires auth). Official X was checked only via one post ID and a site-restricted search.
- Whether the web UI still shows an 'Omni Reference section' when V7 is selected. The Omni doc tells users to drop the image there, but its own 'Image Reference Types' list omits Omni.
- What the alpha-site 'Use Subject' action does. It is mentioned only in the 8/20 changelog.
- Whether the Edit Model supports Niji. The V8.x chart column marks the Niji Version ✗ in general.
- Whether the Discord Vary Region on V8.2 still uses V6.1 (Vary Region doc, updated 2026-07-27, before the Edit Model launched) or now uses the Edit Model (the Version chart says V8 Editor/Pan/Zoom Out 'Using Edit Model').
- What article ID 32162917505293 (formerly the Character Reference slug) is now. A search engine titled it 'Edit Model', but the help-center API returns RecordNotFound.
- Whether an Edit Model perspective or pose edit of the V7 canonical keeps the face recognisably identical. No first-party claim either way.

## Dropped claims (refuted or unsupported in verification)
- Researcher correction #1, that the current Omni Reference doc 'does not contain the words not supported in V8.2'. CONTRADICTED and re-verified: the article HTML has data-title="This feature is not supported in V8.2", and the theme CSS renders it with '.custom_incompatible::before { content: attr(data-title) }'. MODEL_STACK.md:62-63 stands.
- 'Tunable weight: NO', stated as fact. Downgraded to 'none documented', because the live UI was not inspected.
- 'The only documented pixel-exact route … keeps the V7 face pixels exactly'. Unsupported wording. The doc says 'remain unchanged', in the Layers section only; the fill is V6.1 or the Edit Model; HD inputs are downscaled to SD.
- Missing-vs-V7 item: 'web prompt-text syntax, --edit documented for Discord only'. Dropped as a V7→V8 difference: --oref is also documented only for Discord, and the Parameter List lists both without a platform.
- Missing-vs-V7 item: 'only the V6 --cw had documented face semantics'. Corrected: the V7 --ow launch post gives face guidance ('--ow 400'), and --cw is documented as 0–100 with --cw 0 'just focus on face'.
- Could-not-confirm item: 'lower bound of --cw not given'. Resolved first-party: 'from 100 to 0' (updates.midjourney.com/character-refs/, 2024-03-12).
- '2026-06-11 is the only 2026 Wayback capture of the Omni doc'. Contradicted: a 200 capture exists at 20260404144227.
- c14's attribution of the quote '(replaces Character Reference in V7) --oref' to the 2025-05-12 Parameter List capture. Wrong: that capture shows only '--cref'. The Omni entry first appears in 20250702124452.
- c40's implication that '(Uses V7)' was first seen on 2026-07-31. It is already present in the 20260618022947 capture.
- 'The official X account is not fetchable'. Contradicted: it was fetched through cdn.syndication.twimg.com and corroborates the V8.2 default on 2026-07-24.
- c49 (woollyfern opinion that the Edit Model beats OREF). Secondary only; moved to do_not_quote.
- c50 (1472x816 Edit output). Secondary only (a third-party X user, re-fetched); moved to do_not_quote.
- 'Retexture … so it can't change pose'. Inference, replaced by the doc's wording 'keeping the structure of the original image—like a template'.
- The Omni 'closest tunable proxy' presented as a recommendation. Kept only as 'documented as combinable; effect on identity undocumented'.

## DO NOT QUOTE (low/unknown)
- [low] Edit Model character consistency is 'a significant upgrade compared to OREF in V7' — Only a third-party blog says this (woollyferncreative.com). No first-party claim exists.
- [low] Edit Model output is 1472 x 816 at 16:9 — A single third-party X user report (@cfryant, 2026-08-28). There is no first-party figure.
- [low] The Editor erase/layers route keeps the V7 face 'pixel-exact' or 'exactly' — MJ says only 'will remain unchanged', in the Layers section. The fill is V6.1 or the Edit Model, never V7. HD inputs are downscaled to SD, and an unmasked submit re-renders the whole image.
- [low] Retexture 'cannot change pose' — This is an inference. The doc says only that it keeps 'the structure of the original image—like a template'.
- [unknown] The Edit Model has no weight parameter at all — The only supportable claim is that no weight is documented. The live UI was not inspected.
- [unknown] Attaching the anchor as Image Prompt + Edit reference and raising --iw strengthens identity — Combining them is documented. Any effect on identity is not documented, and MJ says references are 'not to copy them exactly'.
- [unknown] '--edit <url>' works through the web prompt bar or the third-party midjourney.api client — The how-to is documented only for Discord. Web and API behaviour is unverified.
- [unknown] Edit Model jobs run in Relax mode — The docs do not say either way. The V8.x chart's Relax ✓ is general, not specific to the Edit Model.
- [unknown] Edit Model works with Draft or Conversational mode — Not documented. The Draft status on V8.x is itself contradictory between first-party docs.
- [unknown] Draft Mode is (or is not) available on V8.1/V8.2 — First-party contradiction: the Version chart says ✗, the Draft doc says 'A single Draft mode prompt in V8.1 or V8.2 will generate a big batch of 24 images'.
- [unknown] Conversational Mode on V8.2 — First-party contradiction: the Version chart says ✓ for 'V8.1 & V8.2', the Draft/Conversational doc says 'version 7 and 8.1'.
- [low] --iw range 0–3 applies to V8.2 — The Image Prompts table labels the column 'Version 8.1' only. The Version chart marks Image Weight ✓ for V8.1 & V8.2 but gives no range.
- [low] --ow minimum is 0 (or 1) — First-party contradiction: the doc says 'between 1 and 1,000', the launch post says '0 to 100 to 1000'. Not load-bearing for --ow 160.
- [unknown] Upload size limit (10MB vs 20MB) — First-party contradiction between Creating on Web (10MB) and web-updates-5 (20 MB).
- [unknown] Any date or plan for retiring V7, --oref or --ow — No first-party statement was found. The only pointer is precedent: V8.0 was pre-announced 'in two weeks' but lasted until 2026-07-24.
- [low] MODEL_STACK.md:213 '--ow has quietly dropped out of the current Parameter List' — Unsupported. --ow is absent from every Parameter List capture checked, 2025-05-12 through 2026-09-05, so it never 'dropped out'.
- [low] Discord Vary Region on V8.2 uses V6.1 — The Vary Region doc (2026-07-27) predates the Edit Model launch and may be stale compared with the Version chart's 'Using Edit Model'.
- [unknown] The meaning of the alpha 'Use Subject' action — It is mentioned only in the 8/20 changelog, with no description.
- [unknown] Edit Model availability on Niji — Not stated. The V8.x chart column marks Niji ✗ in general.
- [unknown] The Edit Model preserves the canonical's face under perspective or pose edits — MJ documents perspective changes but makes no claim about face or identity fidelity.


---

# Track MJ3 — Midjourney video: end frames, versioning, coupling to the image model
Primary mission track: yes · Final confidence: high

## Answer
## MJ3 (final): Midjourney video, end frames, and how video relates to the image-model version (checked 2026-09-23)

### Short answer
- **Video model version.** No official video version is named after "V1". Only two first-party posts name a video model, and both say V1: [3] on 2025-06-11 and [2] on 2025-06-18. The launch tweet is [1]. The current Video doc (updated 2026-08-31) names no version [4]. So do not say the service runs "V1" today; the docs cannot confirm which weights are being served.
- **Start frame, end frame and loop.** All three are documented for uploaded images [4][10], and they shipped on 2025-07-24 [8][9]. Every autogen edge is an upload-start → upload-end clip, which is a documented use.
- **Coupling to the image version.** No first-party doc ties video generation to an image version.
  - Video takes only video parameters, and `--v` has never been one of them [4][5].
  - Omni Reference has been listed as "not compatible with video generations" on every snapshot [5][6][4].
  - V8.2-era docs and changelogs still document start/end-frame video [4][22].
  - One first-party form points the other way: the EU training summary lists the "Image and Video family of models" with "Model dependencies: Midjourney V8, V8.1, and V8.2" [33]. Its dates are internally inconsistent, so the question is unresolved (see Contradictions).
- **If V7 / `--oref` retired tomorrow:**
  - New pose stills lose their documented path.
  - New edges between existing uploaded stills hit no documented blocker.
  - The documented risk is different: the video model itself cannot be pinned and can change underneath the project.

### 1. Video model name/version
| Item | Finding | Src |
|---|---|---|
| Launch | "We're releasing Version 1 of our Video Model" (2025-06-18) | [2][1] |
| Pre-launch | "finishing touches on our V1 Video Model" (2025-06-11) | [3] |
| Later versions | None. Searched all 92 posts [45], @midjourney posts from 2026-06-11 to 2026-09-16 [46], the current Video doc [4] and snapshots from 2025-06-19 to 2026-09-05 [5][6][7]. No "V1", "V2" or "video model" in any doc version. | [4][45][46] |
| Latest alpha changelog (2026-09-24T01:59Z) | Only "Videos play on hover again." No model change. | [24] |

### 2. Uploaded start frame, End Frame, Loop (all first-party)
- **Discord:** "paste your image URL at the beginning of your prompt and then add the --video parameter … A text prompt is optional." [4]
- **Web:** "upload new images … Drag and drop your image into the Animate section." [4]
- **End frame / loop:**
  - "add --loop to the end of your video prompt. To use a different image as your ending frame, add the --end parameter … and paste your image URL." [4]
  - On web: "Loop" checkbox / "Ending Frame section" [4].
  - The Parameter List says: "Create looping video generations with --loop and set a custom end frame using --end" [10].
- **Shipped:** "You can now make videos with a specific start and end images … To set an end frame, use --end image_url" (posted 2025-07-25T00:33Z; X post 2025-07-24) [8][9].
- **External uploads since launch:** "animate images uploaded from outside of Midjourney" [2].
- **Parity caveat:** MJ documents the web UI and Discord only. "Midjourney does not provide an API" [32]. autogen's wire fields (`image_url`, `end_image`, `motion_prompt`, `loop`) belong to the undocumented third-party client. The features match; the interface is not documented.

### 3. Does video depend on the image version?
- **Parameters:** "Video generations are only compatible with video-specific parameters: --motion low, --motion high, --raw, --loop, --end, and --bs #." [4]
  - 2025-06-19: "--motion low, --motion high, and --raw" [5].
  - `--v` has never been listed. The docs describe no way to pin a video version.
- **Any image version:** "All images in your gallery (regardless of what version they were made in) now have Animate Image buttons" (same text since 2025-06-19) [4][5].
- **Image parameters dropped:** "Any image parameters used to generate your original image will be automatically removed when generating videos." [4] This applies to gallery images. autogen uploads its frames anyway [48].
- **`--oref` never fed video.** The "not compatible with video generations" list read:
  - 2025-06-19 to 2026-06-11: "Omni Reference (replaces Character Reference)" [5]
  - 2026-08-18: "Omni Reference (V7)" [6]
  - 2026-09-05 and now: "Edit Model Reference (Attach to prompt) / Style Reference / Image Prompt" [7][4]
- **Web settings:** the version setting is described as "your default Midjourney version for generating images". SD/HD video and video batch size are separate settings. The doc does not say whether the version setting affects video [12].
- **No version banner:** the Video doc carries no "supported / not supported in V8.2" banner; its only callout is "Important" [4]. Omni Reference, by contrast, carries "This feature is not supported in V8.2" [16].
- **Version doc:** zero mentions of video or animate [14].
- **Only version-gated video item:** profile and banner videos: "Currently only V7 and Niji 6 creations can be used." [42] This is not a generation limit.
- **V8.2 era (default since 2026-07-24 [14]):**
  - Video doc edited 2026-08-31 [4].
  - Alpha fix: "dropping images on the Start and End Frame pills now works correctly" [22].
  - Alpha-only breakage: "Animate now works (sorry for breaking it)" (2026-09-16) [23]. The main site is not mentioned.

### 4. Video changes 2025–2026 (first-party)
| Date (UTC) | Change | Src |
|---|---|---|
| 2025-06-18 | V1 launch. Four 5 s videos per job. Extend "roughly 4 seconds at a time - four times total". Relax testing for Pro. | [2] |
| 2025-06-19 | "video relax mode" test for Pro/Mega. "Save for Social Media" encoder (export only). | [25][26] |
| 2025-07-24/25 | End frame, `--loop`, Discord `--video`. Discord: "virtual upscale buttons" for a "higher-quality .mp4"; remix to change the prompt when extending. | [8][9] |
| 2025-08-07 (Aug 6 US Pacific) | HD: "native 720p", "~3.2x more expensive", Pro/Mega only, "does not work with relax mode". Calls SD the "normal SD resolution video model". | [27] |
| 2025-08-13 | HD for Standard. `--bs 1` / `--bs 2`. Thumbnails show the last frame. "improved video moderation accuracy". | [28] |
| Now | Relax video: "only Pro and Mega plans … (SD resolution only)". HD: "only in Fast Mode". | [4][29][30] |
| Now | Default batch 4 (1/2/4, works in Fast and Relax). GPU time: SD 8/4/2 min, HD 26/13/7 min. | [4] |
| Now | 480p SD / 720p HD. 1:1 → 624×624 / 960×960; 2:3 → 512×768 / 784×1168; 4:3 → 77:58; 16:9 → 91:51. "may need to adjust the aspect ratio slightly". | [4] |
| Now | Extend "+4 seconds … up to 4 times, until it reaches 21 seconds". Same GPU cost as a new job. "Extend Manual" lets you change the prompt. | [4] |
| Now | Pro/Mega: concurrent videos "6 Fast or 3 Relax" / "12 Fast or 3 Relax". Queue "10 jobs* (3 Relax videos)". Relax waits "0 to 30 minutes", longer the more you use Relax. | [30][29] |

No first-party notice exists of a new video model, a video deprecation, or a video retrain.

### 5. Silent video-model change: allowed, undetectable, never documented
- **No pin:** there is no video version string and no video `--v` [4].
- **ToS:** "subject to modification and change, including … the algorithms used to generate the Assets … Please do not create any dependencies on any attributes of the Services" [31].
- **EU summary:** "continuously trained and may undergo additional fine-tuning which may be released in new versions" [33].
- **Vendor practice (image models):** weights have been updated in place under an unchanged version string.
  - V7, 2025-04-30: "This applies to all images made with --v 7. you don't need to change anything" [35].
  - V7, 2025-05-02: "The new model should have slightly improved hands, but if you want the old version you can still get it via --q 2" [36].
  - V8.1, 2026-04-30: "improved sharpness and image quality for V8.1" [37].
  - V8.2 edit model, 2026-08-29: "updated our V8.2 edit model" [38][39].
  - Alpha: "Things will change! Perhaps without notice!" [40].
  - `--preview`: "not guaranteed to run consistently over time" [41].
- **Conclusion:** at MJ a version string is not a weight pin. For video no update is documented, but nothing would reveal one. Transition motion can drift with no signal.
- **SD and HD are different renderers:** HD "may give you slightly better coherence or motion" [27]. `VIDEO_MODE="relax"` forces SD [4]. Any HD/Fast re-render would come from a different path and resolution than the existing graph.

### 6. KEY ANALYSIS: V7 / `--oref` retired tomorrow
**Signs of retirement:**
- Omni Reference "can only be used with Midjourney version 7" and is flagged "not supported in V8.2" [16]. The Parameter List says "(replaced by the Edit Model in V8.X)" [10].
- MJ called it interim: "V7 omni-reference is available to use while we finish training the improved version for V8" (2026-06-11) [20]. That condition now appears met: the V8 Edit Model shipped 2026-08-27, "replacing omni-reference" [19].
- No V7 or `--oref` retirement date exists anywhere [14][16]. V7's default period ended 2026-06-09 [14].
- The only precedent is V8.0. It was an alpha-only model, retired after notice given two weeks ahead on both channels [20][21], ending 2026-07-24; its images stay in the gallery [14]. A V7 notice would likely appear on updates.midjourney.com and X, but that is an inference from one precedent.

**What stops:**
- **New pose stills.** The `--oref <hub> --ow 160 --v 7` recipe [48] has no documented non-V8 substitute. The Edit Model "is compatible with Midjourney versions 8.1 and 8.2" [18], which is the closed V8 door.
- **Edges whose endpoint is a new pose,** because they need a new still.

**What the docs do not block:**
- New edges and idle loops between existing uploaded stills. Evidence:
  - The video path takes an uploaded start and end image [4].
  - It takes no `--v` [4] and never accepted `--oref` [5][6].
  - It animates images "regardless of what version" [4].
  - autogen uploads every frame from local disk (`upload_image`) and sends no version argument on `submit_video`: local branch :341-343, :355-356, :364-365, :484, :492; master :337, :351, :360, :449, :457 [47][48].
- Remaining risks for these edges, none of them tied to V7:
  - The video model is unpinned and changeable (§5).
  - The docs promise nothing about identity in the intermediate frames.
  - Relax requires Pro/Mega and SD, with a cap of 3 relax videos [4][30].
  - `VIDEO_TAKES = 4` relies on the default batch of 4 [4][48].
  - The docs warn of moderation friction: "seemingly innocent prompts may be blocked" [4].
  - The ToS and Community Guidelines ban automation (Side findings).

**A new-pose path without `--oref`.** Each step is documented, but MJ never documents them as one workflow:
1. Animate an existing still with a start frame only and a manual motion prompt [4][2]. Optionally use "Extend Manual" to change the prompt, +4 s per extension up to 21 s [4] (Discord: "Turn on remix mode to change the prompt when extending" [8]).
2. Download it: "Download Raw Video … (file format is .mp4)" [4], or on Discord use the virtual upscale buttons for a "higher-quality .mp4" [8].
3. Extract a frame locally. This is not an MJ feature.
4. Re-upload the frame as a start or end image [4].

**Limits of that path:**
- Frames are 480p (SD) or 720p (HD, Fast only). For example, 1:1 is 624×624 / 960×960 and 2:3 is 512×768 / 784×1168 [4]. An upscaled V7 1:1 still is 2048×2048 [43]. The size of autogen's grid variant is undocumented.
- The aspect ratio can shift [4].
- Undocumented: whether `--end` can be combined with Extend, and whether face fidelity holds.

### Side findings
- **Automation ban, independent of the version question:**
  - ToS: "You may not use automated tools to access, interact with, or generate Assets through the Services." Also: "suspend or ban Your access … at any time, and for any reason" [31].
  - Community Guidelines: "Midjourney does not provide an API … automating interactions with Midjourney service is strictly prohibited … Accounts who do not comply … may be blocked" [32].
  - Any unattended third-party client falls under these clauses [48].
- **`--ow` correction:** `--ow` is absent from every Parameter List snapshot checked (2025-05-03, 2025-09-05, 2026-01-21, 2026-07-09, and live) [11][10]. The prior sweep said it "dropped out"; it was never listed there. It is documented on the Omni Reference page: "any value between 1 and 1,000, with the default being --ow 100" [16]. `--oref` is present in the Parameter List by 2025-09-05 [11].

### Contradictions (first-party, not adjudicated)
See the `contradictions` field. In short:
- Legacy Features says the default is V7; the Version doc says V8.2.
- Upload limit: 10 MB vs 20 MB.
- The EU summary's dates vs the Version doc's release dates.
- `--ow` lower bound: 0 vs 1.
- `--oref` in Fast Mode.
None of these changes the MJ3 conclusions.

### DO NOT QUOTE (low/unknown)
- "V2 video model on the post-V8 roadmap": search-summary text only; dropped.
- "First MJ video model in April 2026": SEO, contradicted.
- The served video model is still the V1 weights: unknown.
- The video model was retrained on V8.x: unknown.
- A silent video change has shipped: unknown.
- Upload limit (10 MB vs 20 MB): conflicting.
- "`--ow` recently dropped from the Parameter List": false framing.
- `--end` combined with Extend: undocumented.
- Identity in intermediate frames: undocumented.
- Extracted frames being usable as pose stills: unknown.
- V7/`--oref` end-of-life date: none exists.
- Client sends a video model or version field: unknown.
- The account's plan tier: unverified.
- Whether the alpha Animate breakage hit the main site: unknown.
- Grid-variant pixel size: undocumented.
- EU summary dates used as evidence: unreliable.
- "Default is V7" per Legacy Features: contradicted.
- `--oref` in Fast Mode: ambiguous.
- "autogen payload matches MJ's API": MJ has no API.
- Office Hours / Discord statements: not accessed.
- Whether a "rare exceptions explicitly granted" API permission applies to this project: unknown.

## Sources
[1] FIRST-PARTY · 2025-06-18 (created_at 2025-06-18T16:40:55Z via cdn.syndication.twimg.com, accessed 2026-09-23) · https://x.com/midjourney/status/1935377193733079452 — "Introducing our V1 Video Model. It's fun, easy, and beautiful. Available at 10$/month, it's the first video model for *everyone* and it's available now."
[2] FIRST-PARTY · 2025-06-18 (article:published_time 2025-06-18T16:35:15Z) · https://updates.midjourney.com/introducing-our-v1-video-model/ — "We’re releasing Version 1 of our Video Model to the entire community"; "extend them - roughly 4 seconds at a time - four times total"; "animate images uploaded from outside of Midjourney. Drag an image to the prompt bar and mark it as a “start frame”"; "each job will produce four 5-second videos"; "testing a video relax mode for “Pro” subscribers"; "Many of these learnings will come back to our image models"
[3] FIRST-PARTY · 2025-06-11 (published 2025-06-11T22:26:25Z) · https://updates.midjourney.com/video-rating-party-1/ — "We're putting the finishing touches on our V1 Video Model and we need your help!" (second and only other post naming a video model; also V1)
[4] FIRST-PARTY · updated 2026-08-31T18:48:32Z (Zendesk API); accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — No version named; own-image start frame ("paste your image URL at the beginning of your prompt and then add the --video parameter"; "Drag and drop your image into the Animate section"); --loop/--end and Ending Frame/Loop checkbox; "only compatible with video-specific parameters: --motion low, --motion high, --raw, --loop, --end, and --bs #"; "regardless of what version they were made in"; image params "automatically removed"; not-compatible list = Edit Model Reference/Style Reference/Image Prompt; relax Pro/Mega SD only, HD Fast only; batch 4 default, SD 8/4/2 min, HD 26/13/7 min; 480p/720p dimension table; aspect adjust footnote; extend +4 s to 21 s, Extend Manual; Download Raw Video .mp4; moderation friction; only callout data-title="Important"
[5] FIRST-PARTY · archived 2025-06-19 · https://web.archive.org/web/20250619063500/https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — Archive of first-party doc: params "--motion low, --motion high, and --raw"; "Other Image Reference Types (not compatible with video generations): Image Prompt / Style Reference / Omni Reference (replaces Character Reference)"; 'regardless of what version' present. Same list in 20250905 and 20251201 and 20260611 snapshots (checked).
[6] FIRST-PARTY · archived 2026-08-18 · https://web.archive.org/web/20260818145755/https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — Not-compatible-with-video list reads "Image Prompt / Style Reference / Omni Reference (V7)"; no video version names
[7] FIRST-PARTY · archived 2026-09-05 · https://web.archive.org/web/20260905023030/https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — Not-compatible list becomes "Edit Model Reference (Attach to prompt) / Style Reference / Image Prompt"; params list unchanged, no --v; CDX shows 21 snapshots 2025-06-19..2026-09-05
[8] FIRST-PARTY · 2025-07-25T00:33:24Z (published) · https://updates.midjourney.com/looping-and-end-frame-for-video-video-in-the-discord-bot/ — "2) You can now make videos with a specific start and end images"; "To set an end frame, use --end image_url"; "To make a looping video, use --loop"; "enter the image url at the start of the prompt and use the --video arg"; "To get a higher-quality .mp4, click one of the virtual upscale buttons on a video"; "Turn on remix mode to change the prompt when extending"
[9] FIRST-PARTY · 2025-07-24T23:55:41Z · https://x.com/midjourney/status/1948532572251955462 — "we now support creating videos with specific start and end frames. This also means now do looping videos! Last, we’re bringing video generation to Discord."
[10] FIRST-PARTY · updated 2026-09-01T17:18:30Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — "Create looping video generations with --loop and set a custom end frame using --end"; "Generate videos in Discord using --video"; "Omni Reference! (replaced by the Edit Model in V8.X) --oref"; no --ow
[11] FIRST-PARTY · archived 2025-09-05 (also checked 20250503204241, 20260121170142, 20260709023826) · https://web.archive.org/web/20250905120803/https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — --ow count 0 in all four snapshots; --oref present from 2025-09-05 with "(replaces Character Reference in V7)"; absent in 2025-05-03
[12] FIRST-PARTY · updated 2026-08-31T19:42:17Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/33390732264589-Creating-on-Web — "your default Midjourney version for generating images"; "Switch between SD and HD resolution videos (if your plan allows)"; "Adjust your video batch size"; "The maximum image file size you can upload to Midjourney is 10MB."
[13] FIRST-PARTY · 2026-05-27T18:44:53Z (published) · https://updates.midjourney.com/web-updates-5/ — "Upload error message now shows the correct 20 MB limit." (conflicts with 10MB)
[14] FIRST-PARTY · updated 2026-09-01T17:26:08Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — "The current default Midjourney version is V8.2."; "V8.2 released as the default version on July 24, 2026 … Edit Model, which replaces Omni Reference, Character Reference, and the Retexture tool"; "V8.1 released on April 14, 2026"; V8.0 "no longer available for use" (alpha, until July 24, 2026); "V7 … was the default version from June 17, 2025 to June 9, 2026"; zero mentions of video/animate
[15] FIRST-PARTY · updated 2026-09-01T17:19:52Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — "For information on the current default version (V7), please visit our Version article." (contradicts Version doc)
[16] FIRST-PARTY · updated 2026-09-01T16:30:42Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — data-title="This feature is not supported in V8.2"; "Omni Reference can only be used with Midjourney version 7."; "any value between 1 and 1,000, with the default being --ow 100"; "currently not compatible with Fast Mode, Draft Mode & Conversational Mode, or --q 4"
[17] FIRST-PARTY · 2025-05-01T23:03:26Z (published) · https://updates.midjourney.com/omni-reference-oref/ — "This parameter goes from 0 to 100 to 1000 (100 is default)" (--ow lower bound differs from doc)
[18] FIRST-PARTY · updated 2026-09-04T18:46:32Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model — "(replacing Omni Reference and Character Reference)"; "The Edit model is compatible with Midjourney versions 8.1 and 8.2."; "Shift the perspective and show different views of an object or character"
[19] FIRST-PARTY · 2026-08-27T23:32:15Z (published) · https://updates.midjourney.com/edit-model-for-v8/ — "Generating images with other images (replacing omni-reference) with up to 4 image references at once"
[20] FIRST-PARTY · 2026-06-11T04:08:51Z (published) · https://updates.midjourney.com/v8-1-is-now-the-default-model/ — "V7 omni-reference is available to use while we finish training the improved version for V8"; "we will be deprecating our V8.0 alpha model in two weeks"
[21] FIRST-PARTY · 2026-06-11T04:02:13Z · https://x.com/midjourney/status/2064921117618557292 — "We've made V8.1 the new default model for all users on Midjourney. V8 will now be deprecated in 2 weeks."
[22] FIRST-PARTY · 2026-08-21T16:48:58Z (published) · https://updates.midjourney.com/changelog-8-20-26/ — alpha.midjourney.com: "Video mode: dropping images on the Start and End Frame pills now works correctly"
[23] FIRST-PARTY · 2026-09-16T22:22:24Z (published) · https://updates.midjourney.com/alpha-changelog-9-16-26/ — alpha.midjourney.com: "Animate now works (sorry for breaking it)."
[24] FIRST-PARTY · 2026-09-24T01:59:23Z (published; 9/23 US) · https://updates.midjourney.com/alpha-changelog-9-23-26/ — Only video item: "Videos play on hover again." (no model change)
[25] FIRST-PARTY · 2025-06-19T21:28:59Z (published) · https://updates.midjourney.com/best-ways-to-create-more-videos/ — "running out of fast hours with our new video models"; "Pro and Mega tiers can help us test \"video relax mode\" right now"
[26] FIRST-PARTY · 2025-06-19T05:32:18Z (published) · https://updates.midjourney.com/save-for-social-media/ — "We've created a new optimized encoder" for 'Save for Social Media' (export path only)
[27] FIRST-PARTY · 2025-08-07T01:29:13Z (published; Aug 6 US Pacific) · https://updates.midjourney.com/hd-mode-for-video/ — "~3.2x more expensive than normal Midjourney video"; "HD mode is only available on Pro and Mega plans and does not work with relax mode"; "native 720p resolution. Like our normal SD resolution video model"; "may give you slightly better coherence or motion"
[28] FIRST-PARTY · 2025-08-13T21:47:59Z (published) · https://updates.midjourney.com/new-video-options-and-a-home-for-moodboards/ — "HD video generation is now available for Standard Plan users"; "--bs 1 or --bs 2"; "thumbnails on video jobs so they show the last frame"; "improved video moderation accuracy"
[29] FIRST-PARTY · updated 2026-08-28T23:10:23Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo — "HD resolution videos … are not available while using Relax mode. Relax Mode for videos (SD resolution) is only available on the Pro and Mega Plans."; "wait times ranging from 0 to 30 minutes … depend on how much you've used Relax Mode"; Fast-mode cost table lists "Omni Reference Prompt (V7) 2 minutes", "Batch of 4 SD Videos 8 minutes", "Batch of 4 HD Videos 26 minutes"
[30] FIRST-PARTY · updated 2026-05-18T20:20:25Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans — "For unlimited video generations with Relax Mode, subscribe to the Pro or Mega Plan."; Maximum Concurrent Prompts (videos) Pro "6 Fast or 3 Relax", Mega "12 Fast or 3 Relax"; Maximum Queued Jobs Pro/Mega "10 jobs* (3 Relax videos)"
[31] FIRST-PARTY · Version Effective Date: May 27, 2026 (article updated 2026-08-17); midjourney.com/tos returned 403 to verifiers · https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — "the algorithms used to generate the Assets … Please do not create any dependencies on any attributes of the Services or the Assets."; "We reserve the right to modify or discontinue any aspect of the Service, including pricing and features, at any time."; "You may not use automated tools to access, interact with, or generate Assets through the Services."; "suspend or ban Your access to the Services at any time, and for any reason"
[32] FIRST-PARTY · updated 2026-08-17T20:06:41Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines — "With a few rare exceptions that are explicitly granted, Midjourney does not provide an API, nor provide third-party apps or scripts, and automating interactions with Midjourney service is strictly prohibited … Accounts who do not comply with these rules may be blocked."
[33] FIRST-PARTY · created 2026-08-11T21:20:22Z, updated 2026-08-17; body says 'Last update: March 17, 2026' · https://docs.midjourney.com/hc/en-us/articles/48067080311309-Public-Summary-of-Training-Content — "Versioned model name(s): Midjourney Image and Video family of models"; "Model dependencies: Midjourney V8, V8.1, and V8.2"; "Date of placement of the model on the Union market: March 17, 2026"; "The model is continuously trained and may undergo additional fine-tuning which may be released in new versions."
[34] FIRST-PARTY · C(2025) 8311 final, 'Brussels, 5.12.2025' (as fetched 2026-09-23) · https://ec.europa.eu/newsroom/dae/redirection/document/118480 — EU Commission template definition (first-party for the form, not for MJ): "If the model is the result of a modification, including fine-tuning, of one or more general-purpose AI models already placed on the Union market, specify the model (version) name(s) of that/those models" under 'Model dependencies'
[35] FIRST-PARTY · 2025-04-30T22:59:14Z (published) · https://updates.midjourney.com/v7-update-editor-and-exp/ — "New V7 image model update … This applies to all images made with --v 7 . you don't need to change anything" (in-place weight update, same version string)
[36] FIRST-PARTY · 2025-05-02T21:05:47Z (published) · https://updates.midjourney.com/fast-mode-for-v7/ — "We're launching V7 model speedups today … The new model should have slightly improved hands, but if you want the old version you can still get it via --q 2"; "--oref jobs are still 2x the cost of a normal --fast mode job"
[37] FIRST-PARTY · 2026-04-30T20:47:41Z (published) · https://updates.midjourney.com/v8-1-updates/ — "We've improved sharpness and image quality for V8.1!" (in-place update)
[38] FIRST-PARTY · 2026-08-29T00:35:46Z (published) · https://updates.midjourney.com/edit-image-quality-update/ — "we've updated our V8.2 edit model for better image quality" (in-place update)
[39] FIRST-PARTY · 2026-08-29T00:26:52Z · https://x.com/midjourney/status/2093495563467796751 — "We've updated our V8.2 edit model for better image quality. If you've had any issues in the last 24 hours give it a new shot"
[40] FIRST-PARTY · 2026-04-14T20:33:37Z (published) · https://updates.midjourney.com/v8-1-alpha/ — "Our V8 series of models are still only available on alpha.midjourney.com … Things will change! Perhaps without notice!"
[41] FIRST-PARTY · 2026-06-16T22:04:29Z (published) · https://updates.midjourney.com/draft-mode-for-v8-1-and-new-feature-previews/ — "Images that you create with --preview might be a little unpolished and the jobs are not guaranteed to run consistently over time."
[42] FIRST-PARTY · updated 2026-03-24T22:03:13Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/41117938447629-Profiles — Profile/banner videos: "To use a video, animate an image from your gallery that meets these requirements. Currently only V7 and Niji 6 creations can be used." (only version-gated video item; not a generation limit)
[43] FIRST-PARTY · archived 2025-11-21 · https://web.archive.org/web/20251121094711/https://docs.midjourney.com/hc/en-us/articles/33329374594957-Image-Size-Resolution — "when you use the default 1:1 aspect ratio , Midjourney version 7 creates upscaled images that are 2048 x 2048 pixels (px)"
[44] FIRST-PARTY · updated 2026-07-27T16:00:45Z; accessed 2026-09-23 · https://docs.midjourney.com/hc/en-us/articles/33329374594957-Image-Size-Resolution — Current doc cites only V8.2 sizes ("Midjourney version 8.2 creates HD images that are 2048 x 2048 pixels (px) and SD images that are 1024 x 1024px"); V7 size no longer stated
[45] FIRST-PARTY · accessed 2026-09-23 · https://updates.midjourney.com/sitemap-posts.xml — 92 posts; full-text grep: only video-rating-party-1 and introducing-our-v1-video-model name a video model (V1); others say 'video model(s)' generically
[46] FIRST-PARTY · accessed 2026-09-23 (20 entries 2026-06-11..2026-09-16) · https://syndication.twitter.com/srv/timeline-profile/screen-name/midjourney — No video-model announcement from 2026-06-11 to 2026-09-16; latest is 'Midjourney Weekly Office Hours - 9/16' (X Spaces, not transcribed)
[47] FIRST-PARTY · master efd7607, fetched via gh api 2026-09-23 · https://github.com/Wenjix/living-portraits/blob/master/pipeline/autogen.py — IMAGINE_VERSION = "7" at :82; VIDEO_MODE = "relax" at :89; submit_video calls at :337, :351, :360 (loop=True idle), :449, :457 with no version argument
[48] FIRST-PARTY · local branch free-fixes-route-arrived-takes @7d9cc26 (2026-09-23) · pipeline/autogen.py — prompt = still_prompt + " --oref %s --ow %d --v %s" (:327); VIDEO_MODE = "relax" (:93); client.submit_video(image_url=hub_url, end_image=new_url, motion_prompt=…, loop=False, mode=VIDEO_MODE) (:341-343); reverse :355-356; idle loop=True :364-365; sibling edges :484, :492; all frames via client.upload_image(...) (:324, :337, :482); VIDEO_TAKES = 4 (:414); 'from midjourney.api import MidjourneyAPIClient   # lazy: only present on hil' (:211)

## Contradictions (first-party vs first-party — unresolved)
- Current default image version: Legacy Features (https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features, updated 2026-09-01T17:19:52Z) says 'For information on the current default version (V7), please visit our Version article.' Version (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version, updated 2026-09-01T17:26:08Z) says 'The current default Midjourney version is V8.2.' Both are first-party. Not adjudicated; the MJ3 conclusions do not depend on it.
- Upload size limit: Creating on Web (https://docs.midjourney.com/hc/en-us/articles/33390732264589-Creating-on-Web, updated 2026-08-31) says 'The maximum image file size you can upload to Midjourney is 10MB.' web-updates-5 (https://updates.midjourney.com/web-updates-5/, 2026-05-27) says 'Upload error message now shows the correct 20 MB limit.' Not adjudicated. No image in the local checkout exceeds 10MB (the largest is 1,231,165 bytes), though pose stills may live on hil.
- EU Public Summary of Training Content (https://docs.midjourney.com/hc/en-us/articles/48067080311309-Public-Summary-of-Training-Content) says 'Last update: March 17, 2026' and 'Date of placement … March 17, 2026', yet lists 'Model dependencies: Midjourney V8, V8.1, and V8.2'. The Version doc (https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version) dates those later: 'V8.1 released on April 14, 2026' and 'V8.2 released as the default version on July 24, 2026'. Both are first-party. Not adjudicated, which leaves unresolved whether the video model is coupled to V8.x.
- --ow range: the Omni Reference launch post (https://updates.midjourney.com/omni-reference-oref/, 2025-05-01) says 'This parameter goes from 0 to 100 to 1000 (100 is default)'. The Omni Reference doc (https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference, updated 2026-09-01) says 'any value between 1 and 1,000, with the default being --ow 100'. Minor; irrelevant at --ow 160.
- Tangential (IMAGINE_MODE is closed): the Omni Reference doc says 'Omni Reference is currently not compatible with Fast Mode'. GPU Speed (https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo, updated 2026-08-28) lists 'Omni Reference Prompt (V7) 2 minutes' in its cost table under the Fast Mode section. fast-mode-for-v7 (https://updates.midjourney.com/fast-mode-for-v7/, 2025-05-02) says '--oref jobs are still 2x the cost of a normal --fast mode job'. Not adjudicated.

## Could not confirm
- Any officially named video model version after V1. None appears in the Video doc (current plus Wayback 2025-06-19 to 2026-09-05), in the 92 posts on updates.midjourney.com, or in @midjourney X posts from 2026-06-11 to 2026-09-16.
- Whether the video model served today is the June-2025 V1 weights or a later retrain. The EU summary's 'Model dependencies: Midjourney V8, V8.1, and V8.2' (a field the EC template defines as the models it was modified or fine-tuned from) could imply a V8-based retrain. But the same summary is internally inconsistent: 'Last update: March 17, 2026' predates V8.1 and V8.2.
- Whether a video-model change has ever shipped silently. No first-party notice exists, and there is no documented pin or detection method. In-place updates under an unchanged version string are documented only for image models (V7, V8.1, the V8.2 edit model).
- Whether --end (end frame) can be combined with Extend or Extend Manual. The docs are silent.
- Whether identity or face fidelity holds in the intermediate frames of a start/end-frame clip. Undocumented.
- Whether a frame extracted from an SD (480p-class) or HD (720p-class) MJ video is good enough to serve as a new pose still.
- Pixel size of the grid variant autogen downloads via cdn_variant_url. Only the upscaled V7 1:1 size of 2048x2048 is documented, in an archived doc.
- Any V7 or --oref retirement or end-of-life date. None is published. The interim condition ('while we finish training the improved version for V8') appears met by the 2026-08-27 Edit Model, but no date follows from that.
- Whether MJ's internal web job payload carries a video model or version field, and whether the third-party midjourney.api client's submit_video sends one. The client is not vendored and exists only on hil.
- The account's plan tier. VIDEO_MODE='relax' requires Pro or Mega.
- Whether the account holds one of the Community Guidelines' 'rare exceptions that are explicitly granted' for API or automation.
- Whether the 2026-09-16 alpha 'Animate' breakage also affected the main midjourney.com site.
- Which upload limit is current: 10MB (Creating on Web, 2026-08-31) or 20 MB (web-updates-5, 2026-05-27).
- Discord #announcements was not accessed directly. Weekly Office Hours are X Spaces audio (e.g. 2026-09-16) and were not transcribed, so any roadmap statements made there (e.g. about a video V2) are unverified.
- Wayback CDX for deleted posts on updates.midjourney.com was not checked; the independent verifier reported it timed out.
- midjourney.com/tos itself returned HTTP 403 to the verifiers. The ToS was verified only via the docs.midjourney.com ToS article.

## Dropped claims (refuted or unsupported in verification)
- c37 (secondary): 'the V2 video model is on the post-V8 roadmap, with a new compute cluster enabled in March', attributed to pixverse.ai. Two verifiers marked it unsupported or secondary_only: the text is not on the page, only in a search summary. Dropped; kept in do_not_quote.
- c2 sub-claim 'only one of 92 update posts names a video model'. Refuted by re-fetch: video-rating-party-1 (2025-06-11) also says 'V1 Video Model'. Corrected to two posts, both V1.
- c33 line numbers (:93, :341-343) cited against the GitHub master URL. On master the lines are :89 and :337, while :93 and :341-343 are the local branch. Both are now cited separately.
- c11 phrasing 'the web version setting covers images only'. Softened to what the doc says: it is described as the default version 'for generating images', and the doc is silent about any effect on video.
- c26 '10MB upload limit' as a settled fact. Moved to contradictions (10MB vs 20 MB, both first-party).
- c27 V8.0 as a strong retirement precedent. Qualified: it was an alpha-only model retired after two weeks' notice on updates.midjourney.com and X.
- Answer §2 'This matches exactly what autogen sends'. Replaced with a note that the features match but the interface does not: MJ 'does not provide an API'.
- Answer §5 'The only documented video changes in the updates feed are the table rows above'. Expanded to include the 2025-06-19 relax test and encoder and the 2025-08-13 last-frame thumbnails.
- Prior-sweep premise '--ow reportedly dropped out of the current Parameter List'. Replaced: --ow was never in any Parameter List snapshot checked, from 2025-05-03 through today.
- Independent verifier's '--oref first appears in the Parameter List from 2025-12-02'. Re-check found --oref in the 2025-09-05 snapshot.
- Researcher §4 date '2025-08-06' for HD video, given without a timezone. Now stated as 2025-08-07 UTC (Aug 6 US Pacific).

## DO NOT QUOTE (low/unknown)
- [unknown] 'The V2 video model is on the post-V8 roadmap, with a new compute cluster enabled in March' (attributed to the pixverse.ai blog) — Not present on the cited pixverse page when fetched on 2026-09-23. It exists only in a search-engine summary. No first-party source mentions a video V2.
- [low] 'Midjourney shipped its first video model in April 2026' (aimagicx.com and search summaries) — Secondary SEO claim, contradicted by first-party V1 launch sources dated 2025-06-18.
- [unknown] GenIArt_Fr recap of the 2026-03-25 Office Hours ('V8 Roadmap') — Secondary, seen only truncated, not re-verified.
- [unknown] 'The currently served video model is V1' — V1 is the last named version, but no source says which weights are served now, and the EU summary hints at V8 dependencies.
- [unknown] 'The video model was retrained on / is built on V8.x' — Rests only on the EU summary's 'Model dependencies' line, and that document's own dates are inconsistent.
- [unknown] 'A silent video-model change has shipped' OR 'the video model has never changed' — Neither is documented. There is no pin or version string for video.
- [unknown] Upload limit stated as a single number (10MB or 20 MB) — Two first-party sources conflict: Creating on Web says 10MB, web-updates-5 says 20 MB.
- [low] '--ow recently dropped out of the Parameter List' (prior sweep) — --ow is absent from every Parameter List snapshot checked, 2025-05-03 through today. It was never listed there.
- [unknown] '--end can be combined with Extend / Extend Manual' — Undocumented.
- [unknown] 'Identity is preserved in the intermediate frames of a start/end clip' — Undocumented. The docs promise nothing between the endpoints.
- [unknown] 'A frame extracted from an MJ video can serve as a new pose still' — Documented only step by step, never as a workflow. Frames are 480p/720p-class against 2048px upscaled V7 stills, and fidelity is untested.
- [unknown] Any V7 or --oref retirement date — None is published anywhere first-party.
- [unknown] 'The midjourney.api client sends / does not send a video version field' — The client is not vendored or available locally, and MJ publishes no API.
- [unknown] 'The account is on Pro/Mega' — Not verified. Relax video requires Pro or Mega per the docs.
- [unknown] 'The alpha Animate breakage (fixed 2026-09-16) affected production' — The changelog is scoped to alpha.midjourney.com only.
- [unknown] Pixel size of the cdn_variant_url grid variant — Undocumented.
- [low] EU summary dates ('Last update: March 17, 2026', 'placed March 17, 2026') used to date the video model — These dates conflict with the Version doc's V8.1 (2026-04-14) and V8.2 (2026-07-24) release dates.
- [low] 'Current default version is V7' (Legacy Features) — Contradicted by the Version doc ('The current default Midjourney version is V8.2'). Both were updated 2026-09-01. Not adjudicated.
- [unknown] Whether --oref runs in Fast Mode — First-party sources are ambiguous: the Omni doc says it is not compatible with Fast Mode, while the GPU Speed Fast-cost table and the fast-mode-for-v7 post describe --oref Fast costs. Out of scope (IMAGINE_MODE is closed).
- [low] --ow lower bound (0 vs 1) — The launch post says 0–1000 and the doc says 1–1,000. Irrelevant at --ow 160.
- [low] HD video launch date given as '2025-08-06' without a timezone — The post was published 2025-08-07T01:29:13Z, which is Aug 6 only in US Pacific. Give the date in UTC or state the timezone.
- [low] 'autogen's payload matches MJ's documented API exactly' — MJ documents only the web UI and Discord, and 'does not provide an API'. The field names belong to a third-party client. The features match; the interface does not.
- [low] 'V8.0 retirement is the precedent for how V7 will be retired' — V8.0 was an alpha-only model retired after two weeks' notice. Applying that to V7 is an inference from a single case.
- [low] '--oref first appears in the Parameter List from 2025-12-02' (independent verifier) — Re-check found --oref already present in the 2025-09-05 snapshot.


---

# Track MJ4 — Non-Midjourney stills: single identity anchor, tunable weight, or edit-from-anchor
Primary mission track: yes · Final confidence: medium

## Answer
## Direct answer
**Yes, but only one vendor documents an identity weight, and no vendor shows that any of these tools works on this character.**

- **Re-generating from the anchor with a tunable identity weight: only Kling Image 2.1 (`model_name: kling-v2-1`) documents one.**
  - It takes one `image` plus `image_reference` = `subject` ("character feature reference") or `face` ("character appearance reference") [1].
  - `human_fidelity` is a float in [0,1], default 0.45, described as "Facial reference intensity". It only takes effect with `subject` [1].
  - `image_fidelity` is a float in [0,1], default 0.5 [1].
  - Both carry the note "Only kling-v2-1 supports this parameter". The default `model_name` is `kling-v3` [1]. The capability map lists Character/Face Feature Reference as supported only on Image 2.1, not on 3.0, 3.0 Omni or O1 [2].
  - Price is $0.028 per image-to-image image [3]. Terms: "commercial purposes is not restricted", and Kling will not use your data to train [4].
  - The request body has no seed field. `face` mode needs exactly one face in the image [1].
- **Every other numeric knob controls something other than identity:**
  - Ideogram `image_weight` 1–100: resemblance to the input image [29].
  - Recraft `strength` [0,1]: similarity to the input [41].
  - Firefly style/structure `strength` 1–100 [43][44].
  - Stability `fidelity` 0–1: style only [46].
  - BFL `finetune_strength`: LoRA scale [11].
  - Leonardo Phoenix `guidances.character`: three steps only, LOW/MID/HIGH [47].
- **Several tools edit from the anchor, but none has an identity weight:** FLUX.2 [6], Gemini 3 Pro Image [19], GPT Image 2.5 [24], Seedream 5.0 [26], Qwen-Image-Edit-2511 [37], Luma uni-1 [50], xAI [52], HiDream-O1 [57]. None promises pixel-exact preservation. OpenAI says "The model uses the mask as guidance" [23].
- **Graph impact (my inference, not sourced):**
  - If edited stills *replace* nodes, each one is a newly rendered face, and every MJ edge touching it needs re-rendering.
  - If edited stills only *add* nodes, the 59 V7 stills and 500 edges stay untouched. MJ video accepts your own image URL as the start frame and `--end <url>` as the end frame [64], and autogen already uploads the hub still as both oref and start/end frame [65]. The catch: each new edge then morphs between a V7 face and a non-MJ face on the wall.
- **No first-party source shows any candidate holding a painted Old-Master face across 59 renders.**
  - The only measured drift result is BFL's 2025 FLUX.1 Kontext paper. It tracked AuraFace similarity over successive edits and found Kontext drifts more slowly than the systems it compared against, but it still drifts. The test input was a photo, not a painting [17].

## Comparison table
| Candidate | Anchor mechanism | Identity/reference weight | Output terms / training on your data | Friction | Price per still |
|---|---|---|---|---|---|
| **Kling Image 2.1** (`kling-v2-1`) | 1 image; `image_reference` subject or face [1] | **`human_fidelity` [0,1], default 0.45; `image_fidelity` [0,1], default 0.5** [1] | Commercial use not restricted; no training [4] | Only on v2-1, not the default v3 [1][2]; no seed; face mode needs one face [1] | $0.028 image-to-image [3] |
| **FLUX.2 [pro]/[max]** (BFL API) | Instruction edit, up to 8 refs via API [5] | None [6] | No ownership claim, commercial use OK [14]. BFL may train on **and publicly display** inputs/outputs [15] | `safety_tolerance` 0–5, default 2 [7]. `flux-2-pro` is a fixed snapshot that "will not change" [10] | [pro]: $0.03 first MP + $0.015 per reference MP [9] = docs "from $0.045" [8]. [max]: the two BFL pages conflict (see contradictions) |
| FLUX.2 [flex] | Same | `guidance` 1.5–10, default 5 = prompt adherence, not identity [7] | Same | — | Two BFL pages conflict (see contradictions) |
| FLUX.2 [klein] 4B / Base 4B | Up to 4 refs [10]; LoRA via `-finetuned` endpoints [11] | `finetune_strength`, default 1.0, no range given; docs suggest sweeping 0.7→0.9; **public beta** [11] | Weights Apache 2.0 [13] | LoRAs are trained against a Base model [11]; the dataset would be the MJ stills (see flags) | from $0.014 [8], plus $0.001 per reference MP [9] |
| FLUX.2 [klein] 9B, **hosted** | Up to 4 refs; fixed snapshot `flux-2-klein-9b` [10] | None | API outputs under Developer Terms [14] (only the weights are non-commercial) | — | from $0.015 [8] |
| Gemini 3 Pro Image / 3.1 Flash Image | Up to 5 / up to 4 character images; 3 Pro also takes up to 3 style refs [19] | None. Config is format, aspect ratio, size, plus `thinking_level` on 3.1 Flash [19] | Google won't claim ownership [22]. Paid tier: "Used to improve our products: No" [20] | SynthID watermark on every image; you must hold rights to uploads [19] | $0.134 per 1K/2K (batch $0.067) / $0.067 per 1K [20] |
| GPT Image 2.5 Sunburst/Flare | Up to 16 input images [24] | `input_fidelity` high/low exists in the API reference [24], but the guide scopes it to earlier models [23]. Effect on 2.5 unconfirmed | Customer owns Output; no training unless explicitly opted in [25] | Mask is only guidance; OpenAI admits recurring-character inconsistency; org verification may be required [23] | Token-priced, $30 per 1M output tokens [23] |
| Seedream 5.0 pro/flash (BytePlus) | Up to 10 refs [26] | None; no seed field [26] | No training unless you opt in [28]; output-ownership clause not found | `watermark` defaults to true [26] | pro $0.045 (≤2.61MP) / $0.09 above; reference images: 1st free, then $0.003 each; flash $0.018 [27] |
| Ideogram 3.0 | 1 character reference plus optional mask [29] | Remix `image_weight` 1–100, default 50 = resemblance to input [29] | Commercial use OK [31]; API inputs/outputs not used for training unless flagged [32] | Attribution clause §2.3.1 [32]; custom-model training from a dataset [29][30] | Not confirmed |
| Runway `gen4_image` | Up to 3 tagged refs [34] | None [34] | Commercial use not restricted; may train on your data [36] | `publicFigureThreshold`; "Powered by Runway" required in apps end users can reach [34][36] | 5 / 8 credits at $0.01 each [35] |
| Qwen-Image-Edit-2511 (open weights) | Multi-image edit [37] | None; `true_cfg_scale` 4.0 is ordinary guidance [37] | Apache 2.0 [37] | BF16; rented GPU | Compute only |
| Alibaba hosted qwen-image-2.0-pro / edit-max / edit-plus | 1–3 images, single-turn only [39] | None [39] | Not confirmed | — | $0.075 / $0.075 / $0.03 [40] |
| Recraft image-to-image | Similarity to input; the doc says it can preserve "subject identity" [41] | `strength` [0,1], 0 = almost identical [41] | Not confirmed | Endpoint default model is `recraftv4_1` [41] | $0.04 for V3 only [42]; V4.1 price not listed |
| Adobe Firefly | Style/structure references; Custom Models, including subject models [43][44][45] | Style/structure `strength` 1–100, default 50 [43][44] | Not confirmed | — | Not confirmed |
| Stability (via Bedrock) | Style only | `fidelity` 0–1, style [46] | — | No identity mechanism | — |
| Leonardo Phoenix | 1 character reference [47] | LOW/MID/HIGH [47] | Not confirmed | Leonardo also adds LOW/MID/HIGH on Nano Banana Pro references; the mechanism is undocumented [48] | Not confirmed |
| Luma uni-1 (Agents API) | `image_edit` with a source image plus up to 8 refs [50][51] | None documented [50] | Not confirmed | The legacy Photon API has `character_ref` and a `weight` with no range [49] | $0.0434 per edit [51] |
| xAI grok-imagine-image-2.0 | Instruction edit; lists oil-painting styles [52] | None [52] | Not confirmed | — | $0.04 [53] |
| HiDream-O1-Image 8B (open weights) | `ref_images`; subject-driven personalization; skeleton conditioning [56] | None; `guidance_scale` default 5.0; has `seed` [57] | MIT on HF and GitHub [56][57] | The optional prompt agent uses Gemma weights [56] | Compute only |
| LongCat-Image-Edit / -Turbo (open weights) | Instruction edit [54] | None | Apache 2.0 [54][55] | — | Compute only |
| MiniMax image-01 | 1 `subject_reference` of type `character` [61] | None found | Not confirmed | — | Not confirmed |

## Disqualified (weights or outputs non-commercial / research-only)
- **FLUX.2 [dev], FLUX.2 [klein] 9B / Base 9B weights, FLUX.1 Kontext [dev].** FLUX Non-Commercial License v2.1 says use "in direct interactions with or that has impact on end users" is not a Non-Commercial Purpose. It does allow outputs "for any purpose (including for commercial purposes)" [12][13].
- **Qwen-Image-2.1:** Qwen Research License, "FOR NON-COMMERCIAL PURPOSES ONLY" [38].
- **Ideogram 4 open weights:** license `ideogram-4-non-commercial` [33].
- **InsightFace-dependent pipelines such as InstantID:** InsightFace's models are for "non-commercial research purposes only" [59]. **InfiniteYou:** cc-by-nc-4.0 [60].
- **HunyuanImage-3.0:** not non-commercial, but excluded from the EU, UK and South Korea, and bars displaying outputs outside that territory [58]. Poor fit.

## Shortlist
1. **Kling Image 2.1, subject reference plus `human_fidelity`. For re-generating from the anchor.**
   - It is the only documented continuous, identity-specific weight on a single anchor, which is the closest analogue to `--ow` [1][2].
   - Cheap at $0.028 [3]. Clean terms: commercial use unrestricted and no training [4].
   - Risks: it only works on the older v2-1 model while the default is v3 [1]; there is no seed, which hurts reproducibility behind a one-way door [1]; nothing shows it on painted faces.
2. **FLUX.2 [pro], pinned to `flux-2-pro`. For editing from the anchor.**
   - The fixed snapshot "will not change" [10]. Up to 8 references [5]. About $0.045 per 1MP edit from a 1MP anchor [9]. Commercial outputs [14].
   - Its lineage has the only measured drift result, but that result is for FLUX.1 Kontext, not FLUX.2 [17].
   - Risks: no weight parameter [6]; BFL may train on and publicly display your anchor [15].
3. **Open weights for a frozen, reproducible offline render:**
   - **Qwen-Image-Edit-2511** (Apache 2.0) [37], or
   - **FLUX.2 [klein] Base 4B** (Apache 2.0) [13] plus a character LoRA with `finetune_strength` [11]. This is a weight on the LoRA, not on the anchor. The hosted LoRA endpoints are public beta [11], so run the LoRA locally.

- Runner-up with an explicit character mechanism: **Gemini 3 Pro Image**, which takes up to 5 character references and 3 style references [19] and does not use paid-tier data to improve products [20].
- Runner-up with a single-call weight: **Ideogram 3.0**, which combines 1 character reference and `image_weight` in one call, with no training on API data [29][32].

## Drift and derivation
- **Measured:** the Kontext paper reports AuraFace similarity over edit sequences, and says "Excessive multi-turn editing can introduce visual artifacts" [17].
- **Vendor claims only, no measurements:**
  - FLUX: consistent "even after multiple sequential edits" [16].
  - LongCat: identity consistency in multi-turn editing [54].
  - Qwen-Image-Edit-2511: "mitigate image drift", which the README never defines [37].
  - OpenAI admits recurring-character consistency can slip [23].
- **Google's guidance conflicts with a one-hop design.** It says: "include previously generated images in subsequent prompts to maintain consistency. For complex poses, include a reference image of the selected pose" [19]. That is chaining.
- **Neither approach is established.** Deriving every node in one hop from the anchor is inference. autogen's `hub` defaults to `anchor` but can be any node [65], so a re-render would need to force hub = anchor.
- **Pilot:** re-render a few nodes and score them with AuraFace-v1 (Apache-2.0, "usage in commercial setting") [62]. Test both one-hop and chained derivation.

## Legal and process flags (first-party text; I am not ruling on them)
- **MJ ToS [63]:**
  - "You own all Assets", but a company with more than $1M revenue needs a Pro or Mega plan.
  - "You may not reverse engineer the Services or the Assets." This bears on training a LoRA on the V7 stills.
  - "You may not use automated tools to access, interact with, or generate Assets through the Services." This bears on any unattended client.
- **Uploading the anchor:** Gemini requires "the necessary rights to any images you upload" [19]; BFL gets a licence to publicly display inputs [15].
- **Attribution:** Ideogram §2.3.1 [32] and Runway [36] tie attribution to apps that expose the model to end users. Whether that covers a one-time offline render is unclear.
- **Repo reference:** the autogen lines are at L238/L317 on master and L242/L321 on branch `free-fixes-route-arrived-takes` [65].

## DO NOT QUOTE
See the `do_not_quote` field: suitability for painted faces, anything inferred, unconfirmed prices and terms, and every contradicted figure.

## Sources
[1] FIRST-PARTY · accessed 2026-09-23 · https://kling.ai/document-api/api/image/2-1/image-generation.md — Kling kling-v2-1: image_reference subject|face; 'human_fidelity | float | No | 0.45 | Facial reference intensity...'; 'Value range: [0, 1]'; 'Only kling-v2-1 supports this parameter'; image_fidelity default 0.5; model_name default kling-v3; no seed field; face mode 'must contain only one face'
[2] FIRST-PARTY · Updated At 2026-05-19 · https://kling.ai/document-api/guides/capability-map/image.md — 'Character Feature Reference | - | Not Supported | Not Supported | Not Supported | Supported' (only Kling Image 2.1); same for Face Feature Reference
[3] FIRST-PARTY · accessed 2026-09-23 · https://kling.ai/document-api/pricing/base/image.md — 'Kling Image 2.1 | Image-to-Image | 1K、2K | 8 Units ($0.028) / image'
[4] FIRST-PARTY · Release/Effective Date 2026-04-21 · https://kling.ai/document-api/guides/protocols/paid-service.md — '5.1 We will not use ... your data to train'; '6.3 ... intellectual property rights of the AI-generated content still belong to you'; '6.4 You use of the AI-generated content for commercial purposes is not restricted.'
[5] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/flux_2/flux2_image_editing.md — 'Reference multiple images simultaneously - up to 8 via API, up to 10 in the playground.'
[6] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/api-reference/models/generate-or-edit-an-image-with-flux2-[pro].md — FLUX.2 [pro]/[max] request fields: prompt, input_image..input_image_8, seed, width, height, safety_tolerance, output_format, webhooks; no strength or weight field (the [max] page matches)
[7] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/api-reference/models/generate-or-edit-an-image-with-flux2-[flex].md — guidance 'maximum: 10 minimum: 1.5 ... improve prompt adherence ... default: 5'; safety_tolerance 0-5, default 2
[8] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/quick_start/pricing.md — 'FLUX.2 [pro] | from $0.03 | from $0.045'; '[max] | from $0.07 | from $0.07'; '[flex] | from $0.05'; '[klein] 4B from $0.014'; '[klein] 9B from $0.015'; '[dev] | Local only ... non-commercial'; Kontext [pro] $0.04 / [max] $0.08
[9] FIRST-PARTY · accessed 2026-09-23 (embedded pricing data) · https://bfl.ai/pricing — [max]: 'The first generated megapixel is charged $0.07 ... Reference image(s): We charge $0.03 for each megapixel'; [pro]: $0.03 first MP, $0.015 per reference MP; klein 4B $0.014 + $0.001 per reference MP; [flex]: 'We charge $0.05 for each megapixel on both the reference images and the generated image.'
[10] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/flux_2/flux2_overview.md — 'flux-2-pro | A fixed snapshot ... This endpoint will not change'; 'flux-2-klein-9b | A fixed snapshot'; [klein] up to 4 refs; '[klein] 4B is fully open under Apache 2.0. [klein] 9B ... FLUX Non-Commercial License'; [flex] '$0.06 / MP'; 'Base models ... are not offered on the public API.'
[11] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/flux_2/flux2_lora_inference.md — 'Public Beta — ... Pricing, parameters, and endpoint names may change'; finetune_strength 'Defaults to 1.0'; 'sweep 0.7 → 0.9'; 'One LoRA per request'; lists /v1/flux-2-klein-base-4b-finetuned and -base-9b-finetuned; LoRAs trained 'against a FLUX.2 [klein] Base model'
[12] FIRST-PARTY · committed 2026-01-15 ('FLUX.2 [klein]') · https://raw.githubusercontent.com/black-forest-labs/flux2/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL — 'FLUX Non-Commercial License v2.1'; covers 'FLUX.x [dev]'; use with 'impact on end users' is not a Non-Commercial Purpose; 'You may use Output for any purpose (including for commercial purposes)'
[13] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-base-4B — HF license metadata: FLUX.2-klein-base-4B and klein-4B apache-2.0; FLUX.2-klein-9B and FLUX.2-dev flux-non-commercial-license
[14] FIRST-PARTY · Last Revised August 4, 2026 · https://bfl.ai/legal/developer-terms-of-service — 'we claim no ownership rights in and to your Output ... You and your End Users may use Outputs for ... commercial purposes'
[15] FIRST-PARTY · Last Revised August 4, 2026 · https://bfl.ai/legal/flux-api-service-terms — license to 'publicly display Developer's Input and Output'; 'the Company may use Inputs and Outputs to train and improve its artificial intelligence models'
[16] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/guides/usecases_editing_character_consistency.md — Vendor claim, no metric: 'FLUX excels at maintaining character consistency even after multiple sequential edits.'
[17] FIRST-PARTY · v2 2025-06-24 · https://arxiv.org/html/2506.15742v2 — BFL's FLUX.1 Kontext paper: AuraFace cosine similarity over edit sequences; 'slower drift of FLUX.1 Kontext relative to competing methods'; 'Excessive multi-turn editing can introduce visual artifacts'
[18] FIRST-PARTY · entries through 2026-09-10 · https://docs.bfl.ml/release-notes.md — FLUX 3 phased rollout (July 23, 2026), with image synthesis/editing after video; LoRA inference public beta (April 23, 2026)
[19] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/image-generation — Up to 5 (3 Pro) / 4 (3.1 Flash) character images; 3 Pro 'Up to 3 images to be used as style references'; response_format options plus thinking_level; SynthID on all images; 'necessary rights'; Flash Lite 'Not optimized for ... multi-turn'; 'include previously generated images in subsequent prompts ... For complex poses, include a reference image of the selected pose.'
[20] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/pricing — gemini-3-pro-image '$0.134 per 1K/2K image' (batch $0.067); 3.1 Flash Image '$0.067 per 1K image'; paid tier 'Used to improve our products | No'; gemini-2.5-flash-image 'will be shut down on October 2, 2026'; Flex and Priority sections under Gemini 3 Pro Image
[21] FIRST-PARTY · Last updated 2026-09-03 UTC · https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image — 'Stable: gemini-3-pro-image'; 'Latest update November 2025'; 'Flex inference Not supported', 'Priority inference Not supported'
[22] FIRST-PARTY · Effective March 23, 2026; last updated 2026-04-28 · https://ai.google.dev/gemini-api/terms — 'Google won't claim ownership over that content.'
[23] FIRST-PARTY · accessed 2026-09-23 · https://developers.openai.com/api/docs/guides/image-generation.md — gpt-image-2.5-sunburst / -flare; input_fidelity section is under 'The details below apply to earlier models, not Sunburst or Flare'; masks are guidance; recurring-character consistency limitation; org verification; $30 per million image output tokens
[24] FIRST-PARTY · accessed 2026-09-23 · https://developers.openai.com/api/reference/resources/images/methods/edit — 'you can provide up to 16 images'; input_fidelity 'high' or 'low'; snapshots gpt-image-2.5-sunburst-2026-09-08 / flare-2026-09-08
[25] FIRST-PARTY · Updated Dec 1, 2025; Effective Jan 1, 2026 (Wayback 2026-09-19; live page returns 403) · https://web.archive.org/web/20260919113526/https://openai.com/policies/services-agreement/ — 'Customer ... owns all Output'; 'OpenAI will not use Customer Content to develop or improve the Services, unless Customer explicitly...'
[26] FIRST-PARTY · UpdatedTime 2026-09-22T04:14:47Z · https://docs.byteplus.com/en/docs/ModelArk/1541523 — 'Seedream 5.0 pro and Seedream 5.0 flash support up to 10 reference images'; watermark 'Default: true'; no strength, guidance or seed field
[27] FIRST-PARTY · UpdatedTime 2026-09-22T09:59:28Z · https://docs.byteplus.com/en/docs/ModelArk/1099320 — dola-seedream-5-0-pro-260628: input image 'First image: Free / From the 2nd image: 0.003'; output 0.045 (≤2.61MP) / 0.09; 'dola-seedream-5-0-flash-260915 |Free |0.018'
[28] FIRST-PARTY · accessed 2026-09-23 · https://docs.byteplus.com/en/docs/legal/docs-service-specific-terms — 'Unless you separately opt in, BytePlus will not use your data to train models.'
[29] FIRST-PARTY · accessed 2026-09-23 · https://developer.ideogram.ai/openapi.json — v3 'currently only supports 1 character reference image'; character_reference_images_mask; v3 remix image_weight min 1 / max 100 / default 50 with character_reference_images in the same body; v4 remix image_weight semantics; custom v3 training 'at least 15 images and a maximum of 100'
[30] FIRST-PARTY · accessed 2026-09-23 · https://developer.ideogram.ai/tutorials/custom-model-training.md — 'A dataset needs at least 10 images to start training.' 'up to 100 images'
[31] FIRST-PARTY · Last revised August 14, 2024 · https://ideogram.ai/legal/tos/ — 'we do not restrict your ability to use User Output ... (including for commercial purposes)'
[32] FIRST-PARTY · Last revised August 14, 2024 · https://ideogram.ai/legal/api-tos — §2.3.1 attribution tied to 'User Output generated by users of the Developer Applications'; 'shall not use any User Input or User Output to train the Ideogram AI Model, except if ... flagged'
[33] FIRST-PARTY · created 2026-05-30 · https://huggingface.co/api/models/ideogram-ai/ideogram-4-fp8 — license_name 'ideogram-4-non-commercial'
[34] FIRST-PARTY · accessed 2026-09-23 · https://docs.dev.runwayml.com/api.md — gen4_image 'referenceImages ... max 3 items'; 'publicFigureThreshold ... auto, low'; no weight field
[35] FIRST-PARTY · accessed 2026-09-23 · https://docs.dev.runwayml.com/guides/pricing.md — 'gen4_image | 5 credits per 720p image, or 8 credits per 1080p image'; '$0.01 per credit'; resale of gpt_image_2_5_* at '1–76 credits per image ... plus 1 credit per reference image'
[36] FIRST-PARTY · Last updated September 15, 2026 · https://runwayml.com/terms-of-use — No ownership claim; commercial use not restricted; Inputs/Outputs may be used to train; apps 'made available to end users must prominently display "Powered by Runway"'
[37] FIRST-PARTY · HF lastModified 2025-12-23 · https://huggingface.co/Qwen/Qwen-Image-Edit-2511 — 'mitigate image drift, improved character consistency'; 'Qwen-Image is licensed under Apache 2.0.'; true_cfg_scale 4.0; BF16; still the newest Qwen-Image-Edit repo in the Qwen HF org listing
[38] FIRST-PARTY · created 2026-09-14; license Release Date September 20, 2026 · https://huggingface.co/Qwen/Qwen-Image-2.1 — Qwen RESEARCH LICENSE: 'FOR NON-COMMERCIAL PURPOSES ONLY'
[39] FIRST-PARTY · Last Updated Sep 22, 2026 · https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-api — 'Only single-turn conversations are currently supported'; 'one to three images'; no weight parameter
[40] FIRST-PARTY · Last Updated Sep 24, 2026 (as shown) · https://www.alibabacloud.com/help/en/model-studio/model-pricing — qwen-image-2.0-pro $0.075/image; qwen-image-edit-max $0.075; qwen-image-edit-plus $0.03 (International)
[41] FIRST-PARTY · accessed 2026-09-23 · https://www.recraft.ai/docs/api-reference/endpoints.md — image-to-image 'preserving certain aspects like composition, color, or subject identity'; strength '[0, 1], where 0 means almost identical'; default model recraftv4_1
[42] FIRST-PARTY · accessed 2026-09-23 · https://www.recraft.ai/docs/api-reference/pricing.md — 'Raster image to image – Recraft V3 | $0.04'
[43] FIRST-PARTY · accessed 2026-09-23 · https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/ — style 'strength value between 1 and 100 ... defaults to a value of 50'
[44] FIRST-PARTY · accessed 2026-09-23 (verifier-confirmed) · https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/structure-image-reference/ — structure strength 1-100, default 50
[45] FIRST-PARTY · accessed 2026-09-23 · https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/custom-models/ — 'Subject Models: These focus on representing specific characters, products, or objects.'
[46] FIRST-PARTY · accessed 2026-09-23 · https://docs.aws.amazon.com/bedrock/latest/userguide/stable-image-services.html — Stability Style Guide 'fidelity ... How closely the output image's style resembles the input image's style. Range 0 to 1.'
[47] FIRST-PARTY · updatedAt 2026-07-10 · https://docs.leonardo.ai/docs/phoenix.md — guidances.character '(limited to 1)', strength LOW/MID/HIGH, default MID
[48] FIRST-PARTY · updatedAt 2026-01-22 · https://docs.leonardo.ai/docs/nano-banana-pro.md — Leonardo's own reseller layer: guidances.image_reference up to 6 refs with strength LOW/MID/HIGH (first-party for Leonardo's API only)
[49] FIRST-PARTY · updatedAt 2026-07-10 · https://docs.lumalabs.ai/docs/image-generation.md — Legacy Photon: 'up to 4 images of the same person to build one identity'; 'weight' key with no range; points to the Luma Agents API
[50] FIRST-PARTY · accessed 2026-09-23 · https://docs.agents.lumalabs.ai/guides/images/editing/ — uni-1/uni-1-max type 'image_edit' 'applies it while preserving the parts of the image you did not mention'; no weight or strength parameter
[51] FIRST-PARTY · accessed 2026-09-23 · https://docs.agents.lumalabs.ai/guides/pricing/ — uni-1 'Image edit (image to image) $0.0434'; 'image_edit requests support up to 8 reference images (the source occupies one slot)'
[52] FIRST-PARTY · accessed 2026-09-23 · https://docs.x.ai/developers/model-capabilities/images/editing.md — grok-imagine-image-2.0 editing including 'oil paintings'; no weight parameter
[53] FIRST-PARTY · accessed 2026-09-23 · https://docs.x.ai/developers/pricing.md — 'grok-imagine-image-2.0 | $0.04 / image'
[54] FIRST-PARTY · created 2025-12-05 · https://huggingface.co/meituan-longcat/LongCat-Image-Edit — apache-2.0; vendor claim that subject identity remains invariant 'in multi-turn editing'
[55] FIRST-PARTY · created 2026-02-03 · https://huggingface.co/api/models/meituan-longcat/LongCat-Image-Edit-Turbo — license apache-2.0, image-to-image
[56] FIRST-PARTY · created 2026-05-08; lastModified 2026-06-22 · https://huggingface.co/HiDream-ai/HiDream-O1-Image — license: mit; '8B'; 'text-to-image, image editing, and subject-driven personalization'; 'the IP pipeline now supports layout and skeleton conditioning'; prompt agent uses google/gemma-4-31B-it
[57] FIRST-PARTY · created 2026-05-08; pushed 2026-06-22 · https://github.com/HiDream-ai/HiDream-O1-Image — GitHub license MIT; inference.py args --ref_images, --seed (default 32), --guidance_scale (default 5.0); no identity-weight argument
[58] FIRST-PARTY · License Release Date September 28, 2025 · https://huggingface.co/tencent/HunyuanImage-3.0-Instruct/raw/main/LICENSE — 'DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA'; must not 'display ... Output ... outside the Territory'
[59] FIRST-PARTY · accessed 2026-09-23 · https://github.com/deepinsight/insightface/blob/master/README.md — 'models trained with these data ... are available for non-commercial research purposes only'
[60] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/api/models/ByteDance/InfiniteYou — license cc-by-nc-4.0
[61] FIRST-PARTY · accessed 2026-09-23 · https://platform.minimax.io/docs/api-reference/image-generation-i2i.md — subject_reference 'Currently only supports character (portrait)'; no weight field found
[62] FIRST-PARTY · lastModified 2024-08-26 · https://huggingface.co/fal/AuraFace-v1 — license apache-2.0; 'trained on commercially and publicly available data sources to enable its usage in commercial setting'
[63] FIRST-PARTY · Version Effective Date May 27, 2026; article updated 2026-08-17 · https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — 'You own all Assets'; companies over $1M revenue need Pro or Mega; 'You may not reverse engineer the Services or the Assets. You may not use automated tools to access, interact with, or generate Assets through the Services.' No clause on training
[64] FIRST-PARTY · updated 2026-08-31 · https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — 'To generate a video using your own image, paste your image URL ... add the --video parameter'; 'To use a different image as your ending frame, add the --end parameter ... and paste your image URL'
[65] FIRST-PARTY · master, accessed 2026-09-23 · https://github.com/Wenjix/living-portraits/blob/master/pipeline/autogen.py#L238 — master L238 'hub = p.get("hub", "anchor")'; L317 '# hub still upload -- serves as the imagine identity oref AND the transition start/end frame'; L323 '--oref %s --ow %d --v %s'. On branch free-fixes-route-arrived-takes the same lines are L242/L321/L327

## Contradictions (first-party vs first-party — unresolved)
- BFL FLUX.2 [flex] price. https://docs.bfl.ml/flux_2/flux2_overview.md: '[flex] ... $0.06 / MP'. https://docs.bfl.ml/quick_start/pricing.md: 'FLUX.2 [flex] | from $0.05 | from $0.05'. https://bfl.ai/pricing: 'We charge $0.05 for each megapixel on both the reference images and the generated image.' Unresolved; no side picked.
- BFL FLUX.2 [max] edit price. https://docs.bfl.ml/quick_start/pricing.md gives the [max] edit column as 'from $0.07'. https://bfl.ai/pricing gives [max] 'The first generated megapixel is charged $0.07 ... Reference image(s): We charge $0.03 for each megapixel', so a 1MP edit from a 1MP anchor would be $0.10. For [pro] the two pages agree ($0.03 + $0.015 = $0.045). Unresolved.
- BFL klein Base models on the public API. https://docs.bfl.ml/flux_2/flux2_overview.md: 'Base models are available as open weights for local development and research. They are not offered on the public API.' https://docs.bfl.ml/flux_2/flux2_lora_inference.md lists '/v1/flux-2-klein-base-4b-finetuned | FLUX.2 [klein] Base 4B | FP8' and '/v1/flux-2-klein-base-9b-finetuned'. Unresolved.
- Ideogram custom-model training minimum. https://developer.ideogram.ai/tutorials/custom-model-training.md: 'A dataset needs at least 10 images to start training.' https://developer.ideogram.ai/openapi.json: 'The dataset must contain at least 15 images and a maximum of 100 images.' Unresolved.
- Google gemini-3-pro-image consumption options. https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image: 'Flex inference Not supported / Priority inference Not supported'. https://ai.google.dev/gemini-api/docs/pricing has '### Flex' and '### Priority' price tables under Gemini 3 Pro Image. Not load-bearing; unresolved.

## Could not confirm
- Any first-party evidence that Kling Image 2.1 human_fidelity (or any other candidate) preserves a painted or Old-Master face and its brushwork across pose changes.
- Kling Image 2.1 release date and any deprecation or retirement schedule for kling-v2-1 (the default is now kling-v3, which lacks the parameter).
- Whether input_fidelity is accepted or has any effect on gpt-image-2.5-sunburst / -flare.
- A flat per-image price for GPT Image 2.5 at OpenAI (only token rates are published; Runway's resale credits are Runway's own price).
- Ideogram API per-image prices (character reference, remix v3/v4).
- Leonardo per-image prices and output-ownership terms; the mechanism behind Leonardo's LOW/MID/HIGH strength on resold models.
- Adobe Firefly Services price and output terms.
- BytePlus/Seedream output-ownership clause.
- Alibaba Model Studio output-ownership clause for the Qwen image APIs.
- Recraft API output-ownership clause; Recraft V4.1 image-to-image price.
- Luma Agents (uni-1) output terms; the legacy Photon weight range.
- xAI image output terms.
- MiniMax image-01 price and terms.
- Any first-party quantitative identity-drift measurement for FLUX.2, Gemini 3 Pro/3.1 Flash Image, GPT Image 2.5, Seedream 5.0, Qwen-Image-Edit-2511, LongCat, HiDream-O1 or Kling (only the 2025 FLUX.1 Kontext paper measures drift).
- Whether MJ ToS 'may not reverse engineer ... the Assets' reaches training a LoRA on the 59 V7 stills.
- How the MJ ToS 'automated tools' clause applies to an unattended third-party client (reported, not adjudicated).
- Whether Ideogram §2.3.1 or Runway's 'Powered by Runway' attribution duty applies to a one-time offline render shown on a wall.
- BFL commercial-license prices for the FLUX.2 [dev] / klein 9B weights.
- FLUX 3 image synthesis/editing availability date.
- AuraFace reliability as an identity metric on painted, non-photographic faces.
- Whether any hosted editor guarantees pixel-identical preservation of unedited regions.
- USO/UNO licence chain (a verifier said they are built on FLUX.1-dev; not re-checked this session).
- Kling content-policy behaviour on painted portraits (only the one-face rule for face mode is documented).

## Dropped claims (refuted or unsupported in verification)
- Researcher headline: 'None of the vendors I checked documents an identity-specific, continuous weight on a single anchor.' Refuted: Kling Image 2.1 documents human_fidelity [0,1] 'Facial reference intensity' and image_fidelity [0,1] on a single reference image (re-fetched 2026-09-23).
- Researcher: 'The only knob aimed at character identity is Leonardo Phoenix guidances.character (LOW/MID/HIGH).' Refuted by Kling Image 2.1.
- Researcher table: Leonardo Phoenix is an 'Older model'. No source.
- Researcher c3: Gemini documents 'only' output format, aspect ratio and size. The same page also documents thinking_level (minimal/high) for 3.1 Flash / Flash Lite Image. Corrected.
- Researcher c17: 'FLUX [dev] Non-Commercial License v2.0' governs FLUX.2 [dev]. The current governing text is FLUX Non-Commercial License v2.1 (committed 2026-01-15), with the same substance. Corrected.
- Researcher: FLUX.2 [klein] 9B filed only as disqualified weights. The hosted flux-2-klein-9b fixed-snapshot endpoint falls under BFL Developer Terms (commercial outputs); only the local weights are non-commercial. Corrected.
- Researcher: FLUX.2 [max] edit costs 'from $0.07'. bfl.ai/pricing adds $0.03 per reference MP. Moved to contradictions.
- Researcher: Ideogram 'Requires a Powered by Ideogram tagline on the app' as a blanket duty. The clause attaches to User Output generated by users of a Developer Application; whether it covers an offline render is unclear. Narrowed.
- Researcher: Recraft 'image-to-image similarity, no character reference'. Recraft documents that image-to-image can preserve 'subject identity' (still no separate character input). Corrected.
- Researcher: Recraft $0.04 as the image-to-image price. That is the V3 price only; the endpoint default is recraftv4_1, with no listed price. Narrowed.
- Researcher drift section: Qwen-Image-Edit-2511 'mitigate image drift' used as multi-turn drift evidence. The README never defines the term. Kept only as an undefined vendor claim.
- Researcher drift section: other systems 'lose identity with each edit' presented as a Kontext finding. That sentence is the paper's framing; the measurement shows Kontext drifting more slowly, not that it does not drift. Reworded.
- Researcher: 'derive every node in a single hop ... never chain edits' presented as guidance. It is inference, and Google's first-party doc recommends the opposite for character consistency. Kept only as an untested pilot arm.
- Researcher could-not-confirm items now confirmed and removed from that list: Seedream 5.0 flash price ($0.018), xAI grok-imagine-image-2.0 price ($0.04/image), AuraFace licence (Apache-2.0), Luma's newer API (uni-1 image_edit, $0.0434).
- Researcher c34 source_date 'UpdatedTime 2026-09-23'. The document's own UpdatedTime is 2026-09-22T04:14:47Z; 2026-09-23 belongs to navigation nodes. Corrected.
- Verifier (fidelity) claim that the c61 anchor #L238 is wrong. On master it is L238/L317; L242/L321 is the current branch free-fixes-route-arrived-takes. Both are cited.

## DO NOT QUOTE (low/unknown)
- [unknown] That Kling Image 2.1 human_fidelity will hold the painted Old-Master face or its brushwork across 59 poses — No first-party evidence on painted faces; the parameter's existence is documented, its fitness for this character is not
- [unknown] Kling Image 2.1 release date or remaining service lifetime — Not seen in a first-party source this session; the default model is now kling-v3
- [low] Reproducibility of Kling or Seedream renders — Neither request body exposes a seed; exact re-render behaviour is undocumented
- [low] 'Edit-from-anchor avoids re-rendering the graph' — Inference: true only if edited stills are added as new nodes; replacing nodes forces edge re-renders
- [low] The hybrid (non-MJ stills as new nodes, MJ video renders the edges) looking seamless — MJ docs confirm external start/end frames, but the V7-to-non-MJ face morph along each edge is untested
- [low] 'Derive every node in one hop from the anchor' as best practice — Inference; Google's first-party doc recommends chaining previous generations instead; neither is measured
- [low] FLUX.2 'maintains character consistency even after multiple sequential edits' — Vendor claim with no metric; the only measurement is for FLUX.1 Kontext (2025, photo input)
- [low] Qwen-Image-Edit-2511 'mitigate image drift' as evidence about repeated edits — The README never defines 'image drift'
- [low] LongCat-Image-Edit multi-turn identity consistency — Vendor claim, no metric
- [low] HiDream-O1-Image 'preserve identity / IP across new scenes' — Vendor README caption, no metric; the optional prompt agent uses Gemma weights under a separate licence
- [low] Kontext drift result applied to FLUX.2 — The measured model is FLUX.1 Kontext; no FLUX.2 drift metric exists
- [unknown] Kontext drift result applied to painted faces — The paper's input was a photo
- [unknown] input_fidelity working on gpt-image-2.5-sunburst / -flare — The API reference lists it generically; the guide scopes input-fidelity notes to earlier models
- [unknown] A per-image OpenAI price for GPT Image 2.5 — Only token rates are published; Runway's resale credits are not OpenAI's price
- [unknown] FLUX.2 [flex] price ($0.05 vs $0.06/MP) — First-party BFL pages contradict each other
- [unknown] FLUX.2 [max] single-anchor edit price ($0.07 vs about $0.10) — docs pricing.md and bfl.ai/pricing disagree
- [unknown] Whether klein Base 4B/9B LoRA endpoints are on the public API — The BFL overview and LoRA pages contradict each other
- [low] BFL finetune_strength range, and the stability of the -finetuned endpoint names and prices — No range documented; public beta, and 'may change before general availability'
- [unknown] Ideogram custom-training minimum (10 vs 15 images) — Ideogram's tutorial and OpenAPI contradict each other
- [unknown] Ideogram API per-image prices — The pricing tab is JS-rendered; not seen
- [unknown] Ideogram §2.3.1 / Runway 'Powered by Runway' applying to this offline render — The clauses are tied to end-user-facing apps; applicability is not stated
- [low] Ideogram image_weight as an identity control — Documented as resemblance to the input image, not identity
- [low] Recraft strength as an identity control; Recraft V4.1 image-to-image price — strength is a general similarity knob; only the V3 price is published
- [unknown] Leonardo LOW/MID/HIGH strength on resold Nano Banana Pro / FLUX.2 / Seedream — The upstream APIs have no such parameter; Leonardo does not document the mechanism
- [unknown] Leonardo price and output terms — Not retrieved
- [unknown] Adobe Firefly price and output terms — Not retrieved
- [unknown] Seedream / BytePlus output ownership — The clause was not found in the BytePlus legal pages fetched
- [unknown] Alibaba Model Studio output ownership — Not retrieved
- [unknown] Luma uni-1 output terms; Photon weight range — Not retrieved or not documented
- [unknown] xAI and MiniMax output terms; MiniMax price — Not retrieved
- [unknown] Training a LoRA on the 59 MJ V7 stills being permitted — MJ ToS bars reverse engineering 'the Assets' and says nothing about training; unresolved
- [unknown] How the ToS 'automated tools' clause applies to an unattended third-party client — MJ ToS says 'You may not use automated tools to access ... the Services'; reported, not adjudicated
- [unknown] AuraFace as a valid identity metric on painted faces — Licence confirmed (Apache-2.0); accuracy on paintings unverified
- [unknown] Gemini 3 Pro Image style references preserving Old-Master brushwork — The capability exists; there is no evidence on this style
- [unknown] BFL commercial-licence price for the FLUX.2 [dev] / klein 9B weights — Not published in static pages
- [unknown] FLUX 3 image editing availability date — Release notes say 'phased', with no date
- [unknown] USO / UNO licence status — A verifier asserted they are FLUX.1-dev based; not re-checked this session
- [unknown] Runway muse_image provenance — Not researched
- [unknown] Pixel-exact preservation of unedited regions by any hosted editor — OpenAI explicitly disclaims it; the others are silent
- [low] Hosted FLUX.2 klein 9B outputs being commercially usable — Inferred from BFL Developer Terms covering API Outputs generally; no klein-9B-specific statement


---

# Track MJ5 — Non-Midjourney image-to-video with explicit start AND end frames
Primary mission track: yes · Final confidence: medium

## Answer
## MJ5 (final): non-Midjourney video with a pinned start frame and end frame, checked 2026-09-23

### Direct answer
- **Hosted APIs with a documented end-frame input:**
  - Google Veo 3.1: `lastFrame` [5]
  - Kling 3.0 / 3.0 Omni / O1: `contents[].type: last_frame` [13][14], plus the legacy `image_tail` [17]
  - Luma Ray 3.2: `video.end_frame`, or `keyframes` with indexes 0 and 120 [19]
  - MiniMax H3 and H3-Max: `role: last_frame` [24]
  - Vidu Q2/Q3: `images` = [start, end] [33]
  - Alibaba wan2.2-kf2v-flash: `last_frame_url` [41]; Wan 3.0: `last_frame` [36]
  - LTX-2.5: `last_frame_uri` [53]
  - BFL FLUX 3: two `keyframes`, which BFL marks "experimental" [58]
  - xAI grok-imagine-video-1.5: `last_frame` [61]
  - PixVerse: `first_frame_img` + `last_frame_img` [64]
  - Gemini Omni Flash: two images in the prompt [11]
  - Adobe Firefly v3: keyframe `position` 0 or 1 [68]
  - Runway resells several of these with `position: last` [50]. Runway's own Gen-4.5 takes a first frame only [50].
- **Disqualified or blocked:**
  - **Seedance through BytePlus is disqualified.** BytePlus says "The BytePlus Model Services are not available in the United States" [30], and its availability list has no US entry [31].
  - **MiniMax H3 open weights are disqualified.** The license excludes the US, and the exclusion covers Outputs [27].
  - **Wan 3.0 direct is blocked.** Two first-party pages disagree on whether it is still a preview (see Contradictions). If it is a preview, the Preview terms allow "solely... internal testing, research and evaluation" [38].
- **Documented loop (start == end):**
  - Luma: a `video.loop` flag. It works with `start_frame` but is "not supported with... `end_frame`" [19].
  - Gemini Omni Flash: a prompt recipe, "`<FIRST_FRAME>@Image1 <LAST_FRAME>@Image1`… creating a video that loops" [11]. A first-party tension on Omni's end-frame support is reported below.
  - Seedance: "first-frame and last-frame images can be identical" [29], but Seedance is disqualified above.
  - Every other vendor: start == end is not documented; it must be piloted.
- **Open weights that pin the first and last frame and allow commercial use:**
  - Wan2.1-FLF2V-14B-720P, Apache-2.0 [42]
  - Wan2.1-VACE-14B, Apache-2.0, `mode='firstlastframe'` [46][47]
  - Tencent OmniWeaving, built on HunyuanVideo-1.5, `interpolation` task. Its license Territory excludes only the EU, UK and South Korea, and "Tencent claims no rights in Outputs" [48][49].
  - LTX-2.5 open weights, FLF template. Paid license needed at ≥$10M revenue [56][57].
  - There are no Wan 3 weights. The official Wan2.2 repo has no FLF config [45].
- **Fit constraint from the repo:** the character framing spec says `"aspect": "1:1"` [4], and output is center-cropped to 256² [2].
  - Veo, Omni Flash and LTX-2.5 output only 16:9 or 9:16 [5][11][54].
  - Output that is square or follows the input frame: Luma (1:1) [19], MiniMax (`adaptive`, 1:1) [24], kf2v ("aspect ratio of the output video will match that of the first frame") [41], xAI ("defaults to the input image's aspect ratio") [62], Runway wan3 keyframes (`auto_*p`) [50].

### Re-render inventory (repo HEAD 7d9cc26)
- `video_graph.json` has 59 nodes and 500 edge rows: 204 transitions + 296 idles. **The idles are already inside the 500.** [1]
- All 296 idle rows have start_frame == end_frame and loop = true [1].
- The rows reduce to 251 unique clips (114 transitions + 137 idles). 83 clips carry 4 takes and 168 carry 1 [1][2].
- Autogen spends "1 imagine + 4 videos (fwd + REAL reverse + 2 idles)" per pose [2]. Clips are ~6 s [3].
- Scenarios: **A = 251** (1 take per clip), **B = 500** (1 per current row), **C = 618** (the task's 500 + 2×59; double-counts idles, upper bound only).

### Comparison: hosted APIs
| Vendor / model (as documented) | End-frame param (verbatim) | Loop | Durations | Res / aspect | Price → per clip | Output terms |
|---|---|---|---|---|---|---|
| **Kling 3.0 / 3.0 Omni / O1** | `contents[].type` … `last_frame`; "last-frame-only video generation is not supported" [13] | not documented | 3.0: 3–15 s; O1: 3–10 s [14] | 720p/1080p/4k; input 1:2.5–2.5:1; i2v has no aspect param [13] | $0.084/s no audio 720P ×5 = **$0.42** [15] | "intellectual property rights of the AI-generated content still belong to you"; "commercial purposes is not restricted" [16] |
| Kling 2.6 / 2.5 Turbo | first/last "Only supports 1080P silent videos" / "Only supports 1080P" [14] | not documented | 2.6: 3–10 s [14] | 1080P | $0.07/s ×5 = $0.35 [15] | same [16] |
| **Luma ray-3.2** (Agents API) | `video.start_frame`, `video.end_frame` (called "legacy"); `keyframes` + `keyframe_indexes` (5 s → 0–120) take "the full Ray 3.2 path" [19] | **`video.loop`**: "seamlessly looping"; rejected with `end_frame`/`keyframes` [19] | 5 s (start/end not with 10 s) [19] | 360p–1080p; `9:16`,`3:4`,**`1:1`**,`4:3`,`16:9`,`21:9` [19] | 540p **$0.15**/5 s; 360p $0.06; 720p $0.30; "subject to change ahead of general availability" [20] | See the Luma licensing gates below [21][22][23] |
| **MiniMax H3 / H3-Max** (V2 API) | "2 `image_url` items with `role` set to `first_frame` and `last_frame`" [24] | not documented | H3 4–15 s; H3-Max 5–15 s [24] | H3-Max 480P/768P; `adaptive` default, 1:1 available [24] | H3-Max 480P $0.05/s ×5 = **$0.25** [25] | "you retain your ownership rights in… generated content" [26]; API "Globally available" [28] |
| Vidu Q3-turbo / Q2 | `images`: "first is start frame, second is end frame"; ratio 0.8–1.25 [33] | not documented | q3 1–16 s; q2 1–8 s [33] | 540p/720p/1080p [33]; `audio` default true (q3) | Q3-turbo 540P $0.035/s ×5 = $0.175 [34] | "We don't restrict your use for commercial purposes"; no Output-ownership clause found [35] |
| **Alibaba wan2.2-kf2v-flash** | `last_frame_url` (Required) [41] | not documented | "fixed at 5" | 480P/720P/1080P; aspect = first frame; silent only [41] | 480P $0.015/s ×5 = **$0.075** [40] | "Model Studio does not claim ownership… in the Output" [39]. Filed under "Wan - legacy video models" [41] |
| Alibaba Wan 3.0 (`wan3.0-video`) | `last_frame`: "strictly used as the last frame" [36] | not documented | 2–30 s [36] | 480P–1080P; 1:1, 9:16 [36] | Intl 480P list $0.05/s ×5 = $0.25; US (Virginia)/Global list $0.041256/s ×5 = $0.206 [40] | **BLOCKED** until the preview-vs-GA conflict is resolved [36][37][38] |
| Google Veo 3.1 Lite / Fast / Std (Gemini API, Preview) | `lastFrame`: "Must be used in combination with the image parameter" [5] | not documented | 4/6/8 s [5] | 16:9 or 9:16 only; Lite has no 4k [5][6] | Lite $0.05/s ×6 = $0.30; Fast $0.60; Std $2.40 [6] | "Google won't claim ownership" [7]; audio "Always on"; `allow_adult` for interpolation; 1 video/request [5] |
| Veo 3.1 on Vertex | `lastFrame` [10] | not documented | 4/6/8 s [9] | 9:16, 16:9 [9] | Vertex price unit unclear (not quoted) | `veo-3.1-generate-001` "Launch stage: GA"; "Retirement date: November 17, 2026 or later"; "Pay-as-you-go Not supported / Fixed quota Supported" [9]; `sampleCount` 1–4 [10] |
| Gemini Omni Flash (`gemini-omni-1.1-flash`) | two images, first frame and last frame [11] | **documented same-image loop recipe** [11] | not a documented param on the Gemini API; Vertex: 3–10 s [10] | "9:16", "16:9"; 360p–4k [11] | "approximately $0.10 per second" at 720p [6] | "generally available… paid tier" [6]; Gemini terms [7]; "images containing certain recognizable people is not supported" [11] |
| Runway API (reseller) | `promptImage` `position: first`/`last` on wan3, h3_max, veo3.1(_fast), seedance2*, gemini_omni_flash_1.1 [50] | — | per model | wan3 keyframes must use `auto_480p/720p/1080p` [50] | $0.01/credit; wan3 or h3_max 480p 5 cr/s ×5 = $0.25; seedance2 36 cr/s ×5 = $1.80 [51] | "does not claim ownership of any of your Inputs or Outputs… does not restrict your commercial use"; grants Runway a training license over Inputs/Outputs [52] |
| LTX-2.5 fast / pro | `last_frame_uri` [53] | — | fast 720p: 6–20 s [54] | 1280x720 / 720x1280 [54] | fast 720p $0.09/s ×6 = $0.54 [54]; `generate_audio` default true [53] | "Customer owns Customer Data", which includes Output [55] |
| BFL FLUX 3 (`ii2v`) | two `keyframes`; "the API marks it experimental" [58] | — | 5–20 s | not verified | i2v hd $0.17/s ×5 = $0.85 (the ii2v rate is not listed separately) [59] | "We claim no ownership rights in and to Your Content" (Input + Output) [60] |
| xAI grok-imagine-video-1.5 | `image` + `last_frame` = "Pinned first and last frame" (REST body only) [61] | — | 1–15 s [62] | 1:1 available; i2v output follows input aspect [62] | $0.080/s ×5 = $0.40 [63] | terms page unreadable (Cloudflare block) |
| PixVerse v6 / c1 (transition) | `first_frame_img`, `last_frame_img` [64] | — | v6/c1 1–15 s [64] | 360p–1080p; audio default false [64] | "$1 = 5 videos (v6, 720p, 5s, no audio)" = $0.20 [65] | not checked |
| Pika 2.2 Pikaframes, **RESELLER price (fal)** | `image_urls` 2–5 keyframes [66] | — | 5 s default; total ≤25 s [66] | 720p/1080p [66] | $0.04/s, 5 s minimum = $0.20 [66] | Pika API: "licensed for commercial use" [67] |
| Adobe Firefly v3 | image `position` "0 being the first frame and 1 being the last frame" [68] | — | "a five second video" [68] | — | no published price found | not checked |
| ~~Seedance (BytePlus)~~ | `role` first/last; identical frames allowed [29] | — | — | — | — | **DISQUALIFIED: not available in the US** [30][31] |

### Comparison: open weights (rented GPU; no published per-clip price, so no cost computed)
| Model | FLF mechanism | License / output terms |
|---|---|---|
| Wan2.1-FLF2V-14B-720P | dedicated FLF2V. Sizes `720*1280`, `1280*720`, `480*832`, `832*480` (no square); `frame_num` default 81; Chinese prompts recommended [42][43][44] | Apache-2.0; "We claim no rights over the your generated contents" [42] |
| Wan2.1-VACE-14B (or 1.3B) | `frameref` `mode='firstlastframe'` [46] | Apache-2.0 [47] |
| Tencent HY-OmniWeaving | `interpolation`: "conditioned on start and end frames"; `--video_length` default 81 [48] | Tencent HY Community License: Territory excludes EU/UK/South Korea; a license must be requested above 100M MAU; "Tencent claims no rights in Outputs" [49] |
| LTX-2.5 (open) | `video_ltx2_5_flf2v` template [57] | paid license for "annual revenues of at least $10,000,000"; "claims no rights in the Output" [56] |

### Cost (published first-party prices only; arithmetic = per clip × 251 / 500 / 618)
| Option | Per clip | A = 251 | B = 500 | C = 618 |
|---|---|---|---|---|
| Luma ray-3.2 360p [20] | $0.06 | $15.06 | $30.00 | $37.08 |
| wan2.2-kf2v-flash 480P [40] | $0.075 | $18.83 | $37.50 | $46.35 |
| Luma ray-3.2 540p [20] | $0.15 | $37.65 | $75.00 | $92.70 |
| Vidu Q3-turbo 540P [34] | $0.175 | $43.93 | $87.50 | $108.15 |
| PixVerse v6 720p silent [65] | $0.20 | $50.20 | $100.00 | $123.60 |
| Pika via fal (RESELLER) [66] | $0.20 | $50.20 | $100.00 | $123.60 |
| MiniMax H3-Max 480P [25]; Runway wan3/h3_max 480p [51] | $0.25 | $62.75 | $125.00 | $154.50 |
| Veo 3.1 Lite 6 s [6] | $0.30 | $75.30 | $150.00 | $185.40 |
| Kling 2.6 1080P silent [15] | $0.35 | $87.85 | $175.00 | $216.30 |
| xAI grok-imagine-video-1.5 [63] | $0.40 | $100.40 | $200.00 | $247.20 |
| **Kling 3.0 / O1 720p silent** [15] | $0.42 | $105.42 | $210.00 | $259.56 |
| LTX-2.5 fast 720p 6 s [54] | $0.54 | $135.54 | $270.00 | $333.72 |
| Veo 3.1 Fast 6 s [6] | $0.60 | $150.60 | $300.00 | $370.80 |
| BFL FLUX 3 hd [59] | $0.85 | $213.35 | $425.00 | $525.30 |
| Runway seedance2 480p [51] | $1.80 | $451.80 | $900.00 | $1112.40 |
| Veo 3.1 Standard 6 s [6] | $2.40 | $602.40 | $1200.00 | $1483.20 |

Prices are per render. The Gemini API returns 1 video per request [5]. Vendors with no published identity-drift data need a re-roll budget of unknown size. Cost does not decide the choice: the choice hinges on licensing, aspect fit and drift.

### Luma licensing gates (clear all three before use)
1. The individual ToS says Outputs can be used commercially only "during an active Subscription Term under Customer's paid subscription allowing for the commercial use" [21].
2. API use is governed by the API Terms, which "supplement our Enterprise Terms of Service and Individual User Terms of Service (as applicable)" [22]. The Enterprise ToS assigns Output to the customer and has no such sentence [23].
3. "Trials… alpha, beta, or early access" use is "only for Customer's internal evaluation and testing" [21], and Ray 3.2 video pricing is pre-GA [20].

### Shortlist
1. **Kling 3.0 (new API, `last_frame`)**
   - Strictest documented first+last pinning [13] and the clearest output terms [16].
   - Audio is off by default [13]. Set `multi_shot: false`: the default is `true` [13].
   - Cost: $105 for 251 clips [15].
   - Risks: loops are undocumented; output aspect for a square input is undocumented; billing draws down prepaid "Resource Packages" [18].
2. **Luma ray-3.2, conditional.** The only native `loop` flag plus native 1:1 [19], at $0.15 per 540p clip [20].
   - Idles (137): pin `keyframes` [still, still] at indexes [0, 120], or use `start_frame` + `loop`. Whether `loop` ends exactly on the start frame is undocumented.
   - Transitions (114): `keyframes` at [0, 120], the full Ray 3.2 path [19].
   - **Do not use until Luma confirms in writing that the three licensing gates above are cleared.**
3. **MiniMax H3-Max (`role: last_frame`).**
   - Adaptive/1:1 output [24] at $0.25 per clip [25].
   - Customer keeps ownership [26]; the API is globally available, unlike the H3 weights [28].
   - Risks: loops undocumented; ToS date not visible.

Fallbacks:
- **wan2.2-kf2v-flash**: $0.075 per clip, 5 s fixed, output follows the square first frame [40][41]. It is filed as "legacy", so it is a deprecation risk.
- **Wan2.1-FLF2V / VACE (Apache-2.0) self-hosted**: no vendor dependency [42][46][47]. FLF2V has no square size [44].
- **Veo 3.1** is demoted. Its end-frame parameter is not unique, and it outputs only 16:9 or 9:16 against square stills. Vertex GA exists, but pay-as-you-go is "Not supported" there [9].
- **Omni Flash** has the only documented start == end loop recipe [11]. Pilot it for idles only, given the tension below.

Whichever vendor is chosen, the one-way-door rule applies: A/B about 10 transitions and 10 idles, and audit face drift, before re-rendering all 251 clips.

### Contradictions (reported, not resolved)
- **Wan 3.0 status.**
  - API reference, Sep 23 2026: "Currently in preview" [36].
  - Launch news, Aug 24 2026: "officially launched… now officially available" [37].
  - The Preview terms restrict preview products to internal testing [38].
- **Gemini Omni Flash end-frame support.**
  - Video overview, 2026-06-30: "Use Veo 3.1 for… last-frame control" [12].
  - Omni doc, 2026-09-23: "supports video interpolation… (last frame)" [11]. The Vertex FLF page [10] and Runway's API reference [50] also list Omni 1.1 with a last frame.
- **Veo page self-inconsistency** [5].
  - "available for Veo 3.1 models only", yet `lastFrame` is listed in the Veo 3 column.
  - Veo 3 is "Deprecated" in one place and "Stable" in another.
  - "only available with the generateContent API", yet the samples use `predictLongRunning`.

## Sources
[1] FIRST-PARTY · accessed 2026-09-23 (repo HEAD 7d9cc26) · data/clips/video_graph.json — Recounted in-session: schema living-portrait.video-graph/v3, 59 nodes, 500 edges; kind {'idle':296,'transition':204}; 251 unique (character,kind,label) = {idle:137, transition:114}; takes {1:168, 4:83}; all 296 idle rows start_frame==end_frame and loop=true.
[2] FIRST-PARTY · accessed 2026-09-23 (HEAD 7d9cc26) · pipeline/autogen.py — Line 77 "Each pose now = 1 imagine + 4 videos (fwd + REAL reverse + 2 idles)."; line 182 "def _mp4_to_gif(mp4_path, gif_path, size=256)" center-crop to square; line 408 "MJ bills a 4-up video grid"; line 412 "168 of the graph's 251" label-triples single take. No --ar flag found by grep.
[3] FIRST-PARTY · accessed 2026-09-23 · _preview_graph.py — Line 95: "The MJ clips are ~6s (61 frames @ FPS) with motion up front + a static settle."
[4] FIRST-PARTY · accessed 2026-09-23 · prompts/characters/maxx.json — framing: "aspect": "1:1", "panel_px": "192x192" (phineas.json and seraphina.json also "aspect": "1:1"). Canonical stills data/gen/*.png are not in the repo.
[5] FIRST-PARTY · Last updated 2026-09-17 UTC · https://ai.google.dev/gemini-api/docs/veo — "lastFrame : The final image for an interpolation video to transition. Must be used in combination with the image parameter."; aspectRatio "16:9" (default), "9:16"; durationSeconds "4", "6", "8"; audio "Always on"; "Videos per request ... 1"; "Image-to-video, Interpolation, & Reference images: \"allow_adult\" only"; model codes veo-3.1-*-preview; self-inconsistencies ("Veo 3.1 models only" vs Veo 3 column; "Deprecated" vs "Stable"; generateContent note vs predictLongRunning).
[6] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/pricing — "Veo 3.1 Standard ... $0.40 (720p and 1080p) $0.60 (4k) Veo 3.1 Fast ... $0.10 (720p) $0.12 (1080p) $0.30 (4k) Veo 3.1 Lite ... $0.05 (720p) $0.08 (1080p) (4k output not supported)"; Gemini Omni Flash gemini-omni-1.1-flash "now generally available to developers on the paid tier" ... "5,792 tokens per second of 720p video ... approximately $0.10 per second."
[7] FIRST-PARTY · Last updated 2026-04-28 UTC · https://ai.google.dev/gemini-api/terms — "Some of our Services allow you to generate original content. Google won't claim ownership over that content."
[8] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/models — "Preview Points to a preview model which may be used for production. ... will be deprecated with at least 2 weeks notice."
[9] FIRST-PARTY · Last updated 2026-09-22 UTC · https://cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate — "veo-3.1-generate-001 Launch stage: GA Release date: November 17, 2025 Retirement date: November 17, 2026 or later"; "Text to video, image to video, from first and last frame Supported"; "Pay-as-you-go Not supported Fixed quota Supported"; "Video lengths: 4, 6, or 8 seconds"; "Maximum number of output videos per prompt: 4"; "Supported aspect ratios: 9:16, 16:9".
[10] FIRST-PARTY · Last updated 2026-09-23 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames — Models supporting first+last frames: "gemini-omni-1.1-flash-preview preview ... veo-3.1-lite-generate-001 preview veo-3.1-generate-001 veo-3.1-fast-generate-001"; request body "lastFrame"; "RESPONSE_COUNT ... The accepted range of values is 1 - 4"; Omni DURATION "integers between 3 and 10"; aspect "16:9" "9:16".
[11] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/omni — "Gemini Omni Flash supports video interpolation, allowing you to generate a video that transitions smoothly between a starting image (first frame) and an ending image (last frame)."; "[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1] will use the first image as both the first frame and the last frame, creating a video that loops."; aspect "9:16", "16:9"; resolution 360p/720p/1080p/4k; "Uploading and editing images containing certain recognizable people is not supported."
[12] FIRST-PARTY · Last updated 2026-06-30 UTC · https://ai.google.dev/gemini-api/docs/video — "Use Veo 3.1 for specific capabilities like scene extension, last-frame control, or integration with legacy pipelines are required." (one side of the Omni tension)
[13] FIRST-PARTY · accessed 2026-09-23 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — "`contents[].type` | string | Yes | - | `prompt`, `first_frame`, `last_frame`, `element`"; "last-frame-only video generation is not supported"; input "aspect ratio of the image should fall within the range of 1:2.5 to 2.5:1"; "`settings.multi_shot` | boolean | No | `true`"; audio default `off`; resolution `720p`,`1080p`,`4k`; duration 3–15 default 5. No aspect_ratio setting in the i2v table.
[14] FIRST-PARTY · Updated At: 2026-05-19 · https://kling.ai/document-api/guides/capability-map/video.md — "| First/Last Frame | - | Not Supported | Supported | Supported | Supported | Supported: Only supports 1080P silent videos | Supported: Only supports 1080P |" (3.0 Turbo, 3.0, 3.0 Omni, O1, 2.6, 2.5 Turbo); ranges 3.0 "3~15s", O1 "3~10s", 2.6 "3~10s".
[15] FIRST-PARTY · accessed 2026-09-23 · https://kling.ai/document-api/pricing/base/video.md — "| Kling 3.0 | Per second | No Native Audio | 0.6 Units ($0.084) /s |"; "| Kling O1 | Per second | No Video Input | 0.6 Units ($0.084) /s |"; "| Kling 2.6 | Per second | No Native Audio | 0.3 Units ($0.042) /s | 0.5 Units ($0.07) /s |".
[16] FIRST-PARTY · Release/Effective Date: 2026-04-21 · https://kling.ai/document-api/guides/protocols/paid-service.md — 6.3 "the intellectual property rights of the AI-generated content still belong to you"; 6.4 "You use of the AI-generated content for commercial purposes is not restricted."
[17] FIRST-PARTY · entries 11/17/2025 and 07/15/2026 (verified by verifiers, not re-fetched by reconciler) · https://kling.ai/document-api/updates/api.md — "Passing in the image parameter value and image_tail parameter value can achieve this"; "The legacy API will continue to be available with no current plans for deprecation."
[18] FIRST-PARTY · accessed 2026-09-23 · https://kling.ai/document-api/guides/get-started/quick-start.md — "## Step 2: Purchase Resource Packages ... Video and Image Generation API Resource Packages are now available for purchase."
[19] FIRST-PARTY · accessed 2026-09-23 · https://docs.agents.lumalabs.ai/guides/videos/generation/index.md — "Pass an image as `video.start_frame`, `video.end_frame`, or both"; "Unlike the legacy `start_frame` / `end_frame` pair, multi-keyframe i2v routes through the full Ray 3.2 path"; keyframe_indexes "`5s → 0–120`"; "`video.loop` Boolean. When `true`, generates a seamlessly looping video ... not supported with `duration: \"10s\"`, `hdr: true`, or `end_frame`"; loop "rejected with `10s`, `hdr`, `end_frame`, or `keyframes`"; aspect incl `1:1`; resolutions 360p–1080p.
[20] FIRST-PARTY · accessed 2026-09-23 · https://docs.agents.lumalabs.ai/guides/pricing/index.md — "This tier covers text-to-video, image-to-video, and image-frame interpolation"; SDR per 5s: `360p` $0.0600, `540p` $0.1500, `720p` $0.3000; "Video rates are subject to change ahead of general availability."
[21] FIRST-PARTY · Last updated: May 14, 2026 · https://lumalabs.ai/legal/tos — "it can only use the Outputs for commercial purposes if the Outputs were produced during an active Subscription Term under Customer's paid subscription allowing for the commercial use of those Outputs"; Trials "alpha, beta, or early access offering ... permitted only for Customer's internal evaluation and testing purposes"; API users directed to "Enterprise Terms of Service and API Terms of Use (as applicable)".
[22] FIRST-PARTY · Last updated: April 28, 2026 · https://lumalabs.ai/legal/api-terms-of-use — "These API Terms of Use (\"API Terms\") supplement our Enterprise Terms of Service and Individual User Terms of Service (as applicable)"; must inform API users "that Output generated through the Services is AI-generated content".
[23] FIRST-PARTY · Last updated: April 20, 2026 · https://lumalabs.ai/legal/enterprise-terms-of-service — "Output Ownership . As between the parties ... Customer owns and retains all right, title, and interest in and to the Output and Luma hereby assigns to Customer all of Luma's right, title, and interest in and to the Output." (no paid-subscription commercial sentence found)
[24] FIRST-PARTY · accessed 2026-09-23 · https://platform.minimax.io/docs/api-reference/video-generation-v2-create.md — "**Image-to-video, first & last frame**: `text` + 2 `image_url` items with `role` set to `first_frame` and `last_frame` respectively"; H3-Max `480P`,`768P`; H3 `4`–`15`; H3-Max `5`–`15`; ratio "Defaults to `adaptive`" with `1:1` available.
[25] FIRST-PARTY · accessed 2026-09-23 · https://platform.minimax.io/docs/guides/pricing-paygo.md — "MiniMax-H3-Max | 480P | Billed per second | $0.05 / second"; "MiniMax-H3 | 768P | Billed per second | $0.08 / second".
[26] FIRST-PARTY · accessed 2026-09-23 via verifiers (effective date not visible) · https://platform.minimax.io/protocol/terms-of-service — "you retain your ownership rights in Client input and generated content."
[27] FIRST-PARTY · License date: August 2, 2026 · https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/LICENSE — "“Excluded Territories” means the European Union, the United Kingdom, the Republic of Korea and the United States of America."; "You may not ... display the MiniMax H3 Works or any of their Outputs or results outside the Applicable Territory."
[28] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/docs/QA-about-License.md — "API: Globally available with built-in safeguards and responsible-use controls."
[29] FIRST-PARTY · accessed 2026-09-23 · https://docs.byteplus.com/en/docs/ModelArk/1520757 — "Supported models: Dreamina Seedance 2.5, Dreamina Seedance 2.0 series, Seedance 1.5 pro, and Seedance 1.0 pro."; "The first-frame and last-frame images can be identical."
[30] FIRST-PARTY · Last updated: September 2, 2026 · https://docs.byteplus.com/en/docs/legal/docs-service-specific-terms — "The BytePlus Model Services are not available in the United States." (re-fetched by reconciler)
[31] FIRST-PARTY · Last Updated: 21 April 2026 · https://docs.byteplus.com/en/docs/ModelArk/availability — Country list runs "United Arab Emirates, United Kingdom, Uruguay"; no United States (re-fetched by reconciler).
[32] FIRST-PARTY · Last updated: August 28, 2026 · https://docs.byteplus.com/en/docs/legal/AI-Services-terms?lang=en — "2.1 Input and Output ... you own the Output generated in response to your Input, and BytePlus does not claim ownership of such Output."
[33] FIRST-PARTY · accessed 2026-09-23 · https://platform.vidu.com/docs/start-end-to-video.md — "images | Array[String] | Required | Two images: first is start frame, second is end frame"; "ratio between start/end frame must be in 0.8~1.25"; q3 "available: 1 - 16"; q2 "1 - 8"; resolutions 540p/720p/1080p; `audio` "Default: true" (q3 only).
[34] FIRST-PARTY · accessed 2026-09-23 · https://platform.vidu.com/docs/pricing.md — "Credits are available for $0.005 each"; "| Vidu Q3-turbo | ... start-end2video | 1-16S | 540P | 7 /Second | $0.035 / Second | 4 /Second | $0.02 / Second |" (columns: Pricing, Off_peak Pricing); Q2-turbo 540P "Starts at $0.03, +$0.01/sec".
[35] FIRST-PARTY · Effective on 2025-01-23 (verified by verifiers) · https://platform.vidu.com/docs/terms-of-use.md — "We don’t restrict your use for commercial purposes." (in the Services license grant; no explicit Output-ownership clause).
[36] FIRST-PARTY · Last Updated: Sep 23, 2026 · https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference — "Image-to-Video (first frame/first-last frame) ... Currently in preview ."; "last_frame : Last frame image. Maximum 1 image, strictly used as the last frame of the video."; duration "[2, 30]"; ratios incl 1:1, 9:16.
[37] FIRST-PARTY · Aug 24 2026 · https://www.alibabacloud.com/en/news/product/video-generation-model-wan30-officially-launched-nsb — "Video generation model Wan3.0 officially launched ... The Wan3.0 Video API is now officially available and can be called without the need to apply."
[38] FIRST-PARTY · Last Updated: Aug 20, 2026 · https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-beta-testing-terms — "license to use the Preview Product ... solely for the purposes of internal testing, research and evaluation."
[39] FIRST-PARTY · Last Updated: Aug 28, 2026 · https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-product-terms-of-service-v-3-8-0 — "Model Studio does not claim ownership of any Intellectual Property Rights in the Output."; 3.14 Preview Product governed by preview terms.
[40] FIRST-PARTY · Last Updated: Sep 24, 2026 · https://www.alibabacloud.com/help/en/model-studio/model-pricing — "wan2.2-kf2v-flash International 480P $0.015/second"; "wan3.0-video International 480P List price $0.05/second (Limited-time 30% off)"; US (Virginia)/Global "wan3.0-video Global 480P List price $0.041256/second (Limited-time 30% off)".
[41] FIRST-PARTY · Last Updated: Sep 22, 2026 · https://www.alibabacloud.com/help/en/model-studio/legacy-image-to-video-by-first-and-last-frame-api-reference — Breadcrumb "Wan - legacy video models"; "last_frame_url string (Required)"; "The aspect ratio of the output video will match that of the first frame image."; duration "This value is fixed at 5."; wan2.2-kf2v-flash 480P/720P/1080P; "The service generates silent videos only."
[42] FIRST-PARTY · lastModified 2025-04-17; accessed 2026-09-23 · https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P — license apache-2.0; "Apr 17, 2025: ... We introduce Wan2.1 FLF2V with its inference code and weights!"; "FLF2V-14B ... Supports 720P"; "we recommend using Chinese prompt"; "We claim no rights over the your generated contents".
[43] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Wan-Video/Wan2.1/blob/main/generate.py — "args.frame_num = 1 if \"t2i\" in args.task else 81" (default frame count incl. flf2v).
[44] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Wan-Video/Wan2.1/blob/main/wan/configs/__init__.py — "'flf2v-14B': ('720*1280', '1280*720', '480*832', '832*480')" (no square size).
[45] FIRST-PARTY · accessed 2026-09-23 (verified by verifiers) · https://github.com/Wan-Video/Wan2.2/tree/main/wan/configs — Configs: wan_animate_14B, wan_i2v_A14B, wan_s2v_14B, wan_t2v_A14B, wan_ti2v_5B; no FLF config.
[46] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ali-vilab/VACE/blob/main/UserGuide.md — "| extension | frameref | FrameRefExpandAnnotator | two images a.jpg,b.jpg | mode='firstlastframe' expand_num=80 (default)"
[47] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ali-vilab/VACE/blob/main/README.md — "| Wan2.1-VACE-14B | ... | ~ 81 x 720 x 1280 | [Apache-2.0]"; repo license Apache-2.0; HF Wan-AI/Wan2.1-VACE-14B tag license:apache-2.0.
[48] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Tencent-Hunyuan/OmniWeaving/blob/main/readme.md — "built upon the latest HunyuanVideo-1.5"; "| `interpolation` | Key-Frames-to-Video | Generate a video conditioned on start and end frames. |"; weights huggingface.co/tencent/HY-OmniWeaving; "`--video_length` | int | `81`".
[49] FIRST-PARTY · Tencent HY-OmniWeaving Release Date: March 31, 2026 · https://github.com/Tencent-Hunyuan/OmniWeaving/blob/main/License.txt — "“Territory” shall mean the worldwide territory, excluding the territory of the European Union, United Kingdom and South Korea."; >100 million MAU must request a license; "Tencent claims no rights in Outputs You generate."
[50] FIRST-PARTY · accessed 2026-09-23 · https://docs.dev.runwayml.com/api.md — gen4.5 "`position` ... one of `first`"; wan3 "Use position `first`/`last` for keyframe mode" and "Keyframe image-to-video requests must use `auto_480p`, `auto_720p`, or `auto_1080p`"; gemini_omni_flash_1.1 "an array containing a first frame and optional last frame", "between 3 and 10 seconds".
[51] FIRST-PARTY · accessed 2026-09-23 · https://docs.dev.runwayml.com/guides/pricing.md — "for $0.01 per credit"; "| `wan3` (480p) | 5 credits per second |"; "| `h3_max` (480p) | 5 credits per second |"; "| `seedance2` (480p/720p) | 36 credits per second |"; "| `veo3.1_fast (no audio)` | 10 credits per second |".
[52] FIRST-PARTY · Last updated September 15, 2026 · https://runwayml.com/terms-of-use — "The Company does not claim ownership of any of your Inputs or Outputs. Subject to your compliance with the Agreement, the Company does not restrict your commercial use of your Outputs."; "Inputs and Outputs may be used by the Company to train and improve its AI models"; "Powered by Runway" for end-user apps.
[53] FIRST-PARTY · accessed 2026-09-23 · https://docs.ltx.io/api-documentation/api-reference/async-video-generation/submit-image-to-video.md — "`last_frame_uri` (string, optional) — Image to be used as the last frame of the video."; `generate_audio` "default: true"; automatic duration "Cannot be combined with `last_frame_uri`".
[54] FIRST-PARTY · accessed 2026-09-23 (durations from https://docs.ltx.io/models/ltx-2-5.md) · https://docs.ltx.io/pricing.md — Image-to-Video "Cost per second": "| **ltx-2-5-fast** | `1280x720` / `720x1280` | $0.09 |"; ltx-2-5.md "| **ltx-2-5-fast** | 720p | 24, 25 | 6, 8, 10, 12, 14, 16, 18, 20 |".
[55] FIRST-PARTY · Last Updated: May 12, 2026 (verified by verifiers) · https://static.lightricks.com/legal/ltx-2-api-license-agreement.pdf — "“Customer Data” means (a) Input, (b) Output"; "Customer owns Customer Data to the extent permitted by applicable law."
[56] FIRST-PARTY · accessed 2026-09-23 (verified by verifiers) · https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x — "Entities with annual revenues of at least $10,000,000 (the \"Commercial Entities\") are required to obtain a paid license"; "Licensor claims no rights in the Output you generate using LTX-2.x."
[57] FIRST-PARTY · accessed 2026-09-23 (verified by verifiers) · https://docs.ltx.io/open-source-model/usage-guides/image-to-video.md — "The **First-Frame / Last-Frame** template (`video_ltx2_5_flf2v`) generates the motion *between* a starting image and an ending image."
[58] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/cookbook/video_start_from_images.md — "Two `keyframes` entries** (`ii2v`): your images are the opening **and closing**"; "End-frame pinning is newer than frame-0 pinning and the API marks it experimental".
[59] FIRST-PARTY · accessed 2026-09-23 · https://docs.bfl.ml/quick_start/pricing.md — "| Image to Video (`i2v`) | $0.17/s | $0.29/s | $0.40/s | $0.80/s | $0.06/s |" (hd/fhd/qhd/uhd/Draft); no separate ii2v row.
[60] FIRST-PARTY · accessed 2026-09-23 (no date shown) · https://bfl.ai/legal/terms-of-service — "1.2. Input and Output (“Your Content”) ... We claim no ownership rights in and to Your Content".
[61] FIRST-PARTY · accessed 2026-09-23 · https://docs.x.ai/developers/model-capabilities/video/reference-to-video.md — "On `grok-imagine-video-1.5`, `last_frame` pins the exact last frame of the clip."; "| `image` + `last_frame` | Pinned first and last frame. The model interpolates between the two. |"; "The Python SDK and Vercel AI SDK do not yet expose a dedicated `last_frame` parameter; send it on the REST body."
[62] FIRST-PARTY · accessed 2026-09-23 · https://docs.x.ai/developers/model-capabilities/video/generation.md — "The allowed range is 1–15 seconds."; aspect table includes `1:1`; "For image-to-video generation, the output defaults to the input image's aspect ratio."
[63] FIRST-PARTY · accessed 2026-09-23 · https://docs.x.ai/developers/models.md — "| grok-imagine-video-1.5 | $0.080 / sec |"
[64] FIRST-PARTY · accessed 2026-09-23 · https://docs.platform.pixverse.ai/transitionfirst-last-frame-generation-15123014e0.md — POST /openapi/v2/video/transition/generate; model "v3.5/v4/v4.5/v5/v5.5/v5.6/v6/c1"; duration "v6/c1 : 1~15"; quality "360p"–"1080p"; first_frame_img, last_frame_img; generate_audio_switch "default value : false".
[65] FIRST-PARTY · accessed 2026-09-23 · https://docs.platform.pixverse.ai/pricing-796039m0.md — "$1 = 5 videos (v6, 720p, 5s, no audio)"; V6 "Text-to-video / Image-to-video / Transition" 720p 9 credits/s no audio.
[66] secondary · accessed 2026-09-23 · https://fal.ai/models/fal-ai/pika/v2.2/pikaframes/llms.txt — RESELLER (fal; first-party only for fal's own price): "Your request will cost $0.04 per second for 720p or $0.06 per second for 1080p, with a minimum of 5 billable seconds"; "keyframe images (2-5 images)"; "Total duration of all transitions must not exceed 25 seconds".
[67] FIRST-PARTY · accessed 2026-09-23 (price table recordedAt 9.18.26) · https://pika.art/api — "Can I use outputs commercially? Yes. All API outputs are licensed for commercial use under your Pika API agreement."; model list includes "Pika 2.5 Keyframe" (no API price row for it).
[68] FIRST-PARTY · accessed 2026-09-23 · https://github.com/AdobeDocs/ffs-firefly-api/blob/main/static/firefly-api.json — /v3/videos/generate "Generate a five second video"; image "used as a first frame or final frame"; position "0 being the first frame and 1 being the last frame".

## Contradictions (first-party vs first-party — unresolved)
- Wan 3.0 status (Alibaba, both first-party): https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference (Last Updated: Sep 23, 2026) says "Currently in preview ." whereas https://www.alibabacloud.com/en/news/product/video-generation-model-wan30-officially-launched-nsb (Aug 24 2026) says "Video generation model Wan3.0 officially launched ... The Wan3.0 Video API is now officially available and can be called without the need to apply." Consequence if preview: https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-beta-testing-terms (Aug 20, 2026) limits Preview Products to "solely for the purposes of internal testing, research and evaluation". Not resolved.
- Gemini Omni Flash end-frame support (Google, both first-party): https://ai.google.dev/gemini-api/docs/video (Last updated 2026-06-30) says "Use Veo 3.1 for specific capabilities like scene extension, last-frame control" whereas https://ai.google.dev/gemini-api/docs/omni (Last updated 2026-09-23) says "Gemini Omni Flash supports video interpolation ... between a starting image (first frame) and an ending image (last frame)" and documents a same-image loop. The newer Vertex FLF page (2026-09-23) and Runway's API reference also list Omni 1.1 with a last frame. Likely version drift, but reported without picking a side.
- Veo page https://ai.google.dev/gemini-api/docs/veo (Last updated 2026-09-17) contradicts itself: "Note: This feature is available for Veo 3.1 models only" vs the parameter table listing lastFrame 'Image object' under the Veo 3 & Veo 3 Fast column; the model list says "Veo 3 (Deprecated)" while the features table says "Status: Model availability Preview Preview Stable" (third column = Veo 3); the header note "This feature is currently only available with the generateContent API" vs code samples using predictLongRunning / generateVideos. Does not affect Veo 3.1 use.

## Could not confirm
- Identity drift / face fidelity in first+last-frame mode: no vendor publishes first-party metrics; ranking requires an in-house A/B pilot.
- Seamless start==end behavior for Veo 3.1, Kling, MiniMax H3, Vidu, Wan (kf2v, 3.0), LTX, BFL, xAI, PixVerse, Pika: undocumented.
- Whether Luma `loop: true` + `start_frame` ends exactly on the start frame (needed because graph idles have start_frame == end_frame).
- Which Luma base terms (Individual ToS with paid-subscription commercial condition vs Enterprise ToS without it) govern pay-as-you-go API use; whether Ray 3.2 video counts as a 'Trial/early access' offering.
- Wan 3.0 legal status (preview vs GA); whether Runway's `wan3` resale route inherits Alibaba Preview Product Terms.
- Kling output aspect for a square (1:1) input frame: the i2v doc has no aspect_ratio setting and states only an input constraint.
- Veo/Omni Flash behavior when given square first/last frames with 16:9 or 9:16 output (padding/outpainting undocumented).
- Pixel aspect of the canonical MJ stills: data/gen/*.png is not in the repo; only the framing spec says 1:1 and autogen.py passes no --ar flag.
- xAI output-ownership terms (terms pages blocked by Cloudflare); PixVerse terms (not checked); Adobe Firefly terms and API price (not found).
- Pika first-party API price for Pikaframes / 'Pika 2.5 Keyframe' (only fal reseller price captured).
- US availability of the Kling, Vidu, PixVerse, xAI APIs (only BytePlus was found to exclude the US; MiniMax states API is globally available).
- MiniMax Open Platform ToS effective date (not visible).
- Vertex AI Veo 3.1 per-second price (pricing page unit printed as '/ 1 count', undefined) and minimum commitment under 'Fixed quota' consumption.
- BFL price for two-keyframe `ii2v` (pricing page lists only t2v/i2v/v2v); BFL supported aspect ratios (not verified this session).
- Gemini API duration control for Omni Flash (no documented duration parameter on the Gemini API; Vertex lists 3–10 s).
- Minimum spend of Kling prepaid Resource Packages.
- Rented-GPU per-clip cost for self-hosting Wan2.1-FLF2V, VACE, OmniWeaving or LTX-2.5 (no published price).
- Duration of the Wan 3.0 'Limited-time 30% off' and whether the listed price is pre- or post-discount.
- Tencent Hunyuan hosted (cloud) first+last-frame API: not researched.
- Wan 3.0 'public beta since 2026-08-06' from a prior sweep: not re-confirmed (current doc says 'Currently in preview'; news says launched Aug 24 2026).

## Dropped claims (refuted or unsupported in verification)
- Veo is 'the only vendor with a dedicated end-frame constraint parameter documented in a first-party parameter table': contradicted by Kling `last_frame`, Luma `video.end_frame`, LTX `last_frame_uri`, Alibaba `last_frame_url`, MiniMax `role: last_frame`, Vidu `images`, xAI `last_frame`, PixVerse `last_frame_img`.
- Veo 3.1 Lite is 'one of the cheapest options with it': contradicted. At $0.30 per 6 s clip it is mid-pack (kf2v $0.075, Luma 540p $0.15, Vidu Q3-turbo $0.175, PixVerse $0.20, MiniMax H3-Max $0.25).
- 'Every row re-renders all 251 clips for less than about $215' and 'all but Veo Standard and Runway seedance2 stay near or under $150 even for 500 renders': arithmetically false (Veo Std $602.40 and Runway seedance2 $451.80 at 251; Kling 3.0 $210, Veo Fast $300, LTX $270, BFL $425 at 500). Replaced by the recomputed cost table.
- 'Vendors below return 1 video per request [c11]': sourced only for Veo on the Gemini API; Vertex sampleCount accepts 1–4; other vendors unverified.
- 'The only open-weight first/last-frame model with a permissive license is Wan2.1-FLF2V-14B-720P': contradicted by Wan2.1-VACE-14B (Apache-2.0, firstlastframe mode); OmniWeaving and LTX-2.x are also commercially usable for this project.
- 'The Hunyuan repos have no first/last-frame pipeline': contradicted by Tencent-Hunyuan/OmniWeaving (built on HunyuanVideo-1.5, `interpolation` task, open weights).
- '81 frames (README example)' for Wan2.1-FLF2V: misattributed. Replaced with the generate.py default `frame_num ... 81`.
- Veo table row 'Lite / Fast / Std: 720p/1080p/4k': Veo 3.1 Lite has no 4k ('4k output not supported').
- Kling example with identical first/last image as 'the closest thing to a loop pattern': the same placeholder image_25.png is reused across all examples; no loop semantics documented.
- Kling 'aspect follows image (1:2.5–2.5:1)': the doc states only an input-image constraint; output aspect for i2v is undocumented.
- 'Only Seedance documents identical first/last frames': Gemini Omni Flash documents a same-image loop recipe.
- Seedance 1.5 pro via BytePlus as the $0.06/clip budget fallback: dropped. The BytePlus Model Services 'are not available in the United States' (re-fetched), and the availability list omits the US.
- 'BytePlus/Seedance output-ownership clause not located': superseded. Found in the General Terms for AI Services §2.1 (2026-08-28); moot for direct use.
- Luma licensing blocker resting on the individual ToS only: refined to three gates (API Terms plus Enterprise vs Individual ToS; Trials clause; pre-GA pricing).
- Veo 'Preview status' as the main Veo risk: Vertex AI lists veo-3.1-generate-001 / veo-3.1-fast-generate-001 as GA (with 'Pay-as-you-go Not supported'); Google states Preview models 'may be used for production'.
- Exclusion of Gemini Omni Flash on the strength of the c57 contradiction: the tension is still reported, but Omni is now listed as a pilot candidate for idle loops because newer first-party pages (Omni doc, Vertex FLF, Runway API) document first/last and a loop recipe.
- BFL row 'hd–uhd; 1:1 and 9:16': aspect ratios not verified this session; removed.
- Seedance source date 'Last updated: September 22, 2026' for BytePlus 1520757: not seen verbatim by the independent verifier; cited as accessed 2026-09-23 instead.

## DO NOT QUOTE (low/unknown)
- [unknown] Any ranking of vendors by identity drift or face fidelity — No first-party drift metrics exist for any vendor; only a pilot can establish it.
- [unknown] Claims that Veo, Kling, MiniMax, Vidu, Wan, LTX, BFL, xAI, PixVerse or Pika produce seamless loops from identical first/last frames — Undocumented; only Luma (loop flag), Gemini Omni Flash (same-image recipe) and Seedance (identical frames allowed, but disqualified in the US) document it.
- [unknown] Luma `loop` + `start_frame` returns exactly to the start frame — The doc says 'seamlessly looping' but does not say the loop point equals start_frame.
- [unknown] Luma API output is cleared for commercial public display — Governing base terms for API PAYG are unstated; the individual ToS has a paid-subscription condition and a Trials clause; pricing is pre-GA.
- [unknown] Wan 3.0 (direct Model Studio) is usable for a permanent public display — First-party preview-vs-launched contradiction; Preview terms are internal-testing only.
- [low] Gemini Omni Flash per-clip cost of about $0.50 for 5 s — Token-billed at 'approximately $0.10 per second'; the Gemini API documents no duration parameter; derived arithmetic only.
- [unknown] Vertex AI Veo 3.1 prices — The pricing unit is printed as '/ 1 count' and is undefined; Vertex 3.1 GA lists pay-as-you-go 'Not supported'.
- [low] Vidu Q2-turbo 540P 5 s exact price ($0.07 vs $0.08) — 'Starts at $0.03, +$0.01/sec' is ambiguous about whether the base includes the first second.
- [low] BFL two-keyframe (ii2v) price equals the i2v rate ($0.17/s hd) — The pricing page lists t2v/i2v/v2v only; ii2v is inferred.
- [unknown] BFL FLUX 3 aspect ratios (1:1, 9:16) and resolution range — Not verified in this session.
- [unknown] Pika's own Pikaframes / 'Pika 2.5 Keyframe' API price — Only the fal reseller price ($0.04/s, 5 s minimum) was captured; the Pika model page is login-walled.
- [unknown] xAI grok-imagine-video-1.5 output ownership / commercial terms — The x.ai legal pages returned a Cloudflare block.
- [unknown] PixVerse output terms — Not checked.
- [unknown] Adobe Firefly v3 video price and output terms — No published per-clip price found; terms not checked.
- [unknown] Kling output aspect ratio for square input — Only an input-image constraint (1:2.5–2.5:1) is documented; the i2v doc has no aspect setting.
- [low] Canonical MJ stills are exactly 1:1 — Only the character framing spec says 1:1; data/gen/*.png is not in the repo and autogen.py passes no --ar flag.
- [unknown] Kling minimum prepaid Resource Package spend — Not captured; per-second $ values are unit conversions.
- [unknown] Rented-GPU cost to self-host Wan2.1-FLF2V, VACE, OmniWeaving or LTX-2.5 — No published per-clip price gathered.
- [unknown] MiniMax Open Platform ToS effective date (e.g. 'March 30, 2026') — Not visible on the first-party page; the only date seen was from a secondary source.
- [unknown] Wan 3.0 'public beta since 2026-08-06' — From a prior sweep; not re-confirmed; current first-party pages say 'Currently in preview' / 'officially launched Aug 24 2026'.
- [unknown] US availability of Kling, Vidu, PixVerse, xAI APIs — Not checked; only BytePlus was confirmed to exclude the US.
- [unknown] Whether Runway's `wan3` route avoids Alibaba's Preview Product Terms — Runway's ToS governs Runway outputs, but pass-through obligations were not checked.
- [unknown] Whether Seedance 2.x face moderation would flag painted portrait faces — Moot for direct use (US-excluded), but unverified for reseller routes.
- [low] Effective Wan 3.0 price after the 'Limited-time 30% off' — Only list prices were quoted; the discount's duration and base are unclear.


---

# Track MJ6 — The third-party midjourney client + official API + ToS on automation
Primary mission track: yes · Final confidence: medium

## Answer
## MJ6: FINAL (reconciled 2026-09-23)

### Direct answers
1. **Which client is it? It cannot be identified from any public or local source.**
   - `midjourney.api` is a private package vendored into the project on hil and in the private "life monorepo". Evidence:
     - The code imports it lazily and says it is "only present on hil" [1].
     - The upstream release script leaves it out of the public repo on purpose: `"midjourney",  # vendored client` [6].
     - hil's host ledger ignores `midjourney/` and `sessions/` [7].
   - It authenticates with Firebase, reading `sessions/midjourney.json`, and raises `MidjourneyAPIAuthError` [8].
   - It talks to midjourney.com's web endpoints. The project's own telemetry records `POST /api/storage-upload-file -> 403` [8][9].
   - Nothing public matches its fingerprint:
     - The only public hit for `MidjourneyAPIClient`, `cdn_variant_url`, `from midjourney.api import` and `MidjourneyAPIAuthError` is the upstream living-portraits repo itself [14]. The other `MidjourneyAPIClient` classes have different interfaces [15].
     - PyPI `midjourney` 0.0.1 is an empty placeholder: a 0-byte `__init__.py`, uploaded 2022-11-29 [16].
     - `midjourney-py` 1.0.4 also installs a top-level `midjourney` package but has no `api` module [17].
     - Nothing on this Mac contains it.
   - **Unknown:** repo URL, author, license, last commit, and the `submit_imagine`/`submit_video` payload code.
2. **Can it send several reference images? Not confirmed for the client, and not possible for identity under the V7 pin regardless of the client.**
   - As `autogen.py` calls it, references go only inside the prompt string. `submit_imagine(prompt, mode=)` is given `"<prompt> --oref <url> --ow 160 --v 7"` and no reference argument [1].
   - Whether the client forwards that string unchanged or rewrites it into structured fields is **unknown**.
   - The v8.1 error quoted in autogen.py does not settle the question. At that time `--version 8.1` came from the account default, not from the prompt [1][35].
   - Midjourney documents multi-URL prompt-text syntax only **"in Discord"**: image prompts, `--sref URL URL`, `--edit URL URL` and `--end URL` [30][31][29][32]. On the web, references go into UI slots [30][29]. Nothing first-party says the web API accepts several URLs as prompt text.
   - What MJ allows under V7:
     - Omni Reference takes one image and works only on V7 [28].
     - The Edit Model takes up to 4 references and works only on V8.1/8.2 [29]. That migration is closed.
     - V7 can combine one `--oref` with Image Prompts and Style References [28], but those are not identity locks.
     - Video accepts only `--motion`, `--raw`, `--loop`, `--end` and `--bs`. Image reference types are "not compatible with video generations" [32].
3. **(a) Is there an official Midjourney API? No public one.**
   - Community Guidelines: "With a few rare exceptions that are explicitly granted, Midjourney does not provide an API … automating interactions with Midjourney service is strictly prohibited" [19]. The same text appears in the 2025-02-14 snapshot [22].
   - The only API post is "Enterprise API Survey" (2025-07-16): "We're starting to investigate opening up an Enterprise API" [23].
   - None of the 42 posts in the sitemap dated since 2025-07-01, through `alpha-changelog-9-23-26`, announces an API [24].
   - Group Plans do not offer "Terms and policy negotiations" [25].
4. **(b) What does the Terms of Service say? (Version Effective Date: May 27, 2026; article edited 2026-05-27, updated 2026-08-17) [18]**
   - §1 automation: "You may not reverse engineer the Services or the Assets. You may not use automated tools to access, interact with, or generate Assets through the Services."
   - §1 accounts: "Only one user may use the Services per registered account."
   - §1 enforcement: "Midjourney reserves the right to suspend or ban Your access to the Services at any time, and for any reason."
   - §11 applies separately to Editor/Video: "suspend or ban your access to them at any time, and for any reason."
   - §8: "terminate Your access to the Service for any reason … Any violation of Community Guidelines is a breach of this Agreement. You will not be refunded for the current subscription period".
   - §7: "we reserve the right to rate limit You".
   - §1: "Please do not create any dependencies on any attributes of the Services".
   - **Notice:**
     - The ToS has no notice or warning duty. All 5 occurrences of "notice" are in §5 (DMCA), and "without notice" does not appear.
     - The Community Guidelines say violators "may be warned … given a time-out, or be blocked" [19]. That is optional, not required.
     - The Omni Reference doc says: "Anyone attempting to violate our Community Guidelines will face suspension or banning without refund" [28].
     - The Refund article excludes accounts "suspended or terminated due to a violation of our Terms of Service or Community Guidelines" [26].
   - **History:** the same automation, reverse-engineering, one-user and suspend/ban clauses are in the ToS versions effective February 5, 2025 [20] and February 12, 2026 [21]. The May 27, 2026 version was first archived 2026-06-18 [42]. These clauses are unchanged across all three versions.
5. **STOP: two first-party sources contradict each other.** See `contradictions` #1.
   - Upstream (2026-09-09):
     - "The Midjourney generation path is **retired but intact**. It has been returning HTTP 403 on every image upload since 2026-07-02. Higgsfield replaced it on 2026-08-08." [8]
     - `BACKEND = os.environ.get("LP_GEN_BACKEND", "hf")` [10]
     - "its session is dead" [9]
   - Local MODEL_STACK.md (verified 2026-09-10): Midjourney V7 is the "Live path" for "every pose still and every transition clip" [2].
   - Not resolved here.

### Evidence table
| Item | Finding | Conf. | Src |
|---|---|---|---|
| Fingerprint | `MidjourneyAPIClient()`; `upload_image()["shortUrl"]`; `submit_imagine(prompt, mode=)`; `submit_video(image_url=, end_image=, motion_prompt=, loop=, mode=)`; `job_status([id])`; `download_video(job_id, variant=, out_path=)` (:433); `client._session.get` (:399); `cdn_variant_url(grid, 0)` (:320) | high | [1] |
| Vendored / private | release.py `"midjourney",  # vendored client`; deploy_hil host .gitignore adds `midjourney/` | high | [6][7] |
| Dependencies | AUTONOMY.md: "`midjourney/` client, `curl_cffi`" | high | [3] |
| Where it came from | Prompt note names "kernel.midjourney.generate_video". Inference only. | low | [4] |
| PyPI | `midjourney` 0.0.1 is empty; `midjourney-py` 1.0.4 has no `api.py`; `midjourney-client`, `-web` and `pymidjourney` return 404 | high | [16][17] |
| Omni Reference | "You can only use one image with Omni Reference." "can only be used with Midjourney version 7." `--ow` range 1–1,000, default 100 | high | [28] |
| `--ow` | Missing from the Parameter List (0 hits) but still documented in the Omni Reference article | high | [33][28] |
| Edit Model | "up to 4 reference images"; "compatible with Midjourney versions 8.1 and 8.2" | high | [29] |
| `--cref` | Legacy; "replaced by Omni Reference in V7, and the Edit Model in V8.X" | high | [34] |
| Version dates | V7 default from June 17, 2025 to June 9, 2026. V8.1 default from June 10 to July 23, 2026. V8.2 default from July 24, 2026, "which replaces Omni Reference" | high | [35] |
| Deprecation exposure | "V7 omni-reference is available to use while we finish training the improved version for V8" (2026-06-11). The Edit Model shipped 2026-08-27, "replacing omni-reference". | high | [36][37] |
| Web-UI churn | "we launched a very rough draft of some big changes to alpha.midjourney.com" (2026-08-21). Account-level "Your defaults" added 2026-09-23. | high | [40][41] |
| Web hint | "Automatically strip irrelevant parameters (--cw/--ow) when cref/oref not present" (2026-01-20). Weak: does not establish the wire format. | low | [38] |
| Plan | Video in Relax Mode only on "Pro and Mega plans … (SD resolution only)". Companies with more than $1,000,000 a year in revenue need Pro/Mega to own Assets. | high | [32][18] |
| Ownership | "you own all the images and videos you create, even if you decide to cancel your subscription". The docs say nothing about ownership after a ban. | high | [27] |
| Repo lineage | Local fork of RayyanZahid (MIT, last pushed 2026-07-16). Local autogen history is 1e1db3a (2026-07-11) and 691336f (2026-09-10). No `hf_gen.py` locally. Immersive-commons is Apache-2.0 and not a fork. | high | [5][13] |

### Commands to run on hil (read-only; do NOT make a live MJ call)
1. Find the interpreter first. Upstream lists `lp-gen` as bare `pythonw pipeline\autogen.py …` [8].
   - `schtasks /query /tn lp-gen /v /fo list`
   - `powershell -NoProfile -Command "(Get-ScheduledTask -TaskName lp-gen).Actions | Format-List *"`
   - `where pythonw python`
   - Call the resulting python.exe `<PY>`.
2. `powershell -NoProfile -Command "Get-ChildItem C:\living-portraits\midjourney -Recurse | Select FullName,Length,LastWriteTime"`
3. Import and print the source without constructing a client:
   `<PY> -c "import sys,inspect; sys.path.insert(0,r'C:\living-portraits'); import midjourney, midjourney.api as a; print(midjourney.__file__, getattr(midjourney,'__version__',None)); [print(inspect.getsource(getattr(a.MidjourneyAPIClient,m))) for m in ('__init__','submit_imagine','submit_video','upload_image','job_status')]; print(inspect.getsource(a.cdn_variant_url))"`
4. `powershell -NoProfile -Command "Get-ChildItem C:\living-portraits\midjourney -Recurse -Filter *.py | Select-String -Pattern 'submit-jobs','imagePrompts','imageReferences','characterReferences','videoType','newPrompt','--end','relaxed','firebase','impersonate'"`
5. Provenance:
   - `type C:\living-portraits\DEPLOYED.json | findstr /i midjourney` gives the life-repo SHA [7].
   - Look for LICENSE, README or pyproject files under `midjourney\`.
   - Run `git -C C:\living-portraits\midjourney log -3` only if `midjourney\.git` exists.
6. `<PY> -m pip show -f midjourney midjourney-py curl_cffi` and `<PY> -m pip freeze | findstr /i "midjourney curl"`. A site-packages `midjourney` could be the empty 0.0.1 or `midjourney-py`; neither has `midjourney.api`.
7. Which backend is live:
   - `findstr /n "BACKEND = " C:\living-portraits\pipeline\autogen.py`
   - `dir C:\living-portraits\pipeline\hf_gen.py`
   - `echo %LP_GEN_BACKEND%`
   - `powershell -NoProfile -Command "Get-Content C:\living-portraits\data\mind\gen_events.jsonl -Tail 50"`
8. In the private monorepo (ask the maintainer): `git log --follow --format="%H %ad %an %s" -- <project>/midjourney/api.py`, and look for `kernel/midjourney`.

### Caveats
- GitHub code search only indexes public default branches. A private repo cannot be ruled out.
- All web-API wire-format details are secondary. See do_not_quote.
- The "4 successes since" figure is from a document headed "Written 2026-08-09" [8].

### Commands run by the reconciler
- Local: `sed` of autogen.py (:20-45, :70-100, :195-240, :300-440); `grep` of MODEL_STACK.md, AUTONOMY.md and prompts; `git log -- pipeline/autogen.py`; `git show 1e1db3a:pipeline/autogen.py`.
- Local search, no match: `perl -e 'alarm 240; exec @ARGV' grep -rl --include='*.py' --exclude-dir=node_modules --exclude-dir=.git -E 'class MidjourneyAPIClient|def cdn_variant_url' <local checkouts>`.
- Local environments: no `midjourney` package in any local Python environment (a `find` for site-packages/midjourney* found nothing), and `import midjourney` gives ModuleNotFoundError.
- GitHub: `gh search code` for MidjourneyAPIClient, cdn_variant_url, MidjourneyAPIAuthError, "from midjourney.api import", and split-term `curl_cffi midjourney`, `submit-jobs midjourney` and `submit_video end_image`; `--owner Wenjix` / `--owner Immersive-commons midjourney`.
- GitHub repos: `gh repo list` for Wenjix, RayyanZahid and Immersive-commons; no public copy of the private monorepo exists; upstream files at 5efea6c; repo metadata.
- PyPI: `curl pypi.org/pypi/<8 names>/json`; `uv run --with pip python -m pip download --no-deps` of midjourney 0.0.1 and midjourney-py 1.0.4, then `unzip -l`.
- Midjourney docs: `curl docs.midjourney.com/api/v2/help_center/en-us/articles/<id>.json` for 13 articles.
- Midjourney updates: `updates.midjourney.com/sitemap-posts.xml` plus all 42 posts since 2025-07-01, grepped for API and automation terms.
- Wayback `id_` snapshots of the ToS (20250214070946, 20260511094840, 20260618022947) and Community Guidelines (20250214070946).
- Scratch files: `<session scratch, not kept>/mj6-reconcile/`.

## Sources
[1] FIRST-PARTY · commit 7d9cc26 (2026-09-23) · pipeline/autogen.py — Client fingerprint: L211 'from midjourney.api import MidjourneyAPIClient   # lazy: only present on hil'; L26-27 'the dev box has no vendored midjourney/'; L320 cdn_variant_url; L324 upload_image(...)["shortUrl"]; L327 prompt + ' --oref %s --ow %d --v %s'; L330 submit_imagine(prompt, mode=IMAGINE_MODE); L341 submit_video(image_url=, end_image=, motion_prompt=, loop=, mode=); L225 job_status([job_id]); L399 client._session.get; L433 download_video; L79-81 v8.1 error quote; L90-92 relax->relaxed comment
[2] FIRST-PARTY · Verified as of 2026-09-10 (committed 7d9cc26) · MODEL_STACK.md — L14 'Live path'; L27 '| **Midjourney V7** | ... | every pose still and every transition clip |'; L38 'The shipped 59-node / 500-edge graph is **Midjourney footage**'; L210 'third-party, **not vendored, not in any requirements file**'
[3] FIRST-PARTY · commit 7d9cc26 · AUTONOMY.md — L153 'MJ session + deps (`midjourney/` client, `curl_cffi`,'
[4] FIRST-PARTY · commit 7d9cc26 · prompts/idle_animations.json — 'MJ omni-ref + start/end-loop video flow (kernel.midjourney.generate_video)' (origin hint, inference only)
[5] FIRST-PARTY · 1e1db3a 2026-07-11; 691336f 2026-09-10 · this repo (git log -- pipeline/autogen.py; git show 1e1db3a:pipeline/autogen.py) — Local autogen lineage (RayyanZahid initial 2026-07-11); 1e1db3a L345-351 '# 3. REVERSE transition new -> hub -- its OWN generated clip' with submit_video(image_url=new_url, end_image=hub_url; no hf_gen.py locally
[6] FIRST-PARTY · repo commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/scripts/release.py — L4 'The project lives INSIDE the life monorepo'; L8 'Midjourney path that now 403s on every call'; L49-50 '"sessions",    # auth' / '"midjourney",  # vendored client'
[7] FIRST-PARTY · repo commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/scripts/deploy_hil.py — L50 REMOTE 'C:/living-portraits'; L17 'Writes `DEPLOYED.json` on the host recording the life-repo SHA'; L22 'The host tree is NOT a clone of this monorepo'; L56-57 EXCLUDE_DIRS lacks 'midjourney'; L169-171 host .gitignore adds 'midjourney/' and 'sessions/'; L117 .venv python used for remote hashing
[8] FIRST-PARTY · header 'Written 2026-08-09'; repo commit 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/ARCHITECTURE.md — L51-52 'retired but intact ... HTTP 403 on every image upload since 2026-07-02. Higgsfield replaced it on 2026-08-08'; L438-441 '886 failures reading `POST /api/storage-upload-file -> 403`' and '4 successes since'; L266 lp-gen 'pythonw pipeline\autogen.py generate --auto --limit 1'; L469-473 hil graph 257/1462, local 59/500 stale; L537 'MidjourneyAPIAuthError: missing firebase.api_key or firebase.refresh_token' / 'sessions/midjourney.json'
[9] FIRST-PARTY · 0.2.0 — 2026-08-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/CHANGELOG.md — L509 'Generation moved from Midjourney to Higgsfield'; L510 'Midjourney could only animate forward from a single still'; L515 'The old path faked the return by playing the forward clip backwards'; 'MidjourneyAPIAuthError: POST /api/storage-upload-file -> 403'; L549 'its session is dead'
[10] FIRST-PARTY · repo commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/pipeline/autogen.py — L86-90 'BACKEND: "hf" = Higgsfield ... the default since 2026-08-09. "mj" = the original Midjourney path, RETIRED but deliberately kept intact' ; BACKEND = os.environ.get("LP_GEN_BACKEND", "hf")
[11] FIRST-PARTY · repo commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/install/ENVIRONMENT.md — L56 '| `LP_GEN_BACKEND` | `hf` | `hf` = Higgsfield (production), `mj` = the retired Midjourney path |'
[12] FIRST-PARTY · repo commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/pipeline/hf_gen.py — L43-44 STILL_MODEL = "gpt_image_2", CLIP_MODEL = "kling3_0"; L13 'j4me/infra/deploy/hf_proxy/'
[13] FIRST-PARTY · accessed 2026-09-23 · https://api.github.com/repos/Immersive-commons/living-portraits — Immersive-commons: created 2026-07-17, fork:false, Apache-2.0; Wenjix/living-portraits fork:true parent RayyanZahid/living-portraits MIT; RayyanZahid MIT pushed 2026-07-16
[14] FIRST-PARTY · accessed 2026-09-23 · https://github.com/search?q=MidjourneyAPIClient&type=code — Observation (public default branches only): MidjourneyAPIClient / cdn_variant_url / 'from midjourney.api import' / MidjourneyAPIAuthError hits only Immersive-commons/living-portraits plus unrelated projects with different interfaces (PHP, ComfyUI, Ruby/Rust and other helpers)
[15] FIRST-PARTY · accessed 2026-09-23 · https://github.com/leoleelxh/ComfyUI-MidjourneyNode-leoleexh/blob/43c02f2a88eadd4f684d9e34adecf15f35d3ea07/api_client.py — Different interface: start_generation, upscale_or_vary, wait_for_generation, download_image — not our client
[16] FIRST-PARTY · upload 2022-11-29; accessed 2026-09-23 · https://pypi.org/pypi/midjourney/json — midjourney 0.0.1, summary '', author 'Midjourney'; wheel contains only a 0-byte midjourney/__init__.py
[17] FIRST-PARTY · upload 2023-07-09; accessed 2026-09-23 · https://pypi.org/pypi/midjourney-py/json — midjourney-py 1.0.4 installs top-level midjourney/{__init__,decrypt,index,irequest}.py, no api.py; midjourney-client, midjourney-web, pymidjourney return 404
[18] FIRST-PARTY · Version Effective Date: May 27, 2026; edited_at 2026-05-27T23:54:08Z; updated_at 2026-08-17T20:06:41Z · https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service (retrieved via https://docs.midjourney.com/api/v2/help_center/en-us/articles/32083055291277.json) — 'You may not reverse engineer the Services or the Assets. You may not use automated tools to access, interact with, or generate Assets through the Services.'; 'Only one user may use the Services per registered account.'; 'suspend or ban Your access to the Services at any time, and for any reason'; §11 Editor/Video 'suspend or ban your access to them at any time, and for any reason'; §8 'terminate Your access ... Any violation of Community Guidelines is a breach of this Agreement. You will not be refunded'; §7 'rate limit You'; 'Please do not create any dependencies'; $1,000,000 Pro/Mega ownership rule; all 5 'notice' occurrences within §5 DMCA
[19] FIRST-PARTY · edited_at 2025-12-05; updated_at 2026-08-17 · https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines (via /api/v2/help_center/en-us/articles/32013696484109.json) — 'Unauthorized automation and third party apps are not allowed'; 'With a few rare exceptions that are explicitly granted, Midjourney does not provide an API, nor provide third-party apps or scripts, and automating interactions with Midjourney service is strictly prohibited'; 'Accounts who do not comply with these rules may be blocked'; 'this includes sharing your account'; 'may be warned by a community moderator, given a time-out, or be blocked'
[20] FIRST-PARTY · snapshot 2025-02-14 · https://web.archive.org/web/20250214070946id_/https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — 'Version Effective Date: February 5, 2025' with identical automated-tools, reverse-engineer, one-user and suspend/ban clauses
[21] FIRST-PARTY · snapshot 2026-05-11 · https://web.archive.org/web/20260511094840id_/https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — 'Version Effective Date: February 12, 2026' with identical clauses
[22] FIRST-PARTY · snapshot 2025-02-14 · https://web.archive.org/web/20250214070946id_/https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines — 'does not provide an API, nor provide third-party apps or scripts, and automating interactions with Midjourney service is strictly prohibited'
[23] FIRST-PARTY · published 2025-07-16 · https://updates.midjourney.com/enterprise-api-survey/ — 'We're starting to investigate opening up an Enterprise API for people to start integrating Midjourney into their companies and services.'
[24] FIRST-PARTY · accessed 2026-09-23 (newest lastmod 2026-09-24T01:59:23Z) · https://updates.midjourney.com/sitemap-posts.xml — 92 posts; 42 with lastmod >= 2025-07-01; only API-related slug is enterprise-api-survey; full-text grep of the other 41 found no API/automation announcement
[25] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/27870607078285-Group-Plans-Corporate-Billing — 'Please note that we do not offer the following: Seat or admin management Terms and policy negotiations SSO logins'
[26] FIRST-PARTY · updated 2026-09-17 · https://docs.midjourney.com/hc/en-us/articles/25386088618253-Requesting-a-Refund — 'Refund eligibility does not apply if your account is suspended or terminated due to a violation of our Terms of Service or Community Guidelines'
[27] FIRST-PARTY · updated 2026-03-25 · https://docs.midjourney.com/hc/en-us/articles/27870375276557-Using-Images-Videos-Commercially — 'you own all the images and videos you create, even if you decide to cancel your subscription'
[28] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference — 'You can only use one image with Omni Reference.'; 'Omni Reference can only be used with Midjourney version 7.'; --ow 'between 1 and 1,000, with the default being --ow 100'; 'When using V8.X, use the Edit Model instead'; 'can be combined with Style References and Image Prompts'; 'cost 2x more GPU time'; 'not compatible with Fast Mode'; '--oref' syntax documented 'in Discord'; 'Anyone attempting to violate our Community Guidelines will face suspension or banning without refund.'
[29] FIRST-PARTY · updated 2026-09-04 · https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model — 'up to 4 reference images (replacing Omni Reference and Character Reference)'; 'compatible with Midjourney versions 8.1 and 8.2'; 'To use the Edit model in Discord ... --edit ... separate each URL with a space'; web: 'Attach to prompt ... up to four images'
[30] FIRST-PARTY · updated 2026-08-31 · https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts — 'To use Image Prompts in Discord, paste your image URL at the beginning of your text prompt. If you want to use multiple images, separate each URL with a space.'; web: 'You can even select multiple images to use in your prompt!'
[31] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference — 'compatible with Midjourney versions 6 and later'; 'To use a Style Reference in Discord ... --sref ... separate each URL with a space'
[32] FIRST-PARTY · updated 2026-08-31 · https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video — 'only compatible with video-specific parameters: --motion low , --motion high , --raw , --loop , --end , and --bs #'; --end/--loop prompt syntax under the 'In Discord' tab, web uses 'Ending Frame section'; 'Other Image Reference Types (not compatible with video generations)'; 'only Pro and Mega plans can generate videos in Relax Mode (SD resolution only)'; 'generate 4 videos from each video prompt'
[33] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — '(replaced by the Edit Model in V8.X) --oref'; '--edit' up to four reference images; '--loop' / '--end'; string '--ow' absent (0 occurrences)
[34] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — 'Character Reference is a feature compatible with Midjourney and Niji version 6 ... replaced by Omni Reference in V7, and the Edit Model in V8.X.'
[35] FIRST-PARTY · updated 2026-09-01 · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — 'V8.2 released as the default version on July 24, 2026 ... Edit Model, which replaces Omni Reference'; 'V8.1 ... default version from June 10 to July 23, 2026'; 'V7 ... default version from June 17, 2025 to June 9, 2026'
[36] FIRST-PARTY · published 2026-06-11 · https://updates.midjourney.com/v8-1-is-now-the-default-model/ — 'Note: V7 omni-reference is available to use while we finish training the improved version for V8'
[37] FIRST-PARTY · published 2026-08-27 · https://updates.midjourney.com/edit-model-for-v8/ — '(replacing omni-reference) with up to 4 image references at once'; 'Drag images into the prompt bar under "attach to prompt" ... Type --edit url... on Discord'
[38] FIRST-PARTY · published 2026-01-20 · https://updates.midjourney.com/web-updates-4/ — 'Automatically strip irrelevant parameters (--cw/--ow) when cref/oref not present' (weak hint only)
[39] FIRST-PARTY · published 2025-07-25 · https://updates.midjourney.com/looping-and-end-frame-for-video-video-in-the-discord-bot/ — 'To set an end frame, use --end image_url'; 'enter the image url at the start of the prompt and use the --video arg' (Discord bot)
[40] FIRST-PARTY · published 2026-08-21 · https://updates.midjourney.com/changelog-8-20-26/ — 'we launched a very rough draft of some big changes to alpha.midjourney.com'
[41] FIRST-PARTY · published 2026-09-24T01:59Z · https://updates.midjourney.com/alpha-changelog-9-23-26/ — 'DEFAULT PARAMETERS ... Settings → Advanced → Your defaults'
[42] FIRST-PARTY · snapshot 2026-06-18 · https://web.archive.org/web/20260618022947id_/https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service — First archived copy showing 'Version Effective Date: May 27, 2026' with same clauses
[43] secondary · file commit a018047 2026-06-30 · https://github.com/remorses/egaki/blob/main/midjourney/src/midjourney.ts — SECONDARY ONLY (no license): reverse-engineered /api/submit-jobs shape (prompt string + metadata counters; video videoType 'vid_1.1_i2v_start_end_480'); runs inside a browser page. Not used for any answer claim.
[44] secondary · file commit 7b9bc5a 2026-06-08 · https://github.com/WilliamJizh/midjourney-mcp-web/blob/main/src/midjourney_mcp_web/server.py — SECONDARY ONLY (GPL-3.0): curl_cffi impersonate='chrome', /api/submit-jobs, success[0].job_id. Not used for any answer claim.
[45] secondary · accessed 2026-09-23 · https://github.com/bucagdas/midjourney-unofficial-api/blob/HEAD/scripts/mj_client.py — SECONDARY ONLY (MIT): claims metadata counters are optional for URL refs; uses videoType 'vid_1.1_i2v_480' and f.mode 'relax'. Not used for any answer claim.
[46] secondary · accessed 2026-09-23 · https://github.com/jackwener/OpenCLI/blob/main/clis/midjourney/generate.js — SECONDARY ONLY (Apache-2.0): browser-driven adapter; one omni ref, auto-routes to V7 (generate.js:87; capabilities.js:342). Not used for any answer claim.
[47] secondary · accessed 2026-09-23 · https://github.com/JuyeongYi/jylee_claude_marketplace/blob/HEAD/midjourney-api-dev/skills/midjourney-low-level-api/references/api-reference.md — SECONDARY ONLY: docs for a different Python MJ web client (MidjourneyAPI, curl_cffi Session, Firebase auth, storage-upload-file -> {shortUrl,bucketPathname}); does client-side param validation. Not a fingerprint match.

## Contradictions (first-party vs first-party — unresolved)
- #1 (first-party vs first-party; STOP, not resolved). Upstream https://github.com/Immersive-commons/living-portraits/blob/5efea6c6a85c60c631d88f35f4b854136b1c77dd/ARCHITECTURE.md L51-52 says: 'The Midjourney generation path is **retired but intact**. It has been returning HTTP 403 on every image upload since 2026-07-02. Higgsfield replaced it on 2026-08-08.' The same file (L472) says 'Local `data/` is also stale (59 nodes / 500 edges vs hil's 257 / 1462)'. Other upstream sources agree: CHANGELOG.md 0.2.0 ('its session is dead'), pipeline/autogen.py L90 `BACKEND = os.environ.get("LP_GEN_BACKEND", "hf")`, and install/ENVIRONMENT.md L56 ('`hf` = Higgsfield (production), `mj` = the retired Midjourney path'). Against that, local MODEL_STACK.md (verified 2026-09-10) L14/L27 lists '**Midjourney V7**' under 'Live path — a change here shows up on the wall' for 'every pose still and every transition clip', and L38 says 'The shipped 59-node / 500-edge graph is **Midjourney footage**'. Context only, not a resolution: the local autogen.py comes from 1e1db3a (RayyanZahid, 2026-07-11) plus 691336f (2026-09-10), and the local tree has no hf_gen.py.
- #2 (first-party project doc vs first-party vendor doc and project code). Upstream CHANGELOG.md 0.2.0 says 'Midjourney could only animate forward from a single still' and 'The old path faked the return by playing the forward clip backwards'. Midjourney's Video doc (https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video, updated 2026-08-31) documents a custom ending frame ('add the --end parameter to your video prompt and paste your image URL'). The update post of 2025-07-25 says 'To set an end frame, use --end image_url'. The project's own code at 1e1db3a (2026-07-11), pipeline/autogen.py L345-351, renders a real reverse clip with submit_video(image_url=new_url, end_image=hub_url). The local code also still contains a _reverse_gif helper ('the forward clip played backwards'). Not resolved.
- #3 (first-party project docs, wording). Local MODEL_STACK.md L210 says the client is 'third-party, **not vendored, not in any requirements file**'. Local autogen.py L26-27 says '(the dev box has no vendored midjourney/)', and upstream scripts/release.py L50 says '"midjourney",  # vendored client'. One plausible reading is 'vendored on hil and in the private monorepo, not in this public fork', but that reading is not confirmed. Whether the client is third-party or self-written is unknown.
- #4 (licensing, for the license track; not a factual conflict about one artifact). RayyanZahid/living-portraits and the local Wenjix fork are MIT. Immersive-commons/living-portraits is Apache-2.0 per the GitHub API and its LICENSE file.

## Could not confirm
- Identity, repo URL, author, license and last-commit date of the vendored midjourney/ client. It is excluded from every public repo and is not on PyPI, in GitHub code search, or on this Mac.
- Whether midjourney.api submit_imagine forwards the prompt string unchanged, or parses reference flags into structured fields or metadata counters.
- Whether Midjourney's web API (/api/submit-jobs) accepts several reference URLs as prompt text. Midjourney documents multi-URL prompt syntax only 'in Discord'.
- How midjourney.api submit_video puts start and end frames on the wire, as prompt text with --end or as structured fields, and which videoType it sends.
- The cause of the 403 on POST /api/storage-upload-file since 2026-07-02 (expired session, plan change, endpoint change, or account-level block). Upstream says it did not determine the cause.
- Whether the hil Midjourney account is suspended or banned.
- Which backend hil runs today (hf or mj), and whether the live graph already mixes Higgsfield (gpt_image_2 / kling3_0) and Midjourney footage.
- Which Python interpreter the lp-gen task uses today. Upstream listed bare 'pythonw' as of 2026-08-09.
- Whether Midjourney privately granted an API or automation exception to this account. The Community Guidelines allow 'a few rare exceptions that are explicitly granted'.
- The hil account's plan tier. Relax-mode video requires Pro or Mega.
- Whether the account holder or Immersive Commons crosses the ToS threshold of $1,000,000 a year in revenue.
- Whether asset ownership survives a ban. The docs cover cancellation only.
- Whether the alpha site's account-level 'Your defaults' (2026-09-23) apply to jobs submitted through the web API.
- A private or unindexed GitHub repo holding the client cannot be ruled out. Code search indexes public default branches only.

## Dropped claims (refuted or unsupported in verification)
- c27 as worded: 'Midjourney's server could only produce that if it received --oref/--v inside the prompt string'. Contradicted: --v was the account default at failure time. It is replaced by the weaker first-party fact that autogen.py passes references only inside the prompt argument.
- c28 (egaki wire format: submit-jobs metadata counters, videoType 'vid_1.1_i2v_start_end_480', newPrompt with --end): secondary only, moved to do_not_quote.
- c29 (WilliamJizh curl_cffi client and success[0].job_id shape): secondary only, moved to do_not_quote.
- c30 (Cloudflare bot protection on cdn.midjourney.com): secondary only and not re-observed by the reconciler, moved to do_not_quote.
- c31 (OpenCLI: one omni ref, auto-routes to V7): secondary only, and the quote was misattributed to capabilities.js instead of generate.js:87.
- c21/c22/c23 as worded ('accept multiple images as prompt text' with no qualifier). Corrected: Midjourney documents the prompt-text multi-URL syntax only 'in Discord'.
- Researcher answer §5: 'A site-packages midjourney would be the empty PyPI placeholder'. Contradicted: midjourney-py 1.0.4 also installs a top-level midjourney package.
- Researcher commands_run '0 hits' for split-term searches ('curl_cffi midjourney', 'submit-jobs midjourney', 'submit_video end_image', 'shortUrl upload_image midjourney'). Wrong: the searches ran as phrase searches because the terms were not split. Rerun split, they return many hits, none of which matches the fingerprint.
- Researcher could_not_confirm 'Wayback returned no snapshots / earlier ToS versions unknown'. Superseded: snapshots show the same clauses in the ToS versions effective Feb 5, 2025 and Feb 12, 2026.
- c1 line citations autogen.py 405-406. Corrected to :399 (client._session.get) and :433 (client.download_video).
- c29 commit SHA 8574856 given as the file commit. The file's last commit is 7b9bc5a; 8574856 is the repo HEAD.
- Researcher hil commands that assume C:\living-portraits\.venv\Scripts\python.exe runs autogen. Unverified; replaced with a step that resolves the interpreter first.

## DO NOT QUOTE (low/unknown)
- [unknown] Any identity, repo URL, author, license or commit date for the midjourney.api client — Not found in any public or local source. It is private and vendored.
- [unknown] 'midjourney.api passes the prompt string to Midjourney unchanged', or 'passes any reference flag, including several URLs, through' — The only first-party evidence is that autogen.py puts --oref/--ow/--v into the prompt argument. The client's own code is unreadable.
- [low] 'The v8.1 error proves Midjourney's server parsed --oref from the prompt text' (researcher claim c27) — The error named --version 8.1 while the version came from the account default, not the prompt. The error could also come from client-side validation.
- [unknown] 'Midjourney's web API accepts several image-prompt, --sref or --edit URLs as prompt text' — Midjourney documents that syntax only 'in Discord'. The web uses UI slots.
- [low] Web wire format: POST /api/submit-jobs; metadata counters imagePrompts/imageReferences/characterReferences/depthReferences; t:'imagine'/'video'; newPrompt; bucketPathname; /api/job-status — Secondary reverse engineering only (egaki, WilliamJizh, bucagdas, JuyeongYi). Midjourney does not document it.
- [low] videoType value 'vid_1.1_i2v_start_end_480' (or 'vid_1.1_i2v_480') — Secondary only, and the secondary sources disagree with each other.
- [low] 'Metadata reference counters are cosmetic when the reference is a URL' — A single secondary claim (bucagdas), not confirmed first-party.
- [low] 'cdn.midjourney.com / midjourney.com sit behind Cloudflare bot protection, which is why curl_cffi is needed' — Secondary (egaki AGENTS.md) plus one verifier's curl observation, which the reconciler did not re-check.
- [low] 'Midjourney's wire value for relax mode is "relaxed"' — Only the project's own comment (autogen.py L90-92) supports it. A secondary client sends 'relax'. No Midjourney source.
- [low] 'The client comes from kernel/midjourney in the private monorepo' — Inferred from one prompt note, 'kernel.midjourney.generate_video'.
- [low] 'deploy_hil.py ships midjourney/ to hil' — Inferred from 'midjourney' missing from EXCLUDE_DIRS. Only the host .gitignore entry is explicit.
- [unknown] 'hil runs Midjourney V7 today' or 'hil runs Higgsfield today' — First-party sources contradict each other (contradiction #1).
- [unknown] 'hil's graph is 257 nodes / 1462 edges' presented as current — From an upstream doc headed 'Written 2026-08-09'. It contradicts local MODEL_STACK.md and is not re-checked on hil.
- [unknown] '4 Higgsfield successes since the cutover' presented as a current count — The count is as of about 2026-08-09, not today.
- [unknown] Cause of the 403s since 2026-07-02, including 'the account was banned' — Upstream says it did not determine the cause.
- [unknown] 'lp-gen runs C:\living-portraits\.venv\Scripts\python.exe' — Upstream lists bare 'pythonw' (as of 2026-08-09). The interpreter must be resolved on hil.
- [low] 'A site-packages midjourney on hil must be the empty PyPI placeholder' — midjourney-py 1.0.4 also installs a top-level midjourney package.
- [low] '--ow is deprecated or removed' — It is missing from the Parameter List but still documented in the Omni Reference article (1–1,000, default 100).
- [low] Prior-sweep wording that the Omni Reference doc says 'not supported in V8.2' — That phrase is not in the current article (updated 2026-09-01). Today's text reads 'can only be used with Midjourney version 7' and 'When using V8.X, use the Edit Model instead'.
- [low] Upstream CHANGELOG claims 'Midjourney could only animate forward from a single still' / 'the old path faked the return' — Contradicted by the Midjourney Video doc (--end) and by the project's own 2026-07-11 code (contradiction #2).
- [low] 'API keys are restricted to the Midjourney Enterprise dashboard' (WebSearch/SEO summaries) — No first-party source. Midjourney's only API post is the 2025-07-16 survey.
- [unknown] Any claim that Midjourney granted this project an API or automation exception — No evidence either way.
- [unknown] 'The web UI's multi-image picker equals multi-reference support in the web API' — The UI statement does not establish API behaviour.
- [low] web-updates-4 'strip irrelevant parameters (--cw/--ow)' presented as proof of the web API wire format — It only hints that the web app handles these as prompt parameters.
- [unknown] 'No private repo holds the client' — GitHub code search indexes public default branches only.


---

# Track A — sherpa-onnx per-phoneme durations / alignments (lip-sync without GPL)
Primary mission track: no · Final confidence: high

## Answer
## Verdict (track A)

**sherpa-onnx: NO.** The latest release, v1.13.8 (published 2026-09-10; there is no v2.x tag), returns no per-phoneme, per-token or per-character durations or alignments from TTS, for any model [1]. This applies to Piper/VITS voices too.

**Durations for the same voices: YES, but not through sherpa-onnx.** Two tensors already exist inside the ONNX graphs and can be read directly with onnxruntime (MIT):
- **Piper:** the internal `/Ceil_output_0` (w_ceil) tensor.
- **Kokoro:** sherpa's Kokoro export already has a second, per-token durations output.

**BLOCKER (unresolved, first-party contradiction; see Contradictions).** The two Piper voices tts.py names, `en_GB-alan-medium` and `en_GB-jenny_dioco-medium`, are both "Finetuned from U.S. English lessac voice". The lessac dataset licence is research-only and excludes commercial voice synthesis [28][29][30][33]. The piper-voices repo says `license: mit` [27]. I report both sides and stop, as the standards require. Route A below therefore cannot be recommended for these two voices until this is resolved. Route C (Kokoro, Apache-2.0 weights) has no such conflict.

### sherpa-onnx API surface (v1.13.8, re-checked at the tag)
- **C++:** `struct GeneratedAudio { std::vector<float> samples; int32_t sample_rate; GeneratedAudio ScaleSilence(float) const; }`. No other fields [2].
- **Python:** only `.def_readwrite("samples")` and `("sample_rate")` [3].
- **C API:** `SherpaOnnxGeneratedAudio { const float *samples; int32_t n; int32_t sample_rate; }` [4].
- **Only timing hook:** `GeneratedAudioCallback(samples, n, progress)`. It is called once every `max_num_sentences` sentences, and the default is `max_num_sentences = 1`, so timing is sentence-level at best [2].
- **Model code:** the VITS/Piper and Kokoro paths call `GetOutputNames(...)`, run every graph output, then `return std::move(out[0]);`. Any durations output is computed and discarded [5][6].
- **Empirical test (sherpa-onnx 1.13.8):**
  - `GeneratedAudio` public attributes are `['sample_rate','samples']`.
  - The callback delivered one chunk per sentence.
  - A voice patched to expose `/Ceil_output_0` loads, but the durations are still unreachable [7].
- **Upstream status:**
  - Feature requests #3705 (2026-06-26) and #3727 are open, with no implementing PR.
  - On 2026-07-07 the maintainer wrote: "We don't currently have plans to support this. Instead, we are focusing on an HMM/GMM-based approach" [8][9].
  - The CHANGELOG has no TTS timestamp or duration feature. The only TTS "duration" entry is pause scaling (#1820), and "Whisper timestamps" is ASR [10].
  - Forced alignment request #3536 is open [11].
  - The `timestamps` and `durations` fields in the C API belong to `SherpaOnnxOfflineRecognizerResult` (ASR) only [4].
- **Planned 2.0.0:** issue #3731 adds `std::vector<std::vector<std::string>> tokens;` to `GenerationConfig` so users can supply their own phonemes. It adds no durations. It is still open, with no milestone [15].

### The premise also fails: sherpa-onnx is not GPL-free for Piper today
- **Build:** `SHERPA_ONNX_ENABLE_TTS` defaults to ON. It pulls in `include(espeak-ng-for-piper)` and `include(piper-phonemize)`, links `piper_phonemize` into `sherpa-onnx-core`, and `piper-phonemize-lexicon.cc` includes `espeak-ng/speak_lib.h` [12]. espeak-ng is GPL-3.0-or-later [13].
- **Linux core wheel:** the `sherpa-onnx-core` 1.13.8 manylinux wheel declares `License: Apache-2.0`, but its `libsherpa-onnx-c-api.so` contains espeak symbols [14].
- **macOS wheel (re-checked today):** `sherpa_onnx-1.13.8-cp311-macosx_11_0_arm64` `_sherpa_onnx.cpython-311-darwin.so` exports 50 `espeak_*` symbols (for example `T _espeak_Cancel`). Its METADATA says "Apache licensed" [7].
- **Maintainer's position:** espeak-ng's GPL "introduces license constraints that are incompatible with the Apache-2.0 license of sherpa-onnx". The fix is planned as "sherpa-onnx 2.0.0" [15]. His current advice is `-DSHERPA_ONNX_ENABLE_TTS=OFF` (which removes TTS) or waiting for #3731 [16].
- **Lexicon mode doesn't fix it:** a Piper model given a lexicon and no `data_dir` uses the `Lexicon` frontend and never calls espeak at runtime, but the shipped binary still contains espeak-ng [51].

### Stock rhasspy/piper-voices graphs: no durations output, but the tensor is inside
- **`en_GB-alan-medium.onnx`** (sha256 `0a309668…3330`, 63,201,294 bytes, producer pytorch 2.0.0, opset 15; re-downloaded today) [17]:
  - Inputs: `input` INT64 `[batch_size, phonemes]`, `input_lengths` INT64 `[batch_size]`, `scales` FLOAT `[3]`.
  - Outputs: `output` FLOAT `[batch_size, time, 1, Unsqueezeoutput_dim_3]` only.
  - Exactly one Ceil node: `/Ceil` (input `/Mul_1_output_0`) → **`/Ceil_output_0`**.
- **Config** [18]: `sample_rate 22050`, `espeak.voice en-gb-x-rp`, `phoneme_type espeak`, `noise_w 0.8`.
- **Other voices:** `en_GB-jenny_dioco-medium` has the same single output plus `/Ceil`. `lt_LT-reginute1-medium` (pytorch 2.11.0 export) also has only `output` plus `/Ceil` [19].
- **sherpa's repackaged Piper model:** only its metadata is rewritten ("Add meta data to an ONNX model"). The graph is still single-output [20].
- **Reproduced today:**
  - Method: append `/Ceil_output_0` as a graph output (onnx 1.23.0), then run it with onnxruntime 1.30.0.
  - Input: hand-written IPA `həlˈəʊ wˈɜːld.`, with no espeak. That gave 31 phoneme IDs, laid out as `[1,0,id,0,…,2]`.
  - Output: w_ceil shape `(1,1,31)` float32.
  - With `noise_w=0`: 96 frames → 24,576 samples.
  - With `noise_w=0.8`: 99 frames → 25,344 samples. The durations are stochastic unless `noise_w=0`.
  - Both give **256 samples/frame**, about 11.6 ms at 22050 Hz [17].
  - Piper's own code does the same: `DEFAULT_HOP_LENGTH: Final = 256` and `phoneme_id_samples = result[1] * hop_length` [26].
- **piper-tts (piper1-gpl, GPL-3.0) gets alignments the same way, not from a special export:**
  - "you must first 'patch' a voice's ONNX model file" [21]. The patch does "Mark the model's w_ceil (Ceil) tensor as a graph output." [22]
  - "Patched ONNX models should still work fine with existing Piper installations" [21].
  - The exporter still uses `output_names=["output"]`, and PLANS.md says "all of the existing voices need to be patched" [23].
- **piper-tts versions:**
  - CHANGELOG 1.3.1: "Add experimental support for alignments". 1.3.1 is not on PyPI.
  - PyPI 1.4.0 (2026-01-30) already has `include_alignments`.
  - 1.5.0 (2026-07-17): "Add in-memory patching for alignments".
  - The latest is 1.8.0 (2026-09-04). The PyPI `license` field is `GPL-3.0-or-later` [24][25].
- **piper-tts API fields:** `PhonemeAlignment(phoneme, phoneme_ids, num_samples)`, and `AudioChunk.phoneme_id_samples` / `phoneme_alignments` [26]. libpiper's C struct `piper_audio_chunk` has `alignments` / `num_alignments` [21].

### Routes that DO give durations (licenses; does it link espeak-ng?)
| Route | What you get | Licenses / espeak-ng |
|---|---|---|
| **A. Stock Piper `.onnx` + your own graph patch (expose `/Ceil_output_0`) + onnxruntime** | Frames per phoneme ID × 256 = samples, exact by construction [17][26]. The phoneme-ID layout must be exactly `[1,0,id1,0,…,2]` [21]; sherpa itself shipped this wrong until #3721 was closed on 2026-07-27 [52]. | onnx Apache-2.0 [46], onnxruntime MIT [45]. Write the patch yourself; piper1-gpl's patch script is GPL-3.0 [22]. **G2P:** the voices expect espeak `en-gb-x-rp` IPA [18]. Options: (i) espeak-ng as a separate process (GPL-3.0, not linked) [13]; (ii) OpenPhonemizer, which is BSD-3-Clause-Clear, "Alpha", English only, "no longer being maintained", archived, and warns of LGPL dependencies [47]; (iii) pre-computed IPA for fixed lines. **Voice license: BLOCKED for alan and jenny** (see Contradictions). |
| **B. Kokoro Python `KPipeline`** (tts.py's `bm_george` / `bf_emma`) | `KPipeline.Result.tokens: List[misaki MToken]`, each with **`start_ts` / `end_ts`** (seconds, word level, English lang `a`/`b` only), plus `Result.pred_dur` (LongTensor frames; "Multiply by 600 to go from pred_dur frames to sample_rate 24000", i.e. 25 ms/frame) [36][38]. Present from **kokoro 0.7.0** (2025-02-04), absent in 0.3.5; latest is 0.9.4 (2025-04-05) [37]. | kokoro and misaki are Apache-2.0 [37][38]. **Loads GPL espeak-ng in-process:** `pipeline.py` does `from misaki import en, espeak`, and for lang a/b builds `espeak.EspeakFallback`. `misaki.espeak` imports `phonemizer` (phonemizer-fork 3.3.2, GPLv3+) and `espeakng_loader` (0.2.4; PyPI license metadata empty; the wheel bundles `libespeak-ng.1.52.0.dylib`) [36][39][40]. |
| **C. sherpa's Kokoro int8 graph run directly with onnxruntime + the bundled `lexicon-gb-en.txt`** (no sherpa-onnx, no misaki, no espeak) | `model.int8.onnx` has a second output, `onnx::Shape_3411` INT64, with one duration per token ID. **Reproduced today:** `hello world` via `lexicon-gb-en.txt` + `tokens.txt`, voice `bm_george` (sid 26) → 14 IDs, durations sum to 72 frames × 600 = 43,200 samples exactly [44]. The output exists because kokoro's `KModelForONNX.forward` returns `waveform, duration`, while sherpa's export names only `"audio"` [42][43]. | Weights: hexgrad/Kokoro-82M, `license: apache-2.0` [45]. The graph comes from sherpa's own pipeline, `export_onnx.py` → `add_meta_data.py` → `dynamic_quantization.py` (producer `onnx.quantize 0.1.0`) [41][44]. The bundle's LICENSE is Apache-2.0. `lexicon-gb-en.txt` (191,924 lines) is generated from misaki's `gb_gold.json` / `gb_silver.json` (repo Apache-2.0) [41][38]. Words not in the lexicon have no fallback. Using `misaki.en.G2P` instead needs spacy (MIT) and num2words (LGPL) [50], defaults to `unk='❓'`, and downloads a spaCy model at runtime if it is missing [38]. |
| **D. Forced alignment of the finished audio** (Montreal Forced Aligner) | Word and phone intervals | MFA is MIT, v3.4.2 (2026-08-20); mfa-models is CC-BY-4.0 [48][49]. Transitive dependencies were not checked. sherpa-onnx has no aligner (#3536 is open) [11]. |

**Best-supported option on today's evidence:** route C gives real per-token durations with no GPL code in the process, from Apache-2.0 weights, for the Kokoro voices tts.py already maps (`bm_george` for Phineas/alan, `bf_emma` for jenny). Kokoro-82M's own VOICES.md grades these voices **C** (`bm_george`) and **B-** (`bf_emma`) [45]. Route A is technically equivalent for Piper, but it is blocked on the voice licence.

### Other license notes
- **Kokoro-82M training data:** its card says it was trained on "permissive/non-copyrighted audio", which includes "Synthetic audio generated by closed TTS models from large providers" [45].
- **jenny_dioco dataset:** it also requires attribution: "the voice must be referred to as 'Jenny'", and states "Commercial use is permitted" [34]. That clause does not cure the lessac base-model issue.

## Sources
[1] FIRST-PARTY · 2026-09-10 · https://github.com/k2-fsa/sherpa-onnx/releases/tag/v1.13.8 — Latest release v1.13.8, published 2026-09-10T14:00:23Z; git/matching-refs/tags/v2 is empty (re-checked 2026-09-23)
[2] FIRST-PARTY · v1.13.8 (2026-09-10); accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/csrc/offline-tts.h — "struct GeneratedAudio {\n  std::vector<float> samples;\n  int32_t sample_rate;" ... "GeneratedAudio ScaleSilence(float scale) const;"; "using GeneratedAudioCallback = std::function<int32_t(const float * /*samples*/, int32_t /*n*/, float /*progress*/)>"; "int32_t max_num_sentences = 1;"
[3] FIRST-PARTY · v1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/python/csrc/offline-tts.cc — GeneratedAudio binding: ".def_readwrite(\"samples\", ...)" ".def_readwrite(\"sample_rate\", ...)" only; GenerationConfig fields silence_scale/speed/sid/reference_*/num_steps/extra (no timestamp option)
[4] FIRST-PARTY · v1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/c-api/c-api.h — "typedef struct SherpaOnnxGeneratedAudio { const float *samples; int32_t n; int32_t sample_rate; }"; ASR-only: SherpaOnnxOfflineRecognizerResult "float *timestamps;" "/** Optional token durations in seconds, parallel to @c tokens_arr. */ float *durations;" (ASR fields verified at master 040afe3)
[5] FIRST-PARTY · v1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/csrc/offline-tts-vits-model.cc — L139 "GetOutputNames(sess_.get(), &output_names_, &output_names_ptr_);"; L291 (RunVitsPiperOrCoqui) "return std::move(out[0]);"
[6] FIRST-PARTY · v1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/csrc/offline-tts-kokoro-model.cc — L120 GetOutputNames; L102 "return std::move(out[0]);"
[7] FIRST-PARTY · wheels uploaded 2026-09-10; accessed 2026-09-23 · https://pypi.org/project/sherpa-onnx/1.13.8/ — Empirical (researcher+verifier): GeneratedAudio public attrs ['sample_rate','samples'], one callback chunk per sentence, Ceil-patched Piper still only samples. Empirical (reconciler): sherpa_onnx-1.13.8-cp311-cp311-macosx_11_0_arm64.whl _sherpa_onnx.cpython-311-darwin.so exports 50 espeak_* symbols ("T _espeak_Cancel", "T _espeak_Char", "T _espeak_CompileDictionary"); METADATA "License: Apache licensed, as found in the LICENSE file"
[8] FIRST-PARTY · opened 2026-07-07; maintainer comment 2026-07-07; open as of 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/issues/3727 — "We don't currently have plans to support this. Instead, we are focusing on an HMM/GMM-based approach, which provides a unified framework for both ASR input and TTS output processing."
[9] FIRST-PARTY · 2026-06-26; open · https://github.com/k2-fsa/sherpa-onnx/issues/3705 — Proposal only: "Add optional word-level timestamp support to `OfflineTts::Generate()`"; no implementing PR found
[10] FIRST-PARTY · top entry 1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/master/CHANGELOG.md — No TTS timestamp/duration/alignment entry; "* Support scaling the duration of a pause in TTS. (#1820)"; "* Whisper timestamps (#2945)" (ASR)
[11] FIRST-PARTY · 2026-04-21; open · https://github.com/k2-fsa/sherpa-onnx/issues/3536 — "we prefer not to use CTC for forced alignment. Instead, we prefer to use HMM/GMM like the one in https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner"
[12] FIRST-PARTY · master 040afe3 (2026-09-22); accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/040afe360a38e25daaa325ce8889abf93ea02609/CMakeLists.txt — "option(SHERPA_ONNX_ENABLE_TTS \"Whether to build TTS related code\" ON)"; "if(SHERPA_ONNX_ENABLE_TTS) include(espeak-ng-for-piper) ... include(piper-phonemize)"; csrc/CMakeLists.txt "target_link_libraries(sherpa-onnx-core piper_phonemize)"; piper-phonemize-lexicon.cc "#include \"espeak-ng/speak_lib.h\""; pinned fork csukuangfj/espeak-ng ed530aa (COPYING GPL v3)
[13] FIRST-PARTY · accessed 2026-09-23 · https://github.com/espeak-ng/espeak-ng/blob/master/README.md — "eSpeak NG Text-to-Speech is released under the [GPL version 3](COPYING) or later license."
[14] FIRST-PARTY · wheel 2026-09-10; accessed 2026-09-23 · https://pypi.org/project/sherpa-onnx-core/1.13.8/ — manylinux x86_64 wheel METADATA "License: Apache-2.0"; libsherpa-onnx-c-api.so strings include "espeak_SetVoiceByName", "Wrong version of espeak-ng-data" (researcher+verifier)
[15] FIRST-PARTY · created 2026-07-08; maintainer comment 2026-07-15; open, milestone null (re-checked 2026-09-23) · https://github.com/k2-fsa/sherpa-onnx/issues/3731 — "Since `espeak-ng` is licensed under GPL, it introduces license constraints that are incompatible with the Apache-2.0 license of sherpa-onnx."; "This is a breaking change and will result in a new major release: **sherpa-onnx 2.0.0**."; "We will add a new field to `GenerationConfig`: std::vector<std::vector<std::string>> tokens;"; "a lexicon.txt file will be added to every model directory"
[16] FIRST-PARTY · 2026-09-21; open · https://github.com/k2-fsa/sherpa-onnx/issues/3969 — "Build sherpa-onnx from source by disabling TTS, e.g., pass `-DSHERPA_ONNX_ENABLE_TTS=OFF` to cmake 2. or wait for us to address ... #3731, which removes the GPL dependency eSpeak-NG"
[17] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx — Reconciler re-download: sha256 0a309668932205e762801f1efc2736cd4b0120329622adf62be09e56339d3330, 63201294 bytes; producer pytorch 2.0.0 opset 15; INPUTS input INT64 [batch_size,phonemes], input_lengths INT64 [batch_size], scales FLOAT [3]; OUTPUTS output FLOAT [batch_size,time,1,Unsqueezeoutput_dim_3]; Ceil [('/Ceil',['/Mul_1_output_0'],['/Ceil_output_0'])]; patched run (onnx 1.23.0, ort 1.30.0, IPA 'həlˈəʊ wˈɜːld.', 31 ids): noise_w=0 -> w (1,1,31) sum 96, audio 24576, 256.0 samples/frame; noise_w=0.8 -> sum 99, audio 25344, 256.0
[18] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx.json — {'audio': {'sample_rate': 22050, 'quality': 'medium'}, 'espeak': {'voice': 'en-gb-x-rp'}, 'phoneme_type': 'espeak', 'inference': {'noise_scale': 0.667, 'length_scale': 1, 'noise_w': 0.8}}
[19] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_GB/jenny_dioco/medium — jenny_dioco-medium: OUTPUTS [('output',...)] + /Ceil -> /Ceil_output_0; lt_LT-reginute1-medium (added 2026-09-17, producer pytorch 2.11.0): only 'output' + /Ceil (researcher+verifier)
[20] FIRST-PARTY · accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/040afe360a38e25daaa325ce8889abf93ea02609/scripts/piper/add_meta_data.py — "Add meta data to an ONNX model. It is changed in-place."; packaged vits-piper-en_GB-alan-medium graph still single output 'output', META has_espeak=1
[21] FIRST-PARTY · main 5b355b1 (2026-09-17); accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/docs/ALIGNMENTS.md — "To access alignments, you must first \"patch\" a voice's ONNX model file"; "Patched ONNX models should still work fine with existing Piper installations."; "It looks like [1, 0, id1, 0, id2, 0, ..., 2]"; "`alignments` - array of sample counts whose length is `num_alignments`" (piper_audio_chunk)
[22] FIRST-PARTY · main 5b355b1; accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/src/piper/patch_voice_with_alignment.py — "Mark the model's w_ceil (Ceil) tensor as a graph output."; auto-detects nodes with op_type == "Ceil"; repo license GPL-3.0
[23] FIRST-PARTY · main 5b355b1; accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/docs/PLANS.md — "Experimental [alignment support][ALIGNMENTS.md] has been added. If useful, all of the existing voices need to be patched."; src/piper/train/export_onnx.py L99 output_names=["output"]
[24] FIRST-PARTY · accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/main/CHANGELOG.md — "## 1.3.1 - Add experimental support for alignments"; "## 1.5.0 ... - Add in-memory patching for alignments"; "## 1.3.0 ... - Change license to GPLv3"
[25] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/piper-tts/json — Latest 1.8.0 (2026-09-04T16:47:14); 1.5.0 2026-07-17T20:06:09; 1.4.0 2026-01-30T17:00:01; 1.3.1 absent; license 'GPL-3.0-or-later', license_expression None
[26] FIRST-PARTY · main 5b355b1; accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/src/piper/voice.py — class PhonemeAlignment: phoneme / phoneme_ids / num_samples; AudioChunk phoneme_id_samples, phoneme_alignments; load(..., include_alignments: bool = False); config.py "DEFAULT_HOP_LENGTH: Final = 256"; phoneme_id_samples = result[1] * hop_length
[27] FIRST-PARTY · lastModified 2026-09-17; accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/blob/main/README.md — front matter "license: mit"
[28] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_US/lessac/medium/MODEL_CARD — "* License: https://www.cstr.ed.ac.uk/projects/blizzard/2013/lessac_blizzard2013/license.html"; "Trained from scratch."
[29] FIRST-PARTY · accessed 2026-09-23 · https://www.cstr.ed.ac.uk/projects/blizzard/2013/lessac_blizzard2013/license.html — "3.2 Licensors hereby grant to the User a non-exclusive and non-transferable licence, without the right to sub-licence, to use the Materials exclusively for Research Purposes only throughout the world."; Research Purposes "excludes ... using the Materials for any commercial purpose, including the development, marketing, commercialisation, sale or licencing of voice synthesis ... products or services"
[30] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_GB/alan/medium/MODEL_CARD — "* URL: https://github.com/MycroftAI/mimic3-voices/blob/master/voices/en_UK/apope_low\n* License: See URL"; "Finetuned from U.S. English lessac voice (medium quality)."
[31] FIRST-PARTY · committed 2022-04-01; accessed 2026-09-23 · https://github.com/MycroftAI/mimic3-voices/blob/master/voices/en_UK/apope_low/LICENSE — "Copyright 2022 Mycroft AI\nAll Rights Reserved"
[32] FIRST-PARTY · accessed 2026-09-23 · https://github.com/MycroftAI/mimic3-voices/blob/master/LICENSE — "Attribution-ShareAlike 4.0 International"
[33] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_GB/jenny_dioco/medium/MODEL_CARD — "* URL: https://github.com/dioco-group/jenny-tts-dataset\n* License: See URL"; "Finetuned from U.S. English lessac voice (medium quality)."
[34] FIRST-PARTY · accessed 2026-09-23 · https://github.com/dioco-group/jenny-tts-dataset/blob/main/README.md — "the voice must be referred to as \"Jenny\", and where at all practical, \"Jenny (Dioco)\". ... Commercial use is permitted."
[35] FIRST-PARTY · accessed 2026-09-23 · https://github.com/OHF-Voice/piper1-gpl/blob/5b355b110aecf3de8f4e000ede1ce06831acff35/docs/VOICES.md — "The `MODEL_CARD` file for each voice contains important licensing information. Piper is intended for personal use and text to speech research only; we do not impose any additional restrictions on voice models. Some voices may have restrictive licenses, however, so please review them carefully!"
[36] FIRST-PARTY · main; accessed 2026-09-23 · https://github.com/hexgrad/kokoro/blob/main/kokoro/pipeline.py — L5 "from misaki import en, espeak"; L116-123 lang a/b "fallback = espeak.EspeakFallback(british=lang_code=='b')" ... "en.G2P(..., fallback=fallback, unk='')"; L296 "# Multiply by 600 to go from pred_dur frames to sample_rate 24000"; L324 "t.start_ts = left / MAGIC_DIVISOR"; L328 "t.end_ts = ..."; class Result (tokens, output) with property pred_dur
[37] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/kokoro/json — 0.3.5 2025-02-02 (no join_timestamps/start_ts per wheel grep); 0.7.0 2025-02-04T02:28:02 (present); latest 0.9.4 2025-04-05T22:01:23; hexgrad/kokoro repo license Apache-2.0
[38] FIRST-PARTY · accessed 2026-09-23 · https://github.com/hexgrad/misaki — repo license Apache-2.0; misaki/token.py "start_ts: Optional[float] = None" "end_ts: Optional[float] = None"; en.py "from num2words import num2words" "import spacy"; L522 "def __init__(self, version=None, trf=False, british=False, fallback=None, unk='❓'):"; L526-527 "if not spacy.util.is_package(name): spacy.cli.download(name)"; misaki/data contains gb_gold.json, gb_silver.json
[39] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/phonemizer-fork/json — phonemizer-fork 3.3.2 classifier 'GNU General Public License v3 or later (GPLv3+)'; misaki/espeak.py imports phonemizer EspeakWrapper + espeakng_loader; misaki METADATA extras en: espeakng-loader, phonemizer-fork
[40] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/espeakng-loader/json — espeakng-loader 0.2.4, license None, license_expression None, no license classifiers; wheel contains libespeak-ng.1.52.0.dylib (researcher+verifier)
[41] FIRST-PARTY · master 040afe3; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/040afe360a38e25daaa325ce8889abf93ea02609/scripts/kokoro/v1.0/run.sh — "python3 ./export_onnx.py" -> "python3 ./add_meta_data.py" -> "python3 ./dynamic_quantization.py"; downloads misaki gb_gold.json / gb_silver.json; "./generate_lexicon_en.py" produces lexicon-us-en.txt / lexicon-gb-en.txt
[42] FIRST-PARTY · master 040afe3; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/040afe360a38e25daaa325ce8889abf93ea02609/scripts/kokoro/v1.0/export_onnx.py — torch.onnx.export(KModelForONNX(model), ..., input_names=["tokens", "style", "speed"], output_names=["audio"]); add_meta_data.py L37 hard-codes "model_url": "https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files"
[43] FIRST-PARTY · main; accessed 2026-09-23 · https://github.com/hexgrad/kokoro/blob/main/kokoro/model.py — KModelForONNX.forward: "waveform, duration = self.kmodel.forward_with_tokens(input_ids, ref_s, speed)\n        return waveform, duration"
[44] FIRST-PARTY · asset updated 2026-09-08; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/kokoro-int8-multi-lang-v1_0.tar.bz2 — Reconciler download (132303094 bytes): model.int8.onnx producer onnx.quantize 0.1.0; INPUTS tokens INT64 [1,sequence_length], style FLOAT [1,256], speed FLOAT [1]; OUTPUTS audio FLOAT [audio_length], onnx::Shape_3411 INT64 [Squeezeonnx::Shape_3411_dim_0]; sample_rate 24000; lexicon-gb-en.txt 191924 lines ('hello h ə l ˈ Q', 'world w ˈ ɜ ː l d'); LICENSE Apache 2.0; run 'hello world' bm_george sid 26: 14 ids, dur [12,2,3,2,5,5,4,2,4,3,4,3,13,10] sum 72, audio 43200, 600.0 samples/frame
[45] FIRST-PARTY · lastModified 2025-04-10; accessed 2026-09-23 · https://huggingface.co/hexgrad/Kokoro-82M — "license: apache-2.0"; "Kokoro was trained exclusively on **permissive/non-copyrighted audio data** ... Synthetic audio generated by closed TTS models from large providers"; VOICES.md: bf_emma target B / overall B-; bm_george target B / overall C
[46] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/onnxruntime/1.30.0/json — onnxruntime 1.30.0 'MIT License', 'License :: OSI Approved :: MIT License'
[47] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/onnx/1.23.0/json — onnx 1.23.0 license_expression 'Apache-2.0'
[48] FIRST-PARTY · pushed 2026-03-15; archived; accessed 2026-09-23 · https://github.com/NeuralVox/OpenPhonemizer — "OpenPhonemizer is no longer being maintained."; "attempts to replicate the `espeak` Phonemizer while remaining permissively-licensed"; "Project status: Alpha"; "Supported languages: English"; license BSD-3-Clause-Clear; archived=true; "depends on software under different licenses ... (notably LGPL)"; "Model weights may be licensed under different licenses."
[49] FIRST-PARTY · 2026-08-20 · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/tag/v3.4.2 — latest release v3.4.2 published 2026-08-20T00:18:52Z; repo license MIT
[50] FIRST-PARTY · accessed 2026-09-23 · https://github.com/MontrealCorpusTools/mfa-models — repo license CC-BY-4.0
[51] FIRST-PARTY · accessed 2026-09-23 · https://pypi.org/pypi/num2words/json — num2words 0.5.14 'GNU Library or Lesser General Public License (LGPL)'; spacy 3.8.16 MIT (researcher+verifier)
[52] FIRST-PARTY · v1.13.8; accessed 2026-09-23 · https://github.com/k2-fsa/sherpa-onnx/blob/v1.13.8/sherpa-onnx/csrc/offline-tts-vits-impl.h — Piper uses PiperPhonemizeLexicon only when "!config_.model.vits.data_dir.empty()"; else branch uses the plain Lexicon frontend (config_.model.vits.lexicon)
[53] FIRST-PARTY · closed 2026-07-27 · https://github.com/k2-fsa/sherpa-onnx/issues/3721 — "[BUG] PiperPhonemesToIdsVits (VITS + espeak data_dir) misses the pad token right after BOS, degrading pronunciation across the whole utterance"
[54] FIRST-PARTY · repo HEAD 7d9cc26; accessed 2026-09-23 · pipeline/tts.py — L58-59 "piper": "en_GB-alan-medium" / "kokoro": "bm_george"; L65-66 "piper": "en_GB-jenny_dioco-medium" / "kokoro": "bf_emma"

## Contradictions (first-party vs first-party — unresolved)
- Piper voice licence (alan, jenny_dioco): https://huggingface.co/rhasspy/piper-voices/blob/main/README.md says 'license: mit'. Both https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_GB/alan/medium/MODEL_CARD and .../jenny_dioco/medium/MODEL_CARD say 'Finetuned from U.S. English lessac voice (medium quality).' The lessac MODEL_CARD (https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_US/lessac/medium/MODEL_CARD) points to https://www.cstr.ed.ac.uk/projects/blizzard/2013/lessac_blizzard2013/license.html: 'to use the Materials exclusively for Research Purposes only', excluding 'any commercial purpose, including the development ... of voice synthesis ... products or services'. piper1-gpl VOICES.md adds: 'Some voices may have restrictive licenses'. Both sides are first-party. Not resolved; route A is blocked for these voices until the parent or user decides (standard #5 may disqualify them).
- alan dataset licence: the alan MODEL_CARD defers to 'See URL', i.e. https://github.com/MycroftAI/mimic3-voices/blob/master/voices/en_UK/apope_low/LICENSE, which says 'Copyright 2022 Mycroft AI / All Rights Reserved'. The repo-level https://github.com/MycroftAI/mimic3-voices/blob/master/LICENSE is CC-BY-SA-4.0, and piper-voices says MIT. Not resolved.
- sherpa-onnx licensing: the PyPI metadata for sherpa-onnx 1.13.8 ('Apache licensed') and sherpa-onnx-core 1.13.8 ('License: Apache-2.0') declares Apache. Both shipped binaries contain espeak-ng code (the macOS _sherpa_onnx.cpython-311-darwin.so exports 50 espeak_* symbols; the Linux libsherpa-onnx-c-api.so has espeak strings). Meanwhile the maintainer's https://github.com/k2-fsa/sherpa-onnx/issues/3731 says espeak-ng's GPL 'introduces license constraints that are incompatible with the Apache-2.0 license of sherpa-onnx'. Not resolved (legal).

## Could not confirm
- Any sherpa-onnx 2.0.0 release date or milestone, or whether 2.0.0 adds TTS durations. #3731 is open with no milestone, and its planned API adds only an input `tokens` field.
- Whether the lessac research-only licence legally carries over to voices fine-tuned from lessac (alan, jenny_dioco). This is a legal question; the first-party documents conflict.
- Which licence actually governs the apope_low data behind alan: the per-voice LICENSE (All Rights Reserved) or the repo-level CC-BY-SA-4.0.
- Whether OpenPhonemizer output matches espeak-ng en-gb-x-rp IPA closely enough for alan/jenny (not tested).
- Whether `espeak-ng --ipa` run as a CLI subprocess produces output token-identical to piper-phonemize's espeak_TextToPhonemesWithTerminator path (not tested).
- Hop length 256 for every Piper voice. It is the piper1-gpl default and was measured only on alan-medium; the alan .onnx.json has no hop_length key, so the default applies. Other voices and quality tiers were not measured.
- Perceptual accuracy of w_ceil and Kokoro durations as viseme timing: both match total audio length exactly by construction, but were not compared against a forced aligner.
- Kokoro KPipeline pred_dur index alignment when out-of-vocab phonemes are filtered, and word timestamps for non-English languages (not tested).
- Whether the fp32 kokoro-multi-lang-v1_0 and v1_1 sherpa graphs carry the same second durations output (only int8 v1_0 was inspected).
- Whether thewh1teagle/kokoro-onnx's Python library surfaces the durations output (not inspected).
- Provenance and licence of misaki's gb_gold.json / gb_silver.json dictionaries beyond the repo-level Apache-2.0, which is what lexicon-gb-en.txt is built from.
- Whether sherpa-onnx Windows wheels also embed espeak-ng (checked Linux core .so and macOS arm64 extension only).
- Licences of MFA's transitive dependencies (Kaldi/kalpy, OpenFst) and of specific MFA English models/dictionaries.
- Why csukuangfj/piper-phonemize's LICENSE changed from MIT at the commit sherpa pins to GPL-3.0 on master (reported by the researcher, not re-investigated).
- The torchaudio/MMS CTC forced-alignment route (not investigated).
- Terms-of-service implications of Kokoro-82M having been trained partly on synthetic audio from closed commercial TTS providers.

## Dropped claims (refuted or unsupported in verification)
- c35 provenance 'export via kokoro-onnx (MIT)': replaced with sherpa's own export_onnx.py -> add_meta_data.py -> dynamic_quantization.py pipeline (run.sh). The kokoro-onnx model_url is hard-coded metadata. The licence outcome is still Apache-2.0 weights.
- c23 exact numbers (28 ids / 91 frames / 23296 samples): not reproducible; replaced with the reconciler's recorded run (31 ids; 96 frames / 24576 samples at noise_w=0; 99 / 25344 at noise_w=0.8; 256 samples/frame in both).
- c9 exact callback chunk sizes (25344, 29952): dropped; only 'one chunk per sentence' is kept.
- c26 'PyPI piper-tts license_expression: GPL-3.0-or-later': corrected. The value is in the `license` field; license_expression is None.
- c37 'with no fallback, out-of-dictionary words are dropped': corrected. misaki en.G2P defaults to unk='❓'; words are dropped only with unk='', which KPipeline passes.
- Answer route A 'voices listed as MIT' / 'from the exact MIT voice files' and the recommendation to use route A for alan/jenny: withdrawn because of the unresolved lessac / apope first-party licence contradiction.
- Route C dependency on misaki.en (spacy + LGPL num2words): demoted to optional. sherpa's bundled lexicon-gb-en.txt + tokens.txt drives the graph with no misaki, spacy, num2words or espeak (reproduced).

## DO NOT QUOTE (low/unknown)
- [low] Researcher's exact Piper figures '28 phoneme IDs / 91 frames / 23296 samples' — Not reproducible: the input was not recorded and VITS durations are stochastic at noise_w=0.8. Use the reconciler's recorded run instead (31 ids; noise_w=0 gives 96 frames / 24576 samples).
- [low] Researcher's callback chunk sizes (25344, 0.5), (29952, 1.0) — Input text not recorded; the verifier got different sizes. Only the structural result (one chunk per sentence) is reproducible.
- [low] 'export via kokoro-onnx (MIT)' for sherpa's Kokoro int8 v1.0 graph — Contradicted by sherpa's run.sh (its own export, then add_meta_data, then quantize). The kokoro-onnx model_url is a hard-coded metadata string.
- [unknown] Calling alan-medium / jenny_dioco-medium 'MIT voices' — Only the repo-level HF tag says MIT. The per-voice MODEL_CARD chain leads to the lessac research-only licence, and for alan also to an 'All Rights Reserved' dataset. This is an unresolved first-party contradiction.
- [unknown] Legal status of espeak-ng as a subprocess vs in-process (ctypes/static), and of sherpa-onnx wheels labelled Apache while embedding espeak-ng — These are linking facts, not legal conclusions; no counsel or authoritative ruling was consulted.
- [low] Hop length 256 applies to all Piper voices — It is the piper1-gpl default, but it was measured on alan-medium only.
- [unknown] w_ceil / Kokoro durations are 'lip-sync accurate' — Totals are exact by construction, but per-phoneme timing was not compared with a forced aligner or checked perceptually.
- [unknown] sherpa-onnx 2.0.0 timing or feature set — Issue #3731 is open with no milestone and no v2 tag.
- [unknown] OpenPhonemizer suitability for en-gb-x-rp voices — The project is archived, alpha, and unmaintained; British RP accuracy was not tested.
- [unknown] Durations output in fp32 Kokoro v1_0 / v1_1 sherpa graphs, and in the kokoro-onnx library runtime — Only the int8 v1_0 graph was inspected.
- [unknown] Licence and provenance of misaki gb_gold/gb_silver dictionaries (the source of lexicon-gb-en.txt) — Only the repo-level Apache-2.0 was checked.
- [unknown] MFA transitive dependency and model licences — Only the repo-level licences (MIT, CC-BY-4.0) were checked.
- [unknown] Kokoro-82M training data including synthetic audio from closed commercial TTS — Stated on the model card; any downstream terms-of-service effect is unassessed.


---

# Track B1 — Local expressive TTS — description/instruction-controlled voice design
Primary mission track: no · Final confidence: medium

## Answer
## B1: Local TTS that builds a voice from a written description (Phineas and Seraphina)
Reconciled 2026-09-23. Every number below was re-checked against the source it cites.

### Answer
- **Pick for both registers: VoxCPM2 (OpenBMB).**
  - Code and weights are both Apache-2.0 [1][2].
  - Among the permissive models checked, it is the only one that documents all three steps: build a voice from a description, clone it from a clip, and still take style instructions on the clone ("you can still use control instructions to adjust speed, emotion, or style") [1][3].
  - Accent is one of its training labels [4].
  - It has the best self-reported English InstructTTSEval score, 84.2/83.2/71.4 [3].
  - The card describes the backbone as "Based on MiniCPM-4" [1]. The MiniCPM4 checkpoints listed on HF are Apache-2.0 [12].
- **Alternate for Phineas: Qwen3-TTS-12Hz-1.7B-VoiceDesign, FP32 only.**
  - Apache-2.0 for code and weights [13][14].
  - FP16 fails. Qwen says "we strongly recommend using `float32` for inference on machines that do not support `bfloat16`" [15].
  - Qwen documents a design-then-clone workflow for "a consistent character voice across many lines". The Base clone model does not take instructions [14].
- **Alternate for Seraphina: Maya1.**
  - It is the only candidate whose own card shows British voices [20].
  - Its inline tags include `<chuckle>`, `<sarcastic>` and `<giggle>` [20].
  - Costs:
    - 3,300,928,512 BF16 parameters [21], and the card asks for "16GB+ VRAM" [20].
    - It cannot clone. The org's only answer on keeping the voice consistent is "seed." [23]
    - Provenance risk: the config is Llama-shaped and declares no base model [22], and an org member says "We'll use every open audio source we can find" [24].
- **VRAM.** No candidate fits the ~3-4 GB left beside Ollama at a precision known to be safe on Turing. There are three ways to run one:
  - **(a) CPU in FP32, offline.** This works because asides are cached.
    - The voxcpm 2.0.3 wheel includes the CPU fix and a `--device` flag [5][8].
    - The runtime keeps the checkpoint's BF16 on CPU ("CUDA and CPU keep whatever the checkpoint was trained with"), so FP32 needs the `dtype` field in config.json edited [5][7].
    - Qwen's OpenVINO/CPU path is merged into optimum-intel main (2026-09-16) but is not in release v2.2.0 [17].
  - **(b) Share the GPU in time.** Unload Ollama with `keep_alive` 0 [54], then run FP32 on the whole 11 GB card. PyTorch 2.14 CUDA 12.6.3/13.0.3/13.2.1 builds include Turing(7.5) [53]. FP32 weights alone are tight on 11 GB:
    - VoxCPM2: 2,290,004,544 params plus audiovae.pth 376,951,122 B [2].
    - Qwen VoiceDesign: 1,916,676,352 params plus speech_tokenizer 682,293,092 B [13].
  - **(c) VoxCPM2 through llama.cpp-omni (MIT) GGUF.** The official README links this path and lists "CPU / Metal / CUDA / Vulkan" [3][11].
    - BaseLM-Q8_0 (1,727,309,920 B) plus Acoustic-F16 (1,825,096,352 B) is about 3.55 GB [10].
    - The converter accepts `--dtype` `f16` or `f32` [11], so a self-converted F32 GGUF on CPU is possible.
    - The GGUF is a third-party conversion, and F16/Q8_0 safety on sm_75 is untested.
- **Timings.** No model outputs phoneme timings.
  - VoxCPM main has word-level `--timestamps` through stable-ts (MIT). Character-level is "best-effort", and none of this is in the 2.0.3 release [3][5][6][57].
  - For phone-level timings: Montreal Forced Aligner (MIT, v3.4.2) with the English MFA acoustic model v3.1.0 (CC BY 4.0; its training data includes Google UK and Ireland English), run on the cached wav plus the known text [55][56].

### Table
| model | version / date | license code / weights | size / VRAM | Turing-OK? | control | timings | verdict |
|---|---|---|---|---|---|---|---|
| **VoxCPM2** | HF created 2026-04-03, edited 2026-08-18 [2]; PyPI `voxcpm` 2.0.3 (2026-05-11, latest) [5]; main pushed 2026-09-02 | Apache-2.0 / Apache-2.0 [1] | 2,290,004,544 BF16 + audiovae 376,951,122 B [2]; card: "~8 GB" VRAM [1] | BF16 by default [5]; FP16 is only a contributor's guess [7]; FP32 by editing config.json; GGUF path [10][11] | `(description)text` builds a voice; clone + `(style)` direction [1][3]; accent label [4]; card: "generating 1–3 times is recommended" [1] | word-level (stable-ts), main only [3][6] | **PICK, both** |
| **Qwen3-TTS-12Hz-1.7B-VoiceDesign** | HF 2026-01-21 [13]; `qwen-tts` 0.1.1 (2026-02-06) [16] | Apache-2.0 / Apache-2.0 [13][14] | 1,916,676,352 BF16 + tokenizer 682,293,092 B [13]; VRAM not stated | FP16 asserts, reported on Turing and Ampere; use FP32 [15]; OpenVINO on main only [17] | free-form `instruct` [14]; "thinking pattern" for complex descriptions [18] | none [16] | **alternate, Phineas** |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | same series [14] | Apache-2.0 [14] | – | same as above | instructions over 9 fixed voices; the English ones are Ryan and Aiden ("Sunny American male") [14] | none | reject: no British voice |
| **Maya1** | HF 2025-10-18, edited 2026-07-11 [21] | Apache-2.0 / Apache-2.0 per card [20]; SNAC decoder MIT [25] | 3,300,928,512 BF16 [21]; "16GB+ VRAM" [20] | BF16 checkpoint [22]; FP16 untested | `<description="...">` + tags incl. `<sigh> <chuckle> <whisper> <giggle> <sarcastic>` [20]; no cloning, only a fixed seed [23] | none | **alternate, Seraphina** |
| FireRedTTS3-Instruct | released 2026-08-13 [26] | Apache-2.0 / Apache-2.0 [26] | instruct 8,475,259,708 B + redae 3,775,160,672 B, both float32 configs [26] | FP32 native, but more than 11 GB of weights, so CPU only | free-form design listing "accent" [26]; card contradicts itself on acoustic edits (see contradictions) | none | watch |
| MOSS-VoiceGenerator | HF 2026-02-08 [28] | Apache-2.0 / Apache-2.0 [28] | card says 1.7B; HF lists 2,114,118,656 BF16 [28]; team: "1.7B — 12GB" on L20 [30] | BF16 on CUDA, FP32 on CPU in its code [28] | free-form instruction; British example exists [31]; no model does both clone and instruction [30] | none | reject: its own report admits "weaker prosody in certain English-speaking styles" [29] |
| Parler-TTS mini-v1 / mini-v1.1 / large-v1 | 2024-06-26 / 2024-10-16 / 2024-08-08; repo pushed 2024-12-10 [32][33] | Apache-2.0 / Apache-2.0 [32] | 877,842,290 / 937,803,241 / 2,333,013,362 F32 [32] | FP32 native | description + 34 named speakers; accent control not documented [32] | none | fallback only: Qwen's eval gives mini EN 63.4/48.7/28.6 [14]; pins transformers 4.46.1 [33] |
| Fun-CosyVoice3-0.5B-2512 | HF 2025-12-11 | Apache-2.0 | 0.5B (name) | `fp16=False` by default [34] | fixed instruction list; `inference_instruct2` needs `prompt_wav` [34] | none | outside this angle |
| IndexTTS-2.5 | HF 2026-08-10 [35] | bilibili license: separate license needed above 100M MAU or RMB 1bn revenue [35] | "~0.8B (GPT backbone)"; "roughly 6 GB of VRAM" [35] | not checked | cloning + 8-float emotion vector, or emotion from a text description via QwenEmotion (`use_qwen_emo=True`) [35] | none | outside this angle; possible partner for cloning designed voices |
| OmniVoice (k2-fsa) | HF 2026-03-30 | Apache-2.0 / **CC-BY-NC** [36] | – | – | attributes incl. dialect/accent [36] | – | **DISQUALIFIED** |
| AuK (tencent) | open-sourced 2026-09-09 [37] | MIT / MIT, but it **requires Qwen2.5-Omni-3B**, which is "FOR NON-COMMERCIAL PURPOSES ONLY" [37][38] | auk_base 6,122,209,092 B [37] | – | "Instruct TTS" from a description [37] | – | **DISQUALIFIED** |
| VoiceSculptor-VD | HF 2026-01-06 | Apache-2.0 declared; base Llasa-3B is CC-BY-NC-4.0 [39][40] | 4,009,663,488 BF16 | – | "Chinese only" [39] | – | **DISQUALIFIED** |
| Breeze TTS 2 | HF 2026-08-25 [41] | Apache-2.0 code / weights and outputs "research and non-commercial use only" [41] | ~7.7 GiB eager [41] | – | – | – | **DISQUALIFIED** |
| Higgs TTS 3 4B; Voxtral-4B-TTS-2603; fish s2-pro; Spark-TTS-0.5B; parler-tts-mini-v1-paraspeechcaps; CapSpeech-models | – | research/non-commercial; cc-by-nc-4.0; fish-audio-research; cc-by-nc-sa-4.0; cc-by-nc-sa-4.0; cc-by-nc-4.0 [42][44] | – | – | – | – | **DISQUALIFIED** |
| Step-Audio-EditX | HF 2025-10-29 | Apache-2.0 covers "the code" only; no license for the weights [45] | 3B; 12 GB minimum [45] | – | – | – | **DISQUALIFIED** |
| Dramabox; Higgs TTS 2 3B base; MiMo-Audio-7B-Instruct; OV-InstructTTS | – | LTX-2 community; Llama-3-based custom; MIT; Apache-2.0 [43][46][47][48] | ~24 GB peak; 5,771,283,456; 8,018,587,648; 8,315,179,264 BF16 | no | – | – | too big for the hardware |
| Irodori-TTS-600M-v3-VoiceDesign; ParaStyleTTS; TADA-1b | – | MIT; MIT; llama3.2 [49][50][51] | 617M; 52.5M; – | – | Japanese only; age/emotion/gender/language only; cloning-driven | TADA: one vector per text token [51] | reject |

### Using VoxCPM2
- **Install from a pinned git commit, not PyPI.** Seed support (merged 2026-06-29) and `--timestamps` (2026-06-06) exist only on main [6]. The README's `seed=42` examples fail on the 2.0.3 release [3][5].
- **Precision.** There is no dtype argument, so FP32 means editing config.json [5][7].
- **Reference clips.** Keep them short. One user with a 3-minute reference reported ~13 GB on a 2080 Ti 22G, and a collaborator suggested 10-30 s clips [9].
- **Workflow.** Design several takes → keep the best as the voice's anchor clip → clone from it with `(style)` prefixes, one per line of dialogue.

### Caveats
- No first-party measurement of British-accent quality exists for any model. No Qwen document mentions accent or British.
- InstructTTSEval is judged by Gemini [52], and the scores differ between reports [14][27][29].
- Like the face, the voice is a one-way door. Pin the model revision, seed and anchor clip, and A/B test before anything reaches the wall.

## Sources
[1] FIRST-PARTY · lastModified 2026-08-18; accessed 2026-09-23 · https://huggingface.co/openbmb/VoxCPM2 — Apache-2.0; 'Voice Design — Generate a novel voice from a natural-language description alone'; 'Controllable Cloning — Clone any voice from a short clip, with optional style guidance'; '| dtype | bfloat16 |'; '| VRAM | ~8 GB |'; '| Backbone | Based on MiniCPM-4, totally 2B parameters |'; 'generating 1–3 times is recommended'
[2] FIRST-PARTY · createdAt 2026-04-03, lastModified 2026-08-18; accessed 2026-09-23 · https://huggingface.co/api/models/openbmb/VoxCPM2?blobs=true — license:apache-2.0; {'BF16': 2290004544}; audiovae.pth 376951122 B; model.safetensors 4580080592 B
[3] FIRST-PARTY · repo pushed 2026-09-02; accessed 2026-09-23 · https://github.com/OpenBMB/VoxCPM/blob/main/README.md — InstructTTSEval '| **VoxCPM2** | **85.2** | 71.5 | 60.8 | **84.2** | **83.2** | **71.4** |'; 'The model clones the timbre, and you can still use control instructions to adjust speed, emotion, or style.'; '# Optional post-generation timestamps with stable-ts'; '# Character timestamps are best-effort'; llama.cpp-omni 'native VoxCPM2 GGUF support on CPU / Metal / CUDA / Vulkan'; examples use seed=42
[4] FIRST-PARTY · submitted 2026-06-05 · https://arxiv.org/abs/2606.06928 — VoxCPM2 report: 'voice design attributes (e.g., age, gender, accent, vocal texture, scenario)'
[5] FIRST-PARTY · uploaded 2026-05-11 (latest release as of 2026-09-23) · https://pypi.org/project/voxcpm/2.0.3/ — utils.py: 'CUDA and CPU keep whatever the checkpoint was trained with.'; issue #256 CPU fix reference; --device CLI; wheel core.py has no seed and cli.py has no timestamps (inspected in scratch)
[6] FIRST-PARTY · accessed 2026-09-23 · https://github.com/OpenBMB/VoxCPM/commits/main/src/voxcpm/cli.py — '2026-06-06 Add optional timestamp alignment'; '2026-06-29 Merge pull request #327 from DEVAIEXP/feat-add-seed' (both after 2.0.3)
[7] secondary · comment 2025-12-10; issue open · https://github.com/OpenBMB/VoxCPM/issues/112 — a710128 (CONTRIBUTOR): 'I guess FP16 should work too. You can modify the model's config file `config.json`... change it from `bfloat16` to `float16`.'
[8] secondary · 2026-04-13; closed 2026-07-01 · https://github.com/OpenBMB/VoxCPM/issues/256 — CPU inference fix; user log on Core Ultra 7 255H '96/478 [01:01<04:05, 1.56it/s]'
[9] secondary · 2026-06-23 · https://github.com/OpenBMB/VoxCPM/issues/344 — User on 'NVIDIA GeForce 2080 Ti 22G': ~5 GB after warm-up, ~13 GB on first inference with 3m12s reference; collaborator: references of 10-30 s are reasonable
[10] secondary · created 2026-06-19, lastModified 2026-06-30; accessed 2026-09-23 · https://huggingface.co/DennisHuang648/VoxCPM2-GGUF — Third-party GGUF linked from official VoxCPM README; HF API sizes VoxCPM2-BaseLM-Q8_0.gguf 1727309920 B, VoxCPM2-Acoustic-F16.gguf 1825096352 B, VoxCPM2-BaseLM-F16.gguf 3247980544 B; 'Voice design: prefix the text with `(a calm female voice)…`'; tag license:apache-2.0
[11] FIRST-PARTY · pushed 2026-09-23 · https://github.com/tc-mb/llama.cpp-omni — license MIT; tools/omni/voxcpm2/convert_voxcpm2_to_gguf.py: '--dtype', default='f16', choices=['f16','f32']
[12] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/api/models/openbmb/MiniCPM4-0.5B — license:apache-2.0 (openbmb/MiniCPM4-8B also license:apache-2.0); exact MiniCPM-4 checkpoint behind VoxCPM2 not named
[13] FIRST-PARTY · createdAt 2026-01-21, lastModified 2026-01-29 · https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign?blobs=true — license:apache-2.0; {'BF16': 1916676352}; model.safetensors 3833402552 B; speech_tokenizer/model.safetensors 682293092 B
[14] FIRST-PARTY · repo pushed 2026-03-17; accessed 2026-09-23 · https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md — '2026.1.22: ... released Qwen3-TTS series (0.6B/1.7B)'; generate_voice_design with natural-language instruct; design-then-clone 'consistent character voice across many lines'; Base rows no instruction control; CustomVoice 9 speakers incl. 'Aiden | Sunny American male voice'; eval 'Qwen3TTS-12Hz-1.7B-VD 85.2 81.1 65.1 82.9 82.4 68.4', 'Parler-tts-mini ... 63.4 48.7 28.6'; eval ran 'dtype=torch.bfloat16'; no 'British' anywhere
[15] FIRST-PARTY · collaborator comment 2026-01-26 · https://github.com/QwenLM/Qwen3-TTS/issues/43 — Title: CUDA assert on Turing (RTX 2060) FP16; also 'Same on RTX3080', 3060; wangxiongts (COLLABORATOR): 'we strongly recommend using `float32` for inference on machines that do not support `bfloat16`'
[16] FIRST-PARTY · uploaded 2026-02-06 (latest) · https://pypi.org/project/qwen-tts/0.1.1/ — Version 0.1.1, License Apache-2.0, transformers==4.57.3; no timestamp output
[17] FIRST-PARTY · merged 2026-09-16 · https://github.com/huggingface/optimum-intel/pull/1765 — '[OpenVINO] Add support for Qwen3-TTS model' incl. 1.7B-VoiceDesign, f32 precision hint; compare v2.2.0...c46fb912 = diverged (not in v2.2.0, released 2026-09-17)
[18] FIRST-PARTY · arXiv 2601.15621; accessed 2026-09-23 · https://arxiv.org/html/2601.15621 — 'a probabilistically activated thinking pattern during training to improve instruction following, especially for complex descriptions'
[19] FIRST-PARTY · lastModified 2026-01-29 · https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign — Card usage code loads 'Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice' and calls generate_custom_voice (doc error vs GitHub README)
[20] FIRST-PARTY · lastModified 2026-07-11 · https://huggingface.co/maya-research/maya1 — license apache-2.0; 'a 20s British girl'; 'Male voice in their 40s with a British accent'; '<description="...">'; 'Single GPU with 16GB+ VRAM'; 'We pretrained a 3B-parameter decoder-only transformer (Llama-style)'; emotions.txt: <laugh> <laugh_harder> <sigh> <chuckle> <gasp> <angry> <excited> <whisper> <cry> <scream> <sing> <snort> <exhale> <gulp> <giggle> <sarcastic> <curious>
[21] FIRST-PARTY · createdAt 2025-10-18, lastModified 2026-07-11 · https://huggingface.co/api/models/maya-research/maya1 — license:apache-2.0; {'BF16': 3300928512}
[22] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/maya-research/maya1/blob/main/config.json — 'architectures': ['LlamaForCausalLM'], 'dtype': 'bfloat16'; no base_model declared
[23] FIRST-PARTY · 2025-11-10 / 2025-11-12 · https://huggingface.co/maya-research/maya1/discussions/19 — Q: voice constant across clips? bharathkumarK (isOrgMember true): 'seed.'
[24] FIRST-PARTY · 2025-11-20 · https://huggingface.co/maya-research/maya1/discussions/4 — DheemanthReddy (isOrgMember true): 'We'll use every open audio source we can find to train models'
[25] FIRST-PARTY · accessed 2026-09-23 · https://github.com/hubertsiuzdak/snac — SNAC license MIT
[26] FIRST-PARTY · release 2026-08-13; lastModified 2026-08-24 · https://huggingface.co/FireRedTeam/FireRedTTS3 — '[2026.08.13] We release the FireRedTTS3-Instruct model & code'; license:apache-2.0; '(gender, age, timbre, emotion, pace, accent…)'; line 38 'acoustic editing (speed / pitch / volume) driven by free-form instructions' vs line 212 'free-form phrasing is not supported'; files fireredtts3_instruct/model.safetensors 8475259708 B, redae/model.safetensors 3775160672 B
[27] secondary · repo pushed 2026-09-08 · https://github.com/FireRedTeam/FireRedTTS3/blob/main/README.md — Re-scores all systems with Gemini-2.5-pro: Qwen3-TTS-VD EN 76.4/81.4/64.2; FireRedTTS3-Instruct EN 80.7/82.3/72.0 (first-party only for FireRed)
[28] FIRST-PARTY · createdAt 2026-02-08, lastModified 2026-02-11 · https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator — license:apache-2.0; card '| MOSS‑VoiceGenerator | MossTTSDelay | 1.7B |'; HF {'BF16': 2114118656}; 'dtype = torch.bfloat16 if device == "cuda" else torch.float32'
[29] FIRST-PARTY · v1 2026-03-30 · https://arxiv.org/abs/2603.28086 — 'weaker prosody in certain English-speaking styles'; its Qwen3-TTS-VD row 78.4/78.8/72.0 differs from Qwen's own figures
[30] FIRST-PARTY · 2026-02-11 / 2026-02-12 · https://github.com/OpenMOSS/MOSS-TTS/issues/7 — YWMditto (COLLABORATOR): 'we do not have a single model that supports both voice cloning and instruction-based control'; '1.7B — 12GB VRAM — 42 tokens/s' incl. audio tokenizer on L20
[31] FIRST-PARTY · accessed 2026-09-23 · https://github.com/OpenMOSS/MOSS-TTS/blob/main/assets/text/moss_voice_generator_example_texts.jsonl — 'An elderly female voice, slightly nasal and soft, speaking in a frail, polite British tone'
[32] FIRST-PARTY · lastModified 2024-11-22 · https://huggingface.co/parler-tts/parler-tts-large-v1 — Apache-2.0; 'trained on 34 speakers'; HF API F32 params mini-v1 877842290 (2024-06-26), mini-v1.1 937803241 (2024-10-16), large-v1 2333013362 (2024-08-08)
[33] FIRST-PARTY · pushed 2024-12-10 · https://github.com/huggingface/parler-tts — setup.py 'transformers>=4.46.1,<=4.46.1'
[34] FIRST-PARTY · accessed 2026-09-23 · https://github.com/FunAudioLLM/CosyVoice — cosyvoice/utils/common.py fixed instruct list; cosyvoice.py 'class CosyVoice3(CosyVoice2): def __init__(..., fp16=False, ...)'; 'def inference_instruct2(self, tts_text, instruct_text, prompt_wav, ...)'; HF FunAudioLLM/Fun-CosyVoice3-0.5B-2512 license:apache-2.0 created 2025-12-11
[35] FIRST-PARTY · createdAt 2026-08-10, lastModified 2026-08-12 · https://huggingface.co/IndexTeam/IndexTTS-2.5 — 'Parameters: ~0.8B (GPT backbone)'; 'roughly 6 GB of VRAM'; 'Emotion control with an 8-float vector'; 'Emotion control from a text description needs the QwenEmotion model ... use_qwen_emo=True'; LICENSE 2.2: 'more than 100 million monthly active users ... RMB 1 billion, You must request a separated license'
[36] FIRST-PARTY · createdAt 2026-03-30, lastModified 2026-07-03 · https://huggingface.co/k2-fsa/OmniVoice — 'Our code is released under the Apache 2.0 License. The pre-trained model is licensed under the CC-BY-NC'; voice design attributes incl. 'dialect/accent'
[37] FIRST-PARTY · '[2026/09/09] AuK is now open-source'; lastModified 2026-09-10 · https://huggingface.co/tencent/AuK — license mit; 'Instruct TTS | Generate speech from a voice description alone'; setup 'hf download Qwen/Qwen2.5-Omni-3B'; auk_base.safetensors 6122209092 B
[38] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen2.5-Omni-3B/blob/main/LICENSE — license_name qwen-research; 'FOR NON-COMMERCIAL PURPOSES ONLY'
[39] FIRST-PARTY · repo pushed 2026-02-26 · https://github.com/ASLP-lab/VoiceSculptor/blob/main/docs/voice_design_en.md — 'Chinese only. English is not supported in the current version'; HF VoiceSculptor-VD license:apache-2.0, base_model HKUSTAudio/Llasa-3B, BF16 4009663488
[40] FIRST-PARTY · lastModified 2025-05-10 · https://huggingface.co/HKUSTAudio/Llasa-3B — license:cc-by-nc-4.0; base_model meta-llama/Llama-3.2-3B-Instruct
[41] FIRST-PARTY · created 2026-08-25; LICENSE v1.1 2026-09-01 · https://huggingface.co/BreezeBlue/Breeze-TTS-2 — 'Breeze TTS 2 model weights, derivative models, and self-hosted outputs are for research and non-commercial use only.'; 'approximately 7.7 GiB of GPU memory'
[42] FIRST-PARTY · lastModified 2026-09-04 · https://huggingface.co/bosonai/higgs-tts-3-4b — license_name boson-higgs-tts-3-research-and-non-commercial-license
[43] FIRST-PARTY · lastModified 2026-06-25 · https://huggingface.co/bosonai/higgs-tts-2-3b-base — {'BF16': 5771283456}; license based on Meta Llama 3 Community License, 100,000 annual active users threshold
[44] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/api/models/mistralai/Voxtral-4B-TTS-2603 — license:cc-by-nc-4.0; also HF API: fishaudio/s2-pro fish-audio-research-license; SparkAudio/Spark-TTS-0.5B cc-by-nc-sa-4.0; ajd12342/parler-tts-mini-v1-paraspeechcaps cc-by-nc-sa-4.0; OpenSound/CapSpeech-models cc-by-nc-4.0
[45] FIRST-PARTY · lastModified 2026-02-14 · https://huggingface.co/stepfun-ai/Step-Audio-EditX — '| Step-Audio-EditX | 3B | 41.6Hz | 12 GB |'; 'The code in this open-source repository is licensed under the Apache 2.0 License.'; no license tag on HF
[46] FIRST-PARTY · lastModified 2026-05-13 · https://huggingface.co/ResembleAI/Dramabox — 'VRAM: ~24 GB peak, warm server.'; license_name ltx-2-community
[47] FIRST-PARTY · lastModified 2026-06-17 · https://huggingface.co/api/models/XiaomiMiMo/MiMo-Audio-7B-Instruct — license:mit; {'BF16': 8018587648}
[48] FIRST-PARTY · 2025-11-09 · https://huggingface.co/api/models/y-ren16/OV-InstructTTS — license:apache-2.0; {'BF16': 8315179264}
[49] FIRST-PARTY · created 2026-05-31 · https://huggingface.co/api/models/Aratako/Irodori-TTS-600M-v3-VoiceDesign — license:mit; ja; F32 617060641
[50] FIRST-PARTY · repo pushed 2025-12-21 · https://github.com/haoweilou/ParaStyleTTS — 'supports speaking style control over four dimensions' (age, emotion, gender, language); HF license:mit F32 52511600
[51] FIRST-PARTY · lastModified 2026-03-17 · https://huggingface.co/HumeAI/tada-1b — license:llama3.2; 'encodes audio into a sequence of vectors that perfectly matches the number of text tokens'
[52] FIRST-PARTY · arXiv 2506.16381; accessed 2026-09-23 · https://arxiv.org/abs/2506.16381 — InstructTTSEval features incl. 'social (e.g., accent, age, volume)'; Gemini as automatic judge
[53] FIRST-PARTY · accessed 2026-09-23 · https://github.com/pytorch/pytorch/blob/main/RELEASE.md — 'For Release 2.14 PyTorch Supports following CUDA Architectures:' 12.6.3/13.0.3/13.2.1 include 'Turing(7.5)'
[54] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/docs/api.md — 'If an empty prompt is provided and the `keep_alive` parameter is set to `0`, a model will be unloaded from memory.'; default 5m
[55] FIRST-PARTY · release v3.4.2 2026-08-20 · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner — license MIT; latest release v3.4.2
[56] FIRST-PARTY · accessed 2026-09-23 · https://github.com/MontrealCorpusTools/mfa-models/blob/main/acoustic/english/mfa/v3.1.0/README.md — 'Model version: v3.1.0'; 'License: CC BY 4.0'; training corpora include 'Google UK and Ireland English'
[57] FIRST-PARTY · pushed 2026-05-30 · https://github.com/jianfch/stable-ts — license MIT
[58] secondary · lastModified 2026-08-02 · https://huggingface.co/cstr/qwen3-tts-1.7b-voicedesign-GGUF — Community GGUF of Qwen3-TTS VoiceDesign: f16 3838976832 B, q8_0 2042225536 B; example instruct with 'slight British accent' (third-party, unverified)

## Contradictions (first-party vs first-party — unresolved)
- FireRedTTS3 model card contradicts itself (both first-party, same document https://huggingface.co/FireRedTeam/FireRedTTS3). Line 38: 'acoustic editing (speed / pitch / volume) driven by free-form instructions'. Line 212: 'The instruction must follow the trained templates below (free-form phrasing is not supported)'. Not resolved.
- VoiceSculptor-VD license chain: https://huggingface.co/ASLP-lab/VoiceSculptor-VD declares license:apache-2.0 with base_model HKUSTAudio/Llasa-3B. https://huggingface.co/HKUSTAudio/Llasa-3B declares license:cc-by-nc-4.0. Not resolved; moot because VoiceSculptor is 'Chinese only'.
- MOSS-VoiceGenerator size: the card (https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator) says '1.7B', but HF safetensors metadata for the same repo reports 2,114,118,656 BF16 params. Not reconciled.
- Qwen3-TTS-VoiceDesign usage docs: the HF card (https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign) example loads 'Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice' and calls generate_custom_voice. The GitHub README (https://github.com/QwenLM/Qwen3-TTS) uses generate_voice_design with the VoiceDesign model.
- VoxCPM README (main, https://github.com/OpenBMB/VoxCPM) calls model.generate(..., seed=42). The latest release, voxcpm 2.0.3 on PyPI (2026-05-11), has no seed parameter; seed was merged to main 2026-06-29. The docs track main, not the release.
- Qwen3-TTS-VD English InstructTTSEval scores: Qwen's own 82.9/82.4/68.4 (https://github.com/QwenLM/Qwen3-TTS); MOSS report 78.4/78.8/72.0, claimed as 'sourced from their respective technical reports' (https://arxiv.org/abs/2603.28086); FireRedTTS3 re-score 76.4/81.4/64.2 (https://github.com/FireRedTeam/FireRedTTS3). Only Qwen's figure is first-party for Qwen, so this is not a first-party conflict. It does show the Gemini-judged benchmark is unstable.

## Could not confirm
- No first-party measurement of British-accent quality for any candidate; the picks rest on control features, license and hardware fit.
- No Qwen first-party document (README, VD card, tech report, qwen-tts wheel) names accent or 'British' as a VoiceDesign attribute.
- Qwen3-TTS-VoiceDesign VRAM (not stated anywhere); whether FP32 plus activations fits the 11 GB card; FP32 CPU speed on the i9-9900K.
- Whether optimum-intel's Qwen3-TTS OpenVINO support will ship in a release after v2.2.0; its speed on the i9-9900K.
- Whether a Qwen3-TTS Base model fine-tuned on a designed voice accepts `instruct`.
- Whether VoxCPM2 in FP16 is correct on Turing; BF16 behaviour on sm_75; the dtype used in the 2080 Ti 22G anecdote.
- VoxCPM2 FP32 VRAM with activations; FP32 CPU wall-clock on the i9-9900K (the only CPU datum is 1.56 it/s on a Core Ultra 7 255H).
- Whether VoxCPM2 voice design reliably produces a British accent from a description (accent is a training label; no English/British demo found).
- Whether the llama.cpp-omni VoxCPM2 GGUF path (F16/Q8_0) is numerically sound on the sm_75 CUDA backend; its CPU speed; the quality of a self-converted F32 GGUF.
- The exact MiniCPM-4 checkpoint VoxCPM2 derives from (the MiniCPM4-0.5B and -8B checkpoints on HF are Apache-2.0).
- Maya1 weight provenance: its config is Llama-shaped, it declares no base_model and the card says 'pretrained'. Whether Llama 3.2 Community License terms apply is unconfirmed.
- Whether a fixed seed keeps Maya1's voice identical across different texts; Maya1 FP16 behaviour on Turing.
- MOSS-VoiceGenerator's own VRAM (the team's 12 GB figure is for a generic '1.7B' model); whether MOSS shipped the clone-plus-instruction model promised 2026-03-09.
- FireRedTTS3-Instruct parameter count, VRAM, CPU speed, FP16 behaviour; whether all of RedAE is needed at inference; whether acoustic edits accept free-form or only templated phrasing (the card says both).
- Whether Parler-TTS descriptions can control accent (not documented on the cards).
- Voice consistency across hundreds of cached lines for description-only models (Maya1, Qwen VD called per line, MOSS).
- Per-phoneme timings from any engine (none documented); MFA English v3.1.0 accuracy on synthetic British theatrical speech.
- RAM available on supercommons2 for CPU FP32 inference.
- Whether combining VoxCPM2/Qwen design with IndexTTS-2.5 cloning plus text-emotion works well (untested idea).

## Dropped claims (refuted or unsupported in verification)
- 'Four models with Apache-2.0 code and weights can design a voice' as an exhaustive count: reworded. Parler-TTS and MOSS-VoiceGenerator also qualify on license.
- 'Two ways to run' (CPU FP32 or time-shared GPU): expanded to three, adding the officially linked llama.cpp-omni GGUF path for VoxCPM2.
- 'VoxCPM2 FP32 about 9.2 GB' and 'Qwen VD FP32 about 7.7 GB': corrected to include the separately shipped codec files (audiovae.pth 376,951,122 B; speech_tokenizer 682,293,092 B).
- 'FP16 is only a maintainer's guess' (VoxCPM issue #112): the responder is marked CONTRIBUTOR, so reworded to 'contributor's guess'.
- 'MossTTSLocal 1.7B needs 12 GB': the first-party reply says only '1.7B'; the MossTTSLocal attribution was removed.
- 'FireRedTTS3 speed/pitch/volume edits accept only fixed phrasing' as a fact: the card also says free-form, so moved to contradictions.
- IndexTTS-2.5 'cloning + 8-number emotion vector' as its full control surface: corrected; the card also documents emotion from a text description via QwenEmotion.
- Dramabox 'prompt with stage directions': not verified against a source this session; removed.
- Breeze TTS 2 'description + direction' control: not verified; removed (the license disqualification stands).
- Step-Audio-EditX 'fixed emotion/style menu': not verified; removed (disqualified on missing weight license regardless).
- '~4x slower than realtime on CPU' for VoxCPM2 and '~2.1B params' for FireRedTTS3: researcher derivations with no first-party figure; removed from the answer and listed in do_not_quote.
- Maya1 discussion #19 'seed.' reply marked secondary: re-marked first-party (the responder is a maya-research org member). Kept, at low weight.

## DO NOT QUOTE (low/unknown)
- [low] FP32 weight footprints: VoxCPM2 about 9.5 GB, Qwen3-TTS-VD about 8.4 GB — My arithmetic (params x 4 bytes + codec files as stored). Excludes activations. The speech_tokenizer's stored dtype was not checked.
- [low] VoxCPM2 FP16 'should work' by editing config.json — Guess by a GitHub CONTRIBUTOR (not a verified maintainer). The reporter saw no speedup. VoxCPM's own code says fp16/bf16 drift glitches output on MPS.
- [low] VoxCPM2 ~13 GB peak on a 2080 Ti 22G — One user's anecdote with a 3-minute reference clip; dtype unknown.
- [low] VoxCPM2 CPU speed (1.56 it/s, or any 'x-times realtime' derived from it) — One user log on a Core Ultra 7 255H; not the i9-9900K; the realtime ratio would be a derivation.
- [low] VoxCPM2 GGUF via llama.cpp-omni fits ~3.55 GB and runs on Turing CUDA — File sizes are real, but the GGUF is a third-party conversion. F16/Q8_0 correctness on sm_75 is untested, and the RTF 1.76 figure is for Apple M4 Pro/Metal only.
- [low] Community Qwen3-TTS VoiceDesign GGUF (cstr) and its 'slight British accent' example — Third-party, unverified. Qwen warns its code predictor is 'extremely sensitive to precision'.
- [unknown] Any claim that Qwen's docs show a 'British English accent' example — Came from a web-search summary; no British example appears in any Qwen first-party file.
- [low] Maya1 is derived from Llama 3.2 3B (Llama license obligations) — Inferred from config shape and a secondary (unsloth) mirror comparison; the card says 'pretrained' and declares no base_model.
- [low] A fixed seed keeps Maya1's voice constant across lines — Only a one-word org-member reply ('seed.'); no documentation or test.
- [low] MOSS '1.7B needs 12 GB' applied to MOSS-VoiceGenerator specifically — The collaborator's figure is for a generic '1.7B' model (incl. tokenizer, on L20), not stated for VoiceGenerator.
- [low] FireRedTTS3-Instruct ~2.1B parameters — Derived from file size; no first-party figure.
- [unknown] FireRedTTS3 acoustic edits are template-only (or free-form) — The first-party card says both.
- [low] Cross-report InstructTTSEval numbers for Qwen3-TTS-VD (78.4/78.8/72.0 from MOSS; 76.4/81.4/64.2 from FireRed) — Secondary for Qwen; Gemini-judged; they disagree with Qwen's own 82.9/82.4/68.4.
- [unknown] Relative British-accent quality of VoxCPM2 vs Qwen VD vs Maya1 — No first-party or independent measurement exists; must be A/B listened.
- [low] Qwen3-TTS OpenVINO CPU path as a shipping option — Only on optimum-intel main (merged 2026-09-16); not in the v2.2.0 release; speed unknown.
- [unknown] Qwen3-TTS-VD FP32 fits on the 11 GB card with activations — VRAM not documented; only weight arithmetic available.
- [unknown] Parler-TTS can render a British accent from a description — Not documented on the model cards.
- [unknown] VoiceSculptor-VD is Apache-2.0 clean — Its declared base Llasa-3B is CC-BY-NC-4.0; unresolved first-party conflict (moot: Chinese-only).
- [low] IndexTTS-2.5 as a clone partner with text-described emotion for designed voices — An untested combination proposed by the verifier; no source documents it for this use.
- [unknown] MFA English v3.1.0 gives accurate phone timings on synthetic theatrical British speech — Not measured anywhere.


---

# Track B2 — Local expressive TTS — reference cloning + emotion/style controls
Primary mission track: no · Final confidence: medium

## Answer
## B2 (angle 2): local expressive TTS with reference cloning and style controls. Final answer as of 2026-09-23

### Direct answer

**Phineas** ("dry patrician baritone, grandiloquent, self-pitying", British)
1. **PICK: Chatterbox, the original English 500M model.** Code and weights are both MIT [1][2].
   - Reference clip: clone from the CC0 Voice-Zero clip `simon_evers.flac`, labelled "English, Public School (Received Pronunciation)". It comes from *Celebration of Dialects and Accents* Vol 2, and the repo says accent labels from those volumes "should be accurate" [54].
   - Emotion colour: an optional reference is the CC0 synthetic variant `voices-emotion/simon_evers/sad.flac` (or `tired.flac`) [55].
   - Settings: the vendor's "Expressive or Dramatic Speech" recipe is "lower `cfg` values (e.g. `~0.3`) and increase `exaggeration` to around `0.7` or higher … reducing `cfg` helps compensate with slower, more deliberate pacing" [1].
   - Install: PyPI `chatterbox-tts` 0.1.7 (2026-03-26) is still current. It pins `torch==2.6.0` and `transformers==5.2.0` [2][3].
2. **CONDITIONAL alternative: Zonos v0.1-transformer.** Code and weights are both Apache-2.0 [17][18].
   - Controls: an 8-dim emotion vector (it includes Sadness), `pitch_std` ("60-150 for expressive speech"), `speaking_rate`, and an explicit `'en-gb-x-rp'` language code [20].
   - Blocker on Turing: the shipped code hard-codes bf16 (`.to(device, torch.bfloat16)`) and the weights are stored as BF16 [17][19]. It needs a code patch to fp16/fp32 before it can run on the 2080 Ti.
   - The HF card and the GitHub README contradict each other on GPU support (see contradictions).
   - Needs espeak-ng, which is GPL-3.0 [16].
- **Legal review required before use: IndexTTS-2 / 2.5.** It has the richest emotion control checked: an 8-float vector including `melancholic`, an emotion reference with `emo_alpha`, and `duration_factor` [25][26].
  - The license is the custom bilibili Model Use License [24].
  - Its "Derivative Work" definition covers "model outputs", so the terms, including revocation on breach, reach the generated audio [24].
  - The README separately says "For commercial usage and cooperation, please contact" bilibili [25].

**Seraphina** ("quick dry mezzo, complicit and amused", British)
1. **PICK: Chatterbox original English 500M.** Same engine and venv as Phineas.
   - Reference clip: clone from CC0 `ruth_golding.flac` ("English, Received Pronunciation ('No regional accent')", from Celebration Vol 1, so the label should be accurate) [54]. `karen_savage2.flac` is also labelled RP, but it is from a Dolittle reading, where accent labels are "often based on guesswork" [54].
   - Settings: roughly the defaults (`exaggeration=0.5`, `cfg=0.5`). The vendor says that for a fast reference speaker, "lowering `cfg` to around `0.3` can improve pacing" [1].
   - Emotion references: CC0 variants exist under `voices-emotion/ruth_golding/` and `voices-emotion/karen_savage2/` [55].
2. **Offline alternative: VoxCPM2.** Code and weights are both Apache-2.0; 2B parameters.
   - Control: "Clone any voice from a short clip, with optional style guidance to steer emotion, pace, and expression" [31].
   - Memory: the published figures are bf16 at "~8 GB" of VRAM [31]. That does not fit next to the ~7 GB Ollama load.
   - Precision risk on Turing: the vendor's own code says "bfloat16/float16 produce enough numerical drift in the diffusion AR loop that the output is glitched… float32 is the only stable option today". That note is about MPS; CUDA "keep[s] whatever the checkpoint was trained with" [32].
   - Use it only as an offline batch job with Ollama unloaded.
- **Watch only: Chatterbox-Turbo (350M) and Nano (110M).**
  - They have native `[laugh]`/`[chuckle]`-style tags [7][8].
  - The Turbo tokenizer also carries `[sarcastic]`, `[dramatic]`, `[narration]` and `[whispering]` tokens, but their effect is undocumented [9].
  - Both **ignore `exaggeration` and `cfg`** [4].
  - Nano exists only on the GitHub `master` branch (commit 5de7a54, 2026-07-21), not in any PyPI release [3][4].

**A way to avoid third-party voice rights entirely:** Qwen3-TTS (Apache-2.0) documents a "Voice Design then Clone" workflow [27].
- Step 1: "use the **VoiceDesign** model to synthesize a short reference clip that matches your target persona" [27].
- Step 2: clone that clip in Chatterbox.
- Caveats: none of its preset speakers is British [28], its examples use bf16 plus FlashAttention-2 [27], and FA2 needs a separate repo for Turing [30]. Run it as a one-time offline job.

**Operational caveats**
- Every Chatterbox output carries the Perth watermark [1].
- The Voice-Zero maintainer reports that Chatterbox "has a strange tendency to babble incoherently, scream… It also randomly shouts curse words" [55]. This is a secondary report about Chatterbox, but for an unattended public wall it means every clip should be generated offline and checked before it plays.
- None of the picks emits word or phoneme timings.

### Candidate table

| model | version / last release seen | license: code / weights | size / VRAM | Turing-OK? | control | timings | verdict |
|---|---|---|---|---|---|---|---|
| Chatterbox EN (orig) | PyPI 0.1.7, 2026-03-26 [3]; repo master pushed 2026-07-21 [2] | MIT / MIT [1][2] | 0.5B; t3_cfg 2129.7 MB + s3gen 1056.5 MB [10] | no dtype cast in the load path, so presumably FP32; not benchmarked [5] | clone, `exaggeration`, `cfg_weight` [1] | none | **PICK, both roles** |
| Chatterbox Multilingual V3 | opt-in on master since 3f35dfc (2026-05-01); the 0.1.7 wheel loads only v2 [3][6] | MIT / MIT [1] | 500M [1] | as above | clone + `exaggeration`; includes "en"; "improves… accent preservation across languages" [1][6] | none | watch (git-only) |
| Chatterbox Turbo / Nano | Turbo HF 2025-12-15; Nano HF 2026-07-21, master only [4][7][8] | MIT / MIT [7][8] | 350M / 110M; Nano "3x faster than realtime on 8 cores" (vendor CPU) [7] | not verified | clone + `[tags]`; no exaggeration/cfg [4][9] | none | speed fallback |
| chatterbox-flash | PyPI 0.1.0, 2026-05-28 [11] | MIT / (Chatterbox weights) [11] | — | default `gpu` backend is torch SDPA in bf16; `--dtype {bf16,fp16,fp32}` override; FlashInfer is an optional extra [11][12] | `exaggeration`, `cfg_scale` [11] | none | untested on Turing |
| Kokoro-82M | v1.0 2025-01-27; PyPI 0.9.4, 2025-04-05 [13] | Apache-2.0 / Apache-2.0 [13] | 82M [13] | small; not benchmarked | speed (float or callable), voice averaging; **no cloning** ("no encoder release") [13][15] | **per-word start_ts/end_ts from predicted durations** [15] | lip-sync fallback. British 4F/4M voices, best is bf_emma at B-; uses the GPL espeak-ng `en-gb` fallback [14][16] |
| Zonos v0.1-transformer | HF 2025-06-03; last repo push 2025-03-05 [17][18] | Apache-2.0 / Apache-2.0 [17][18] | 1.62B, BF16 [17] | **bf16 hard-coded in model.py** [19]; card and README disagree [17][18] | emotion vector, pitch_std, speaking_rate, `en-gb-x-rp` [20] | none | conditional Phineas alternative (needs a patch) |
| ZONOS1-GGUF | HF 2026-07-15 [21] | — / Apache-2.0 [21] | `zonos1-f16.gguf` 3.25 GB [21] | its runtime, github.com/Zyphra/zonos1.cpp, returns **404** [21] | same as Zonos | none | cannot be used today |
| ZONOS2 | HF 2026-06-22 [22] | MIT / Apache-2.0 [22] | model.pth 15.34 GB, bf16 [22] | no (Linux-only, bf16, sgl_kernel) [22]; the zonos2.cpp port has no license [23] | emotion sliders, valence [22] | none | out |
| IndexTTS-2 / 2.5 | v2.5.0 and v2.0.0, both 2026-08-13 [25] | bilibili custom / bilibili custom [24] | ~0.8B, "roughly 6 GB" [26] | README: FP16 for v2, BF16 for 2.5 [25] | 8-float emotion vector, emotion reference audio, emo_alpha, emotion from text, duration_factor [25][26] | none | CONDITIONAL (legal) |
| Qwen3-TTS 1.7B Base / VoiceDesign (+0.6B Base) | HF created 2026-01-21 [27] | Apache-2.0 / Apache-2.0 [27] | 1.93B BF16 [27] | examples are bf16 + FA2 [27][30] | VoiceDesign instruct; Base = 3-second clone [27] | none | reference-clip generator; pins transformers==4.57.3 [29] |
| VoxCPM2 | 2.0.3, 2026-05-11 [31] | Apache-2.0 / Apache-2.0 [31] | 2B; bf16 "~8 GB" [31] | fp16 drift risk (MPS note) [32] | voice design + style-guided clone [31] | none | Seraphina #2, offline only |
| Maya1 | — | — / Apache-2.0 [33] | "16GB+ VRAM" [33] | no | voice design (British example) + emotion tags [33] | none | out (VRAM) |
| CosyVoice 3 0.5B | HF 2026-02-03 [34] | Apache-2.0 / Apache-2.0 [34] | 0.5B | `fp16=False` by default [34] | fixed instruct list (e.g. "as loudly as possible") [34] | none | too coarse; pins torch 2.3.1 / transformers 4.51.3 [34] |
| Dia 1.6B | HF 0626 [35] | Apache-2.0 / Apache-2.0 [35] | fp16 "~4.4GB" [35] | fp16 row exists; "tested on only GPUs" [35] | audio-prompt clone; `(laughs)`, `(sighs)` and other tags [35] | none | possible, not preferred |
| Dia2 2B | HF 2025-12-01 [36] | Apache-2.0 / Apache-2.0; Mimi codec is CC-BY-4.0 [36] | — | CLI dtype choices are auto / float32 / bfloat16 [36] | prefix conditioning | **word timestamps** [36] | watch; "intended for research and educational use" (see contradictions) |
| Pocket TTS | v3.2.0, 2026-09-23 [37] | MIT / CC-BY-4.0 [37] | 100M, runs on CPU [37] | CPU | wav clone; no emotion control | only via a community fork [37] | neutral CPU fallback; the cloning repo is gated and forbids cloning "without explicit and lawful consent" [37] |
| Kyutai TTS 1.6B | HF 2025-09 [38] | MIT (Python) / CC-BY 4.0 [38] | "actually 1.8B" [38] | — | precomputed embeddings only [38] | — | out |
| Orpheus 3B ft | HF 2025-05-06 [39] | Apache-2.0 tag, but base_model is Llama-3.2-3B-Instruct [39] | 3.78B F32 [39] | no | presets tara…zoe + 8 tags [39] | none | out |
| Sesame CSM-1B | — | Apache-2.0, gated [40] | — | — | context only; "not fine-tuned on any specific voice" [40] | none | out |
| StyleTTS2 | — | MIT / no rights grant, only a disclosure condition [41] | — | "noise… in older GPUs" [41] | style | — | **DISQUALIFIED** (weights unlicensed) |
| MeloTTS EN | HF 2024-12-24 [42] | MIT / MIT [42] | "CPU real-time" [42] | yes | speed; British preset [42] | — | no expressiveness |
| F5-TTS | 1.1.22 | MIT / **CC-BY-NC** [43] | — | — | — | — | **DISQUALIFIED** |
| XTTS-v2 | — | — / **CPML**: "only non-commercial use… and its outputs" [44] | — | — | — | — | **DISQUALIFIED** |
| Fish S2 Pro | — | Fish Audio Research License [45] | — | — | — | — | **DISQUALIFIED** |
| Higgs TTS 3 / 2 | HF 2026-09-04 / 2026-06-25 | v3: research and non-commercial, "does **not** cover… embedding the model in a product" [46]; v2: Llama-3-based community license [47] | — | no | — | — | **DISQUALIFIED** / out |
| Breeze TTS 2 | HF created 2026-08-25 [53] | Apache-2.0 / "research and non-commercial use only", which includes self-hosted outputs [53] | — | — | — | — | **DISQUALIFIED** |
| VibeVoice 1.5B | — | MIT tag, but "limited to research purpose use"; audible AI disclaimer in every output [48] | — | — | — | — | EXCLUDED (contradiction) |
| Dramabox | — | LTX-2 Community [49] | "~24 GB peak" [49] | no | prompt-driven | — | out |
| Step-Audio-EditX | — | Apache-2.0 (code) / not stated [50] | 3B; "12GB is just a critical value" [50] | no | emotion and style editing | — | out |
| MOSS-TTS v1.5 / VoiceGenerator | — | Apache-2.0 [51] | v1.5 8.49B BF16 [51] | v1.5 no | VoiceGenerator: text-to-timbre design [51] | — | VoiceGenerator not evaluated |
| NeuTTS Air / 2E | — | Air Apache 2.0; 2E "NeuTTS Open License 1.0" [52] | — | — | Air: clone; 2E: "4 fixed speakers" [52] | — | neutral fallback only |

### Licensable reference clips
- **Voice-Zero** [54][55]: "Unless otherwise noted, all files in this repository are under the CC0 license", sourced from LibriVox, Archive.org and freesound.
  - RP-labelled clips: `simon_evers` (male), `ruth_golding` (female), `karen_savage2` (female, label is a guess).
  - `voices-emotion/` holds CC0 synthetic variants made with Chatterbox in 13 emotions (anger, calm, confused, enthused, excited, frustrated, happy, neutral, sad, shout, surprised, tired, worried) for simon_evers, ruth_golding, karen_savage2, karen_savage, stuart_bell and anna_simon.
  - GitHub's license detector reports NOASSERTION for the repo; the CC0 grant is stated in LICENSE.md text.
- **LibriVox** [56]: recordings are "public domain (definitely in the USA…)… anyone can use all our recordings however they wish (even to sell them)."
- **kyutai/tts-voices** [57]:
  - `voice-donations/` (228 voices) and `voice-zero/` are CC0. Unmute's own recordings "you may use… as CC0", except p329_022, which is from VCTK and so CC BY 4.0.
  - `alba-mackenna/` is CC BY 4.0.
  - `expresso/` and `ears/` are **non-commercial. Do not use them.**
- **VCTK** [58]: CC BY 4.0, "110 English speakers with various accents". Attribution is required.

### Stack notes
- **MODEL_STACK's Chatterbox line is confirmed, with corrections.**
  - The repo's default branch is `master`, not `main`, so `/blob/main/` URLs return 404 [2].
  - Nano and Multilingual V3 are on master only [3][4][6].
  - Flash ships as its own PyPI package, `chatterbox-flash` 0.1.0 [11].
- **Each engine needs its own venv because the pins clash:**
  - Chatterbox: transformers==5.2.0 [2]
  - qwen-tts: transformers==4.57.3 [29]
  - CosyVoice: torch 2.3.1 and transformers 4.51.3 [34]
- **GPL runtime dependencies:**
  - Kokoro pulls in phonemizer-fork (GPLv3+) and espeak-ng (GPL-3.0) [16]. Kokoro's British voices use the espeak-ng `en-gb` fallback [14].
  - Zonos also needs eSpeak [17].
  - This is the same policy question as piper-tts.
- **Lip-sync:** only Kokoro [15] and Dia2 [36] return word timings natively. Timings for Chatterbox output would need a separate forced aligner, which was not researched.

## Sources
[1] FIRST-PARTY · HF lastModified 2026-06-10; accessed 2026-09-23 · https://huggingface.co/ResembleAI/chatterbox — license: mit; '0.5B Llama backbone'; 'Unique exaggeration/intensity control'; defaults 'exaggeration=0.5, cfg=0.5'; 'If the reference speaker has a fast speaking style, lowering cfg to around 0.3 can improve pacing'; 'Try lower cfg values (e.g. ~0.3) and increase exaggeration to around 0.7 or higher… slower, more deliberate pacing'; accent-inheritance note (cross-language only); 'Every audio file generated by Chatterbox includes… Perth… Watermarker'; Multilingual V3 500M 'Improves voice identity and accent preservation across languages'
[2] FIRST-PARTY · accessed 2026-09-23 (repo default_branch master, license MIT, pushed 2026-07-21) · https://github.com/resemble-ai/chatterbox/blob/master/pyproject.toml — version = "0.1.7"; "torch==2.6.0; python_version < '3.14'"; "transformers==5.2.0"; resemble-perth git dependency; /blob/main/ returns 404
[3] FIRST-PARTY · uploaded 2026-03-26T08:43:46; wheel inspected 2026-09-23 · https://pypi.org/project/chatterbox-tts/0.1.7/ — latest release is 0.1.7 (MIT); wheel contains 0 files referencing 'nano'; wheel mtl_tts.py loads only 't3_mtl23ls_v2.safetensors'
[4] FIRST-PARTY · commit 5de7a54 2026-07-21; accessed 2026-09-23 · https://github.com/resemble-ai/chatterbox/blob/master/src/chatterbox/tts_turbo.py — NANO_REPO_ID = "ResembleAI/chatterbox-nano"; 'CFG, min_p and exaggeration are not supported by the {self.model_label} version and will be ignored.'
[5] FIRST-PARTY · accessed 2026-09-23 · https://github.com/resemble-ai/chatterbox/blob/master/src/chatterbox/tts.py — tts.py:149 't3.to(device).eval()' with no dtype/half/bfloat cast; models/t3/t3.py:62-63 'self.cfg = LlamaConfig(**config_dict)' / 'self.tfmr = LlamaModel(self.cfg)' (FP32-by-default is inferred)
[6] FIRST-PARTY · commit 3f35dfc 2026-05-01 'Add opt-in v3 multilingual checkpoint'; accessed 2026-09-23 · https://github.com/resemble-ai/chatterbox/blob/master/src/chatterbox/mtl_tts.py — DEFAULT_MULTILINGUAL_T3_MODEL = "t3_mtl23ls_v2.safetensors"; "v3": "t3_mtl23ls_v3.safetensors"; "en": "English"; prepare_conditionals(..., exaggeration=0.5)
[7] FIRST-PARTY · HF lastModified 2026-07-21 · https://huggingface.co/ResembleAI/chatterbox-nano — license mit; 'Built on a streamlined 110M parameter architecture, Nano delivers high-quality speech on CPU - 3x faster than realtime on 8 cores'; 'ChatterboxTurboTTS.from_pretrained(device="cuda", nano=True)'; t3_nano_v1.safetensors 869.9 MB
[8] FIRST-PARTY · HF lastModified 2025-12-15 · https://huggingface.co/ResembleAI/chatterbox-turbo — license mit; '350M parameter architecture'; 'Paralinguistic tags are now native to the Turbo model, allowing you to use [cough], [laugh], [chuckle], and more'
[9] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/ResembleAI/chatterbox-turbo/blob/main/added_tokens.json — "[dramatic]": 50262; "[narration]": 50263; "[sarcastic]": 50266; "[whispering]": 50260 (efficacy undocumented)
[10] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/api/models/ResembleAI/chatterbox?blobs=true — t3_cfg.safetensors 2129.7 MB; s3gen.safetensors 1056.5 MB; t3_mtl23ls_v3.safetensors 2144.0 MB; s3gen_v3.safetensors 1056.4 MB
[11] FIRST-PARTY · uploaded 2026-05-28T22:47:15 · https://pypi.org/project/chatterbox-flash/0.1.0/ — 0.1.0, MIT; requires 'chatterbox-tts>=0.1.7'; 'flashinfer-python>=0.2; extra == "flashinfer"' (optional); generate() exaggeration, cfg_scale
[12] FIRST-PARTY · repo pushed 2026-06-01; accessed 2026-09-23 · https://github.com/resemble-ai/chatterbox-flash/blob/master/README.md — '| gpu (default) | torch SDPA | cuda | bf16 | on'; 'Override the per-backend compute dtype with --dtype {bf16,fp16,fp32}'
[13] FIRST-PARTY · HF lastModified 2025-04-10; PyPI kokoro 0.9.4 2025-04-05 · https://huggingface.co/hexgrad/Kokoro-82M — license apache-2.0; 'open-weight TTS model with 82 million parameters'; 'Decoder only: no diffusion, no encoder release'; '| v1.0 | 2025 Jan 27 |'
[14] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md — 'British English: 4F 4M'; 'espeak-ng en-gb fallback'; bf_emma B-, bm_fable C, bm_george C, bm_lewis D+
[15] FIRST-PARTY · accessed 2026-09-23 · https://github.com/hexgrad/kokoro/blob/main/kokoro/pipeline.py — 'If multiple voices are requested, they are averaged.'; 'speed: Union[float, Callable[[int], float]] = 1'; 'KPipeline.join_timestamps(tks, output.pred_dur)'; 't.start_ts = left / MAGIC_DIVISOR'
[16] FIRST-PARTY · accessed 2026-09-23 (phonemizer-fork PyPI classifier GPLv3+; espeak-ng/espeak-ng GitHub license GPL-3.0) · https://github.com/hexgrad/misaki/blob/main/pyproject.toml — en = ["num2words", "spacy", "spacy-curated-transformers", "phonemizer-fork", "espeakng-loader", "torch", "transformers"]; GPL runtime deps
[17] FIRST-PARTY · HF lastModified 2025-06-03 · https://huggingface.co/Zyphra/Zonos-v0.1-transformer — license apache-2.0; 'only supports Linux systems… with recent NVIDIA GPUs (3000-series or newer, 6GB+ VRAM)'; 'phonemization via eSpeak'; safetensors {'BF16': 1624411136}
[18] FIRST-PARTY · repo Apache-2.0, last push 2025-03-05 · https://github.com/Zyphra/Zonos/blob/main/README.md — 'GPU: 6GB+ VRAM, Hybrid additionally requires a 3000-series or newer Nvidia GPU'; 'Zonos can also run on CPU provided there is enough free RAM'
[19] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Zyphra/Zonos/blob/main/zonos/model.py — L79 'model = cls(config, backbone_cls).to(device, torch.bfloat16)'; L95 'spk_embedding.unsqueeze(0).bfloat16()'; L198 setup_cache dtype default torch.bfloat16
[20] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Zyphra/Zonos/blob/main/zonos/conditioning.py — 'Happiness, Sadness, Disgust, Fear, Surprise, Anger, Other, Neutral'; '60-150 for expressive speech'; 'Speaking rate in phonemes per minute (0 to 40)'; language codes 'en-gb', 'en-gb-x-rp'
[21] FIRST-PARTY · HF created 2026-07-15 · https://huggingface.co/Zyphra/ZONOS1-GGUF — license apache-2.0; 'zonos1-f16.gguf | 3.25 GB | F16 backbone — lossless from the bf16 checkpoint'; points to github.com/Zyphra/zonos1.cpp, which returned HTTP 404 on 2026-09-23
[22] FIRST-PARTY · repo MIT; HF Zyphra/ZONOS2 lastModified 2026-06-22 · https://github.com/Zyphra/ZONOS2 — 'Platform Support: Linux only (x86_64)'; emotion_sliders, emotion_valence; HF license apache-2.0; model.pth 15.34 GB
[23] FIRST-PARTY · pushed 2026-07-28 · https://github.com/Zyphra/zonos2.cpp — GitHub API license null (no license)
[24] FIRST-PARTY · accessed 2026-09-23 · https://github.com/index-tts/index-tts/blob/main/LICENSE — 'Derivative Work: … (i) any modification of the Model, model outputs, or their derivatives'; 'Use… publicly displaying'; royalty-free license; 100 million MAU / RMB 1 billion threshold; revocation on breach
[25] FIRST-PARTY · releases v2.5.0 and v2.0.0 published 2026-08-13 · https://github.com/index-tts/index-tts/blob/main/README.md — 'For commercial usage and cooperation, please contact indexspeech@bilibili.com'; 'enable BF16 (IndexTTS-2.5) / FP16 (IndexTTS-2)'; emo_audio_prompt + emo_alpha; use_emo_text
[26] FIRST-PARTY · HF lastModified 2026-08-12 · https://huggingface.co/IndexTeam/IndexTTS-2.5 — license_name bilibili-model-license; 'Parameters: ~0.8B (GPT backbone)'; 'roughly 6 GB of VRAM'; '[happy, angry, sad, afraid, disgusted, melancholic, surprised, calm]'; duration_factor
[27] FIRST-PARTY · HF created 2026-01-21 · https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base — license apache-2.0; '#### Voice Design then Clone… use the VoiceDesign model to synthesize a short reference clip that matches your target persona'; 0.6B-Base '3-second rapid voice clone'; examples dtype=torch.bfloat16, attn_implementation="flash_attention_2"; BF16 1,928,677,440 params; VoiceDesign repo apache-2.0
[28] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice — preset speakers: English only Ryan and Aiden ('Sunny American male voice'); no British preset
[29] FIRST-PARTY · accessed 2026-09-23 · https://github.com/QwenLM/Qwen3-TTS/blob/main/pyproject.toml — "transformers==4.57.3"
[30] FIRST-PARTY · accessed 2026-09-23 · https://github.com/Dao-AILab/flash-attention/blob/main/README.md — 'For Turing GPUs (T4, RTX 2080), see the separate flash-attention-turing repo'; 'bf16 requires Ampere, Ada, or Hopper GPUs'
[31] FIRST-PARTY · HF lastModified 2026-08-18; GitHub release 2.0.3 2026-05-11 · https://huggingface.co/openbmb/VoxCPM2 — license apache-2.0; '2B parameters'; 'Controllable Cloning — Clone any voice from a short clip, with optional style guidance to steer emotion, pace, and expression'; '| dtype | bfloat16 |'; '| VRAM | ~8 GB |'
[32] FIRST-PARTY · accessed 2026-09-23 · https://github.com/OpenBMB/VoxCPM/blob/main/src/voxcpm/model/utils.py — 'On Apple Silicon (MPS), bfloat16/float16 produce enough numerical drift in the diffusion AR loop that the output is glitched… float32 is the only stable option today. CUDA and CPU keep whatever the checkpoint was trained with.'
[33] FIRST-PARTY · HF lastModified 2026-07-11 · https://huggingface.co/maya-research/maya1 — license apache-2.0; 'Male voice in their 40s with a British accent. low pitch, gravelly timbre, slow pacing'; 'Single GPU with 16GB+ VRAM'
[34] FIRST-PARTY · HF Fun-CosyVoice3-0.5B-2512 lastModified 2026-02-03 · https://github.com/FunAudioLLM/CosyVoice — common.py instruct list e.g. 'Please say a sentence as loudly as possible.'; requirements.txt torch==2.3.1, transformers==4.51.3; cli/cosyvoice.py fp16=False; HF license apache-2.0
[35] FIRST-PARTY · repo Apache-2.0, pushed 2025-11-19; HF Dia-1.6B-0626 apache-2.0 · https://github.com/nari-labs/dia/blob/main/README.md — '| float16 | x2.2 | x1.3 | ~4.4GB |'; 'Dia has been tested on only GPUs'; (laughs), (sighs) nonverbal tags
[36] FIRST-PARTY · HF lastModified 2025-12-01 · https://huggingface.co/nari-labs/Dia2-2B — license apache-2.0; 'word timestamps relative to Mimi's ~12.5 Hz frame rate'; 'All third-party assets (Kyutai Mimi codec, etc.) retain their original licenses' (kyutai/mimi cc-by-4.0); 'intended for research and educational use'; dia2/cli.py choices=["auto", "float32", "bfloat16"]
[37] FIRST-PARTY · release v3.2.0 published 2026-09-23T15:47:24Z · https://huggingface.co/kyutai/pocket-tts-without-voice-cloning — license cc-by-4.0; code MIT (kyutai-labs/pocket-tts); '100M parameters'; '--voice… plain wav file… for voice cloning'; pocket-tts-timestamped community fork; kyutai/pocket-tts gated 'auto' with 'voice impersonation or cloning without explicit and lawful consent' prohibited
[38] FIRST-PARTY · HF 2025-09 (per researcher/verifier); accessed 2026-09-23 · https://huggingface.co/kyutai/tts-1.6b-en_fr — 'actually 1.8B parameters'; 'Model weights are licensed under CC-BY 4.0'; 'restrict the voice cloning ability to the use of pre-computed voice embeddings'; Python code MIT per github.com/kyutai-labs/delayed-streams-modeling README (verifier-checked)
[39] FIRST-PARTY · HF lastModified 2025-05-06 · https://huggingface.co/canopylabs/orpheus-3b-0.1-ft — license apache-2.0; base_model ['meta-llama/Llama-3.2-3B-Instruct', …]; F32 3,782,986,752; GitHub canopyai/Orpheus-TTS README presets 'tara, leah, jess, leo, dan, mia, zac, zoe' and 8 emotive tags
[40] FIRST-PARTY · accessed 2026-09-23 · https://github.com/SesameAILabs/csm — HF sesame/csm-1b apache-2.0, gated; 'not been fine-tuned on any specific voice'; needs Llama-3.2-1B access
[41] FIRST-PARTY · accessed 2026-09-23 · https://github.com/yl4579/StyleTTS2/blob/main/README.md — 'Code: MIT License'; pre-trained models carry only a disclosure condition; 'numerical float differences in older GPUs'
[42] FIRST-PARTY · HF lastModified 2024-12-24 · https://huggingface.co/myshell-ai/MeloTTS-English — license mit; English (British) preset; 'Fast enough for CPU real-time inference'
[43] FIRST-PARTY · release 1.1.22 2026-07-23 · https://github.com/SWivid/F5-TTS/blob/main/README.md — 'Our code is released under MIT License. The pre-trained models are licensed under the CC-BY-NC license'
[44] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/coqui/XTTS-v2/blob/main/LICENSE.txt — 'This license allows only non-commercial use of a machine learning model and its outputs.'
[45] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/fishaudio/s2-pro — license_name fish-audio-research-license; 'Research and non-commercial use is permitted free of charge. Commercial use requires a separate license'
[46] FIRST-PARTY · HF lastModified 2026-09-04 · https://huggingface.co/bosonai/higgs-tts-3-4b — license_name boson-higgs-tts-3-research-and-non-commercial-license; 'does not cover… embedding the model in a product or application'
[47] FIRST-PARTY · HF lastModified 2026-06-25 · https://huggingface.co/bosonai/higgs-tts-2-3b-base — LICENSE 'based upon the Meta Llama 3 Community License Agreement'
[48] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/microsoft/VibeVoice-1.5B — license mit; 'The VibeVoice model is limited to research purpose use'; 'Embedded an audible disclaimer… into every synthesized audio file'
[49] FIRST-PARTY · HF lastModified 2026-05-13 · https://huggingface.co/ResembleAI/Dramabox — license_name ltx-2-community; Gemma 3 12B text embeddings; 'VRAM: ~24 GB peak'
[50] FIRST-PARTY · HF 2026-02-14 · https://huggingface.co/stepfun-ai/Step-Audio-EditX — '3B-parameter'; '12GB is just a critical value, and 16GB GPU memory shoule be safer'; 'The code in this open-source repository is licensed under the Apache 2.0 License' (no weights license tag)
[51] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator — license apache-2.0; 'voice design model that creates speaker timbres directly from free-form text'; MOSS-TTS-v1.5 apache-2.0, BF16 8,489,841,664 params
[52] FIRST-PARTY · accessed 2026-09-23 · https://github.com/neuphonic/neutts/blob/main/README.md — '| License | Apache 2.0 | NeuTTS Open License 1.0 | NeuTTS Open License 1.0 |'; NeuTTS-2E '4 fixed speakers'
[53] FIRST-PARTY · HF created 2026-08-25; lastModified 2026-09-09 · https://huggingface.co/BreezeBlue/Breeze-TTS-2 — 'Source code is licensed under Apache 2.0. Breeze TTS 2 model weights, derivative models, and self-hosted outputs are for research and non-commercial use only.'
[54] FIRST-PARTY · repo pushed 2026-05-14 · https://github.com/OwenTyme/voice-zero/blob/main/voices/README.md — 'simon_evers.flac | English, Public School (Received Pronunciation) | Celebration of Dialects and Accents, Vol 2, Track 18'; 'ruth_golding.flac | English, Received Pronunciation (No regional accent) | Celebration… Vol 1, Track 4'; 'karen_savage2.flac | English, Received Pronunciation | The Voyages of Doctor Dolittle'; accents 'often based on guesswork… though… Celebration of Dialects and Accents should be accurate'; LICENSE.md 'all files in this repository are under the CC0 license'
[55] FIRST-PARTY · repo pushed 2026-05-14 · https://github.com/OwenTyme/voice-zero/blob/main/voices-emotion/README.md — 13 emotions list; folders for simon_evers, ruth_golding, karen_savage2, karen_savage, stuart_bell, anna_simon; synthetic via Chatterbox; maintainer report 'Chatterbox has a strange tendency to babble incoherently, scream… randomly shouts curse words' (secondary evidence about Chatterbox)
[56] FIRST-PARTY · accessed 2026-09-23 · https://librivox.org/pages/public-domain/ — 'all our recordings are public domain (definitely in the USA, and maybe in your country as well…). This means anyone can use all our recordings however they wish (even to sell them).'
[57] FIRST-PARTY · HF lastModified 2026-03-09 · https://huggingface.co/kyutai/tts-voices — voice donations 'licensed as CC0', '228 voices'; unmute-prod-website 'our own recordings and you may use them as CC0' (p329_022 from VCTK = CC BY 4.0); alba-mackenna 'CC BY 4.0'; voice-zero 'CC0'; expresso/ears 'Non-commercial use only'
[58] FIRST-PARTY · issued 2019-11-13; accessed 2026-09-23 · https://datashare.ed.ac.uk/handle/10283/3443 — 'Creative Commons Attribution 4.0 International Public License'; '110 English speakers with various accents'

## Contradictions (first-party vs first-party — unresolved)
- Zonos v0.1 GPU requirement. The HF card (https://huggingface.co/Zyphra/Zonos-v0.1-transformer) says 'only supports Linux systems… with recent NVIDIA GPUs (3000-series or newer, 6GB+ VRAM)'. The GitHub README (https://github.com/Zyphra/Zonos/blob/main/README.md) says 'GPU: 6GB+ VRAM, Hybrid additionally requires a 3000-series or newer Nvidia GPU', lists macOS, and says 'Zonos can also run on CPU'. Not resolved. Separately, model.py hard-codes bfloat16 (https://github.com/Zyphra/Zonos/blob/main/zonos/model.py).
- VibeVoice. The HF license tag is 'mit' (https://huggingface.co/microsoft/VibeVoice-1.5B), but the same card says 'The VibeVoice model is limited to research purpose use'. Not resolved; excluded.
- IndexTTS. The LICENSE (https://github.com/index-tts/index-tts/blob/main/LICENSE) grants a 'royalty-free limited license to Use', where Use includes 'publicly displaying', below 100M MAU / RMB 1B revenue. The README (https://github.com/index-tts/index-tts/blob/main/README.md) says 'For commercial usage and cooperation, please contact indexspeech@bilibili.com'. Not resolved; conditional.
- Dia2. The card license is apache-2.0 (https://huggingface.co/nari-labs/Dia2-2B), but the same card says the model is 'intended for research and educational use'. Not resolved.

## Could not confirm
- No first-party VRAM, latency or correctness benchmark for any candidate on an RTX 2080 Ti (sm_75) or an i9-9900K. The ~4 GB GPU headroom is arithmetic from the brief (11 GB minus ~7 GB Ollama), not a measurement.
- Chatterbox runtime VRAM and CPU speed of the original 500M model. FP32-by-default is inferred from the load path (no dtype cast), not documented. Whether an fp16 cast works was not tested.
- Whether Chatterbox's English 500M model reproduces an RP accent from an RP reference. The vendor documents accent inheritance only for cross-language transfer.
- Whether the Turbo/Nano tokens [sarcastic], [dramatic], [narration] and [whispering] change delivery. They exist in added_tokens.json, but the card documents only [cough]/[laugh]/[chuckle] 'and more'.
- Whether chatterbox-flash runs correctly on Turing with --dtype fp16 or fp32.
- Nano's '3x faster than realtime on 8 cores' on an i9-9900K. Nano needs a git install from master.
- Whether Chatterbox Multilingual V3 (opt-in on master) with language 'en' preserves a British accent better than the English 500M model.
- Zonos v0.1-transformer on a 2080 Ti: the model code hard-codes bf16 and the HF card vs README conflict. Whether patching it to fp16/fp32 gives clean output is unknown.
- ZONOS1-GGUF usability: its runtime repo github.com/Zyphra/zonos1.cpp returned 404 on 2026-09-23.
- Qwen3-TTS fp16 with sdpa correctness on Turing, runtime VRAM, and whether VoiceDesign honours a British-accent request.
- VoxCPM2 fp16/fp32 stability on CUDA Turing and its fp32 memory footprint.
- Maya1 on 11 GB (third-party quants only).
- A legal reading of the IndexTTS bilibili license for a permanent public installation, given that it reaches model outputs.
- Vocal range of the reference voices: whether simon_evers sounds like a baritone and ruth_golding/karen_savage2 like mezzos. No listening was done.
- Whether the kyutai voice-donations set (CC0) contains suitable British voices; not enumerated.
- A forced-alignment tool and its license, for word/phoneme timing of Chatterbox output; not researched.
- License of the community pocket-tts-timestamped fork.
- Whether Llama 3.2 Community License terms attach to Orpheus 3B despite the apache-2.0 tag (base_model is Llama-3.2-3B-Instruct).
- Whether the Voice-Zero voices-emotion clips (generated with Chatterbox) carry the Perth watermark.
- No listening or quality comparison of the two theatrical registers across any model.

## Dropped claims (refuted or unsupported in verification)
- chatterbox-flash '520M decoder': no first-party parameter count; only a config label was seen.
- chatterbox-flash 'defaults to bf16 + FlashInfer': corrected. The default GPU backend is torch SDPA in bf16; FlashInfer is an optional extra; the README documents --dtype {bf16,fp16,fp32}.
- Orpheus 'American presets': unsourced. The first-party README lists 'tara, leah, jess, leo, dan, mia, zac, zoe' for English.
- Higgs TTS 3 'code Apache-2.0': no first-party source ties its inference code to the Apache-2.0 repo.
- Chatterbox 'Nano on git main' and the /blob/main/ URLs for c4, c6, c12: the default branch is master, and main URLs return 404. Corrected to master URLs.
- Chatterbox 'accent comes from the reference clip' as a documented property of the English model: downgraded to inference (documented only for cross-language transfer).
- Zonos v0.1-transformer as an unconditional 'alt pick for Phineas': downgraded to CONDITIONAL, because model.py hard-codes bf16 and the weights are BF16.
- MOSS-VoiceGenerator '1.7B' in the table: removed (the card and HF safetensors counts disagree; not re-checked).

## DO NOT QUOTE (low/unknown)
- [low] Chatterbox runs FP32 on Turing by default — Inferred from source (no dtype cast in tts.py/t3.py), not documented; not run on a 2080 Ti.
- [low] Chatterbox will reproduce a British/RP accent from simon_evers or ruth_golding — Vendor documents accent inheritance only for cross-language transfer; not tested.
- [unknown] Chatterbox (any variant) fits alongside ~7 GB Ollama in 11 GB — Only checkpoint sizes seen (~3.2 GB fp32 files); runtime VRAM not measured.
- [unknown] Turbo/Nano [sarcastic]/[dramatic]/[narration]/[whispering] tags produce the intended delivery — Tokens exist in added_tokens.json; behaviour undocumented.
- [unknown] chatterbox-flash has a '520M decoder' — Only a config label 'Llama_520M' was seen by the verifier; no first-party parameter count. Dropped.
- [unknown] chatterbox-flash works on Turing with --dtype fp16/fp32 — Override is documented; Turing behaviour untested.
- [unknown] Chatterbox Nano is 3x realtime on the i9-9900K — Vendor figure is for an unspecified 8-core CPU.
- [low] Chatterbox Multilingual V3 improves British accent retention in English — Card claim is about accent preservation 'across languages'; English-to-English not addressed.
- [unknown] Zonos v0.1-transformer runs on the RTX 2080 Ti — bf16 hard-coded in model.py; HF card and GitHub README contradict each other on GPU support.
- [unknown] ZONOS1-GGUF F16 as a Turing workaround — Its runtime repo zonos1.cpp returns 404.
- [unknown] IndexTTS-2/2.5 is licensable for a permanent public MIT installation — Custom bilibili license reaches outputs, allows revocation; README routes commercial use to bilibili. Needs legal read.
- [unknown] Qwen3-TTS VoiceDesign can produce a convincing British RP reference on Turing — No British preset; examples use bf16 + FA2; untested.
- [unknown] VoxCPM2 runs cleanly in fp16 on CUDA Turing — Vendor code says bf16/fp16 drift glitches output on MPS; CUDA Turing untested; fp32 memory unknown.
- [low] karen_savage2 is RP — Not from the Celebration of Dialects volumes; Voice-Zero says such labels are 'often based on guesswork'.
- [unknown] simon_evers is a baritone / ruth_golding and karen_savage2 are mezzos — No listening done.
- [low] Chatterbox 'randomly shouts curse words' — Secondary field report from the Voice-Zero maintainer, not a vendor statement; use only as a reason to review output.
- [unknown] Orpheus presets are American — First-party README lists English presets without saying 'American'. Dropped.
- [unknown] Higgs TTS 3 inference code is Apache-2.0 — No first-party source ties Higgs TTS 3 code to the Apache-2.0 higgs-audio repo. Dropped.
- [low] MOSS-VoiceGenerator is 1.7B — Card table says 1.7B; verifier saw HF safetensors 2,114,118,656 params; not re-checked here.
- [low] ~4 GB free VRAM beside Ollama — Arithmetic from the brief, not measured on supercommons2.
- [unknown] Orpheus weights are purely Apache-2.0 — base_model is Llama-3.2-3B-Instruct; whether Llama license terms attach is unresolved.
- [unknown] Dia2 usable for a permanent public installation — Apache-2.0 license vs 'intended for research and educational use' disclaimer on the same card.
- [unknown] VibeVoice usable commercially — MIT tag vs 'limited to research purpose use'.
- [unknown] pocket-tts-timestamped fork license — Not checked.
- [unknown] kyutai voice-donations include usable British voices — Not enumerated.
- [unknown] GPL espeak-ng runtime dependency (Kokoro British path, Zonos) is acceptable — Policy call, same as piper-tts in MODEL_STACK.
- [unknown] Any ranking of models by quality on the Phineas/Seraphina registers — No listening comparison done.


---

# Track C — Qwen3.5-9B thinking default + ollama#14579 throughput scope
Primary mission track: no · Final confidence: high

## Answer
## Verdict

**C1: Qwen3.5-9B thinks by default.**
- **Qwen's official artifacts say ON.** With `enable_thinking` unset, the official template opens `<think>\n`. Only an explicit `enable_thinking=false` renders the empty `<think>\n\n</think>\n\n` [1][2]. The card agrees: "Qwen3.5 models operate in thinking mode by default" [3]. The repo has no `generation_config.json` [4].
- **Unsloth's "disabled by default" describes Unsloth's own GGUFs.** Its doc says "For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default" [11]. That holds for the 9B and 4B GGUFs Unsloth ships, whose embedded templates invert the condition [12][13]. It does not hold for the Qwen model.
- **This is a reconciliation by artifact, not a genuine contradiction.** No Unsloth text was found saying the inversion was deliberate.
- **Ollama `qwen3.5:9b` is also ON by default** [16][19][22].
- **`"think": false` on `/api/chat` disables thinking for qwen3.5** [20][21][23].
- **`/no_think` is not officially supported by Qwen3.5** [3], and nothing in Ollama's qwen3.5 renderer or parser handles it [20][22].

**C2: #14579 is not MoE-only, but nobody has reported the dense 9B.**
- The issue body is about Qwen3.5-35B-A3B [38]. Comments add the dense qwen3.5:27b [39][41]. None of the 12 comments mentions the 9B [38].
- The issue is OPEN. The only commit saying "Fixes #14579" is in a fork [44]. No release note cites the issue.
- The Ollama engine that was measured was removed in v0.30.0 [45][46].
- The more relevant risk for our RTX 2080 Ti is a separate llama.cpp Turing regression on the qwen35 architecture [49]. Ollama vendored it from v0.30.4 through v0.32.5 [51].
- No dense 9B text throughput versus llama.cpp has been measured on CUDA or Turing. Measure on supercommons2 before quoting any number.

## C1 evidence

| Artifact | Default when unset | Evidence (verbatim) |
|---|---|---|
| Qwen/Qwen3.5-9B `chat_template.jinja` (`tokenizer_config.json` is byte-identical) | **ON** | `{%- if enable_thinking is defined and enable_thinking is false %} {{- '<think>\n\n</think>\n\n' }} {%- else %} {{- '<think>\n' }}` [1][2] |
| Qwen3.5-9B card | **ON** | "Qwen3.5 will think by default before response." [3] |
| `generation_config.json` | absent | HF file list omits it; raw fetch returns 404 [4] |
| Template history | ON throughout | The 2026-02-27 upload always emitted `<think>\n`, with no switch [5]. The `enable_thinking` branch was added in commit ef3d031a90 on 2026-03-01 [4] |
| Official 0.8B / 2B | **OFF** | "Qwen3.5-0.8B operates in non-thinking mode by default" [6]; the 2B card says the same [7] |
| Official 4B / 27B / 35B-A3B | **ON** | Same "thinking mode by default" text and template branch as the 9B [8][9][10] |
| Unsloth doc (page "Last updated" 2026-08-13) | "disabled" | "As an example for Qwen3.5-9B to enable thinking (default is disabled)" [11] |
| Unsloth 9B and 4B GGUF embedded `tokenizer.chat_template` | **OFF** | `{%- if enable_thinking is defined and enable_thinking is true %} {{- '<think>\n' }} {%- else %} {{- '<think>\n\n</think>\n\n' }}` [12][13]. Unsloth also says "Qwen3.5 Small models have reasoning disabled by default." [14] |
| Ollama `qwen3.5:9b` (6488c96fa5fa, Q4_K_M, 6.6GB) | **ON** | No template layer. Config: `"renderer":"qwen3.5","parser":"qwen3.5","requires":"0.17.1"` [15][16]. Renderer: `&Qwen35Renderer{isThinking: true, emitEmptyThinkOnNoThink: true, ...}` [19]. Parser: `if thinkValue == nil { thinkingEnabled = true` [22] |

**How `think` works in Ollama for qwen3.5:**
- **Request override.** The request's value replaces the default: `if think != nil && think.Value != nil { isThinking = think.Bool()`. With thinking off, the renderer writes `<think>\n\n</think>\n\n`, which is the same prefill Qwen's template uses for `enable_thinking=false` [20]. A unit test asserts the "explicit no-think prefill" [21].
- **Docs.** "`false`: request no thinking output, if the model permits it. `null`: use the model default." [23]
- **`/api/show`.** From v0.34.3 it "advertises each model's thinking controls and default" [26]. For this renderer the code returns `Values: []any{false, true}, Default: r.isThinking` [20]. I read this from source and did not run it.

**Minimum Ollama version for how the repo calls the model:**
- `director/llm.py` sends `"think": False` plus `format: "json"` [36]. `director/stage_manager.py` does the same [37].
- On qwen3.5, `format` was ignored when `think=false`: #14645, filed against 0.17.6 [28].
- PR #15901 fixed it and is contained in the v0.31.2 tag [29]. The v0.31.2 notes say "Fixed structured output for thinking models when thinking is disabled" [30].
- The v0.34.4 notes add: "Structured outputs on thinking models now apply in a single pass" [27].

**`/no_think` on Qwen3.5:**
- The card says: "Qwen3.5 does not officially support the soft switch of Qwen3, i.e., `/think` and `/nothink`." [3]
- The qwen3.5 renderer and parser contain no `/no_think` handling [20][22].
- The repo appends `\n/no_think` to the system prompt in llm.py [36] and to the user prompt in stage_manager.py [37]. On qwen3.5 that string reaches the model as literal text. What the model then does with it has not been verified.
- This gap is specific to qwen3.5. Qwen3, today's `qwen3:8b` brain, documents the soft switch [33]. Ollama's Nemotron3Nano renderer does parse `/no_think` on its non-v35 path [25].

**Sampling mismatch when thinking is off:**
- The `qwen3.5:9b` params blob is `{"presence_penalty":1.5,"temperature":1,"top_k":20,"top_p":0.95}` [18]. The 2b and 4b tags share the same blob.
- That equals the card's "Thinking mode for general tasks" preset. The card's non-thinking general preset is `temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5` [3].
- The repo overrides only temperature [36][37], so `top_p` stays at 0.95 with `think:false`.

**Caveats:**
- **Ollama does not mirror Qwen's defaults for every size.** `qwen3.5:2b` uses the same `qwen3.5` renderer [17][19], so Ollama defaults it to ON while Qwen's 2B defaults to OFF [7]. For the 9B they agree.
- **An Unsloth HF GGUF would likely behave differently in Ollama.** GGUF models without an Ollama renderer "use llama-server's chat_template handling" [34], so pulling one would likely bring its inverted, OFF-by-default template. This is inferred from the code and not tested. Unsloth's doc also says "Currently no Qwen3.5 GGUF works in Ollama" [11]; that may be stale given the v0.30.0 GGUF note [46].
- **Anthropic-compatible `/v1/messages`.** In v0.34.4, `thinking.type=="disabled"` maps to `think=false`; v0.23.0 had only the "enabled" branch [31]. A missing `thinking` field leaves the model default (ON); #15287 is still OPEN [32]. The repo uses `/api/chat`.
- **License.** Qwen3.5-9B is tagged `license:apache-2.0` and ships an Apache 2.0 LICENSE [3][4]. Ollama's license blob for the tag is also Apache 2.0 [16].

## C2 evidence

**#14579 itself** ("Qwen3.5 Much slower speeds compared to LlamaCPP"; OPEN; 12 comments, the last on 2026-03-27) [38]:

| Who / where | Model | Hardware / setup | Reported |
|---|---|---|---|
| Body (author) [38] | Qwen3.5-35B-A3B, "same Q4 quant" | Win11, 3090Ti, 64GB RAM; Ollama version written as "0.7.15" | "15 to 20 tokens per second" on Ollama vs "100 tokens per second" on llama.cpp, "context 160000" |
| Comment 4004337758 [39] | qwen3.5:27b (7653528ba5cb), **dense** | RTX 3090 24GB, Ollama 0.17.5, "100% GPU", context 16000 | four inferences: "46 seconds for gemma3 and 3118 seconds for qwen3.5" |
| Comment 4063476310 (author) [41] | Qwen3.5-27B-Q4, **dense** | same 16k context; GPU not restated | "there is still double the performance when running straight llama cpp" (no matched-context numbers given) |
| Comment 4140398057 [43] | qwen3.5:35b-a3b-q4_K_M | RTX 5080 16GB, WSL2 | asks Ollama to expose `--n-cpu-moe`; llama.cpp "~70 tok/s on this hardware" |

- **No 9B.** A case-insensitive search for "9b" across all comments finds nothing [38]. Another commenter blames context overflow for the 27b case (GPU not named) [40]. Ollama's default context is 4k for "< 24 GiB VRAM" [35], so that explanation does not carry over to an 11 GB card.
- **No fix.**
  - The only commit that says "Fixes #14579" is phreer/ollama 82516fd, "correct GPU memory estimation for hybrid Mamba+Attention architectures". It lives in a fork and no upstream PR was found [44].
  - No release note cites #14579.
- **The measured engine is gone.**
  - In March an Ollama collaborator wrote: "ollama has its own implementation of the qwen3.5 model." [47]
  - PR #16031 (merged 2026-05-29): "llama-server ... is now the sole inference engine for GGUF-based models". It is contained in the v0.30.0 tag [45][46].
  - For MoE on CUDA after the switch: RTX 4090, `qwen3.6:35b-a3b`, 32K context, `-ngl 36`. Ollama 0.23.1 gave 30.7 tok/s and llama-server b9917 gave 57.7. Ollama 0.30.0 gave "~14–17 tok/s". v0.31.2-rc2 gave "50–60 tok/s ... within ~10–15% of raw llama.cpp master b9917" [48]. This is MoE and qwen3.6, not the 9B.

**Turing regression (llama.cpp #25162)** [49]:
- **The report.** "24-42% performance regression on Turing GPUs (RTX 2080 Ti, SM75) for Qwen3.5/Qwen3.6 models", on a 22GB 2080 Ti running upstream llama-server. Dense Qwen3.6-27B Q4_K_XL (Qwen35 arch) went from 27.20 tok/s at `bc81d47ab` to 20.76 tok/s at `9e58d4d69`.
- **The closure.** The reporter closed it on 2026-08-03 with "0b14b87d7 give：27.47 tok/s".
  - 0b14b87d7 is just a later master commit ("server: add notice for upcoming default port change") [64], and the close comment does not restate model or GPU.
  - The commit that actually fixed it is unidentified.
  - PR #25185 was suggested as the fix, but no Turing result was posted [49][50].
- **Same architecture as the 9B.** Qwen3.5-9B is `general.architecture qwen35`, `block_count 32`, `full_attention_interval 4` [12].

| Ollama tags (non-prerelease) | llama.cpp build [51] | has 9e58d4d69 (regression) | has #25185 | has 0b14b87d7 (reporter's recovered build) |
|---|---|---|---|---|
| v0.30.0 – v0.30.3 | b9452, b9479 | no | no | no |
| v0.30.4 – v0.30.11 | b9493 – b9781 | **yes** | no | no |
| v0.31.1 | b9840 [52] | **yes** | no | no |
| v0.31.2 – v0.32.1 | b9888 | **yes** | yes | no |
| v0.32.3 – v0.32.5 | b10091 | **yes** | yes | no |
| v0.32.6 onward (v0.33.0 = b10488, v0.34.4 = b11081) | b10242+ | yes | yes | **yes** |

Containment was checked with the GitHub compare API. Recovery through Ollama's own qwen35 blobs has not been measured.

**Adjacent reports** (user reports; see do_not_quote):
- #14715: qwen3.5:9b gave Xid 43/31 on a modified 22GB 2080 Ti with Ollama 0.17.5. Closed NOT_PLANNED after a log request [53].
- #17218: qwen3.5:4b Q4_K_M on an RTX 3070 Laptop with `think=false` VQA. 0.18.2 took 321.6 s wall-clock and 0.31.1 took 617.2 s. Accuracy fell from 81.4% to 64.2%. The collaborator's workaround is `LLAMA_ARG_IMAGE_MIN_TOKENS=1024` [54].
- #18038: high llama-server CPU use (open) [57].

**Bottom line for the repo:**
- The repo's current call shape (`think:false` plus `format:"json"`) needs Ollama v0.31.2 or later for qwen3.5 [30].
- On the 2080 Ti, avoid v0.30.4 through v0.32.5 (regression commit present, recovered build absent) [51].
- Get the Ollama version on hil and on supercommons2, then benchmark before quoting any throughput.

## Sources
[1] FIRST-PARTY · last changed in commit ef3d031a90 2026-03-01; accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/chat_template.jinja — Official template defaults thinking ON: lines 149-152 '{%- if enable_thinking is defined and enable_thinking is false %} {{- '<think>\n\n</think>\n\n' }} {%- else %} {{- '<think>\n' }}'
[2] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/tokenizer_config.json — tokenizer_config.json chat_template is string-identical to chat_template.jinja (verified by Python equality)
[3] FIRST-PARTY · README lastModified 2026-03-02 (commit c202236235); accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-9B — 'Qwen3.5 models operate in thinking mode by default'; 'Qwen3.5 will think by default before response.'; 'Qwen3.5 does not officially support the soft switch of Qwen3, i.e., `/think` and `/nothink`.'; disable via 'chat_template_kwargs': {'enable_thinking': False}; sampling presets (Thinking general: temperature=1.0, top_p=0.95, top_k=20, presence_penalty=1.5; Instruct general: temperature=0.7, top_p=0.8); license tag apache-2.0
[4] FIRST-PARTY · lastModified 2026-03-02T00:51:43Z; accessed 2026-09-23 · https://huggingface.co/api/models/Qwen/Qwen3.5-9B — File list has no generation_config.json (raw fetch 404); commit history: 21eca8a083 2026-02-27 'Upload folder', ef3d031a90 2026-03-01 'Upload 6 files'; tags include license:apache-2.0
[5] FIRST-PARTY · 2026-02-27 · https://huggingface.co/Qwen/Qwen3.5-9B/raw/21eca8a083/chat_template.jinja — Initial template: no enable_thinking branch (grep count 0); ends "{{- '<|im_start|>assistant\n<think>\n' }}"
[6] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-0.8B — '**Qwen3.5-0.8B operates in non-thinking mode by default**.'; template uses 'enable_thinking is defined and enable_thinking is true'
[7] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-2B — '**Qwen3.5-2B operates in non-thinking mode by default**.'; template uses 'enable_thinking is true' branch
[8] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-4B — 'Qwen3.5 models operate in thinking mode by default'; template uses 'enable_thinking is false' branch
[9] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-27B — 'Qwen3.5 models operate in thinking mode by default'; template 'enable_thinking is false' branch
[10] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-35B-A3B — 'Qwen3.5 models operate in thinking mode by default'; template 'enable_thinking is false' branch
[11] FIRST-PARTY · page 'Last updated' dateTime 2026-08-13T13:53:20Z; accessed 2026-09-23 · https://unsloth.ai/docs/models/qwen3.5 — '**For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default**.'; 'As an example for Qwen3.5-9B to enable thinking (default is disabled):'; '**Currently no Qwen3.5 GGUF works in Ollama due to separate mmproj vision files. Use llama.cpp compatible backends.**' (first-party for Unsloth's own GGUFs, not for Qwen's model)
[12] FIRST-PARTY · repo sha 3885219b, lastModified 2026-03-02T14:08:36Z; GGUF header parsed 2026-09-23 · https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/blob/main/Qwen3.5-9B-Q4_K_M.gguf — Embedded tokenizer.chat_template inverted: '{%- if enable_thinking is defined and enable_thinking is true %} {{- '<think>\n' }} {%- else %} {{- '<think>\n\n</think>\n\n' }}'; general.architecture qwen35, qwen35.block_count 32, qwen35.full_attention_interval 4
[13] FIRST-PARTY · repo sha e87f1764, lastModified 2026-03-02T14:08:17Z; GGUF header parsed 2026-09-23 · https://huggingface.co/unsloth/Qwen3.5-4B-GGUF/blob/main/Qwen3.5-4B-Q4_K_M.gguf — Same inverted template (thinking only if enable_thinking is true)
[14] FIRST-PARTY · 2026-03-02T14:32:31Z · https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/discussions/2 — Title 'Enabling or disabling reasoning (default is disabled)', danielhanchen: 'Qwen3.5 Small models have reasoning disabled by default.'
[15] FIRST-PARTY · 'Updated 6 months ago'; accessed 2026-09-23 · https://ollama.com/library/qwen3.5:9b — '6488c96fa5fa · 6.6GB'
[16] FIRST-PARTY · accessed 2026-09-23 · https://registry.ollama.ai/v2/library/qwen3.5/blobs/sha256:be595b49fe22012bd1f5605ec14c7ffa58331783a88a4fd8c22e5fc8ec42cf9f — 9b manifest (sha256 6488c96fa5fa...) layers: model, license, params; no template layer. Config: {'model_type':'9.7B','file_type':'Q4_K_M','renderer':'qwen3.5','parser':'qwen3.5','requires':'0.17.1'}. License blob 7339fa41... is Apache License 2.0
[17] FIRST-PARTY · accessed 2026-09-23 · https://registry.ollama.ai/v2/library/qwen3.5/blobs/sha256:ee043a99abe5e8317272712ed08ee2993af1f7930d69aefa3eba562cdc2822bd — qwen3.5:2b config: 'model_type':'2.3B','file_type':'Q8_0','renderer':'qwen3.5','parser':'qwen3.5' (same renderer as 9b)
[18] FIRST-PARTY · accessed 2026-09-23 · https://registry.ollama.ai/v2/library/qwen3.5/blobs/sha256:9371364b27a52acac9d87f88bd93c9db1174d8d6ec57f6888925cdc1788871ff — params blob shared by 9b/4b/2b: {"presence_penalty":1.5,"temperature":1,"top_k":20,"top_p":0.95}
[19] FIRST-PARTY · v0.34.4 tag; accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/renderer.go — 'case "qwen3.5": renderer := &Qwen35Renderer{isThinking: true, emitEmptyThinkOnNoThink: true, useImgTags: RenderImgTags}'
[20] FIRST-PARTY · last file change d0c8cdb795 2026-09-18 (#18473); accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/qwen35.go — 'isThinking := r.isThinking / if think != nil && think.Value != nil { isThinking = think.Bool()'; no-think writes '<think>\n\n</think>\n\n'; 'return &model.Thinking{Values: []any{false, true}, Default: r.isThinking}'; no /no_think or /nothink strings
[21] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/qwen35_test.go — TestQwen35RendererNoThinkPrefill: Render(msgs, nil, &api.ThinkValue{Value: false}) must end with '<|im_start|>assistant\n<think>\n\n</think>\n\n' ('expected explicit no-think prefill')
[22] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/model/parsers/qwen35.go — 'thinkingEnabled := thinkValue != nil && thinkValue.Bool() / if thinkValue == nil { thinkingEnabled = true'; no /no_think handling
[23] FIRST-PARTY · last commit c173758997 2026-09-23T01:28Z (#18501) · https://github.com/ollama/ollama/blob/v0.34.4/docs/capabilities/thinking.mdx — '`false`: request no thinking output, if the model permits it.' / '`null`: use the model default.'
[24] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/server/model_thinking.go — legacyThinking metadata keyed by template digest ('// Qwen3 template with explicit /think and /no_think controls.'); '// Preserve the local endpoint's historical default-on behavior.' (forces Default=true when renderer supports true). Metadata only, not /no_think parsing
[25] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/nemotron3nano.go — Nemotron3Nano parses /no_think on non-v35 path: '} else if strings.Contains(content, "/no_think") { enableThinking = false' (refutes 'only legacy Qwen3')
[26] FIRST-PARTY · publishedAt 2026-09-19 · https://github.com/ollama/ollama/releases/tag/v0.34.3 — '`GET /api/show` now advertises each model's thinking controls and default'
[27] FIRST-PARTY · publishedAt 2026-09-23T02:24:43Z (tag commit b2da9e468a committed 2026-09-23T23:36Z) · https://github.com/ollama/ollama/releases/tag/v0.34.4 — 'Structured outputs on thinking models now apply in a single pass, making them faster and more reliable.'; 'Updated llama.cpp, MLX, and XGrammar.'
[28] FIRST-PARTY · closed 2026-07-07T18:54:52Z · https://github.com/ollama/ollama/issues/14645 — 'format is ignored when think is disabled for qwen3.5 series'; 'Ollama version: 0.17.6'
[29] FIRST-PARTY · merged 2026-07-07T18:54:50Z (merge 892e7f6) · https://github.com/ollama/ollama/pull/15901 — 'server: apply format constraint for all thinking parsers when think=false' covering qwen3.5; compare: not in v0.31.1 (behind_by 17), in v0.31.2 (ahead_by 1)
[30] FIRST-PARTY · publishedAt 2026-07-06T22:28:22Z, createdAt 2026-07-07T22:28:42Z (inconsistent) · https://github.com/ollama/ollama/releases/tag/v0.31.2 — 'Fixed structured output for thinking models when thinking is disabled'; LLAMA_CPP_VERSION b9888
[31] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/anthropic/anthropic.go — 'if r.Thinking != nil && r.Thinking.Type == "disabled" { think = &api.ThinkValue{Value: false}' in v0.34.4; v0.23.0 has only the 'enabled' branch
[32] FIRST-PARTY · opened 2026-04-03; OPEN as of 2026-09-23 · https://github.com/ollama/ollama/issues/15287 — 'The Anthropic-compatible `/v1/messages` endpoint always enables thinking ... regardless of whether the `thinking` field is present in the request.'
[33] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3-8B — Qwen3 soft switch: 'you can add `/think` and `/no_think` to user prompts or system messages to switch the model's thinking mode'
[34] FIRST-PARTY · accessed 2026-09-23 · https://github.com/ollama/ollama/blob/v0.34.4/llm/llama_server.go — 'Models with explicit Ollama renderers/parsers ... still render prompts in Go and call /completion. Other GGUF chat models use llama-server's chat_template handling through /v1/chat/completions.'
[35] FIRST-PARTY · last commit f0078ae476 2026-06-07 · https://github.com/ollama/ollama/blob/v0.34.4/docs/context-length.mdx — 'Ollama defaults to the following context lengths based on VRAM: < 24 GiB VRAM: 4k context; 24-48 GiB VRAM: 32k context'
[36] FIRST-PARTY · branch free-fixes-route-arrived-takes @ 7d9cc26; accessed 2026-09-23 · director/llm.py — lines 166-177: body has "think": False, system content + "\n/no_think", options temperature only, body["format"] = "json" when json_mode
[37] FIRST-PARTY · branch free-fixes-route-arrived-takes @ 7d9cc26; accessed 2026-09-23 · director/stage_manager.py — MODEL = "qwen3:8b"; prompt ends '\n/no_think' (line 48); call_ollama sends "format": "json", "think": False, options temperature 0.85
[38] FIRST-PARTY · opened 2026-03-03; OPEN; 12 comments, last 2026-03-27; accessed 2026-09-23 · https://github.com/ollama/ollama/issues/14579 — Body (user report): 'I am running the same Q4 quant of Qwen3.5-35B-A3B / On ollama I get around 15 to 20 tokens per second' vs '100 tokens per second ... context 160000'; 'Win11 3090Ti 64Gb ram'; Ollama version '0.7.15'. No comment mentions 9b (grep count 0)
[39] FIRST-PARTY · 2026-03-05 · https://github.com/ollama/ollama/issues/14579#issuecomment-4004337758 — User report: 'very slow performance of qwen3.5:27b' on 'RTX 3090 with 24GB of VRAM', 'ollama version is 0.17.5', '100% GPU', context 16000, '46 seconds for gemma3 and 3118 seconds for qwen3.5'
[40] secondary · 2026-03-15 · https://github.com/ollama/ollama/issues/14579#issuecomment-4062931091 — User TsengSR attributes 27b slowness to 32k default context overflowing '24 GB VRAM'; GPU model not named (numbers withheld)
[41] FIRST-PARTY · 2026-03-15 · https://github.com/ollama/ollama/issues/14579#issuecomment-4063476310 — Author: 'if you take same exact model (Qwen3.5-27B-Q4) and use the SAME amount of context (aka set to 16k), there is still double the performance when running straight llama cpp'. Related comments 4063430616 ('testing llama cpp at 60-120k tokens and still manage 35-40tk/s') and 4063462934 ('12tk/s vs 35tk/s') are at different/unstated contexts
[42] secondary · 2026-03-26 · https://github.com/ollama/ollama/issues/14579#issuecomment-4134295284 — Author claims it got worse; no hardware restated
[43] FIRST-PARTY · 2026-03-27 · https://github.com/ollama/ollama/issues/14579#issuecomment-4140398057 — User report: 'RTX 5080 16GB VRAM', qwen3.5:35b-a3b-q4_K_M, asks to expose --n-cpu-moe; '~70 tok/s on this hardware' with llama.cpp
[44] FIRST-PARTY · authored 2026-03-15; referenced on #14579 2026-03-16 · https://github.com/phreer/ollama/commit/82516fd5e724baba65e8d3f0918e49814879da54 — Fork commit 'fix: correct GPU memory estimation for hybrid Mamba+Attention architectures ... Fixes #14579'; the only commit referencing the issue
[45] FIRST-PARTY · merged 2026-05-29T20:35:47Z · https://github.com/ollama/ollama/pull/16031 — 'llama-server (built from upstream llama.cpp via FetchContent) is now the sole inference engine for GGUF-based models.'; merge 9db4bdb contained in v0.30.0, not in v0.24.0 (compare API)
[46] FIRST-PARTY · publishedAt 2026-05-13, createdAt 2026-06-01 (inconsistent); tag commit 2026-06-01 · https://github.com/ollama/ollama/releases/tag/v0.30.0 — 'improved compatibility and performance using llama.cpp'; 'support for a wider range of models, including GGUF-based models from Hugging Face ... faster performance on NVIDIA hardware'; LLAMA_CPP_VERSION b9452
[47] FIRST-PARTY · 2026-03-15 · https://github.com/ollama/ollama/issues/14861#issuecomment-4063856446 — Collaborator rick-github: 'ollama has its own implementation of the qwen3.5 model.' (tps table has no hardware)
[48] FIRST-PARTY · 2026-07-08 · https://github.com/ollama/ollama/issues/14861#issuecomment-4916633997 — User report on RTX 4090 (24 GB, WSL2/Docker), qwen3.6:35b-a3b, 32K ctx, -ngl 36: Ollama 0.23.1 30.7 tok/s vs llama-server b9917 57.7 (comment 4915923840); 0.30.0 ~14–17 tok/s; v0.31.2-rc2 'warm decode 50–60 tok/s ... within ~10–15% of raw llama.cpp master b9917'. Contributor pdevine (4916460129): 'It should be the same speed as llama.cpp.'
[49] FIRST-PARTY · opened 2026-06-30, closed 2026-08-03 · https://github.com/ggml-org/llama.cpp/issues/25162 — '24-42% performance regression on Turing GPUs (RTX 2080 Ti, SM75) for Qwen3.5/Qwen3.6 models'; RTX 2080 Ti 22GB; Qwen3.6-27B Q4_K_XL dense Qwen35 arch: bc81d47ab 27.20 tok/s, 9e58d4d69 20.76 tok/s; close: '0b14b87d7 give：27.47 tok/s， close issue'; no #25185 Turing test result posted
[50] FIRST-PARTY · merged 2026-07-01T08:55:14Z · https://github.com/ggml-org/llama.cpp/pull/25185 — 'CUDA: consistent use of __restrict__ + PDL for FA'; merge b820cc8e in b9888 and b10091, not b9840
[51] FIRST-PARTY · accessed 2026-09-23 (read at every release tag via gh api contents?ref=<tag>) · https://github.com/ollama/ollama/blob/v0.34.4/LLAMA_CPP_VERSION — v0.30.0 b9452; v0.30.2-3 b9479; v0.30.4 b9493; v0.30.5-8 b9509; v0.30.9 b9626; v0.30.10 b9672; v0.30.11 b9781; v0.31.1 b9840; v0.31.2/v0.32.0/v0.32.1 b9888; v0.32.3-5 b10091; v0.32.6-7 b10242; ... v0.32.15/v0.33.0 b10488; v0.34.4 b11081. Compare API: 9e58d4d69 absent in b9452/b9479, present b9493+; 0b14b87d7 absent b10091 and earlier, present b10242, b10353, b10380, b10434, b10488, b11081
[52] FIRST-PARTY · publishedAt 2026-06-30 · https://github.com/ollama/ollama/releases/tag/v0.31.1 — 'Updated the underlying llama.cpp engine to build 9840'
[53] secondary · 2026-03-08 to 2026-03-20, CLOSED NOT_PLANNED · https://github.com/ollama/ollama/issues/14715 — User report: qwen3.5:9b on 'RTX 2080 Ti (22GB VRAM, Modified)', v0.17.5, 'driver resets (Xid 43, Xid 31)'; collaborator asked for logs
[54] secondary · opened 2026-07-16, OPEN · https://github.com/ollama/ollama/issues/17218 — User report: qwen3.5:4b (Q4_K_M), RTX 3070 Laptop 8 GiB, think=false VQA, 226 requests: 321.6 s (0.18.2) vs 617.2 s (0.31.1); accuracy 81.4% vs 64.2%; collaborator: 'Set `LLAMA_ARG_IMAGE_MIN_TOKENS=1024`'
[55] secondary · comment 2026-03-06 · https://github.com/ollama/ollama/issues/14662 — User on M3 Ultra: '40~50 tokens/sec (for 35b:a3b, 9b, and 4b)', compared to qwen3-vl:8b, not llama.cpp
[56] secondary · 2026-04-23, CLOSED COMPLETED 2026-06-04 · https://github.com/ollama/ollama/issues/15771 — User report: Qwen3.6-35B-A3B slower on Ollama 0.21.0 than llama.cpp on RX 7900 XTX ROCm (MoE, AMD; not relevant to 9B)
[57] secondary · 2026-08-26, OPEN · https://github.com/ollama/ollama/issues/18038 — User report: llama-server spawned by Ollama uses high CPU during generation (M4 Max, gemma4)
[58] secondary · 2026-07-28, OPEN · https://github.com/ollama/ollama/issues/17434 — User report: qwen3.6:35b CUDA illegal memory access with JSON-schema format + think:false on 0.32.5, DGX Spark GB10
[59] secondary · closed 2026-03-14 DUPLICATE; comment 2026-07-17 · https://github.com/ollama/ollama/issues/14850 — User comment: qwen3.5:27b with a complex format still mismatched (version not stated)
[60] secondary · 2026-08-31, OPEN · https://github.com/ollama/ollama/issues/18152 — User report: Windows+NVIDIA driver TDR regression between 0.32.15 and 0.33.0 with a qwen3:8b Modelfile (SYSTEM /no_think)
[61] secondary · comment 2026-08-08 · https://github.com/ollama/ollama/issues/14716 — User on qwen3.5:9b with 'SYSTEM /no_think': 'It will still start with thinking, but switch to outputting a real answer right after it.'
[62] secondary · 2026-03-07, CLOSED NOT_PLANNED · https://github.com/ggml-org/llama.cpp/issues/20182 — User on llama-cli, Qwen3.5-9B-Q4_K_M, RTX 3060: 'The model still thinks event with `enable_thinking:false`'; maintainer pwilkin: 'Please use `--reasoning-budget 0` for now'
[63] secondary · 2026-06-12, OPEN · https://github.com/ollama/ollama/issues/16685 — User report: qwen3.5:9b, think=false, long Chinese generation degrades after ~3-4k generated tokens (Vulkan and CPU)
[64] FIRST-PARTY · 2026-08-03T10:45:24Z · https://github.com/ggml-org/llama.cpp/commit/0b14b87d7c20cb753b94b96854dd7b45306fc696 — Commit is 'server: add notice for upcoming default port change 8080 --> 9931 (#26508)', i.e. a master tip the #25162 reporter tested, not a fix commit

## Contradictions (first-party vs first-party — unresolved)
- APPARENT, resolved by artifact (not a same-artifact contradiction): Qwen card + template https://huggingface.co/Qwen/Qwen3.5-9B say 9B thinking is ON by default; Unsloth doc https://unsloth.ai/docs/models/qwen3.5 (last updated 2026-08-13) says 'For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default'. Unsloth's 9B and 4B GGUFs (https://huggingface.co/unsloth/Qwen3.5-9B-GGUF, https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) embed an inverted template (think only if enable_thinking is true), so each source is right about its own artifact. Unsloth's sentence is unscoped, and no Unsloth text says the inversion was deliberate.
- DIVERGENCE between runtime and model vendor (not about the 9B): Ollama qwen3.5:2b uses renderer 'qwen3.5' with isThinking:true (https://registry.ollama.ai/v2/library/qwen3.5/blobs/sha256:ee043a99abe5e8317272712ed08ee2993af1f7930d69aefa3eba562cdc2822bd, https://github.com/ollama/ollama/blob/v0.34.4/model/renderers/renderer.go), so its default is ON. Qwen's official 2B is 'non-thinking mode by default' (https://huggingface.co/Qwen/Qwen3.5-2B). For the 9B both are ON.
- First-party release metadata inconsistency (not resolved): v0.30.0 publishedAt 2026-05-13 vs createdAt/tag commit 2026-06-01, while containing PR #16031 merged 2026-05-29 (https://github.com/ollama/ollama/releases/tag/v0.30.0, https://github.com/ollama/ollama/pull/16031). v0.31.2 publishedAt 2026-07-06T22:28Z vs createdAt/tag commit 2026-07-07T22:28Z, while containing PR #15901 merged 2026-07-07T18:54Z (https://github.com/ollama/ollama/releases/tag/v0.31.2); a contributor still called v0.31.2-rc2 a pre-release on 2026-07-08 (https://github.com/ollama/ollama/issues/14861#issuecomment-4916460129). v0.34.4 publishedAt 2026-09-23T02:24Z vs tag commit b2da9e468a committed 2026-09-23T23:36Z (https://github.com/ollama/ollama/releases/tag/v0.34.4).

## Could not confirm
- Any measured tok/s for dense qwen3.5:9b text generation on Ollama vs llama.cpp on CUDA, and specifically on an RTX 2080 Ti / Turing (none in #14579, related issues, or release notes).
- Which llama.cpp commit actually fixed the #25162 Turing regression; 0b14b87d7 is only the master tip the reporter tested (a server port-notice commit). Whether Ollama builds b9888-b10091 (which contain #25185) are recovered on Turing is unknown.
- Whether the Turing recovery measured on upstream llama-server (Qwen3.6-27B, 22GB 2080 Ti) carries over to Ollama's llama-server with Ollama-format qwen35 blobs.
- Actual /api/show 'thinking' output for qwen3.5:9b on v0.34.3+ (inferred from code, not executed).
- What Qwen3.5-9B actually does with a literal '/no_think' string in the prompt when think=false already prefills an empty think block (untested).
- Whether an Unsloth HF GGUF pulled into Ollama would use its embedded default-OFF template (inferred from llama_server.go comment; untested), and whether Unsloth's 'no Qwen3.5 GGUF works in Ollama' statement is still current.
- Whether Unsloth inverted the template deliberately (no Unsloth text found saying so; reconciliation is by artifact).
- The Ollama version installed on hil and on supercommons2, and whether hil runs Windows.
- Whether phreer/ollama 82516fd was ever proposed upstream (search found no ollama/ollama PR).
- Whether #14715 (Xid 43/31 on a modified 22GB 2080 Ti, 0.17.5) reproduces on a stock 11GB 2080 Ti or on Ollama >= v0.30.0.
- The '0.7.15' Ollama version in #14579's body (verbatim; likely a typo).
- True public release dates of Ollama v0.30.0, v0.31.2, v0.34.4 (GitHub publishedAt/createdAt/tag-commit dates disagree).
- GPU model behind TsengSR's #14579 numbers and behind the author's '12tk/s vs 35tk/s' comment.

## Dropped claims (refuted or unsupported in verification)
- c20 'Ollama's special handling of /no_think exists only for the legacy Qwen3 template': contradicted. nemotron3nano.go also parses /no_think, and the model_thinking.go Qwen3 entry is template-digest metadata, not parsing. Replaced with: the qwen3.5 renderer and parser have no /no_think handling.
- 'The /no_think soft switch does not work on Qwen3.5': overstated. The card says 'does not officially support'. Replaced with 'not officially supported; not handled by Ollama's qwen3.5 code; reaches the model as literal text; effect untested'.
- C2 bullet 'with the same Qwen3.5-27B-Q4 at 16k context, llama.cpp is still about double, 12tk/s vs 35tk/s': merges two comments. The 12 vs 35 figures were not a matched-16k measurement. Kept the qualitative 'double' claim; moved the numbers to do_not_quote.
- TsengSR's 17/25/40 tok/s numbers in the answer: no GPU named. Moved to do_not_quote.
- c7 source_date 'page-level date not shown': wrong. The Unsloth page shows 'Last updated' dateTime 2026-08-13T13:53:20Z.
- Implicit framing that the Turing regression entered Ollama at v0.31.1 and was first recovered at v0.33.0: corrected by compare API. 9e58d4d69 is first present at b9493 (v0.30.4). 0b14b87d7 is first present at b10242 (v0.32.6). 0b14b87d7 is a master tip (server port notice), not the fix commit.
- c10 'Unsloth default is irrelevant to Ollama': only partially supported. Ollama v0.30.0+ supports HF GGUFs, and non-renderer GGUFs use llama-server's chat_template, so the Unsloth default may apply if someone pulls an Unsloth GGUF. Kept only as a caveat.

## DO NOT QUOTE (low/unknown)
- [low] TsengSR's #14579 figures (17 tok/s at 32k, 25 at 16k, 40 at 8k context for qwen3.5-27b) — No GPU model or quant named; only '24 GB VRAM' implied. Violates the attribute-every-number rule.
- [low] '12tk/s vs 35tk/s' (Ollama vs llama.cpp, Qwen3.5-27B) from the #14579 author — From a different comment than the matched-16k-context claim; the author's llama.cpp 35-40 tk/s was stated at 60-120k context; GPU not restated. Not a matched measurement.
- [low] 'Qwen3.5-35B quant runs at 140tk/s' on llama.cpp (#14579 author, 2026-03-26) — No hardware, quant, or version stated.
- [low] rick-github's #14861 tps table (qwen3.5:35b 89.27 vs unsloth UD on llama.cpp engine 218.86) — No hardware stated; MoE; pre-v0.30.0 engine.
- [low] '40~50 tokens/sec (for 35b:a3b, 9b, and 4b)' on M3 Ultra (#14662) — The only 9B tok/s seen: Apple Silicon, quant and Ollama version not stated, compared with qwen3-vl:8b rather than llama.cpp; irrelevant to CUDA/Turing.
- [low] '0b14b87d7 give: 27.47 tok/s' (#25162 close comment) — The close comment does not restate model or GPU. 0b14b87d7 is a master tip, not the fix. Measured on upstream llama-server, not Ollama.
- [unknown] llama.cpp #25185 as 'the fix' for the Turing qwen35 regression — Suggested by users (#25162, #14861 comment); no Turing test result posted; the PR title scopes it to FA kernels while the regression names SSM kernels.
- [unknown] Any claim that Ollama >= v0.32.6 restores qwen35 throughput on the 2080 Ti — Only build containment is verified; recovery through Ollama's qwen35 blob path is unmeasured.
- [low] /api/show thinking output for qwen3.5:9b ({false,true}, default true) — Read from source (qwen35.go, model_thinking.go); not executed.
- [low] Behaviour of '/no_think' text on qwen3.5:9b ('will still start with thinking' per #14716) — Single user report; the card only says the soft switch is 'not officially supported'.
- [low] Unsloth HF GGUF in Ollama defaulting thinking OFF via llama-server chat_template — Inference from a code comment in llm/llama_server.go; untested; Unsloth doc says no Qwen3.5 GGUF works in Ollama (possibly stale).
- [low] Unsloth doc 'reasoning is disabled by default' for 4B/9B as a statement about the Qwen model — Contradicted for the Qwen model by Qwen's card and template; true only of Unsloth's inverted GGUF templates.
- [low] #14715 qwen3.5:9b Xid 43/31 crash on RTX 2080 Ti — Single report on a modified 22GB card, Ollama 0.17.5, placeholder driver/log fields, closed NOT_PLANNED without logs.
- [low] #17434 JSON-schema + think:false CUDA crash (qwen3.6:35b, 0.32.5, DGX Spark GB10) — User report, different model/hardware; the repo uses format 'json', not a schema.
- [low] #14850 2026-07-17 comment that qwen3.5:27b with think=False still ignores a complex format — User comment, Ollama version not stated, issue closed as duplicate.
- [low] #18152 Windows TDR crash on 0.33.x with qwen3:8b — Single user report; hil's OS not confirmed here.
- [low] #16685 qwen3.5:9b long-form collapse with think=false — Single user report on Vulkan/CPU at ~3-4k generated tokens; the brain emits short JSON.
- [low] #17218 qwen3.5:4b figures (321.6 s -> 617.2 s; 81.4% -> 64.2%) — Single user report; image-heavy VQA on an RTX 3070 Laptop; not text throughput and not the 9B.
- [low] #15771 Qwen3.6-35B-A3B Ollama 0.21.0 vs llama-cli numbers on RX 7900 XTX — AMD ROCm, MoE, pre-v0.30.0 engine; quant not re-verified; irrelevant to the 9B on Turing.
- [unknown] Ollama 'released on' dates for v0.30.0, v0.31.2, v0.34.4 — GitHub publishedAt predates the contained merges and tag commits (e.g. v0.31.2 publishedAt 2026-07-06 vs PR #15901 merged 2026-07-07; v0.34.4 publishedAt 02:24Z vs tag commit 23:36Z the same day). Tag containment is reliable; dates are not.
- [low] Ollama version '0.7.15' in #14579 body — Verbatim but implausible; likely a typo.
- [low] phreer/ollama 82516fd as a fix for #14579 — Fork-only memory-estimation change; never found upstream; not a throughput fix.


---

# Track D — Local-brain bake-off shortlist under 7 GB (Ollama)
Primary mission track: no · Final confidence: high

## Answer
## Track D (final): local-brain bake-off shortlist for Ollama, model file under 7 GB, RTX 2080 Ti 11 GB shared

**Direct answer**
- **Shortlist: seven tags, all Apache-2.0, all with a file size of 6.6 GB or less.** The incumbent is `qwen3:8b`. The six challengers are `qwen3.5:9b` (the lead), `qwen3.5:4b`, `qwen3:4b-instruct-2507-q4_K_M`, `gemma4:e4b-it-qat`, `granite4.2:8b` and `ministral-3:8b`.
- **The lead's figures re-verify:** `qwen3.5:9b` is 6.6 GB, Q4_K_M, 9.65B parameters, 256K context and Apache-2.0 [1][2][4].
- **Gemma licence and 12B release are settled.**
  - Gemma 4 is Apache 2.0, not the custom Gemma Terms. Google's licence page shows the Apache text ("Last updated 2026-04-01 UTC") [14]. The Gemma Terms page itself says "For Gemma 4 terms, see the Gemma 4 license" [15]. The launch blog [17] and the HF cards [18][19] agree.
  - Gemma 4 12B was released on "June 3, 2026" [16], under apache-2.0 on HF [19].
  - **The 12B tags fail the size cap:** `gemma4:12b` is 7.6 GB and `gemma4:12b-it-qat` is 7.2 GB [12].
- **Three settings apply to every candidate:**
  - Pin `num_ctx` to the same value for all of them.
  - Send a top-level `think:false`.
  - Upgrade the host's Ollama to **at least 0.31.2**. Below that, `think:false` plus `format` silently ignores the format on qwen3.5 [43][44][45]. 0.34.4, released 2026-09-23 and the latest, is preferred [49].

### Included candidates
| tag | size | ctx | license (+URL) | lab | thinking toggle | notes | verdict |
|---|---|---|---|---|---|---|---|
| `qwen3:8b` (=`:latest`) | 5.2 GB, Q4_K_M, 8.19B [7][8] | 40K [7] | Apache-2.0: [blob](https://ollama.com/library/qwen3:8b/blobs/d18a5cc71b84) ("Copyright 2024 Alibaba Cloud") [8]; [HF](https://huggingface.co/Qwen/Qwen3-8B) [9] | Qwen / Alibaba Cloud [8][9] | **On by default.** The card says "enable_thinking=True … Default is True" [9]. Ollama's legacy table marks this template digest `ae370d884f10` as `Default: true` [35][50]. Send top-level `think:false` | Baseline. Pin num_ctx | **INCLUDE (baseline)** |
| `qwen3.5:9b` (=`:latest`, `:9b-q4_K_M`) | 6.6 GB, Q4_K_M, 9.65B; the vision tower is inside the same GGUF (`qwen35.vision.block_count`=27) [1][2][50] | 256K [1]; the card says "262,144 natively" [4] | Apache-2.0: [blob](https://ollama.com/library/qwen3.5:9b/blobs/7339fa418c9a) [2]; [HF](https://huggingface.co/Qwen/Qwen3.5-9B) [4] | Qwen (HF org) [4]. The Ollama page names only the brand "Qwen3.5" [2] | **On by default.** The card says "operate in thinking mode by default" [4], and the official template emits an empty think block only when `enable_thinking` is false [5]. The Ollama renderer uses `isThinking: true, emitEmptyThinkOnNoThink: true` [36]. `think:false` works. The `/no_think` soft switch is **not supported** [4] | Ollama ships the thinking-mode sampler set `{"presence_penalty":1.5,"temperature":1,"top_k":20,"top_p":0.95}` [50]. Override it with the card's non-thinking set (0.7 / 0.8 / 20 / 1.5) [4]. The registry declares `requires 0.17.1` [50] and 0.17.5 fixed Qwen3.5 crashes and repetition [42], but **the effective floor is 0.31.2** [45]. Pin num_ctx | **INCLUDE (lead)** |
| `qwen3.5:4b` (=`:4b-q4_K_M`) | 3.4 GB, Q4_K_M, 4.66B [1][3] | 256K [1] | Apache-2.0: [blob](https://ollama.com/library/qwen3.5:4b/blobs/7339fa418c9a) [3]; [HF](https://huggingface.co/Qwen/Qwen3.5-4B) [6] | Qwen [6] | Same as the 9B (same renderer and parser) [50] | Same floors, sampler override and num_ctx pin as the 9B | **INCLUDE** |
| `qwen3:4b-instruct-2507-q4_K_M` (=`qwen3:4b-instruct`) | 2.5 GB, 4.02B [7][10] | 256K [7]; the card says "262,144 natively" [11] | Apache-2.0: [blob](https://ollama.com/library/qwen3:4b-instruct-2507-q4_K_M/blobs/d18a5cc71b84) [10]; [HF](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) [11] | Qwen / Alibaba Cloud [10][11] | **Non-thinking only**: "supports only non-thinking mode" [11], and the Ollama Go template has no `.Think` [50]. `think:false` is accepted; `think:true` returns HTTP 400 [34] | Pin the exact tag: bare `qwen3:4b` is the **thinking** variant (the same digest as `qwen3:4b-thinking`) [7]. Pin num_ctx | **INCLUDE** |
| `gemma4:e4b-it-qat` | 6.1 GB = 5.2 GB Q4_0 model + 992 MB BF16 vision projector, 7.46B [13] | 128K [12] | Apache-2.0: [blob](https://ollama.com/library/gemma4:e4b-it-qat/blobs/0d542e0c8804) [13]; [Google license](https://ai.google.dev/gemma/docs/gemma_4_license) [14]; [HF](https://huggingface.co/google/gemma-4-E4B-it) [18]. Google's own QAT Q4_0 GGUF repo is also apache-2.0 [20] | Google DeepMind (named on the Ollama page) [13][18] | Upstream, thinking is toggled by the `<\|think\|>` token [18]. **On local Ollama it is effectively ON by default**: `gemma4.go` says `Default: false`, but `server/model_thinking.go` flips it ("Preserve the local endpoint's historical default-on behavior"), and `ollama show gemma4` prints "default true" [35][36][48]. Send `think:false` | Do not use `gemma4:e4b` or `:latest` (9.6 GB) [12]. Requires Ollama 0.30.5 [50]. The Gemma 4 `think=false` structured-output fix landed in v0.21.1, below that floor [46]. Pin num_ctx | **INCLUDE** |
| `granite4.2:8b` (=`:latest`) | 5.3 GB, Q4_K_M, 8.79B [22] | 128K [22]; the card says "Natively Supports 128K" [24] | Apache-2.0: [blob](https://ollama.com/library/granite4.2:8b/blobs/58d1e17ffe51) [22]; [HF](https://huggingface.co/ibm-granite/granite-4.2-8b) [24] | IBM (the Ollama page says "Developers: Granite Team, IBM") [23][24] | **On by default**: "full thinking (default)", and "`enable_thinking=False`" turns it off [24]. The tag has no template layer and no renderer [25], so Ollama uses llama-server's GGUF chat-template path and maps top-level `think` to `chat_template_kwargs.enable_thinking` [32]. The page readme's `"options": {"think": …}` is **ignored**: `think` exists only on the request structs, and unknown options log "invalid option provided" [23][37] | Released August 25, 2026, "the mid-size reasoning model" [24]. It shipped a `PARAMETER num_ctx` that caused OOMs; the parameter was removed on 2026-09-04, so re-pull [26]. The GGUF `context_length` is 131072 [25]. The page shows no capability labels [23]. Pin num_ctx (highest risk) | **INCLUDE (first test think:false + schema on the host)** |
| `ministral-3:8b` (=`:latest`) | 6.0 GB, Q4_K_M, 8.92B [27] | 256K [27][28] | Apache-2.0: [blob](https://ollama.com/library/ministral-3:8b/blobs/43070e2d4e53) [27]; [HF](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512) [28]; Mistral's announcement: "All models are released under the Apache 2.0 license" [29] | Mistral AI, announced "December 2, 2025" [29]. **The Ollama page names only "Ministral 3"** [27] | **No thinking.** The parser is `MinistralParser{hasThinkingSupport: false}` [38], the template has no think, and the labels are vision and tools [27][50]. `think:false` is accepted; `think:true` returns 400 [34] | Ships `{"temperature":0.15}` [27]. Mistral recommends "temperature below 0.1" for production [28]. The repo overrides temperature (0.85 and 1.0) [71]. Requires Ollama 0.13.1 [27]. Pin num_ctx | **INCLUDE (lab-name flag)** |

### Reserves (verified, lower priority)
- `granite4.1:8b`: 5.3 GB, 128K, Apache-2.0, IBM, released "April 29th, 2026". Its Go template has no `.Think`; label: tools. It is the fallback if the Granite 4.2 llama-server path misbehaves [51][52].
- `phi4-mini:3.8b-q4_K_M` (=`:latest`): 2.5 GB, 128K, MIT ("Copyright (c) Microsoft Corporation"), released February 2025. Label: tools, no thinking [53][54].
- `gemma4:e2b-it-qat`: 4.3 GB (3.3 GB Q4_0 + 987 MB projector), 128K, Apache-2.0. The default `gemma4:e2b` is 7.2 GB, so pin the `-it-qat` tag [12].
- `llama3.1:8b`: 4.9 GB, 128K, Llama 3.1 Community License [55]. Two obligations:
  - Distributing or "mak[ing] available" a product or service containing the Llama Materials requires that you "prominently display 'Built with Llama'".
  - A licensee with more than 700M monthly active users "must request a license from Meta".

### HOLD
- `olmo-3:7b-instruct`: 4.5 GB, 64K, Apache-2.0 [56].
  - Ai2's card adds "It is intended for research and educational use" [57], which needs a legal read under rule 5.
  - The Ollama page names no lab [56].
  - `olmo-3:latest` is the **7b-think** variant [56].
- `nemotron-3-nano:4b`: 2.8 GB, 256K. Two first-party sources give different licence names: the Ollama layer says "NVIDIA Open Model License Agreement, Last Modified: October 24, 2025" [58], while NVIDIA's card and licence page say "NVIDIA Nemotron Open Model License, Last Modified: December 15, 2025" [59][60]. Both say the models are "commercially usable". Unresolved.

### EXCLUDE
- **Over 7 GB:**
  - Gemma 4: `gemma4:12b` 7.6 GB, `:12b-it-qat` 7.2 GB, `:e4b`/`:latest` 9.6 GB, `:e2b` 7.2 GB [12].
  - Qwen: `qwen3.6` (27b 18 GB, 35b 23 GB), `qwen3.8` (27b 18 GB), `qwen3.8-flash-next` (125b-a6b, 120 GB or more) [65].
  - Others: `glm-4.7-flash` 19 GB, `gpt-oss:20b` 14 GB, `muse-glimmer:30b` 18 GB, `nemotron-3.5-lightning` 25 GB, `laguna-xs-2.1` 20 GB, `north-mini-code-1.0` 19 GB, `olmo-3.1` 19 GB, `nemotron3:33b` 28 GB, `phi4:14b` 9.1 GB [66].
- **Cloud only:** `glm-5.3-flash:cloud` and `deepseek-v4.1-flash:cloud` [67].
- **Licence:**
  - `exaone3.5`: "EXAONE AI Model License Agreement 1.1 - NC" [62].
  - `glm4:9b`: commercial use requires registration [63].
  - `ornith-1.5:9b`: no licence row. `ornith:9b`: an unfilled "MIT License Copyright (c) [year] [fullname]" [64].
  - `gemma3` and `gemma3n`: custom Gemma Terms of Use, superseded by the Apache Gemma 4 [21].
  - `lfm2.5:8b-a1b` (5.2 GB): "Any Commercial Use … by a Legal Entity that exceeds the Threshold is not licensed", where the threshold is $10M annual revenue [61]. This is **not** non-commercial, so excluding it is a judgment call, not a rule-5 disqualification.
- **Poor fit:**
  - `deepseek-r1:8b`: MIT, but labelled tools and thinking; a reasoning distill [68].
  - `rnj-1:8b-instruct-q4_K_M`: 32K, and its template hard-codes "You are rnj-1…" [69].
  - `falcon3:7b` (TII Falcon License, 32K) and `mistral:7b` (32K): older generations, not evaluated further [70].
  - `minicpm-v4.5` (6.1 GB, 40K): a vision MLLM, not evaluated [73].

### Ollama mechanics
- **Structured outputs are not model-restricted in the docs, but the docs never literally say "model-agnostic".**
  - The docs say "Provide a JSON schema to the `format` field." The only exclusion they state is "Ollama's Cloud currently does not support structured outputs" [30].
  - The API reference says "The model will generate a response that matches the schema" [31].
  - In the source, the schema goes to llama-server as `json_schema`/grammar on the GGUF chat-template path [32].
  - Version-specific bugs:
    - qwen3.5 with `think:false` ignored `format` (reported on 0.17.6), fixed by PR #15901 in v0.31.2 [43][44][45].
    - Gemma 4 was fixed in v0.21.1 [46].
    - A format that "applies after a response's thinking" runs in a single pass only from v0.34.4 [32][49].
  - The repo sends `"format":"json"`, not a schema [71]. A schema would enforce the {goal, mood, urgency, reason} keys.
- **Thinking:**
  - The docs define `think:false` as "request no thinking output, if the model permits it" [33].
  - In routes.go, a thinking-capable model with `think` unset gets the resolved default, which is ON for qwen3, qwen3.5, gemma4 and granite4.2. A non-thinking model sent `think:true` returns 400 "does not support thinking". `false` always passes [34][35].
  - `/api/show` reports each model's thinking values and default from **v0.34.3 (2026-09-19)** [48]; the doc was committed 2026-09-23 [33].
  - Remove `/no_think` for Qwen3.5 (`stage_manager.py:48`, `llm.py:172`) [4][71].
- **num_ctx: pin it for all seven, at one shared value.**
  - Current code sets `defaultNumCtx = 4096` when total VRAM is under 23 GiB [34]. The docs say "< 24 GiB VRAM: 4k context" [39]; this default arrived in v0.15.5 [41].
  - The Modelfile doc still says "(Default: 2048)" [40]. See contradictions.
  - `OLLAMA_CONTEXT_LENGTH` overrides the default [39], and a model's params can too; Granite 4.2 did [26].
  - None of the seven tags' params blobs set num_ctx today [50].
  - Pin priority: `granite4.2:8b` first, then the 256K tags (`qwen3.5:*`, `qwen3:4b-instruct`, `ministral-3:8b`), then `gemma4` (128K), then `qwen3:8b` (40K).
  - Qwen's advice of "at least 128K" is "to preserve thinking capabilities" and does not apply with `think:false` [4].
- **Host version floors:**

  | Requirement | Minimum Ollama | Source |
  |---|---|---|
  | qwen3.5 with think:false + format | 0.31.2 | [45] |
  | gemma4 QAT tags | 0.30.5 (declared by the tag) | [50] |
  | granite4.2 llama-server chat-template path | exists in the v0.30.0 source (`llm/llama_server.go` 404s at v0.29.0); not declared by the tag | [32][47] |
  | ministral-3 | 0.13.1 | [27] |
  | `/api/show` thinking discovery | 0.34.3 | [48] |

### Caveats
- File size is not runtime VRAM. A repo note says the director "holds ~8GB" with the 5.2 GB `qwen3:8b`; that figure is unmeasured [72].
- The qwen3.5 GGUFs carry vision weights, and gemma4 QAT carries a 992 MB projector [13][50]. Whether either loads into VRAM on text-only calls is unknown.
- **Lab-naming rule.** The Ollama pages for `qwen3.5` and `ministral-3` give only brand names ("Qwen3.5", "Ministral 3") with no organisation; the lab is established via the HF org cards and mistral.ai [4][28][29]. The `olmo-3` page names no lab at all. Whether this satisfies the rule is the orchestrator's call.
- The Qwen3.5 card contradicts itself on the non-thinking *reasoning* sampler set. The *general* set used here is the same in both places (see contradictions).

## Sources
[1] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3.5/tags — qwen3.5:9b latest 6488c96fa5fa 6.6GB 256K; qwen3.5:4b 2a654d98e6fb 3.4GB 256K; 2b 2.7GB; 0.8b 1.0GB; 27b 17GB; 35b 24GB
[2] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3.5:9b — '6488c96fa5fa · 6.6GB model arch qwen35 · parameters 9.65B · quantization Q4_K_M 6.6GB license Apache License Version 2.0'; params {presence_penalty 1.5, temperature 1, top_k 20, top_p 0.95}; license blob 7339fa418c9a returns 200 (Apache text)
[3] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3.5:4b — '2a654d98e6fb · 3.4GB model arch qwen35 · parameters 4.66B · quantization Q4_K_M 3.4GB license Apache License'
[4] FIRST-PARTY · repo lastModified 2026-03-02; accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-9B — 'license: apache-2.0'; 'Context Length: 262,144 natively'; 'Qwen3.5 models operate in thinking mode by default'; 'does not officially support the soft switch of Qwen3, i.e., /think and /nothink'; non-thinking general sampler 'temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5'; 'at least 128K tokens to preserve thinking capabilities'; internal sampler discrepancy lines 836 vs 1142
[5] FIRST-PARTY · accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-9B/raw/main/chat_template.jinja — lines 149-152: '{%- if enable_thinking is defined and enable_thinking is false %} {{- '<think>\n\n</think>\n\n' }} {%- else %} {{- '<think>\n' }}'
[6] FIRST-PARTY · repo lastModified 2026-03-02; accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3.5-4B — 'license: apache-2.0'; 'Context Length: 262,144 natively'
[7] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3/tags — qwen3:8b latest 500a1f067a9f 5.2GB 40K; qwen3:4b-instruct = qwen3:4b-instruct-2507-q4_K_M 0edcdef34593 2.5GB 256K; qwen3:4b = qwen3:4b-thinking 359d7dd4bcda
[8] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3:8b — '500a1f067a9f · 5.2GB model arch qwen3 · parameters 8.19B · quantization Q4_K_M'; license blob https://ollama.com/library/qwen3:8b/blobs/d18a5cc71b84 'Copyright 2024 Alibaba Cloud Licensed under the Apache License, Version 2'
[9] FIRST-PARTY · repo lastModified 2025-07-26; accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3-8B — 'license: apache-2.0'; 'enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.'
[10] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3:4b-instruct-2507-q4_K_M — '0edcdef34593 · 2.5GB model arch qwen3 · parameters 4.02B'; license Apache (blob d18a5cc71b84)
[11] FIRST-PARTY · repo lastModified 2025-09-17; accessed 2026-09-23 · https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 — 'NOTE: This model supports only non-thinking mode and does not generate <think></think> blocks'; 'Context Length: 262,144 natively'; 'license: apache-2.0'
[12] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/gemma4/tags — gemma4:latest/e4b c6eb396dbd59 9.6GB 128K; e2b 7fbdbf8f5e45 7.2GB; 12b 4eb23ef187e2 7.6GB 256K; 12b-it-qat 7.2GB; e4b-it-qat ee6656371218 6.1GB 128K; e2b-it-qat 07ea59a47401 4.3GB 128K; 26b 19GB; 31b 20GB
[13] FIRST-PARTY · 'Updated 3 months ago'; accessed 2026-09-23 · https://ollama.com/library/gemma4:e4b-it-qat — 'ee6656371218 · 6.1GB model arch gemma4 · parameters 7.46B · quantization Q4_0 5.2GB projector arch clip · parameters 478M · quantization BF16 992MB license Apache License Version 2.0'; readme 'Gemma is a family of open models built by Google DeepMind'; labels vision tools thinking audio cloud; e2b-it-qat page: 4.63B Q4_0 3.3GB + 987MB projector
[14] FIRST-PARTY · Last updated 2026-04-01 UTC · https://ai.google.dev/gemma/docs/gemma_4_license — 'Apache License 2.0 Apache License Version 2.0 , January 2004'
[15] FIRST-PARTY · Last modified: April 1, 2026 · https://ai.google.dev/gemma/terms — 'The terms below apply to Gemma models listed in the Appendix at bottom of this page. For Gemma 4 terms, see the Gemma 4 license.'
[16] FIRST-PARTY · Last updated 2026-07-02 UTC · https://ai.google.dev/gemma/docs/releases — 'June 3, 2026 Release of Gemma 4 12B Unified.' 'March 31, 2026 Release of Gemma 4 in E2B, E4B, 31B and 26B A4B sizes.'
[17] FIRST-PARTY · Apr 02, 2026 · https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ — 'That's why Gemma 4 is released under a commercially permissive Apache 2.0 license.'
[18] FIRST-PARTY · repo lastModified 2026-07-20; accessed 2026-09-23 · https://huggingface.co/google/gemma-4-E4B-it — 'license: apache-2.0'; 'license_link: https://ai.google.dev/gemma/docs/gemma_4_license'; 'built by Google DeepMind'; 'Thinking is enabled by including the <|think|> token at the start of the system prompt. To disable thinking, remove the token.'
[19] FIRST-PARTY · repo lastModified 2026-07-20; accessed 2026-09-23 · https://huggingface.co/google/gemma-4-12b-it — 'license: apache-2.0' (HF API tag license:apache-2.0)
[20] FIRST-PARTY · repo lastModified 2026-07-17; accessed 2026-09-23 · https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf — Google publishes an official E4B QAT Q4_0 GGUF, HF API tag license:apache-2.0, not gated
[21] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/gemma3:4b — 'license Gemma Terms of Use Last modified: February 21, 2024'; gemma3n:e2b page: 'Gemma Terms of Use Last modified: March 24, 2025'
[22] FIRST-PARTY · 'Updated 3 weeks ago'; accessed 2026-09-23 · https://ollama.com/library/granite4.2:8b — 'f586c02fdecd · 5.3GB model arch granite · parameters 8.79B · quantization Q4_K_M 5.3GB license Apache License'; params {temperature 1, top_p 0.95}; /tags: granite4.2:latest = 8b 5.3GB 128K
[23] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/granite4.2 — no capability labels (only '3b 8b 30b'); readme 'Developers: Granite Team, IBM'; readme REST example passes think inside options
[24] FIRST-PARTY · repo lastModified 2026-09-04 · https://huggingface.co/ibm-granite/granite-4.2-8b — '| **Release Date** | August 25, 2026 |'; 'mid-size reasoning model'; 'full thinking (default), non-thinking, and low-effort'; '| **Non-thinking** | enable_thinking=False |'; 'Natively Supports 128K'; License Apache 2.0; 'Developers | Granite Team, IBM'
[25] FIRST-PARTY · accessed 2026-09-23 · https://registry.ollama.ai/v2/library/granite4.2/manifests/8b — layers model/license/params only (no template), config has no renderer/parser; GGUF header: general.license apache-2.0, general.base_model.0.organization 'Ibm Granite', granite.context_length 131072, tokenizer.chat_template contains <think> and </think>
[26] FIRST-PARTY · opened 2026-08-27, closed 2026-09-04 · https://github.com/ollama/ollama/issues/18074 — 'ship with context_length = 131072 in their GGUF metadata'; 'The model is published with a num_ctx parameter'; 'The models have all been updated in ollama.com/library/granite4.2 to remove the PARAMETER num_ctx entry. A fresh pull should remove that'
[27] FIRST-PARTY · 'Updated 9 months ago'; accessed 2026-09-23 · https://ollama.com/library/ministral-3:8b — '1922accd5827 · 6.0GB model arch mistral3 · parameters 8.92B · quantization Q4_K_M 6.0GB license Apache License'; params {temperature 0.15}; labels 'vision tools'; 'This model requires Ollama 0.13.1'; /tags 256K; readme names only 'The Ministral 3 family'
[28] FIRST-PARTY · repo lastModified 2026-07-15 · https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512 — 'license: apache-2.0'; 'Supports a 256k context window'; 'Use a temperature below 0.1 for daily-driver and production environments'
[29] FIRST-PARTY · December 2, 2025 (datePublished 2025-12-02T16:00:00Z) · https://mistral.ai/news/mistral-3/ — 'By Mistral AI'; 'we release the Ministral 3 series, available in three model sizes: 3B, 8B, and 14B parameters'; 'All models are released under the Apache 2.0 license.'
[30] FIRST-PARTY · last doc commit 2026-06-07 (f0078ae4) · https://docs.ollama.com/capabilities/structured-outputs — 'Ollama's Cloud currently does not support structured outputs.' 'Provide a JSON schema to the format field.'
[31] FIRST-PARTY · last commit 2026-09-15 · https://github.com/ollama/ollama/blob/main/docs/api.md — 'Structured outputs are supported by providing a JSON schema in the format parameter. The model will generate a response that matches the schema.'
[32] FIRST-PARTY · main, accessed 2026-09-23 (header text present at v0.30.0; 'applies after a response's thinking' present at v0.34.4, absent at v0.34.3; file 404 at v0.29.0) · https://github.com/ollama/ollama/blob/main/llm/llama_server.go — 'Other GGUF chat models use llama-server's chat_template handling through /v1/chat/completions.'; 'a JSON schema is passed to llama-server via its json_schema field'; 'A format that applies after a response's thinking is sent as a grammar'; llamaServerChatTemplateKwargs: '"enable_thinking": think.Bool()'
[33] FIRST-PARTY · doc commit 2026-09-23 (c1737589, #18501) · https://docs.ollama.com/capabilities/thinking — 'false: request no thinking output, if the model permits it.'; 'Use /api/show to discover the values a model supports and the value Ollama uses by default'
[34] FIRST-PARTY · main, accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/server/routes.go — 'if req.Think == nil && thinking == nil { req.Think = &api.ThinkValue{Value: true} }' / else 'if req.Think != nil && req.Think.Bool() { ... "%q does not support thinking"'; VRAM tier: 'totalVRAM >= 23*format.GibiByte: s.defaultNumCtx = 32768 / default: s.defaultNumCtx = 4096'
[35] FIRST-PARTY · main, accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/server/model_thinking.go — '// Preserve the local endpoint's historical default-on behavior. if thinking.Default == false && thinking.Supports(true) { thinking.Default = true }'; legacyThinking 'sha256:ae370d884f10...': {Values: []any{false, true}, Default: true} ('Qwen3 template with explicit /think and /no_think controls')
[36] FIRST-PARTY · main, accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/model/renderers/renderer.go — 'case "qwen3.5": renderer := &Qwen35Renderer{isThinking: true, emitEmptyThinkOnNoThink: true'; qwen35.go:367 'Default: r.isThinking'; gemma4.go:841 'return &model.Thinking{Values: []any{false, true}, Default: false}' (overridden by server/model_thinking.go)
[37] FIRST-PARTY · main, accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/api/types.go — Think field only on GenerateRequest (line 109) and ChatRequest (line 158), not Options; FromMap: 'if !ok { slog.Warn("invalid option provided", "option", key); continue }'; ValidateLegacyThinking passes booleans
[38] FIRST-PARTY · main, accessed 2026-09-23 · https://github.com/ollama/ollama/blob/main/model/parsers/parsers.go — 'case "ministral": p = &MinistralParser{hasThinkingSupport: false}'; 'case "gemma4": return &Gemma4Parser{hasThinkingSupport: true}'
[39] FIRST-PARTY · doc commit 2026-06-07 · https://docs.ollama.com/context-length — '< 24 GiB VRAM: 4k context'; OLLAMA_CONTEXT_LENGTH override
[40] FIRST-PARTY · doc commit 2026-09-15 · https://docs.ollama.com/modelfile — num_ctx 'Sets the size of the context window used to generate the next token. (Default: 2048)'
[41] FIRST-PARTY · 2026-02-03 · https://github.com/ollama/ollama/releases/tag/v0.15.5 — 'Ollama will now default to the following context lengths based on VRAM: < 24 GiB VRAM: 4,096 context'
[42] FIRST-PARTY · 2026-03-02 · https://github.com/ollama/ollama/releases/tag/v0.17.5 — 'Fixed crash in Qwen 3.5 models when split over GPU & CPU'; 'Fixed issue where Qwen 3.5 models would repeat themselves due to no presence penalty'
[43] FIRST-PARTY · opened 2026-03-05, closed 2026-07-07 · https://github.com/ollama/ollama/issues/14645 — 'Format is ignored when think is disabled for qwen3.5 series' (Ollama version: 0.17.6)
[44] FIRST-PARTY · merged 2026-07-07 · https://github.com/ollama/ollama/pull/15901 — 'server: apply format constraint for all thinking parsers when think=false' ... 'covers qwen3.5, qwen3-thinking' ... 'Fixes #14645'
[45] FIRST-PARTY · 2026-07-06 · https://github.com/ollama/ollama/releases/tag/v0.31.2 — 'Fixed structured output for thinking models when thinking is disabled'
[46] FIRST-PARTY · 2026-04-22 · https://github.com/ollama/ollama/releases/tag/v0.21.1 — 'Fixed structured outputs for Gemma 4 when think=false'
[47] FIRST-PARTY · 2026-05-13 · https://github.com/ollama/ollama/releases/tag/v0.30.0 — 'Ollama 0.30 is now available, with improved compatibility and performance using llama.cpp'
[48] FIRST-PARTY · 2026-09-19 · https://github.com/ollama/ollama/releases/tag/v0.34.3 — 'GET /api/show now advertises each model's thinking controls and default'; 'ollama show gemma4 ... levels false, true default true'
[49] FIRST-PARTY · 2026-09-23 · https://github.com/ollama/ollama/releases/tag/v0.34.4 — 'Structured outputs on thinking models now apply in a single pass, making them faster and more reliable.'; latest release per gh api releases/latest
[50] FIRST-PARTY · accessed 2026-09-23 · https://registry.ollama.ai/v2/library/qwen3.5/manifests/9b — qwen3.5:9b/4b config renderer qwen3.5, parser qwen3.5, requires 0.17.1, params {presence_penalty 1.5, temperature 1, top_k 20, top_p 0.95}; GGUF qwen35.vision.block_count 27, context_length 262144, no general.organization; gemma4/manifests/e4b-it-qat requires 0.30.5; qwen3/manifests/8b template ae370d884f10 has .Think; qwen3:4b-instruct template eade0a07cac7 no .Think; ministral-3/manifests/8b parser ministral, template no .Think; no num_ctx in any of the seven params blobs
[51] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/granite4.1:8b — '444af1c4b2fe · 5.3GB model arch granite · parameters 8.79B'; Apache; labels tools; 128K; Go template 89a0ab46e638 no .Think
[52] FIRST-PARTY · repo lastModified 2026-05-04 · https://huggingface.co/ibm-granite/granite-4.1-8b — 'Release Date: April 29th, 2026'; 'License: Apache 2.0'
[53] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/phi4-mini:3.8b-q4_K_M — '78fad5d182a7 · 2.5GB model arch phi3 · parameters 3.84B'; 'license Microsoft. Copyright (c) Microsoft Corporation. MIT License'; labels tools; 128K
[54] FIRST-PARTY · repo lastModified 2025-12-10 · https://huggingface.co/microsoft/Phi-4-mini-instruct — 'license: mit'; 'Release date: February 2025'
[55] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/llama3.1:8b/blobs/0ba8f0e314b4 — 'If you distribute or make available the Llama Materials ... or a product or service ... that contains any of them, you shall ... prominently display "Built with Llama"'; 'greater than 700 million monthly active users ... you must request a license from Meta'; /tags llama3.1:8b 4.9GB 128K
[56] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/olmo-3/tags — olmo-3:7b-instruct ea72df8c85d7 4.5GB 64K; olmo-3:latest = olmo-3:7b-think b8d4c92ac9c1; tag page license Apache, no Ai2/AllenAI string on page
[57] FIRST-PARTY · repo lastModified 2026-06-25 · https://huggingface.co/allenai/Olmo-3-7B-Instruct — 'This model is licensed under Apache 2.0. It is intended for research and educational use in accordance with Ai2's Responsible Use Guidelines.'
[58] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/nemotron-3-nano:4b/blobs/355e036064fa — 'NVIDIA Open Model License Agreement Last Modified: October 24, 2025'; 'Models are commercially usable.'; tag 6cc467f05439 2.8GB 256K
[59] FIRST-PARTY · repo lastModified 2026-03-20; 'Release Date: 3/16/2026' · https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 — 'Governing Terms: Use of this model is governed by the NVIDIA Nemotron Open Model License'; license_name nvidia-nemotron-open-model-license
[60] FIRST-PARTY · Last Modified: December 15, 2025 · https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/ — 'NVIDIA Nemotron Open Model License'; 'Works are commercially usable.'
[61] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/lfm2.5:8b-a1b-q4_K_M/blobs/058cb51ed3d5 — '"Threshold" shall mean annual revenue of 10 million United States dollars ($10,000,000) or more.' '(b) Any Commercial Use of the Work or a Derivative Work by a Legal Entity that exceeds the Threshold is not licensed under this Agreement.'; tag 5.2GB 125K
[62] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/exaone3.5:7.8b-instruct-q4_K_M — 'license EXAONE AI Model License Agreement 1.1 - NC'
[63] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/glm4:9b/blobs/e4f0dc83900a — 'For users who wish to use the models for commercial purposes, please do so [here](https://open.bigmodel.cn/mla/form) Complete registration.'
[64] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/ornith-1.5:9b — details list model + projector rows, no license row; ornith:9b page: 'license MIT License Copyright (c) [year] [fullname]'
[65] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/qwen3.6/tags — qwen3.6 only 27b (18GB) and 35b (23GB); qwen3.8/tags only 27b (18GB); qwen3.8-flash-next/tags only 125b-a6b (120GB+)
[66] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/glm-4.7-flash/tags — glm-4.7-flash 19GB; gpt-oss:20b 14GB; muse-glimmer:30b 18GB; nemotron-3.5-lightning 25GB; laguna-xs-2.1 20GB; north-mini-code-1.0 19GB; olmo-3.1 32b 19GB; nemotron3:33b 28GB; phi4:14b 9.1GB (each from its own /tags page)
[67] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/glm-5.3-flash/tags — only 'glm-5.3-flash:cloud'; deepseek-v4.1-flash/tags only ':cloud'
[68] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/deepseek-r1:8b — labels 'tools thinking'; 'license MIT License Copyright (c) 2023 DeepSeek'; 5.2GB
[69] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/rnj-1:8b-instruct-q4_K_M — template 'You are rnj-1, a foundation model traine...'; 5.1GB 32K; Apache
[70] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/falcon3:7b — '472ea1c89f64 · 4.6GB ... license Falcon 3 TII Falcon License December 2024'; 32K; mistral:7b 4.4GB 32K Apache
[71] FIRST-PARTY · repo HEAD 7d9cc26, 2026-09-23 · director/llm.py — llm.py:170-177 sends 'think': False, system + '\n/no_think', format 'json', no num_ctx; stage_manager.py:48 '/no_think', :65-71 'format': 'json', 'think': False, temperature 0.85
[72] secondary · repo HEAD 7d9cc26 · pipeline/_bake.py — line 24: 'VRAM: pause lp-director + `ollama stop qwen3:8b` first (the director holds ~8GB).' (internal note, unmeasured); MODEL_STACK.md:245 records the open Qwen3.5 thinking-default question
[73] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/library/minicpm-v4.5/tags — minicpm-v4.5:8b 6.1GB 40K (vision MLLM; license not evaluated)
[74] FIRST-PARTY · accessed 2026-09-23 · https://ollama.com/search?o=newest — newest-library listing used to sweep for new families (qwen3.8-flash-next, glm-5.3-flash, ornith-1.5, granite4.2, qwen3.8, nemotron-3.5-lightning, muse-glimmer, lfm2.5, minicpm-v4.5, ...)

## Contradictions (first-party vs first-party — unresolved)
- Default num_ctx across Ollama's own docs. https://docs.ollama.com/modelfile says num_ctx '(Default: 2048)' (doc commit 2026-09-15). https://docs.ollama.com/context-length says '< 24 GiB VRAM: 4k context'. The current source (https://github.com/ollama/ollama/blob/main/server/routes.go) sets 4096 when total VRAM is under 23 GiB. I do not pick a side; pinning num_ctx per request makes it moot.
- Nemotron-3-Nano-4B licence name. The Ollama layer (https://ollama.com/library/nemotron-3-nano:4b/blobs/355e036064fa) says 'NVIDIA Open Model License Agreement, Last Modified: October 24, 2025'. NVIDIA's card (https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16) and licence page (https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/) say 'NVIDIA Nemotron Open Model License, Last Modified: December 15, 2025'. Both say it is commercially usable. Unresolved, so the model stays on HOLD.
- Qwen3.5-9B card, internally (https://huggingface.co/Qwen/Qwen3.5-9B). The Quickstart gives the non-thinking reasoning set as 'temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5'. Best Practices gives 'temperature=1.0, top_p=1.0, top_k=40, min_p=0.0, presence_penalty=2.0'. Not resolved. The non-thinking general set (0.7 / 0.8 / 20 / 1.5) is the same in both sections.
- Granite 4.2 thinking control. The Ollama library readme (https://ollama.com/library/granite4.2) says to pass think inside options ('"options": { "think": "high" }'). Ollama's API docs and source make think a top-level request field only (https://docs.ollama.com/capabilities/thinking; https://github.com/ollama/ollama/blob/main/api/types.go, where unknown option keys log 'invalid option provided' and are skipped). The implementation settles which one works; the readme example is non-functional. It is recorded here as a documentation inconsistency.

## Could not confirm
- Runtime VRAM (weights + KV cache + compute buffers) of any candidate on the RTX 2080 Ti at a pinned num_ctx. Also unconfirmed: whether each fits next to the other resident Ollama models. A file size under 7 GB is not the runtime footprint.
- Whether Ollama loads the gemma4 QAT vision projector (992 MB) or the qwen3.5 in-GGUF vision tower into VRAM on text-only requests.
- Which Ollama version runs on supercommons2 and on hil, and therefore whether the host meets the 0.31.2 floor (qwen3.5 think:false+format), 0.30.5 (gemma4 QAT), 0.34.3 (/api/show thinking) and 0.34.4 (single-pass structured outputs).
- Whether granite4.2:8b honours think:false plus a JSON-schema format end to end on the llama-server chat-template path. The minimum Ollama version for that tag is not declared: the path exists in the v0.30.0 source, but the tag's config has no 'requires'.
- Tokens per second or latency of any candidate on Turing sm_75.
- In-character theatrical voice quality and schema-adherence rate per model. Only the bake-off can establish these.
- Whether the Ollama gemma4:e4b-it-qat weights are byte-identical to Google's gemma-4-E4B-it-qat-q4_0-gguf. Likewise for the qwen3.5 and ministral-3 GGUFs against the official HF checkpoints.
- Whether a brand-only lab name on the Ollama page satisfies the 'page names a lab' rule. qwen3.5 says only 'Qwen3.5' and ministral-3 says only 'Ministral 3'; olmo-3 names no lab at all. This is the orchestrator's call.
- The legal effect of Ai2's 'intended for research and educational use' sentence on an Apache-2.0 OLMo 3 model.
- Whether Immersive Commons, or a downstream user of the MIT engine, exceeds LFM2.5's $10M revenue threshold. The exclusion is a judgment call, not a rule-5 disqualification.
- Current prompt token counts of the heartbeat and stage-manager prompts, and therefore whether the VRAM-tier 4096 default truncates them today.
- Whether other small major-lab models exist outside the Ollama library. Only ollama.com library pages and the newest listing's first page were checked; server-side pagination returned the same 20 entries.

## Dropped claims (refuted or unsupported in verification)
- Researcher: gemma4 'The Ollama renderer defaults to off'. Dropped as a statement of served behaviour. gemma4.go has Default:false, but server/model_thinking.go flips it to true for local models, and the v0.34.3 notes show 'default true'. Corrected in the table.
- Researcher: qwen3.5 'Needs Ollama >=0.17.1 (0.17.5 for fixes)' as the operative floor. Replaced by 0.31.2, because think:false plus format was ignored for qwen3.5 until PR #15901 shipped in v0.31.2 (issue #14645).
- Researcher: Granite 4.2 'shipped with num_ctx 131072'. The value is not quoted in any source. Reworded: it shipped a PARAMETER num_ctx of unquoted value; the GGUF context_length is 131072.
- Researcher: the /api/show thinking object was 'documented 2026-09-23' as the availability date. The feature shipped in v0.34.3 on 2026-09-19; only the doc commit is dated 2026-09-23.
- Researcher: 'The opposing claim came from Unsloth, a secondary source'. Dropped as secondary_only; no Unsloth URL was seen this session.
- Researcher: Llama 3.1 'requires a prominently displayed Built with Llama … caps licensees at 700M MAU'. Reworded to the licence's conditional text: the display duty applies on distributing or making available the materials, and above 700M MAU a licence must be requested from Meta.
- Researcher: the Granite 4.2 options.think vs top-level think item as an 'unresolved' first-party contradiction. Resolved by api/types.go: options.think is dropped.
- Researcher: the 'Ministral-3-8B release date could not be confirmed' item. Now confirmed as December 2, 2025 on mistral.ai.
- Researcher c31, 'format … is applied after the thinking block closes', as general behaviour. Limited to Ollama v0.34.4 and later (single pass); earlier versions used a different path.
- Verifier: 'stage-manager prompt ≈600 tokens'. Not re-measured, so kept out of answer_md.

## DO NOT QUOTE (low/unknown)
- [low] 'The director holds ~8GB' of VRAM with qwen3:8b — An internal repo note (pipeline/_bake.py:24), not a measurement, and not a first-party vendor source.
- [unknown] Any runtime VRAM figure for any candidate on the 2080 Ti — Not measured; the file size is not the footprint.
- [unknown] Tokens/sec or latency on Turing, including whether the dense qwen3.5:9b shares the throughput gap in ollama/ollama#14579 — No primary measurement was found or run.
- [low] 'Ollama structured outputs are model-agnostic' as a literal Ollama statement — The docs state no model restriction and exclude only Ollama Cloud. 'Model-agnostic' is an inference, and per-model version bugs existed (qwen3.5 until 0.31.2, gemma4 until 0.21.1).
- [unknown] Unsloth's claim that Qwen3.5-9B does not think by default — No Unsloth URL was seen this session; it appears only via MODEL_STACK.md:245. All first-party sources say thinking is on by default.
- [low] Ministral-3-8B 'released 2025-10-31' — That is the HF repo createdAt. The first-party announcement date is December 2, 2025.
- [low] Granite 4.2 'shipped with num_ctx 131072' — Issue #18074 never quotes the removed PARAMETER num_ctx value; 131072 is the GGUF context_length.
- [low] Stage-manager prompt of about 600 tokens — A verifier estimate from file byte counts, not re-measured and not tokenised.
- [unknown] The minimum Ollama version for granite4.2:8b — The tag declares no 'requires'. v0.30.0 is only the first release whose source contains the llama-server chat-template path.
- [low] Excluding lfm2.5:8b-a1b — A judgment call on a revenue-threshold licence, not a non-commercial licence; not a rule-5 disqualification.
- [unknown] The OLMo 3 HOLD rationale that it is 'research-only' — The licence is Apache 2.0. The 'intended for research and educational use' sentence needs a legal reading.
- [low] Ollama page 'Updated N weeks/months ago' ages — Relative dates that change daily; not usable as release dates.
- [unknown] Byte-identity of Ollama GGUFs with the official HF checkpoints — Not checked. The GGUF headers for qwen3.5 carry no organization field.
- [unknown] In-character voice quality and JSON-adherence rankings of the candidates — Only the bake-off can establish these.


---

# Gap-fill results (2026-09-24)

## G1 — track MJ5: No track evaluated Higgsfield, which upstream already uses as its Midjourney replacement (also affects MJ4 and MJ6). Immersive-commons/living-portraits@5efea6c (2026-09-09), pipeline/hf_gen.py: 'the H…

**Why it matters:** The migration options table and its recommendation have to include, and judge the terms of, the replacement the project has already shipped upstream. Several things decide whether it is safe for a permanent public wall: Higgsfield's training licence over Inputs (the anchor stills), its rules on automation and CLI use, whether pass-through vendor terms apply, and whether a model ID pins its weights. A reseller page is first-party for the reseller's own terms.

**Gap-fill confidence:** medium

### Answer
## MJ5 gap: Higgsfield, the Midjourney replacement upstream already ships (checked 2026-09-24)

### What upstream runs
- Upstream `Immersive-commons/living-portraits@5efea6c` routes stills through `gpt_image_2 --image REF.png`, using the canonical anchor as an Input. Clips go through `kling3_0 --start-image --end-image --aspect_ratio 1:1 --duration 5 --sound off`. Everything passes through one owner-host proxy that runs the `hf` CLI [c59]. Cutover date: 2026-08-08 [c59].
- Side note: upstream's GitHub licence is Apache-2.0. The local repo is MIT [c60].

### (a) Terms of Use
**Version and dates**
- Current version: "Last updated: July 26, 2026". It took effect immediately for new users, and on 2026-08-27 for accounts registered earlier [c1].
- The Wayback Machine shows "August 30, 2025" through 2026-07-22, then a July 23, 2026 version, then the July 26 version from 2026-07-28 onward [c2].
- The July 23 version is marked "did not take effect" [c3].
- Higgsfield's X post of 2026-07-24 announced the revision [c4].
- **Upstream's Aug-2026 uploads may therefore have fallen under the 2025 terms.** Those terms gave Higgsfield an "irrevocable, perpetual… transferable" licence over Inputs and Outputs, including for marketing [c9]. Which version applied depends on when the account was registered, which is unknown.

**Current clauses**
- **Ownership and commercial use:** Higgsfield claims no ownership of Inputs or Outputs and "nor does it restrict your commercial use of Outputs" [c5]. The help centre says this applies to all users, with no separate licence to buy [c27].
- **Training on Inputs:**
  - "Inputs" explicitly include "reference images", so the anchor stills are Inputs.
  - Higgsfield "may" train on "Your Content, Inputs, and Outputs" [c6].
  - The only opt-out is deleting the content or the account, and it applies going forward only. Anything already trained on stays [c7].
  - **Enterprise is the only exception:** no training, and content handled as confidential [c8][c48][c50].
- **CLI and API are explicitly licensed.** They count as "Developer Access" [c10][c11]. All automated or agent activity is treated as the account holder's own [c12]. Being a pass-through or service bureau is banned [c13].
- **Account sharing is banned** [c14]. So is using multiple accounts to evade limits [c15].
- **Suspension:**
  - Any breach of the Developer Terms is a material breach and allows suspension "immediately and without notice" [c16].
  - Developer Access can also be suspended if use "may adversely impact" the Service [c17].
  - Credits are forfeited on termination for cause [c18].
- **Takedown:** after a notice, you must delete the Output and "refrain from re-generating substantially the same Output" [c19].
- **Provenance markers:** Higgsfield may embed invisible markers, and you must not remove them [c20]. Open question: whether the pipeline's center-crop mp4→gif step (`_mp4_to_gif` in the local `pipeline/autogen.py`) counts as removal.
- **Automation on Unlimited plans:** Unlimited use is web-only. There, "Automation tools, scripting, credential sharing… strictly prohibited" [c47][c63]. CLI and MCP use always spends credits instead [c46][c28].

### (b) Official CLI, API and model IDs
**The CLI is official**
- Repo: github.com/higgsfield-ai/cli, MIT, "Copyright (c) 2026 Higgsfield AI".
- Package: npm `@higgsfield/cli`, current version **v1.1.26**, released 2026-09-18 [c30]. Higgsfield's own install page points to it [c29].
- The release binary is named `hf`. The installer adds `higgsfield` and `higgs`, and adds an optional `hf` shortcut [c31].
- The binary is built from the private module `github.com/higgsfield-ai/cli-src v1.1.26` (not public on GitHub). It calls `/developer/v2alpha/` endpoints [c32].
- Higgsfield calls its platform and models "proprietary" [c58].

**There is also a separate paid API**
- api.higgsfield.ai, launched 2026-09-16. It has its own USD balance and does not use plan credits [c52][c57].
- It lists 82 catalog entries. There is no OpenAI or GPT image model in it [c55].

**Model IDs** (CLI flags from MODELS.md and the official skills docs; API from docs.higgsfield.ai)

| ID | Start + end frame | Reference or identity input | Source |
|---|---|---|---|
| `kling3_0` | **Yes** (`--start-image`, `--end-image`). API: `image_url` + `last_image_url` | CLI: none. API: `elements` (Kling element IDs owned by the account) | [c33][c41] |
| `kling3_0_turbo` | **No.** API: "no… elements, or last-frame field" | No | [c34] |
| `gpt_image_2` | not applicable (image model) | `--image-references`/`--image`, repeatable. No weight parameter | [c36] |
| `seedance_2_0` | Yes | Image references, up to 9 total counting start and end frames | [c37] |
| `seedance_2_5` | Yes, per the skills docs. MODELS.md has no schema entry | `image_references` (omni_reference mode) | [c38] |
| `wan2_7` | Yes ("End_image requires start_image") | No image references (audio only) | [c39] |
| `wan3_0` | Not in any CLI docs. The API `alibaba/wan-3.0/image-to-video` has `end_image_url`. It launched on Higgsfield 2026-08-24, after upstream's 08-09 bake-off | API has a separate reference-to-video endpoint | [c40] |
| `grok_video_v15` | **No.** Start frame is required; there is no end frame | API: `image_urls` in reference mode | [c35] |

**Kling 3.0 Omni "element"**
- It is exposed on the web [c42] and on the API: `kling-video/o3/image-reference` takes `first_frame_url` + `last_frame_url` + `image_urls` + `elements` [c41].
- It is **not** exposed on the CLI's `kling3_0`. In the CLI, `--kling_element_ids` appears only on `cinematic_studio_video_v2` [c41].
- Upstream found that the cost endpoint does not validate these combinations, and "only a render proves support" [c59].

### (c) Upstream vendor terms (OpenAI, Kuaishou, ByteDance)
- Only the providers' acceptable-use and prohibited-use policies pass through, and "the more restrictive terms govern" [c21].
- Infrastructure providers may moderate or refuse content "regardless of any claimed license" [c22].
- No clause passes through OpenAI, Kuaishou or ByteDance ownership terms.
- **US availability of Seedance:**
  - First-party: Seedance 2.5 **Draft Mode** is available in "all regions except the US, where the model is unavailable on the provider's side" (2026-09-22) [c43].
  - Enterprise gets Seedance "on dedicated US GPU infrastructure" [c44].
  - No first-party statement covers standard Seedance 2.0 or 2.5 for US subscription or API users.

### (d) Deprecation and whether a model ID pins weights
- **No model ID pins its weights.** The ToS allows Higgsfield to "substitute, deprecate, retire, or remove any model, model version", and says substitution "does not, by itself, constitute a failure" [c23].
- Notice is promised only if a paid plan is "materially and adversely" degraded [c23].
- Developer Access can change "at any time" [c24][c25]. The July 23 draft promised 15 days' notice for breaking changes; the July 26 terms dropped it [c24].
- On the web, Higgsfield "uses the latest available version" of a model family [c26].
- **Consequence:** `kling3_0` could silently change weights mid-graph. That breaks the one-way-door rule for the rendered face.

### (e) Plans
**Subscription**
- The monthly allowance resets and does **not roll over**. Annual plans reset every 30 days [c45]. Upstream measured 3,000 credits granted on the 23rd [c59].
- Credit Packs expire after 90 days [c45].
- Paid plans carry no visible watermark; the free plan does [c51].
- Commercial rights apply on every plan [c27].
- **Per-tier numbers for individual plans (credits, concurrency) could not be confirmed.** The pricing page renders in JavaScript and could not be read. Upstream measured 8 concurrent jobs on its plan [c59].
- Business plans: 16/16 (Team) and 32/32 (Scale) parallel generations. Only Enterprise has "No data training" and indemnification [c48][c50].
- Concurrency Boost adds +4 to +16 on top of a plan's base limit [c49].

**API**
- Minimum top-up $5; funds expire after one year [c52].
- 20 concurrent requests when a key is created (but see Contradictions) [c52][c53].
- Outputs are kept at least 7 days [c54].
- Kling 3.0 std image-to-video: $0.042–0.063/s during a 50%-off offer; the standard rate starts at $0.084/s [c56]. This figure is ambiguous (see Contradictions).

### Row for the MJ4/MJ5 options tables
| Option | End frame | Identity | Output terms | Blocking issues for the public wall |
|---|---|---|---|---|
| Higgsfield `kling3_0` through the CLI (deployed upstream) | `--end-image` [c33] | none on the CLI; `elements` on the API [c41] | Outputs owned, commercial use allowed [c5] | Higgsfield trains on the anchors unless on Enterprise [c6][c8]; no weight pinning or notice [c23][c24]; takedown clause [c19]; plan-tier details unconfirmed |
| Higgsfield `gpt_image_2` (stills) | not applicable | anchor passed as a reference [c36] | same as above | same as above; not in the API catalog [c55]; the CLI README now recommends `gpt_image_2_5` [c36] |

### Contradictions
Reported, not resolved. The URLs are in the contradictions field.

### Could not close
Listed in could_not_confirm.

### Claims
- [c1] FIRST-PARTY · Last updated: July 26, 2026 (accessed 2026-09-24) · https://higgsfield.ai/terms-of-use-agreement — Current Higgsfield ToS last updated July 26, 2026; effective immediately for new users, Aug 27, 2026 for pre-July-26 registrants — "Last updated: July 26, 2026 Effective: immediately for users who register on or after July 26, 2026; on August 27, 2026 for users who registered before July 26, 2026, or upon earlier acceptance."
- [c2] FIRST-PARTY · snapshots 2025-12-15 to 2026-09-08 (accessed 2026-09-24) · https://web.archive.org/cdx/search/cdx?url=higgsfield.ai/terms-of-use-agreement&output=json — Wayback: ToS showed 'Last Updated Date: August 30, 2025' in snapshots 20251215–20260722; 20260725 snapshot shows July 23, 2026 version (existing users Aug 7); 20260728, 20260807, 20260827, 20260908 show July 26, 2026 version — "20260722142903: 'Last Updated Date: August 30, 2025'; 20260725045811: 'Last updated: July 23, 2026' / 'on August 7, 2026 for users who registered before July 23'; 20260728084057: 'Last updated: July 26, 2026'"
- [c3] FIRST-PARTY · accessed 2026-09-24 · https://higgsfield.ai/terms-of-use-agreement-23-07-2026 — The July 23, 2026 ToS version never took effect and is superseded — "This is a prior version of the Terms of Use, posted July 23, 2026, and scheduled to take effect for existing users on August 7, 2026. That scheduled change did not take effect, and this version has been superseded."
- [c4] FIRST-PARTY · 2026-07-24T17:02:16Z (first 272 chars via cdn.syndication.twimg.com; full text via api.fxtwitter.com mirror) · https://x.com/higgsfield/status/2080700103283679275 — Higgsfield X post 2080700103283679275 (2026-07-24) announced the ToS revision limiting its content licence — "Higgsfield's license to your content will be limited to what is necessary to provide, operate, and maintain the best service and experience. The update published on July 23 will become binding for all users by August 7."
- [c5] FIRST-PARTY · Last updated: July 26, 2026 · https://higgsfield.ai/terms-of-use-agreement — Higgsfield claims no ownership of Inputs/Outputs and does not restrict commercial use of Outputs; rights survive cancellation — "Company does not claim ownership of any of your Inputs or Outputs, nor does it restrict your commercial use of Outputs. Your rights in Outputs you have generated and exported survive cancellation of your subscription"
- [c6] FIRST-PARTY · Last updated: July 26, 2026 · https://higgsfield.ai/terms-of-use-agreement — Inputs include reference images; Higgsfield may train on Your Content, Inputs and Outputs (non-Enterprise) — "such as descriptive and instructive text prompts, reference images and videos, and other content (the “Input,” ... You acknowledge and agree that Your Content, Inputs, and Outputs may be used by Company to train, develop, enhance, evolve, and improve its (and its affiliates’) AI models"
- [c7] FIRST-PARTY · Last updated: July 26, 2026 (§4.4, §16.5(c)) · https://higgsfield.ai/terms-of-use-agreement — Training opt-out is only by deleting content/account, forward-only; content already trained on is not removed — "You can stop this going forward by deleting Your Content or your Account ... (iii) content already used to develop or improve Company's AI models before deletion, which cannot feasibly be disassociated from models already trained"
- [c8] FIRST-PARTY · Last updated: July 26, 2026 · https://higgsfield.ai/terms-of-use-agreement — Enterprise Agreement customers: no training on customer content, handled as confidential; Enterprise Agreement controls over ToS — "under those agreements, Company does not use the customer's content to train or improve its AI models, and that content is handled as confidential."
- [c9] FIRST-PARTY · Last Updated Date: August 30, 2025 (snapshot 2026-07-22) · https://web.archive.org/web/20260722142903/https://higgsfield.ai/terms-of-use-agreement — Prior (Aug 30, 2025) ToS, live until at least 2026-07-22 and binding on pre-July-26 accounts until Aug 27, 2026 unless earlier acceptance, granted an irrevocable perpetual transferable licence over Inputs/Outputs incl. marketing — "as well as for marketing and promotional purposes. As such, you hereby grant to the Company a non‑exclusive, irrevocable, perpetual, worldwide, royalty‑free, fully paid, transferable, sublicensable right and license to use any Inputs and Outputs"
- [c10] FIRST-PARTY · Last updated: July 26, 2026 (§1.2) · https://higgsfield.ai/terms-of-use-agreement — Licence covers APIs, MCP, CLI tools for personal/internal business purposes or apps for end users under §11 — "access and use any APIs, MCP integrations, CLI tools, Supercomputer Agent, and other integrations Company makes available to you (if any), solely for your own personal or internal business purposes or, where applicable, to build and operate applications for your end users in accordance with Section "
- [c11] FIRST-PARTY · Last updated: July 26, 2026 (§11.1) · https://higgsfield.ai/terms-of-use-agreement — Developer Terms (§11) apply to CLI use — "This Section 11 applies to you if you access or use the Service through the API, MCP, CLI, or any other programmatic means ("Developer Access")."
- [c12] FIRST-PARTY · Last updated: July 26, 2026 (§11.12) · https://higgsfield.ai/terms-of-use-agreement — Automated/agent access is permitted but treated as the account holder's activity — "Company treats all activity conducted through your Developer Access as your activity, regardless of whether it was initiated by you directly or by an automated agent acting on your behalf."
- [c13] FIRST-PARTY · Last updated: July 26, 2026 (§11.5) · https://higgsfield.ai/terms-of-use-agreement — No pass-through/service-bureau resale of Developer Access — "You shall not sublicense, resell, redistribute, or make Developer Access available on a standalone basis to any third party, or act as a pass-through or service bureau for the Service with no independent value added."
- [c14] FIRST-PARTY · Last updated: July 26, 2026 (§2.4, §11.3) · https://higgsfield.ai/terms-of-use-agreement — Account/credential sharing prohibited; API keys for your use only — "You may not share your Account or login credentials with anyone ... API Keys are confidential credentials issued for your use only."
- [c15] FIRST-PARTY · Last updated: July 26, 2026 (§1.5) · https://higgsfield.ai/terms-of-use-agreement — Usage Limits (incl. concurrency) may be changed without notice; multiple accounts to evade limits prohibited — "Company may impose or modify Usage Limits without notice. ... including by creating multiple Accounts, distributing requests across Accounts"
- [c16] FIRST-PARTY · Last updated: July 26, 2026 (§16.2) · https://higgsfield.ai/terms-of-use-agreement — Breach of Developer Terms is a material breach; suspension/termination immediately without notice — "Company has the right to immediately and without notice suspend or terminate any Service provided to you. Without limiting the foregoing, a breach of Section 11 (Developer Terms) ... constitutes a material breach"
- [c17] FIRST-PARTY · Last updated: July 26, 2026 (§11.9) · https://higgsfield.ai/terms-of-use-agreement — Developer Access can be suspended without notice for performance impact — "Company may suspend or restrict your Developer Access immediately and without prior notice if it reasonably believes that: ... (ii) your use may adversely impact the performance or availability of the Service"
- [c18] FIRST-PARTY · Last updated: July 26, 2026 (§16.4) · https://higgsfield.ai/terms-of-use-agreement — On termination for cause, fees non-refundable and subscription credits forfeited — "If Company terminates your Account for violation of this Agreement ... all Fees paid are non-refundable and all unused Subscription Credits and Promotional Credits are immediately forfeited"
- [c19] FIRST-PARTY · Last updated: July 26, 2026 (§6.6) · https://higgsfield.ai/terms-of-use-agreement — Removal-request clause obliges deleting Output and not regenerating it — "you will promptly (a) stop using and distributing it, (b) delete it from the accounts and systems within your control, and (c) refrain from re-generating substantially the same Output."
- [c20] FIRST-PARTY · Last updated: July 26, 2026 (§6.4, §5.5) · https://higgsfield.ai/terms-of-use-agreement — Higgsfield may embed imperceptible provenance markers; users must not remove them — "Company may embed machine-readable watermarks, secure metadata, or content-provenance signals (such as those based on the C2PA / Content Credentials standard) into Outputs ... you will not remove, alter, or obscure any provenance signals or markings Company applies under Section 6.4."
- [c21] FIRST-PARTY · Last updated: July 26, 2026 (§8) · https://higgsfield.ai/terms-of-use-agreement — Only third-party model providers' acceptable-use policies pass through; more restrictive governs — "When you use a feature or model powered by a third party, you agree to comply with that provider’s applicable acceptable-use or prohibited-use policies (as updated from time to time), in addition to this Agreement; where those policies are more restrictive, the more restrictive terms govern"
- [c22] FIRST-PARTY · Last updated: July 26, 2026 (§15) · https://higgsfield.ai/terms-of-use-agreement — Third-party infrastructure providers may moderate/refuse content regardless of rights documentation — "Company, and in some cases its Third-Party Infrastructure providers, reserve the right to moderate, remove, or decline to process any content regardless of any claimed license or rights documentation submitted by you."
- [c23] FIRST-PARTY · Last updated: July 26, 2026 (§1.7) · https://higgsfield.ai/terms-of-use-agreement — Higgsfield may substitute/retire any model or model version at any time; substitution is not a failure; notice only for material degradation of a paid plan — "Company may add, modify, substitute, deprecate, retire, or remove any model, model version, or feature at any time ... a change to or substitution of an underlying model does not, by itself, constitute a failure to provide the Service."
- [c24] FIRST-PARTY · July 23, 2026 (archived) vs July 26, 2026 (current) · https://higgsfield.ai/terms-of-use-agreement-23-07-2026 — Developer Access may be changed at any time; the July 23 draft's 15-day notice for breaking changes was removed in the July 26 version — "July 23: 'Company will use commercially reasonable efforts to provide at least 15 days’ advance notice before making any change that is not backwards-compatible.' July 26 (§11.10): 'Company may modify, update, or discontinue any aspect of Developer Access at any time.'"
- [c25] FIRST-PARTY · Last updated: July 26, 2026 (§13.8) · https://higgsfield.ai/terms-of-use-agreement — API/MCP schemas, endpoints or supported models may change at any time — "Company may change the API, MCP interfaces, schemas, endpoints, or supported models at any time"
- [c26] FIRST-PARTY · Aug 1, 2026 · https://higgsfield.ai/creator-hub/help-center/ai-models/which-ai-model-should-i-use — On the web, Higgsfield auto-selects the latest version within a model family — "You don't need to pick a specific version: start with the family that matches your goal, and Higgsfield uses the latest available version within it."
- [c27] FIRST-PARTY · Aug 2, 2026 · https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially — Ownership help article: rights apply to all users; no separate commercial licence; indemnification Enterprise-only — "This applies to all users of the Service. ... There is no separate commercial license to purchase ... Legal indemnification, protection against third-party IP claims, is available on the Enterprise plan only."
- [c28] FIRST-PARTY · Aug 1, 2026 · https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli — CLI use falls under Developer Terms, uses plan credits, no API key, no Unlimited/free gens — "Accessing Higgsfield through the CLI falls under the Developer Terms in the Terms of Use ... Both use the same Higgsfield account and plan credits with no API key, and Unlimited models and free generations don't apply to either."
- [c29] FIRST-PARTY · accessed 2026-09-24 · https://higgsfield.ai/cli — higgsfield.ai/cli official page instructs installing @higgsfield/cli and links github.com/higgsfield-ai/cli — "1. Install the CLI: run `npm i -g @higgsfield/cli` . 2. Authenticate: run `higgsfield auth login`"
- [c30] FIRST-PARTY · repo created 2026-04-29; release 2026-09-18; accessed 2026-09-24 · https://github.com/higgsfield-ai/cli — Official CLI repo is MIT (Copyright 2026 Higgsfield AI); latest release v1.1.26 on 2026-09-18; npm @higgsfield/cli latest 1.1.26, licence MIT — "MIT License  Copyright (c) 2026 Higgsfield AI; releases: v1.1.26 2026-09-18T23:39:48Z; npm dist-tags {'latest': '1.1.26'}"
- [c31] FIRST-PARTY · accessed 2026-09-24; assets hf_1.1.26_{darwin,linux,windows}_{amd64,arm64}.tar.gz · https://github.com/higgsfield-ai/cli/blob/main/install.sh — The release binary is named hf; installer installs higgsfield + higgs and an optional hf shortcut — "# Installs `higgsfield` (primary) + `higgs` symlink (always). # Tries to install `hf` shortcut unless taken (e.g. by huggingface CLI)."
- [c32] FIRST-PARTY · binary built 2026-09-18; inspected 2026-09-24 · https://github.com/higgsfield-ai/cli/releases/tag/v1.1.26 — hf binary is built from a non-public Go module and calls v2alpha developer endpoints; notices reserve rights — "go buildinfo: 'mod github.com/higgsfield-ai/cli-src v1.1.26' (gh api repos/higgsfield-ai/cli-src → 404); strings: '/developer/v2alpha/jobs/'; THIRD-PARTY-NOTICES: 'Higgsfield reserves all rights not expressly granted herein.'"
- [c33] FIRST-PARTY · MODELS.md last commit 2026-09-11 (accessed 2026-09-24) · https://github.com/higgsfield-ai/cli/blob/main/MODELS.md — CLI kling3_0 accepts start and end image, aspect 16:9/9:16/1:1, sound default on, modes std/pro/4k; no image-reference/element flag — "### kling3_0 — Kling v3.0 ... | `--end-image` (single) | false | — | UUID or path | ... | `--sound` | false | `on` | `on`, `off` | | `--start-image` (single) | false | — | UUID or path |"
- [c34] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/models/kling-3/turbo-image-to-video.md — kling3_0_turbo has no end frame (CLI and API) — "This endpoint has no sound, multi\_shots, elements, or last-frame field."
- [c35] FIRST-PARTY · repo pushed 2026-09-14 (accessed 2026-09-24) · https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/media-inputs.md — grok_video_v15 requires a single start frame; no end frame — "| `grok_video_v15` | `start_image` | Required single start frame. CLI also accepts `--image` and maps it to `start_image`. |"
- [c36] FIRST-PARTY · 2026-09-11 commit; changelog 2026-09-22 · https://github.com/higgsfield-ai/cli/blob/main/MODELS.md — gpt_image_2 takes repeated image references, aspect incl 1:1, default resolution 2k; CLI docs now recommend gpt_image_2_5; GPT Image 2.5 launched 2026-09-22 — "### gpt_image_2 — GPT Image 2 ... | `--image-references` (or `--image`) (repeated) | false | — | UUID or path | ... | `--resolution` | false | `2k` | `1k`, `2k`, `4k` |; gpt_image_2_5: 'Recommended default for high-fidelity image generation' (commit 3e52877, 2026-09-11)"
- [c37] FIRST-PARTY · accessed 2026-09-24 · https://github.com/higgsfield-ai/cli/blob/main/MODELS.md — seedance_2_0 accepts start and end image plus image references (≤9 incl. frames), audio on by default — "At most 9 image references are allowed (counting start_image and end_image). ... | `--generate_audio` | false | `true` | boolean |"
- [c38] FIRST-PARTY · accessed 2026-09-24 · https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/media-inputs.md — seedance_2_5 accepts start_image, end_image, image_references (per skills docs); MODELS.md has no seedance_2_5 schema; API i2v: output framing follows image_url — "| `seedance_2_5` | `start_image`, `end_image`, `image_references`, `video_references`, `audio_references` | Use `--mode omni_reference` for reference generation. `t2v` accepts no media. |; API: 'Output framing follows image\_url; end\_image\_url is the optional last frame.'"
- [c39] FIRST-PARTY · accessed 2026-09-24 · https://github.com/higgsfield-ai/cli/blob/main/MODELS.md — wan2_7 accepts end image only with a start image; aspect incl 1:1; no image references — "### wan2_7 — Wan 2.7 ... | `--end-image` (single) | false | — | UUID or path | ... - End_image requires start_image."
- [c40] FIRST-PARTY · accessed 2026-09-24; changelog 2026-08-24 · https://docs.higgsfield.ai/docs/models/wan-3/image-to-video.md — wan3_0 is absent from all CLI docs; API Wan 3.0 i2v has end_image_url and aspect default adaptive; Wan 3.0 launched on Higgsfield 2026-08-24 — "Use image\_url for the first frame and optional end\_image\_url for the last frame. Reference arrays belong to the reference-to-video endpoint.; changelog: 'Wan 3.0 and Wan 3.0 Prime. Now on Higgsfield' (Mon, 24 Aug 2026)"
- [c41] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/models/kling-o3/image-reference.md — Kling elements exposed on API (Kling 3.0 i2v, Omni/O3 image-reference); Kling O3 image-reference schema combines first_frame_url, last_frame_url, image_urls, elements, aspect 1:1; Omni/O3 first-last-frame have no elements; CLI element flag only on cinematic_studio_video_v2 — "elements contains Kling element IDs as decimal strings. Each ID must belong to the account making the request; arbitrary provider IDs are rejected.; params: elements, image_urls, aspect_ratio ("16:9","9:16","1:1"), last_frame_url, first_frame_url; CLI MODELS.md: '| `--kling_element_ids` | false | — "
- [c42] FIRST-PARTY · Aug 1, 2026 · https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-kling — Web Kling family includes Kling 3.0 Omni and Elements with start/end frames — "Kling 3.0 Omni Highest-quality generation and editing in one model 4K 3-15s ... Upload Start and End Frames. ... Add Elements if needed. Elements lock specific characters, products, or objects"
- [c43] FIRST-PARTY · Tue, 22 Sep 2026 · https://higgsfield.ai/creator-hub/changelog#seedance-2-5-draft-mode-preview-before-the-final — Seedance 2.5 Draft Mode unavailable in the US on the provider's side — "Availability: all regions except the US, where the model is unavailable on the provider's side."
- [c44] FIRST-PARTY · Wed, 19 Aug 2026 · https://higgsfield.ai/creator-hub/changelog#higgsfield-for-enterprise — Enterprise offers Seedance on dedicated US GPU infrastructure — "Enterprise access to Seedance models on dedicated US GPU infrastructure, with dedicated capacity and concurrency."
- [c45] FIRST-PARTY · Aug 3, 2026; ToS July 26, 2026 · https://higgsfield.ai/creator-hub/help-center/credits/how-credits-work — Subscription credits reset per billing period and do not roll over (annual: every 30 days); Credit Packs expire 90 days — "Subscription credits reset regularly and don't roll over: on monthly plans with each paid renewal, on annual plans every 30 days.; ToS §9.4: 'Subscription Credits are allocated per billing period and do not roll over to subsequent billing periods'"
- [c46] FIRST-PARTY · Aug 3, 2026 · https://higgsfield.ai/creator-hub/help-center/credits/how-credits-work — MCP/CLI/automated generations always deduct credits; Unlimited is website-only — "any generation made outside it, including through MCP, CLI, Canvas, Supercomputer, and other automated tools, always deducts credits, regardless of plan."
- [c47] FIRST-PARTY · Aug 3, 2026 · https://higgsfield.ai/creator-hub/help-center/credits/what-are-unlimited-models-and-which-plans-include-them — Unlimited fair use prohibits automation, scripting, credential sharing — "Unlimited is designed for personal, human use only. Automation tools, scripting, credential sharing, and reselling access are strictly prohibited."
- [c48] FIRST-PARTY · Aug 2, 2026 · https://higgsfield.ai/creator-hub/help-center/business/team-and-business-higgsfield — Business plan comparison: parallel gens Team 16/16, Scale 32/32; no-data-training and indemnification only on Enterprise — "Parallel generations (image / video) 16 / 16 32 / 32 Dedicated capacity ... SOC 2 and legal indemnification No No Yes No data training No No Yes"
- [c49] FIRST-PARTY · Aug 3, 2026 · https://higgsfield.ai/creator-hub/help-center/credits/how-does-concurrency-boost-work — Concurrency Boost adds +4 to +16 over base concurrency — "Added concurrency +4, +8, +12, or +16 on top of your base limit ... The maximum additional concurrency is +16 above your base limit."
- [c50] FIRST-PARTY · accessed 2026-09-24 · https://higgsfield.ai/enterprise — Enterprise: full IP ownership, contract-backed indemnification, contractual no-train guarantee — "Enterprise agreements include full IP ownership of your outputs and contract-backed indemnification ... Higgsfield Enterprise never trains models on your data. ... under a contractual no-train guarantee"
- [c51] FIRST-PARTY · Aug 3, 2026 · https://higgsfield.ai/creator-hub/help-center/credits/watermark-and-how-to-remove — Free accounts watermark every generation; paid plans no visible watermark; invisible markers may remain — "On a free account, every generation carries a Higgsfield watermark. On any paid plan, generations come without a watermark."
- [c52] FIRST-PARTY · Sep 16, 2026 · https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api — Higgsfield API is a separate product: USD prepaid, $5 min top-up, funds expire in 1 year, key unlocks 20 concurrent requests — "Creating a key unlocks 20 concurrent requests. ... the minimum top-up is $5. ... Funds expire one year after they are added to the balance."
- [c53] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/concepts/rate-limits.md — API docs: limits depend on account and model; example error shows 4 concurrent — "Rate limits depend on the account and the selected model. ... "detail": "Maximum number of concurrent requests (4) has been reached""
- [c54] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/concepts/billing-and-retention.md — API outputs retained at least 7 days; failed/NSFW not charged — "Generated output is accessible for at least seven days after creation and may be removed after that period.; 'Requests ending as `failed` or `nsfw` are not charged.'"
- [c55] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/models.md — API image catalog has no OpenAI/GPT image model; catalog 82 entries as of 2026-09-22 — "SOUL, Soul ID training, Marketing Studio, Grok, Recraft, Qwen Image, Ideogram, and Z-Image. ... The catalog covers 82 entries listed for sale as of September 22, 2026: 16 Image and 66 Video."
- [c56] FIRST-PARTY · accessed 2026-09-24 · https://open.higgsfield.ai/models/kling-video/v3.0/std/image-to-video — API Kling 3.0 std i2v price_range $0.042–0.063/s during 50%-off promo; standard stated as $0.084/$0.126 per second — ""price_range":{"min_amount":"0.042","max_amount":"0.063","currency":"USD","unit":"sec"}; 'Note: these rates are 50% off; standard rates are $0.084 per second for 1 second clips and $0.126 per second for 3 or 15 second clips.'"
- [c57] FIRST-PARTY · Wed, 16 Sep 2026 · https://higgsfield.ai/creator-hub/changelog#higgsfield-api-is-here — Higgsfield API launched 2026-09-16, separate from plans, with launch discounts — "Separate from higgsfield.ai plans and credits. ... Launch offer: 15% off all models, up to 50% off on 4 models of your choice."
- [c58] FIRST-PARTY · Sep 5, 2026 · https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms — Higgsfield states its platform and models are proprietary; official surfaces are higgsfield.ai or linked from it — "The Higgsfield platform and its models are proprietary ... Every official Higgsfield surface is either part of higgsfield.ai or linked from it"
- [c59] secondary · bakeoff run 2026-08-09; commit 5efea6c 2026-09-09 · https://github.com/Immersive-commons/living-portraits/blob/main/_bakeoff/README.md — Upstream measurements/config (first-party only for upstream's own account): gpt_image_2 + kling3_0 via proxy; 3000 credits/month on the 23rd no rollover; 8 concurrent; kling3_0 1:1/5s 960x960 7.5 credits sound off; turbo/grok refused end frame; seedance_2_5 returned 1280x720; cutover 2026-08-08 — "The plan caps CONCURRENT jobs at 8 (`error_type: rate_limit_reached`, `concurrent_jobs_limit: 8`); hf_gen.py: 'Credits are a MONTHLY pool (3000, granted on the 23rd, and NOT rolled over)'; ARCHITECTURE.md: 'Higgsfield replaced it on 2026-08-08.'"
- [c60] FIRST-PARTY · accessed 2026-09-24 · https://github.com/Immersive-commons/living-portraits/blob/main/LICENSE — Upstream Immersive-commons/living-portraits is Apache-2.0 while local Wenjix repo LICENSE is MIT — "Apache License Version 2.0, January 2004 (upstream) vs local LICENSE 'MIT License Copyright (c) 2026 Rayyan Zahid / Immersive Commons'"
- [c61] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/models/kling-3/pro-image-to-video.md — API Kling 3.0 i2v schema has no aspect_ratio field (CLI kling3_0 has one) — ""required": ["image_url"], "properties": {"sound" ... "duration" ... "elements" ... "cfg_scale" ... "image_url" ... "multi_shots" ... "multi_prompt" ... "last_image_url"}"
- [c62] FIRST-PARTY · Aug 1, 2026 · https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-seedance — Older Seedance versions remain available (no formal deprecation policy found) — "Older versions (Seedance 1.5 Pro, Seedance Pro, and Seedance Pro Fast) remain available under All models in the model picker."
- [c63] FIRST-PARTY · Last updated: July 26, 2026 (§10.6) · https://higgsfield.ai/terms-of-use-agreement — Unlimited plan usage that is automated may be throttled/suspended — "Company may restrict, suspend, throttle, or place on a slower processing queue usage that is automated or materially exceeds typical individual use"

### Could not confirm
- Individual subscription tiers: plan names, prices, monthly credit counts and per-tier concurrency. The pricing page https://higgsfield.ai/pricing renders client-side, the r.jina.ai renderer was blocked (403), and Wayback snapshots are empty shells. '3000 credits on the 23rd' and '8 concurrent jobs' come only from upstream's own account measurements.
- Whether any Higgsfield model ID pins weights, either a CLI job_set_type such as kling3_0 or an API endpoint ID such as kling-video/v3.0/std/image-to-video. No first-party pinning or version-freeze statement exists, and ToS §1.7 reserves the right to substitute models.
- Any model deprecation notice period for Developer Access. None exists in the current ToS; the 15-day notice appears only in the July 23 draft that never took effect.
- Whether upstream vendor output or ownership terms (OpenAI, Kuaishou, ByteDance) pass through Higgsfield. Only acceptable-use and prohibited-use policies pass through (ToS §8). Higgsfield publishes no per-vendor terms page.
- US availability of standard (non-Draft) Seedance 2.0 and 2.5 for US subscription, CLI or API users. No explicit first-party statement was found.
- Whether wan3_0 is still a valid CLI job_set_type. It is absent from every CLI doc revision checked; confirming it needs an authenticated `higgsfield model list`.
- The seedance_2_5 CLI flag schema. MODELS.md has no entry; only the skills docs list start_image and end_image.
- Whether Kling O3 image-reference actually honours first_frame_url + last_frame_url + elements together. Only the schema was seen, and upstream found that accepted parameters are not always honoured.
- Output aspect for a square input on API Kling 3.0 image-to-video. The schema has no aspect_ratio field.
- Mapping of Higgsfield API names ('Kling Omni', released 2025-12-01; 'Kling O3', released 2026-02-01) to Kuaishou's names ('Kling 3.0 Omni', 'O1').
- Upstream's claim that the CLI session uses one-time-use refresh tokens. The first-party README says only 'tokens are short-lived. Re-run `higgsfield auth login`.'
- Whether the MIT licence covers the distributed hf binary. The repo holds only docs and an installer; the binary comes from the non-public module github.com/higgsfield-ai/cli-src.
- Which ToS version governed upstream's August 2026 anchor uploads. The 2025 perpetual/irrevocable licence applied to pre-July-26 accounts until 2026-08-27 unless the user accepted the new terms earlier; the account's registration date and acceptance date are unknown.
- Subscription credit prices per model and configuration (for example, 7.5 credits for kling3_0 at 1:1, 5 s, sound off). Higgsfield publishes no credit table; cost appears only on the Generate button or through `hf generate cost`. Upstream measured those numbers.
- The sound-off API price per 5 s clip for Kling 3.0 image-to-video or O3 first-last-frame. The first-party descriptions are ambiguous ('for 1 second clips... 3 or 15 second clips'), and the promo discount has no stated expiry.
- Whether the pipeline's mp4→gif center-crop transcode counts as removing provenance markers under ToS §5.5/§6.4. It is also unknown whether Higgsfield embeds such markers in CLI outputs at all.
- The remainder of the X post's replies. The Community Note (secondary) described the July 23 draft's perpetual licence.

### Verification (combined lens)
I re-fetched every cited source on 2026-09-24. The ToS quotes (§§1.2, 1.5, 1.7, 2.4, 4.4, 5.5, 6.4, 6.6, 8, 9.4, 10.6, 11.1–11.12, 13.8, 15, 16.2, 16.4, 16.5) match the July 26, 2026 text word for word. The Wayback chronology checks out: May 12 2025, then Aug 30 2025 (through 20260722), then July 23 2026 (20260725), then July 26 2026 (from 20260728). The CLI facts are also confirmed: github.com/higgsfield-ai/cli is MIT, v1.1.26 released 2026-09-18, npm @higgsfield/cli 1.1.26, and the hf binary is built from the non-public github.com/higgsfield-ai/cli-src and calls /developer/v2alpha. So are the model-flag tables in MODELS.md and the skills docs, the API docs schemas, the changelog items (Seedance 2.5 Draft Mode is not available in the US; Enterprise gets Seedance on US GPUs; the API post is dated 09-16; Wan 3.0 on 08-24), and upstream's measurements.

Where the answer is weak:
- **c3 overstated:** the July 23 ToS was stated as immediately effective for new registrants.
- **c4:** the quoted post text comes only from a third-party mirror.
- **c23:** the quote drops a proviso.
- **c37:** first-party sources contradict each other on seedance_2_0 --generate_audio.
- **c41/c42:** mapping 'Kling O3' to 'Kling 3.0 Omni', and Omni Elements on the web, are unsupported.
- **c56:** the API price comes from a JSON field whose text varies by page.
- **§(e):** Higgsfield's own blog does give per-tier credits (Starter 200, Plus 1,000, Ultra 3,000) and Ultra's 8+8 parallel limit, which contradicts 'could not confirm'.

Important misses:
- ToS §5.2(iv) bans training any model on Outputs.
- ToS §11.7 bans presenting Outputs as human-made.
- ToS §3.2 makes the most permissive visibility the default.
- Enterprise plans get rollover credits.
- The July 25 ToS blog post.
- §19.6 notice was also cut from 15 days to 'reasonable'.
- The 30-day price-increase notice.
- Official SDKs, plus an earlier 2025 API SDK.
- Two first-party contradictions on API pricing and credits terminology.
- Upstream's HF_PROXY.md warns against using someone else's proxy, which is the account-sharing risk.

Scratch files are in <session scratch, not kept>/mj5-verify/.

Checks not marked "supported":
- **partially_supported**: The July 23, 2026 ToS version never took effect and is superseded → Only the scheduled Aug 7 effect for EXISTING users did not take effect; the July 23 text (with §4.3 'transferable, perpetual, irrevocable' licence) was stated as immediately effective for users registering July 23-25, 2026. Whether it bound them is not stated.
- **partially_supported**: X post 2080700103283679275 (2026-07-24) announced the ToS revision → Date/author first-party; full quoted text secondary_only (mirror).
- **partially_supported**: Higgsfield may substitute/retire any model version at any time; substitution not a failure; notice only for material degradation of paid plan → The quote's ellipsis drops the proviso 'provided that the Service continues to provide substantially similar overall functionality'. Conclusion (no weight pinning) still holds.
- **partially_supported**: seedance_2_0 start+end, refs ≤9 incl frames, audio on by default → First-party contradiction on seedance_2_0 audio flag between higgsfield-ai/cli MODELS.md and higgsfield-ai/skills media-inputs.md; not resolved.
- **partially_supported**: Kling elements on API; O3 image-reference combines first/last frame + image_urls + elements; CLI element flag only on cinematic_studio_video_v2 → Schema facts supported; answer's identification of API 'Kling O3' as 'Kling 3.0 Omni' is not stated in any first-party source seen (researcher's own could_not_confirm says so).
- **partially_supported**: Web Kling family includes Kling 3.0 Omni and Elements with start/end frames → Elements + start/end frames are described for the generic Kling multi-shot flow, not specifically for Kling 3.0 Omni; answer's 'Omni element is exposed on the web' overstates.
- **partially_supported**: API Kling 3.0 std i2v $0.042–0.063/s promo; standard $0.084/$0.126 → The $0.084/$0.126 'standard' figures come from a related_models_description field whose text differs per page, so it may not describe this endpoint; a separate overview price of $0.0840/second also appears. Treat API per-second price as unconfirmed.
- **contradicted**: Per-tier individual plan credits/concurrency could not be confirmed (answer §e and could_not_confirm) → First-party (marketing blog) figures exist: Ultra = 3,000 credits/month and up to 8 parallel video jobs, matching upstream's measured 3000/8. Pricing page itself remains JS-rendered.

Flagged as unconfirmed by the verifier:
- API Kling 3.0 std image-to-video 'standard rate starts at $0.084/s' (answer §e, c56): taken from a related_models_description field whose text differs per page (O3 page gives $0.056/$0.112 for the same field). The same page also shows overview price 0.0840/second and says 'Public pricing information is not available'. Not confirmed as this endpoint's price.
- 'Kling 3.0 Omni element is exposed on the web' and 'kling-video/o3/image-reference' = Kling 3.0 Omni: no first-party page seen equates API 'Kling O3' with 'Kling 3.0 Omni', and the web help article ties Elements to the generic Kling multi-shot flow.
- 'Higgsfield API launched 2026-09-16': true only for the standalone product announced in the changelog. higgsfield-client 0.1.0 ('Higgsfield API Python SDK', 2025-11-17, cloud.higgsfield.ai) shows an earlier API existed.
- 'Per-tier numbers for individual plans could not be confirmed' and 'Higgsfield publishes no credit table': Higgsfield's own blog (Sep 15, 2026 / Jun 26, 2026) publishes Starter/Plus/Ultra credits (200/1,000/3,000), Ultra concurrency (8 video + 8 image), and sample per-clip credit costs.
- 'The July 23 version is marked did not take effect': the banner says only the scheduled Aug 7 effect for existing users did not happen. That version said it was effective immediately for users registering on or after July 23, 2026.
- Process counts in commands_run ('all 67 help-center articles', '13 snapshots') were not reproduced. The creator-hub sitemap lists 95 non-changelog URLs, including category pages.

---

## G2 — track MJ5: Neither track answers whether any non-MJ API takes an identity anchor in the same call as explicit start and end frames (also affects MJ4). I found that the Kling 3.0/3.0 Omni image-to-video doc (http…

**Why it matters:** Mission question (3) asks for a single identity anchor plus start/end-frame image-to-video. An identity element alongside first/last frames is the closest documented analogue to the current oref-plus-end-frame pipeline, and it could reduce face drift in the frames between the endpoints. Kling ranks #1 in both MJ4 and MJ5, so if US access or the terms fail, both shortlists collapse.

**Gap-fill confidence:** high

### Answer
## MJ5/MJ4 gap: Kling identity element plus first and last frames in one call (checked 2026-09-24, first-party Kling docs only)

**Verdict:** Yes, Kling does this. Kling 3.0 and Kling 3.0 Omni accept an `element` in the same request as `first_frame` and `last_frame`, up to 3 elements [c1][c2][c3][c5][c6]. O1 explicitly does not allow it [c7][c8]. Kling 2.6 has no `element` input at all [c9][c10]. 3.0 Turbo has no last frame [c11]. The docs name no US exclusion, but they also give no positive list of supported countries (see section 4).

### 1. Which models take element + first_frame + last_frame
| Model | Endpoint | Element with first+last frame? | Limit / constraints |
|---|---|---|---|
| **Kling 3.0** | `POST /image-to-video/kling-3.0` | **Yes.** The enum is `prompt, first_frame, last_frame, element` [c1], and the doc has an example headed "First_frame & last_frame & element" [c3]. | "Up to 3 Elements can be specified" [c2]. Last-frame-only is not supported [c4]. `settings.multi_shot` defaults to `true`, so it must be set to false for a single shot [c4]. There is no aspect_ratio setting. |
| **Kling 3.0 Omni** | `POST /omni-video/kling-3.0-omni` | **Yes.** The doc's example sends first frame + last frame + 2 elements [c6]. | "When using the first frame or first and last frames to generate video, a maximum of 3 element are supported" [c5]. `aspect_ratio` accepts 16:9, 9:16 or 1:1, but is "required" only when there is no first frame [c5]. |
| Kling O1 | `POST /omni-video/kling-o1` | **No.** "Using first+last frames: Elements are not supported." [c7], confirmed by the 2026-03-11 changelog entry [c8] | With both frames set, "no additional reference images can be added" [c7]. |
| Kling 2.6 | `POST /image-to-video/kling-2.6` | **No.** The enum is `prompt, first_frame, last_frame, voice` [c9], and the capability map marks Element Control "Not Supported" [c10]. | First+last frame output is 1080p only [c9]. |
| Kling 3.0 Turbo | `/image-to-video/kling-3.0-turbo` | No last frame at all [c11]. | |
- Kling's own user guide says the same for 3.0: "binding up to 3 elements in start frame/start and end frames generation" [c19]. It adds that "The elements must appear in the reference frames" [c19].
- The 2026-05-07 changelog removed the old block on combining multi-shot with first/last frames, for `kling-v3-omni` and `kling-v3` [c12].

### 2. Creating an element
- **Endpoint and inputs:** `POST /v1/general/advanced-custom-elements` with `reference_type: image_refer`. It needs "at least one frontal reference image (frontal_image), and 1 to 3 additional reference images (image_url) that differ from the front". Each image must be ≤10MB and ≥300px, with aspect ratio between 1:2.5 and 2.5:1 [c13].
- **Only one anchor image is needed.** The project has a single canonical anchor. `POST /v1/general/ai-multi-shot` takes one `element_frontal_image` and generates the extra views, at 20 Units ($0.07) per call [c20][c40].
- **Painted, non-photographic faces:** no API page addresses them.
  - The only style restriction in the API applies to video-built elements: "only realistic-style humanoid figures can be customized through video" [c14]. No such restriction is stated for `image_refer`.
  - The consumer guide lists allowed character types that include "historical/fantasy characters, anime-style characters, CG-rendered characters" [c15].
  - Painted or Old-Master faces are not named anywhere. Whether they are accepted, and whether content moderation lets them through, is unconfirmed.
- **Do elements persist or expire?**
  - No expiry or TTL is documented. Status is `succeed` or `deleted`, and there is an explicit delete endpoint [c16].
  - The documented 30-day purge applies to "generated results" [c38]. Nothing says whether it covers elements.
  - Elements from the old element API cannot be queried through the new one [c18].
  - The two element pages give different delete paths (see Contradictions).
- **Identity-conditioned stills:**
  - Kling Image 3.0 (`kling-v3`, at `/v1/images/generations`) and 3.0 Omni / O1 (at `/v1/images/omni-image`) all take an `element_list`. Reference images plus elements must total 10 or fewer [c22][c23].
  - The image capability map still marks "Character Feature Reference" and "Face Feature Reference" as supported **only on Kling Image 2.1**. It marks "Subject Control" as "Supported: Multi-image main image only" on 3.0, 3.0 Omni and O1 [c21].
  - Elements have no strength or weight knob. `human_fidelity` is still "Only kling-v2-1" [c22].
  - What this changes in MJ4: "only kling-v2-1 documents identity" should narrow to "only kling-v2-1 documents a **tunable** face/identity weight". Element-based subject reference is documented for v3, v3-omni and O1 stills.

### 3. Does an element change the price?
- The video pricing table has no element dimension. The only billing axes are audio, video input, motion control and resolution [c24].
  - Kling 3.0 "No Native Audio": 0.6 Units ($0.084)/s at 720P.
  - Kling 3.0 Omni "No Video Input x No Native Audio": 0.6 Units ($0.084)/s at 720P.
  - So a 5 s clip at 720p with no audio comes to $0.42 (my arithmetic) whether or not an element is attached, as far as the table shows.
- Image pricing: Kling Image 3.0 / 3.0 Omni / O1 cost 8 Units ($0.028) per image [c25].
- The API price of **creating** an element is not listed [c27]. The consumer guide says "Creating an element is free", but that is the consumer app [c26].

### 4. Can US customers use the API?
- **No explicit US exclusion appears** in the API terms, the API privacy policy or the Terms of Service. No list of supported countries was found.
- Contracting entity and law:
  - The contract is with Kling AI Pte. Ltd. [c28].
  - Governing law is "the laws of Singapore", with SIAC arbitration seated in Singapore [c29].
  - Users must represent that they are not subject to sanctions [c30].
  - The license runs "within the geographical scope of business" (the term is not defined) [c28].
  - Clause 11.10 says Kling does not guarantee the Services "are or will be appropriate or available for any other location or jurisdiction" [c28].
- Signals that US users are expected:
  - The API privacy policy has a "California (United States)" CCPA section [c31].
  - Data is stored "on our servers located in Singapore" [c31].
- Endpoints: there is only one, `https://api-singapore.klingai.com`, which is "suitable for users whose servers are located outside of China" [c32]. No US region endpoint is documented.
- Sign-up is by email login at kling.ai/dev, with no country list [c33].

### 5. Model lifecycle
- **No deprecation notice exists for kling-v2-1 (image) or kling-v3 / Kling 3.0 (video)** in the API updates page [c36].
- Stated notice period: Kling will give "at least 30 days" notice before it adjusts or terminates services (terms clause 4.1) [c34].
- 2026-07-15 changelog: "The legacy API will continue to be available with no current plans for deprecation." [c35]
- Launch dates: kling-v2-1 image-to-image launched 2025-07-30. The 3.0 Omni and V3 models (video and image) launched 2026-02-25 [c37].
- The only discontinuation notices on the updates page are for video effects, some given with less than 30 days' warning (see Contradictions).

### Effect on the MJ4/MJ5 shortlists
- Kling 3.0 `/image-to-video/kling-3.0` with `first_frame` + `last_frame` + one `image_refer` element built from the canonical anchor is the closest documented analogue to MJ `--oref` plus an end frame.
- Kling documents it as improving consistency. There is no weight knob, and no evidence covers painted faces.
- US access is not excluded but not positively confirmed either. A pilot sign-up is the only way to close that.

### Claims
- [c1] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — Kling 3.0 image-to-video (POST /image-to-video/kling-3.0) accepts contents[].type values prompt, first_frame, last_frame and element in one request. — "| `contents[].type` | string | Yes | - | `prompt`, `first_frame`, `last_frame`, `element` | Input type. Supports: prompt, first frame, last frame, Element |"
- [c2] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — Kling 3.0 i2v allows at most 3 elements. — "`contents[].type.element`: Up to 3 Elements can be specified."
- [c3] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — The Kling 3.0 i2v doc gives a worked example combining first_frame, last_frame and element in one POST to api-singapore.klingai.com/image-to-video/kling-3.0. — "### First_frame & last_frame & element ... "type": "last_frame", ... "type": "element", "element_id": "163", "id": "element_1""
- [c4] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — Kling 3.0 i2v constraints: first frame is required, last-frame-only is not supported, multi_shot defaults to true, input image ≥300px and aspect 1:2.5 to 2.5:1; there is no aspect_ratio setting. — "Supports first-frame-to-video and first-and-last-frame-to-video generation; last-frame-only video generation is not supported. / | `settings.multi_shot` | boolean | No | `true` |"
- [c5] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/video-omni.md — Kling 3.0 Omni (POST /omni-video/kling-3.0-omni) supports up to 3 elements with a first frame or with first and last frames; aspect_ratio (16:9, 9:16, 1:1) is required only when there is no first frame or reference video. — "When using the first frame or first and last frames to generate video, a maximum of 3 element are supported. / `settings.aspect_ratio`: When there is no first frame or reference video, the current parameter is required."
- [c6] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/video-omni.md — The Kling 3.0 Omni doc gives an example with first_frame, last_frame and two elements in one request. — "### First_frame & last_frame & element ... "element_id": "162", "id": "element_1" ... "element_id": "163", "id": "element_2""
- [c7] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/o1/video-omni.md — Kling O1 does not support elements when both first and last frames are used, and allows no extra reference images in that mode. — "Using first+last frames: Elements are not supported. / When using both the first and last frames, no additional reference images can be added."
- [c8] FIRST-PARTY · entry 03/11/2026; accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — The changelog confirms that O1 cannot reference an element when generating from start and end frames. — "When generating the start & end frames of a video using the`kling-video-o1` model, referencing a element is not supported."
- [c9] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/2-6/image-to-video.md — Kling 2.6 i2v has no element input (its enum is prompt/first_frame/last_frame/voice), and first+last frame output is 1080p only. — "| `contents[].type` | string | Yes | - | `prompt`, `first_frame`, `last_frame`, `voice` | / When generating videos using the first and last frames, only 1080P videos can be generated."
- [c10] FIRST-PARTY · Updated At: 2026-05-19 · https://kling.ai/document-api/guides/capability-map/video.md — Video capability map: first/last frame is supported on 3.0, 3.0 Omni, O1, 2.6 and 2.5 Turbo but not 3.0 Turbo; Element Control is supported on 3.0 and 3.0 Omni, multi-image elements only on O1, and not on 2.6. — "| Element Control | Video character + multi-image elements | Not Supported | Supported | Supported | Supported: Multi-image elements only | Not Supported | Not Supported |"
- [c11] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-turbo/image-to-video.md — Kling 3.0 Turbo i2v accepts only prompt and first_frame. — "| `contents[].type` | string | Yes | - | `prompt`, `first_frame` | Reference type, supported by: prompt words, first_frame image |"
- [c12] FIRST-PARTY · entry 05/07/2026; accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — The mutual exclusion between multi-shot and first/last frames was removed on 2026-05-07 for kling-v3-omni and kling-v3. — "Remove the mutual exclusion between the "multi-shot" and "first and last frames" functions ... Supported model ranges: `kling-v3-omni`, `kling-v3`"
- [c13] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/elements.md — Elements are created via POST /v1/general/advanced-custom-elements; an image_refer element needs one frontal image plus 1–3 additional images, each ≤10MB, ≥300px, aspect 1:2.5 to 2.5:1; name ≤20 chars, description ≤100. — "at least one frontal reference image (frontal_image), and 1 to 3 additional reference images (image_url) that differ from the front."
- [c14] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/elements.md — The only documented style restriction on elements applies to video-built elements (realistic humanoid only); none is stated for image_refer. — "`element_video_list`: Currently, only realistic-style humanoid figures can be customized through video."
- [c15] FIRST-PARTY · Feb 5, 2026 · https://kling.ai/quickstart/klingai-element-library-3-user-guide — Kling's Element Library guide lists non-photoreal character types (historical/fantasy, anime, CG) as valid multi-image elements; painted faces are not named. — "Characters | Modern realistic characters, historical/fantasy characters, anime-style characters, CG-rendered characters, etc."
- [c16] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/elements.md — Element status is only succeed or deleted, and an explicit delete endpoint exists; no expiry or TTL field is documented. — ""status": "succeed" //Element status: succeed when normal, deleted when removed"
- [c17] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/image/3-0-omni/elements.md — The delete-element endpoint path differs between the video and image Element Management pages. — "- Path: `/v1/general/delete-elements` (image page) vs `/v1/general/delete-advanced-elements` (https://kling.ai/document-api/api/video/3-0-omni/elements.md)"
- [c18] FIRST-PARTY · entry 02/25/2026; accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — The new element service is separate from the old element API, and the two cannot query each other's elements. — "The new element service adopts a brand-new API (advanced-custom-elements). The existing API can still be used normally, but the elements library is relatively independent and cannot perform cross-API queries."
- [c19] FIRST-PARTY · Feb 5, 2026 · https://kling.ai/quickstart/klingai-element-library-3-user-guide — Kling's guide says 3.0 can bind up to 3 elements in start/start+end frame generation to reduce subject drift, and the elements must appear in the reference frames. — "The Kling 3.0 model supports binding up to 3 elements in start frame/start and end frames generation. ... In Video 3.0, after uploading a frame or start and end frames, you can bind up to 3 additional elements. The elements must appear in the reference frames to enhance their specific consistency."
- [c20] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/pricing/base/image.md — AI Multi-Shot (POST /v1/general/ai-multi-shot) takes a single element_frontal_image and is priced at 20 Units ($0.07) per call. — "| General | AI Multi-Shot | 1K | 20 Units ($0.07) / call |"
- [c21] FIRST-PARTY · Updated At: 2026-05-19 · https://kling.ai/document-api/guides/capability-map/image.md — Image capability map: Character and Face Feature Reference are supported only on Kling Image 2.1; Subject Control is 'Multi-image main image only' on 3.0, 3.0 Omni and O1. — "| Character Feature Reference | - | Not Supported | Not Supported | Not Supported | Supported | ... | Subject Control | - | Supported: Multi-image main image only | Supported: Multi-image main image only | Supported: Multi-image main image only | Not Supported |"
- [c22] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/image/3-0-omni/image-generation.md — /v1/images/generations: model_name is kling-v2-1 or kling-v3 (default kling-v3) and accepts element_list (elements + images ≤ 10); human_fidelity works only on kling-v2-1. — "| `model_name` | string | No | `kling-v3` | `kling-v2-1`, `kling-v3` | ... | `element_list` | array | No | ... `human_fidelity`: > Only kling-v2-1 supports this parameter"
- [c23] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/image/3-0-omni/image-omni.md — /v1/images/omni-image: model_name is kling-image-o1 or kling-v3-omni, it accepts element_list (elements + images ≤ 10), and aspect_ratio includes 1:1. — "| `model_name` | string | No | `kling-image-o1` | `kling-image-o1`, `kling-v3-omni` | ... `element_list`: The sum of reference elements and reference images must not exceed 10"
- [c24] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/pricing/base/video.md — The video pricing table has no element dimension. Kling 3.0 with no audio and 3.0 Omni with no video input and no audio both cost 0.6 Units ($0.084)/s at 720P. — "| Kling 3.0 | Per second | No Native Audio | 0.6 Units ($0.084) /s | ... | Kling 3.0 Omni | Per second | No Video Input x No Native Audio | 0.6 Units ($0.084) /s |"
- [c25] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/pricing/base/image.md — Kling Image 3.0, 3.0 Omni (1K/2K) and O1 cost 8 Units ($0.028) per image; 2.1 image-to-image is also 8 Units. — "| Kling Image 3.0 | Text-to-Image, Image-to-Image | 1K、2K | 8 Units ($0.028) / image |"
- [c26] FIRST-PARTY · Feb 5, 2026 · https://kling.ai/quickstart/klingai-element-library-3-user-guide — The consumer guide says element creation is free in the app; this is consumer-app credits, not API pricing. — "Q: Does it cost anything to create an element? A: Creating an element is free."
- [c27] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/elements.md — The API element-task query response includes a unit-deduction field; no element-creation price appears in the API pricing tables. — ""final_unit_deduction": "string", //Final unit deduction for the task"
- [c28] FIRST-PARTY · Release/Effective Date: 2026-04-21 · https://kling.ai/document-api/guides/protocols/paid-service.md — The API contract is with Kling AI Pte. Ltd.; the license runs within an undefined 'geographical scope of business'; Kling does not guarantee availability in other jurisdictions. — "a legally binding contract between you and Kling AI Pte. Ltd. ... license to use the products and technologies in this Service within the geographical scope of business ... 11.10 We do not claim, and cannot guarantee that Services we provide are or will be appropriate or available for any other loca"
- [c29] FIRST-PARTY · Last Updated Date: 2026/04/21 · https://kling.ai/docs/user-policy — The Kling AI Terms of Service (which the API terms defer to for matters they do not cover) are governed by Singapore law, with SIAC arbitration seated in Singapore. — "12. GOVERNING LAWS ... will be governed by and construed in accordance with the laws of Singapore ... arbitration administered by the Singapore International Arbitration Centre ("SIAC") ... The seat of the arbitration will be Singapore."
- [c30] FIRST-PARTY · Last Updated Date: 2026/04/21 · https://kling.ai/docs/user-policy — Users must represent that they are not subject to sanctions or embargoes; no named country exclusion was found. — "You further represent and warrant that you are not subject to any applicable sanctions, embargoes, or other legal or regulatory restrictions"
- [c31] FIRST-PARTY · Release/Update Date: 2026-04-21 · https://kling.ai/document-api/guides/protocols/privacy-policy.md — The API privacy policy stores data in Singapore and includes a California (United States) CCPA section. — "We store your Data on our servers located in Singapore. ... **California (United States)** If you are a California resident, the following additional privacy disclosures under the California Consumer Privacy Act"
- [c32] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/get-started/authentication.md — There is a single documented API domain, api-singapore.klingai.com, described as suitable for users with servers outside China. — "The API endpoint has been changed from https://api.klingai.com to **https://api-singapore.klingai.com**. This API is suitable for users whose servers are located outside of China."
- [c33] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/guides/get-started/quick-start.md — API onboarding is an email login at kling.ai/dev; the quick-start gives no country list. — "Log in using your email. Your console account is the same as your Kling AI web account."
- [c34] FIRST-PARTY · Release/Effective Date: 2026-04-21 · https://kling.ai/document-api/guides/protocols/paid-service.md — Kling commits to at least 30 days' notice before adjusting or terminating services. — "4.1 We have the right to **adjust or terminate part or all of the services at any time** ... However, We shall notify you at **least 30 days** in advance"
- [c35] FIRST-PARTY · entry 07/15/2026; accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — The legacy API has no current deprecation plans. — "The legacy API will continue to be available with no current plans for deprecation."
- [c36] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — The API updates page (latest entry 09/15/2026) has no deprecation notice for kling-v2-1 or kling-v3/Kling 3.0; its only discontinuation notices are for video effects. — "Notice: magic_match_tree will be discontinued on July 3rd, 2026 (entry 07/03/2026); Notice:celebration and c4d_cartoon will be discontinued on December 30, 2025 (entry 12/11/2025)"
- [c37] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/updates/api.md — kling-v2-1 image-to-image launched 2025-07-30; the 3.0 Omni and V3 video and image models launched 2026-02-25. — "## 07/30/2025 **Image Generation | Support V2.1 model** - Update image-to-image kling-v2-1 model ... ## 02/25/2026 **Video Generation | 3.0 Omni and V3 model launched** **Image Generation | 3.0 Omni and V3 model launched**"
- [c38] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md — Generated results are purged after 30 days. — "To ensure information security, generated results will be cleared after 30 days. Please make sure to save them promptly."
- [c39] FIRST-PARTY · entry 01/23/2026 · https://kling.ai/document-api/updates/api.md — The AI multi-view completion changelog entry prices it at 0.5 units per visit. — "Through the front view of the element, other angle images of the element can be automatically inferred ... Charged based on the times of service visits, with 0.5 units deducted per visit."
- [c40] FIRST-PARTY · accessed 2026-09-24 · https://kling.ai/document-api/api/image/common/subject-completion.md — The AI Multi-Shot endpoint needs only one frontal image; the guide says additional views can be generated from a single main reference image. — "| `element_frontal_image` | string | Yes | - | - | The frontal side of element image |"

### Could not confirm
- Positive confirmation that US-resident customers can sign up, pay and call the Kling API. No first-party list of supported countries or payment regions was found, and no US exclusion was found either. The only secondary result (videoai.me, milvus.io) is not usable as evidence.
- Whether a painted or Old-Master (non-photographic) face is accepted as an image_refer element and passes content moderation. Only realistic-only for video_refer is documented; the consumer guide lists anime/CG/fantasy characters.
- Whether elements expire, count against an API-account quota, or fall under the 30-day purge of generated results. Only consumer-app quotas (30–500 elements by membership tier) are documented.
- API price of creating an element (final_unit_deduction exists in the response; no row in the pricing tables). 'Free' is stated only for the consumer app.
- Whether attaching an element changes per-second video billing beyond what the pricing table shows; the table has no element dimension.
- Output aspect ratio for a 1:1 first/last frame on /image-to-video/kling-3.0 (no aspect setting), and whether the 3.0 Omni aspect_ratio 1:1 is honoured when a first frame is given.
- Any first-party measurement that an element reduces face drift between the endpoints; only qualitative marketing claims exist ('effectively solves the pain point of subjects losing their shape').
- Whether the legacy (model_name-style) image2video API offers element + image_tail for kling-v3. The legacy docs are not in llms.txt and were not fetched.
- Meaning of 'kling-video-o3' in the elements page ('Video-customized elements are only supported for kling-video-o3 and later models'). No other first-party page defines that model id.
- Wayback dating of when the 'First_frame & last_frame & element' examples were added: the Wayback CDX returned 'Temporarily Offline'.

### Verification (combined lens)
I re-fetched all 23 cited kling.ai/document-api markdown pages, the ToS HTML and the Element Library guide on 2026-09-24. The researcher's output holds up. 38 of 40 claims are supported verbatim on first-party pages. c4 is partial: 'must set multi_shot=false' is an inference. c36 is partial: it misses the 12/18/2025 effects-discontinuation notice. The core finding stands. Kling 3.0 (POST /image-to-video/kling-3.0, enum 'prompt, first_frame, last_frame, element', 'Up to 3 Elements') and 3.0 Omni (POST /omni-video/kling-3.0-omni, 'a maximum of 3 element') both document first_frame + last_frame + element in one call, each with a worked example. O1 explicitly excludes elements with first+last frames. 2.6 has no element input. 3.0 Turbo has no last frame. All four reported contradictions re-verified. No fabricated versions, prices or dates were found. Two prose overstatements: the pricing axes omit Voice Control, and the multi_shot advice is inference. The main gap is licensing and display terms, which the answer never covered despite standard 5. ToS 4.5 requires Output to be labelled 'Kling AI', and the API terms defer to the ToS on this. ToS 4.6 forbids commercial use of Output without written permission, while API terms 6.4 say commercial use is 'not restricted' and claim precedence; both are reported, per the rules. ToS 4.7.1 grants Kling a royalty-free public-display license over Input and Output, while API 5.5 says there is no training on paid-API data and 30-day logs. US availability is still unconfirmed. Fresh site-restricted searches found no first-party country list, and the Wayback CDX has only a status-446 snapshot of the i2v page, so the 'First_frame & last_frame & element' example cannot be dated. Scratch files are in <session scratch, not kept>/verify-mj5-kling/.

Checks not marked "supported":
- **partially_supported**: Kling 3.0 i2v: first frame required, last-frame-only unsupported, multi_shot default true, >=300px, aspect 1:2.5-2.5:1, no aspect_ratio; answer adds 'so it must be set to false for a single shot' → Same URL: "Required in the first_frame, optional in the last_frame"; "last-frame-only video generation is not supported"; "| `settings.multi_shot` | boolean | No | `true` |"; settings table has no aspect_ratio row. Only note on multi_shot is "When set to false, multi-shot prompts will not produce mu
- **partially_supported**: Updates page (latest 09/15/2026) has no deprecation for kling-v2-1 or kling-v3; only discontinuations are video effects → updates/api.md: latest entry "## 09/15/2026"; grep for discontinu/deprecat finds only effects notices. Claim is correct but its list omits a third notice: ## 12/18/2025 "Notice:kiss,fight,hug,thumbs_up,tiger_hug,pet_lion, 3d_cartoon_1 will be discontinued on January 30, 2026" (~43 days' notice).

Flagged as unconfirmed by the verifier:
- None of the version numbers, model IDs, prices, dates or limits in the answer is fabricated. Each was re-seen on a first-party kling.ai page on 2026-09-24.
- Inference presented as documentation: 'multi_shot defaults to true, so it must be set to false for a single shot'. The doc says only 'When set to false, multi-shot prompts will not produce multi-shot output.'
- Overstatement: 'The only billing axes are audio, video input, motion control and resolution'. The table also has a Voice Control axis.
- '$0.42' for a 5 s, 720p clip is the researcher's own arithmetic (0.084 x 5). It is labelled as such and is correct against the table.

---

## G3 — track MJ4: MJ1 answers 'how much warning' for Midjourney (0 days guaranteed), but no track answers it for the alternatives (also affects MJ5). Scattered first-party facts exist without synthesis. BFL: 'flux-2-pr…

**Why it matters:** The exit exists because MJ retires things with no notice. Moving the whole graph to a vendor with the same exposure repeats the one-way-door risk. To make a recommendation, each option needs a pinnable snapshot ID and a stated minimum notice period.

**Gap-fill confidence:** high

### Answer
## MJ4 gap: pinnable IDs, notice periods and retirement dates for the non-MJ candidates (checked 2026-09-24)

**Summary.**
- Only three vendors publish a numeric minimum notice for retiring a model:
  - OpenAI: at least 6 months for GA models [c1]
  - Alibaba: 30 days for dated snapshots, 3 months for mainline models [c54]
  - Google Vertex: the model is available for at least 12 months after release, and a listed retirement date is never moved earlier [c25]
- Kling and Luma have a contract clause of 30 days [c39][c44]. Luma's clause is "commercially reasonable efforts" and covers only "material breaking changes".
- These publish no number: BFL (the ToS allows zero notice [c34]), the Gemini API for stable models [c15][c18], MiniMax [c50] and Higgsfield [c59].
- Dated or fixed snapshot IDs exist only at:
  - OpenAI: `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare-2026-09-08` [c5][c7][c8]
  - BFL: `flux-2-pro`, `flux-2-klein-9b` [c31][c32]
  - Google: version-pinned `-001` GA IDs on Vertex [c26], plus the stable `gemini-3-pro-image` [c20][c27]
- Kling, Luma, MiniMax, Alibaba kf2v and FLUX 3 have version names or `latest` only [c37][c42][c46][c49][c56].

| Vendor / model | Pinnable ID | Stated notice | Announced retirement | Source + date |
|---|---|---|---|---|
| OpenAI gpt-image-2 | `gpt-image-2-2026-04-21` (the default snapshot of `gpt-image-2`) [c5][c6] | GA ≥6 months. Specialized variants ≥3 months. Preview models "such as 2 weeks". Safety/compliance exception [c1][c2][c3]. The policy section was added between 2026-05-29 and 2026-06-03 [c4] | None. On the deprecations page it appears only as a replacement [c10] | developers.openai.com/api/docs/models/gpt-image-2.md; /api/docs/deprecations.md (both accessed 2026-09-24) |
| OpenAI gpt-image-2.5-sunburst | `gpt-image-2.5-sunburst-2026-09-08` [c7] | Same policy. The name has no `preview`, which is the policy's own marker for preview models [c2]. Its tier (GA or specialized variant) is not stated | None. Released Sep 8 [c9] | /models/gpt-image-2.5-sunburst.md; /changelog.md (accessed 2026-09-24) |
| OpenAI gpt-image-2.5-flare | `gpt-image-2.5-flare-2026-09-08` [c8] | Same as Sunburst | None | /models/gpt-image-2.5-flare.md (accessed 2026-09-24) |
| Gemini API gemini-3-pro-image | `gemini-3-pro-image` ("Stable", not dated; "Latest update November 2025") [c20] | None stated for stable models: "Stable models usually don't change" [c15], and shutdown dates are "earliest possible… advance notice" [c18]. Preview ≥2 weeks [c16]. `latest` alias: 2-week email [c17] | "No shutdown date announced" [c19] | ai.google.dev/gemini-api/docs/models, /deprecations (last updated 2026-09-23) |
| Vertex gemini-3-pro-image | `gemini-3-pro-image` GA [c27] | ≥12 months after release; dates "won't be moved to an earlier date" [c25]. GCP Terms give 12 months unless the Service is replaced by a "materially similar" one; pre-GA is excluded [c29] | "May 28, 2027 or later" [c27] | docs.cloud.google.com/…/models/model-versions and …/gemini/3-pro-image (2026-09-22) |
| Vertex veo-3.1-generate-001 / veo-3.1-fast-generate-001 | The `-001` GA IDs [c26] | Same as the Vertex row above | **"November 17, 2026 or later"**, 54 days from today [c26] | docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate (2026-09-22) |
| Gemini API veo-3.1-generate-preview / -fast-preview | Preview IDs only | ≥2 weeks [c16] | "No shutdown date announced" [c24] | ai.google.dev/gemini-api/docs/deprecations (2026-09-23) |
| BFL flux-2-pro | `flux-2-pro`: "fixed snapshot… will not change" [c31][c33] | None in the docs. Developer ToS: "may not provide you with any notice beforehand" [c34]. The API terms allow model modifications "at any time" [c35] | None | docs.bfl.ml/flux_2/flux2_overview.md (accessed 2026-09-24); bfl.ai/legal/developer-terms-of-service (Rev. Aug 4, 2026) |
| BFL flux-2-klein-9b (hosted) | `flux-2-klein-9b`, fixed snapshot [c32] | Same as flux-2-pro | None | Same |
| BFL FLUX 3 | None. `version` is const `latest`; "dated pinnable release tags are added here as they are published". FLUX 3 is a "preview" model; image editing is a later phase [c37][c38] | Same as flux-2-pro | None | docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3.md; flux3_overview.md; release-notes.md (accessed 2026-09-24) |
| Kling (kling-v2-1 image, kling-v3, -omni, o1) | Version names only; no statement that they are immutable. kling-v2-1 image was added 07/30/2025 [c42] | "at least 30 days" in advance to "adjust or terminate part or all of the services" (Paid Service Terms §4.1) [c39] | None for models. The legacy API has "no current plans for deprecation" [c40] | kling.ai/document-api/guides/protocols/paid-service.md (effective 2026-04-21); /updates/api.md (accessed 2026-09-24) |
| Luma ray-3.2 (Agents API) | `ray-3.2` only; API header `X-API-Version` 2026-04-01 [c46][c48] | "commercially reasonable efforts" for ≥30 days, only for "material breaking changes"; "no obligation" for other changes [c44]. Video pricing is pre-GA [c45] | None for ray-3.2. The legacy Ray 2/3 models are retiring, with the date in each account's notice [c47] | lumalabs.ai/legal/api-terms-of-use (Apr 28, 2026); docs.agents.lumalabs.ai/guides/pricing/, /videos/migration/, /faq/ (accessed 2026-09-24) |
| MiniMax MiniMax-H3 / MiniMax-H3-Max | Undated names [c49]. H3-Max was "post-trained by fal.ai" [c52] | "will notify you in advance", with no number [c50]. For a material reduction in functionality: a "reasonable period" if you have subscribed to notifications [c51] | None. Hailuo 2.3/02 are filed under "Legacy Models" [c52] | platform.minimax.io/docs/api-reference/video-generation-v2-create.md; /protocol/terms-of-service (effective Mar 30, 2026) |
| Alibaba wan2.2-kf2v-flash | Undated name. Alibaba defines a "snapshot" as a name with a date in it [c54] | Snapshots 30 days; mainline models 3 months. Which class kf2v is in is not stated [c54]. Two past batches had "No dedicated announcement" [c55] | None. It is absent from the retirement notices for Oct 10, 2026 that I checked [c57]. It is filed under "Wan - legacy video models" [c56] | alibabacloud.com/help/en/model-studio/model-depreciation (Sep 11, 2026); legacy-image-to-video-by-first-and-last-frame-api-reference (Sep 22, 2026) |
| Higgsfield | None published | None stated. The docs say only "Availability and access can change" [c59] | None | docs.higgsfield.ai/docs/models.md (accessed 2026-09-24) |

**Notice actually given, computed from first-party announcement and shutdown dates:**
- OpenAI, image and video models:
  - gpt-image-1: 184 days [c11]
  - gpt-image-1.5 / -1-mini / chatgpt-image-latest: 182 days [c12]
  - DALL·E: 179 days; Sora 2: 184 days
  - Outside images: gpt-5.4-cyber got 20 days [c13]
- Gemini API:
  - **Veo 2.0/3.0 GA `-001` models: 15 days** (Jun 15 → Jun 30, 2026) [c21]
  - Imagen 4 GA: 63 days [c22]
  - gemini-3-pro-image-preview: 28 days [c23]
- BFL: flux-pro-1.0 endpoints and the Finetuning API got 28 days, with "No migration path available" [c36].
- Kling video effects: 0, 19 and 43 days [c41].
- Alibaba: 36 days for snapshots; 92–124 days for the Oct 10 batches; two batches with no dedicated announcement [c55][c57].
- Vertex held veo-3.0-generate-001 for only 336 days, although it is listed under the "at least 12 months" table (see contradictions) [c60].

**Not verified (inferences):**
- A "fixed snapshot" (BFL) or a dated snapshot (OpenAI) pins behaviour. It does not prevent retirement.
- None of the notice periods above is a zero-notice guarantee except BFL's, whose ToS explicitly allows zero notice [c34].

### Claims
- [c1] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — OpenAI minimum notice before retiring generally available models is at least 6 months; specialized variants at least 3 months — "Generally available models:** At least 6 months. - **Specialized variants of generally available models:** At least 3 months."
- [c2] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — OpenAI preview models (identified by 'preview' in the name) may be retired on ~2 weeks notice — "Preview models, identified by `preview` in the model name, may be retired with much shorter notice, such as 2 weeks."
- [c3] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — OpenAI minimum notice periods have a safety/compliance exception — "If safety or compliance concerns require us to retire a model sooner, we will provide as much notice as reasonably possible."
- [c4] FIRST-PARTY · Wayback captures 2026-02-10 through 2026-09-14 · http://web.archive.org/web/20260603190331/https://developers.openai.com/api/docs/deprecations — The 'Model deprecation notice periods' section is new: absent in the Wayback copy of 2026-05-29, present in the copy of 2026-06-03 — "'notice periods' / 'At least 6 months' found in 20260603190331 and 20260802061733 captures; absent in 20260529195735, 20260508011246, 20260426114525, 20260403214827, 20260210130538 captures"
- [c5] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/models/gpt-image-2.md — gpt-image-2 default snapshot is gpt-image-2-2026-04-21 (the only listed snapshot) — "Default snapshot: `gpt-image-2-2026-04-21`"
- [c6] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/models/gpt-image-2.md — OpenAI describes snapshots as locking model version for consistent behavior — "Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent."
- [c7] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst.md — gpt-image-2.5-sunburst has dated snapshot gpt-image-2.5-sunburst-2026-09-08 — "Default snapshot: `gpt-image-2.5-sunburst-2026-09-08`"
- [c8] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/models/gpt-image-2.5-flare.md — gpt-image-2.5-flare has dated snapshot gpt-image-2.5-flare-2026-09-08 — "Default snapshot: `gpt-image-2.5-flare-2026-09-08`"
- [c9] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/changelog.md — GPT Image 2.5 Sunburst and Flare were released on Sep 8 (2026) — "### Sep 8 ... Released [GPT Image 2.5 Sunburst](...) and [GPT Image 2.5 Flare](...) for image generation and editing"
- [c10] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — No deprecation announced for gpt-image-2 or 2.5; gpt-image-2 appears on the deprecations page only as a recommended replacement — "| Dec 1, 2026   | `gpt-image-1.5`        | `gpt-image-2`           |"
- [c11] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — gpt-image-1 deprecation announced 2026-04-22 with shutdown October 23, 2026 (184 days) — "### 2026-04-22: Legacy GPT model snapshots ... | October 23, 2026 | `gpt-image-1` | `gpt-image-2` |"
- [c12] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — Older GPT Image models notified June 2, 2026 for removal December 1, 2026 — "On June 2, 2026, we notified developers using older GPT Image models of their deprecation and removal from the API on December 1, 2026."
- [c13] FIRST-PARTY · accessed 2026-09-24 · https://developers.openai.com/api/docs/deprecations.md — gpt-5.4-cyber was deprecated 2026-09-11 with removal October 1, 2026 (20 days); page does not state which policy tier/exception applies — "### 2026-09-11: GPT-5.4-Cyber The `gpt-5.4-cyber` model is deprecated and will be removed from the API on October 1, 2026."
- [c14] FIRST-PARTY · Updated December 1, 2025; Effective January 1, 2026 (Wayback 2026-09-19; live page 403) · https://web.archive.org/web/20260919113526/https://openai.com/policies/services-agreement/ — OpenAI Services Agreement modifications clause: notice by email for material functionality reduction, no day count — "2.3. Modifications. OpenAI may update the Services periodically. If an OpenAI update materially reduces the Services functionality, OpenAI will notify Customer at the Account email address."
- [c15] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/models — Gemini API stable models: no numeric notice; described as usually not changing — "Points to a specific stable model. Stable models usually don't change. Most production apps should use a specific stable model."
- [c16] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/models — Gemini API preview models will be deprecated with at least 2 weeks notice — "Points to a preview model which may be used for production. Preview models will typically have billing enabled, might come with more restrictive rate limits and will be deprecated with at least 2 weeks notice."
- [c17] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/models — Gemini API 'latest' alias gets 2-week email notice before a breaking swap — "For breaking changes, a 2-week notice will be provided through email before the version behind latest is changed."
- [c18] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/deprecations — Gemini API shutdown dates are earliest-possible dates with unspecified advance notice — "The shutdown dates listed in the table indicate the earliest possible dates on which a model might be retired. We will communicate the exact shutdown date to users with advance notice"
- [c19] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/deprecations — Gemini API gemini-3-pro-image released May 28, 2026, no shutdown date announced — "gemini-3-pro-image | May 28, 2026 | No shutdown date announced"
- [c20] FIRST-PARTY · Last updated 2026-09-03 UTC · https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image — Gemini API model page lists gemini-3-pro-image as Stable with latest update November 2025 — "Stable: gemini-3-pro-image | Latest update | November 2025"
- [c21] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/changelog — Gemini API gave 15 days notice to GA Veo -001 models: announced June 15, 2026, shutdown June 30, 2026 — "June 15, 2026 ... Deprecation announcement: The following video generation models are being deprecated and will be shut down on June 30, 2026: Veo models: veo-2.0-generate-001 veo-3.0-generate-001 veo-3.0-fast-generate-001"
- [c22] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/changelog — Gemini API gave 63 days to GA Imagen 4 models (announced June 15, shutdown August 17, 2026) — "Deprecation announcement: The following image generation models are being deprecated and will be shut down on August 17, 2026: ... imagen-4.0-generate-001"
- [c23] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/changelog — gemini-3-pro-image-preview deprecated on GA day May 28, 2026, shut down June 25, 2026 (28 days) — "Deprecation announcement: The gemini-3.1-flash-image-preview and gemini-3-pro-image-preview models are deprecated and will be shut down on June 25, 2026."
- [c24] FIRST-PARTY · Last updated 2026-09-23 UTC · https://ai.google.dev/gemini-api/docs/deprecations — Gemini API Veo 3.1 preview IDs have no shutdown date announced — "veo-3.1-generate-preview | October 15, 2025 | No shutdown date announced | veo-3.1-fast-generate-preview | October 15, 2025 | No shutdown date announced"
- [c25] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions — Vertex/Agent Platform: listed models available at least 12 months after release; retirement dates may extend but not move earlier — "While retirement timelines may be extended, they won't be moved to an earlier date than what is listed. Models available for at least 12 months after release"
- [c26] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate — Vertex veo-3.1-generate-001 and veo-3.1-fast-generate-001 are GA, released Nov 17, 2025, retirement Nov 17, 2026 or later — "veo-3.1-generate-001 Launch stage: GA Release date: November 17, 2025 Retirement date: November 17, 2026 or later ... veo-3.1-fast-generate-001 Launch stage: GA Release date: November 17, 2025 Retirement date: November 17, 2026 or later"
- [c27] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image — Vertex gemini-3-pro-image is GA with retirement May 28, 2027 or later — "gemini-3-pro-image Launch stage: GA Release date: May 28, 2026 Retirement date: May 28, 2027 or later"
- [c28] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions — Vertex short-term-availability models get at least 45 days to migrate once a retirement date is posted — "When we schedule a model for retirement, we post a fixed date in the following table that gives you at least 45 days to migrate."
- [c29] FIRST-PARTY · Last modified September 2, 2026 · https://cloud.google.com/terms — GCP Terms: 12 months notice before discontinuing a Service unless replaced by a materially similar one; excludes pre-GA — "Google will notify Customer at least 12 months before: (i) discontinuing any Service (or associated material functionality) unless Google replaces such discontinued Service or functionality with a materially similar Service or functionality ... does not apply to Cloud Identity Services or pre-genera"
- [c30] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate — Vertex veo-3.1-lite-generate-001 is Preview (pre-GA) — "veo-3.1-lite-generate-001 Launch stage: Preview Release date: April 2, 2026"
- [c31] FIRST-PARTY · accessed 2026-09-24 · https://docs.bfl.ml/flux_2/flux2_overview.md — BFL flux-2-pro is a fixed snapshot that will not change — "`flux-2-pro` | A fixed snapshot of FLUX.2 \[pro]. This endpoint will not change, making it suitable for workflows that require reproducibility."
- [c32] FIRST-PARTY · accessed 2026-09-24 · https://docs.bfl.ml/flux_2/flux2_overview.md — BFL flux-2-klein-9b is a fixed snapshot — "`flux-2-klein-9b` | A fixed snapshot of FLUX.2 \[klein] 9B. Choose this when you need reproducibility."
- [c33] FIRST-PARTY · entry March 3, 2026 · https://docs.bfl.ml/release-notes.md — BFL introduced flux-2-pro-preview on March 3, 2026 and kept flux-2-pro unchanged as fixed snapshot — "The existing `flux-2-pro` endpoint remains **unchanged** as a fixed snapshot for workflows that require reproducibility."
- [c34] FIRST-PARTY · Last Revised on August 4, 2026 · https://bfl.ai/legal/developer-terms-of-service — BFL Developer ToS permits stopping any FLUX Service at any time without prior notice — "we may also suspend or stop providing any of the FLUX Services altogether. We may take any of these actions at any time for any reason, and when we do, we may not provide you with any notice beforehand."
- [c35] FIRST-PARTY · Last Revised on August 4, 2026 · https://bfl.ai/legal/flux-api-service-terms — BFL API terms allow modification of FLUX AI Models at any time — "The Company may modify, change, update, and/or enhance the FLUX API and/or the FLUX AI Models, or any specifications or functionalities of the FLUX API and/or FLUX AI Models (a "Modification"), at any time in the Company's sole and exclusive discretion."
- [c36] FIRST-PARTY · entries October 3, 2025 and October 31, 2025 · https://docs.bfl.ml/release-notes.md — BFL deprecated flux-pro-1.0 endpoints and the Finetuning API with 28 days notice (Oct 3 -> Oct 31, 2025), no migration path for finetuning — "### October 31, 2025 - Flux Pro 1.0 Endpoints ... No migration path available. Finetuning functionality will be discontinued."
- [c37] FIRST-PARTY · accessed 2026-09-24 (flux3_overview.md: 'FLUX 3 is a **preview** model.') · https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3.md — FLUX 3 has no pinnable version yet (version const 'latest') and is a preview model — "Endpoint version. `latest` (default) serves the current release; dated pinnable release tags are added here as they are published."
- [c38] FIRST-PARTY · entry July 23, 2026 · https://docs.bfl.ml/release-notes.md — FLUX 3 image synthesis/editing comes in a later rollout phase after early access — "Capabilities become available in phases, each after an early access period: video generation and editing first, action prediction with selected partners, image synthesis and editing, and open-weight access"
- [c39] FIRST-PARTY · Release/Effective Date 2026-04-21 · https://kling.ai/document-api/guides/protocols/paid-service.md — Kling API Paid Service Terms: at least 30 days notice before adjusting/terminating part or all services — "4.1 We have the right to **adjust or terminate part or all of the services at any time** (including but not limited to offline, iteration, integration, etc.) ... However, We shall notify you at **least 30 days** in advance"
- [c40] FIRST-PARTY · entry 07/15/2026 · https://kling.ai/document-api/updates/api.md — Kling legacy API has no current deprecation plans — "The legacy API will continue to be available with no current plans for deprecation."
- [c41] FIRST-PARTY · entries 12/11/2025, 12/18/2025, 07/03/2026 · https://kling.ai/document-api/updates/api.md — Kling video effects were discontinued with 0-43 days notice per the updates page — "## 07/03/2026 ... Notice: magic_match_tree will be discontinued on July 3rd, 2026; ## 12/11/2025 ... Notice:celebration and c4d_cartoon will be discontinued on December 30, 2025"
- [c42] FIRST-PARTY · entry 07/30/2025 · https://kling.ai/document-api/updates/api.md — Kling kling-v2-1 image-to-image added 07/30/2025; model IDs are version names without dates — "## 07/30/2025 ... **Image Generation | Support V2.1 model** - Update image-to-image kling-v2-1 model"
- [c43] FIRST-PARTY · entry 09/15/2026 · https://kling.ai/document-api/updates/api.md — Kling Virtual Try-On 3.0 adapted V1/V1.5 parameters onto the 3.0 pipeline (ambiguous whether old model names are re-routed) — "This upgrade is compatible with existing users. V1/V1.5 model parameters have been adapted on the engineering side, allowing users to seamlessly switch to the 3.0 pipeline."
- [c44] FIRST-PARTY · Last updated: April 28, 2026 · https://lumalabs.ai/legal/api-terms-of-use — Luma API Terms: commercially reasonable efforts for 30 days notice on material breaking changes only; no obligation otherwise — "Luma will use commercially reasonable efforts to provide Customer with at least thirty (30) days' prior written notice. Luma shall have no obligation to provide advance notice in connection with any other modifications"
- [c45] FIRST-PARTY · accessed 2026-09-24 · https://docs.agents.lumalabs.ai/guides/pricing/ — Luma Ray 3.2 video pricing is pre-GA — "Video rates are subject to change ahead of general availability."
- [c46] FIRST-PARTY · accessed 2026-09-24 · https://docs.agents.lumalabs.ai/guides/videos/migration/ — Luma's only public video model ID is ray-3.2 (no dated snapshot) — "The public model identifier on /v1/generations is ray-3.2. Do not send an older Ray model name; legacy identifiers are not accepted by the new API."
- [c47] FIRST-PARTY · accessed 2026-09-24 · https://docs.agents.lumalabs.ai/guides/videos/migration/ — Luma legacy Ray 3/2/2 Flash/2 Relaxed/3 Reference/3 Refiner are retiring on per-account notice dates — "If you received a deprecation notice, use the retirement date in that message as the cutoff for your account."
- [c48] FIRST-PARTY · accessed 2026-09-24 · https://docs.agents.lumalabs.ai/guides/faq/ — Luma API versioning: X-API-Version 2026-04-01; deprecation window length unstated — "The current value is 2026-04-01. ... Breaking changes ship behind a new X-API-Version value; the previous version remains available during a deprecation window."
- [c49] FIRST-PARTY · accessed 2026-09-24 · https://platform.minimax.io/docs/api-reference/video-generation-v2-create.md — MiniMax V2 video models are MiniMax-H3 and MiniMax-H3-Max (undated names) — "Currently supported models: `MiniMax-H3`, `MiniMax-H3-Max`."
- [c50] FIRST-PARTY · Effective Date: March 30, 2026 · https://platform.minimax.io/protocol/terms-of-service — MiniMax ToS: may take services offline at any time with advance notice, no number of days — "We reserve the right to adjust or terminate certain or all services (including, but not limited to, taking services offline, iterating, or consolidating them) at any time based on its operational needs. However, we will notify you in advance"
- [c51] FIRST-PARTY · Effective Date: March 30, 2026 · https://platform.minimax.io/protocol/terms-of-service — MiniMax ToS: material functionality reductions get 'reasonable period' notice only if subscribed — "we will use commercially reasonable efforts to notify you within a reasonable period before the change becomes effective, provided that you have subscribed to receive notifications of such changes."
- [c52] FIRST-PARTY · accessed 2026-09-24 · https://platform.minimax.io/docs/guides/models-intro.md — MiniMax files Hailuo 2.3/2.3Fast/02 under Legacy Models; H3 Max is post-trained by fal.ai — "High-speed video model post-trained by [fal.ai](https://fal.ai/) on MiniMax H3 ... <Accordion title="Legacy Models"> ... MiniMax Hailuo 2.3"
- [c53] FIRST-PARTY · accessed 2026-09-24 · https://platform.minimax.io/docs/release-notes/models.md — MiniMax H3 released Jul. 31, 2026 — "#### Jul. 31, 2026 <Card title="MiniMax H3""
- [c54] FIRST-PARTY · Last Updated: Sep 11, 2026 · https://www.alibabacloud.com/help/en/model-studio/model-depreciation — Alibaba Model Studio: snapshot (date-in-name) models get 30 days sunset notice; mainline models 3 months — "For snapshot models, which are identified by a specific date in their name ... we issue a sunset notice 30 days before the official sunset date. For mainline models, which are the core versions of a model series, we issue a sunset notice 3 months before"
- [c55] FIRST-PARTY · Last Updated: Sep 11, 2026 · https://www.alibabacloud.com/help/en/model-studio/model-depreciation — Alibaba lists two past deprecation batches with no dedicated announcement — "Deprecated on January 30, 2026 No dedicated announcement was published for this batch. Deprecated on August 20, 2025 No dedicated announcement was published for this batch."
- [c56] FIRST-PARTY · Last Updated: Sep 22, 2026 · https://www.alibabacloud.com/help/en/model-studio/legacy-image-to-video-by-first-and-last-frame-api-reference — wan2.2-kf2v-flash is documented under 'Wan - legacy video models', still live — "Wan - legacy video models ... Last Updated:Sep 22, 2026 ... The name of the model. Example: wan2.2-kf2v-flash."
- [c57] FIRST-PARTY · published Jul 10, 2026 (also checked _7d4 Jul 09, _79e Jun 08, _717/_718 Apr 03, _7d0 Jul 06) · https://www.alibabacloud.com/en/notice/model_studio_notice_of_retirement_for_selected_legacy_models_7d9?_p_lc=1 — Alibaba Oct 10, 2026 retirement notices (published Jun 8, Jul 9, Jul 10, 2026) do not list wan2.2-kf2v-flash; wan appears only as replacement wan2.7-r2v — "Jul 10, 2026 ... Alibaba Cloud Model Studio will retire the models listed in the table below on October 10, 2026."
- [c58] FIRST-PARTY · Last Updated: Sep 11, 2026 · https://www.alibabacloud.com/help/en/model-studio/model-depreciation — Alibaba throttles retiring models from the notice date — "Starting from the date of the retirement notice, the QPM (queries per minute) and TPM (tokens per minute) for retiring models will gradually decrease."
- [c59] FIRST-PARTY · accessed 2026-09-24 · https://docs.higgsfield.ai/docs/models.md — Higgsfield publishes no deprecation/notice policy; only that availability can change — "The catalog covers 82 entries listed for sale as of September 22, 2026 ... Availability and access can change; check the [API Console](https://console.higgsfield.ai) for your account."
- [c60] FIRST-PARTY · Last updated 2026-09-22 UTC · https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions — Vertex lists veo-3.0-generate-001 (released July 29, 2025, retired June 30, 2026) under the 'at least 12 months' heading — "The following table lists the models that will be available for at least 12 months after initial release: ... veo-3.0-generate-001 | July 29, 2025 | June 30, 2026 | veo-3.1-generate-001"
- [c61] FIRST-PARTY · Last updated 2026-09-23 UTC / 2026-09-22 UTC · https://ai.google.dev/gemini-api/docs/deprecations — Same model ID has different lifecycle per Google platform: gemini-2.5-flash-image shuts down Oct 2, 2026 on Gemini API but retires March 15, 2027 on Vertex — "gemini-2.5-flash-image | October 2, 2025 | October 2, 2026 (Vertex model-versions: 'gemini-2.5-flash-image | October 2, 2025 | March 15, 2027')"

### Could not confirm
- OpenAI: which policy tier (GA at ≥6 months, or specialized variant at ≥3 months) covers gpt-image-2.5-sunburst/-flare. The model pages do not state a launch stage. The name has no 'preview', which the policy uses to mark preview models.
- OpenAI: whether a dated snapshot guarantees identical weights. The docs say only 'performance and behavior remain consistent'.
- Gemini API: any numeric minimum notice for stable models. None is stated, and stable Veo 3.0 -001 models on the Gemini API got 15 days.
- Gemini: whether the GA gemini-3-pro-image (released May 28, 2026) has the same weights as the Nov 2025 preview. The model page says 'Latest update November 2025'.
- Google: whether GCP Terms §1.4(e) (12 months) applies to retiring an Agent Platform generative model that has a replacement. The clause excepts cases where a 'materially similar' replacement exists.
- BFL: any retirement date or minimum-notice policy for the flux-2-pro / flux-2-klein-9b fixed snapshots. None was found in the docs, release notes or legal pages.
- BFL: when FLUX 3 image synthesis/editing will ship, and when the first dated pinnable FLUX 3 version tag will be published.
- Kling: whether a model_name (kling-v2-1, kling-v3, kling-v3-omni, kling-video-o1) is immutable or can be upgraded in place. The '12/16/2025 V2.6 model upgraded' and '09/15/2026 Virtual Try-On 3.0' entries are ambiguous.
- Kling: any retirement date for kling-v2-1, the only version with human_fidelity. None was announced on the updates page.
- Kling: whether the 30-day clause in §4.1 is meant to cover retiring a model.
- Luma: an explicit GA or preview label for ray-3.2. Only the pricing caveat 'ahead of general availability' was found.
- Luma: how long the X-API-Version deprecation window lasts.
- Luma: the retirement dates for legacy Ray models, which are sent only in per-account notices.
- MiniMax: a numeric notice period, and any snapshot or version-pinning policy for MiniMax-H3 / MiniMax-H3-Max.
- MiniMax: whether the fal.ai post-training of H3-Max creates a separate lifecycle dependency.
- Alibaba: whether wan2.2-kf2v-flash counts as a 'mainline' model (3 months' notice) or some other class, and what the 'legacy' filing in the docs means. The page never defines it.
- Alibaba: the Chinese-language notices linked from the policy page (zh/notice/detail?id=1841, 2009, 1950, 1949, 1938, 1934) render client-side and could not be read. kf2v's absence from the Oct 10, 2026 batch is confirmed only for the six English notices I fetched.
- Higgsfield: any ToS clause on discontinuation. higgsfield.ai/terms-of-service, /terms, /api-terms and cloud.higgsfield.ai/terms all returned 404.
- Change history (Wayback) was not checked for the BFL, Kling, Luma, MiniMax or Alibaba policy pages. Only OpenAI's was bracketed in time.

### Verification (combined lens)
I re-opened every cited source today (2026-09-24). Of the 61 claims, 57 are supported: every OpenAI, Gemini API, Vertex, BFL, Kling, Luma, MiniMax and Alibaba quote matched verbatim. c4's Wayback bracket held on the two captures I could fetch (0529 absent, 0603 present). c6, c29 and c36 are only partly supported. c6: the dated snapshot gpt-image-2-2026-04-21 gained a preview feature on Aug 20. c29: the GCP clause leaves out a carve-out for 'substantial economic or material technical burden'. c36: BFL's Oct 31 entry says 'deprecated', not shut down, and 'no migration path' applied only to finetuning.

The researcher's Higgsfield row is contradicted (c59). A first-party model-retirement clause exists at https://higgsfield.ai/terms-of-use-agreement (§1.7, §11.10, §13.8, Jul 26, 2026): models may be substituted or retired 'at any time', and users should not rely on any model version. That also disproves the closing line that only BFL's terms allow zero notice; Luma and MiniMax also have no-notice carve-outs.

Figures in the answer I could not source: 'Alibaba 36 days for snapshots' has no URL and I could not reproduce it. The '92–124 days' range leaves out an Apr 13 notice that gave 180 days. Two c57 notice slugs did not resolve and '_717/_718' was not found. The other notices exist under different slugs, and none lists wan2.2-kf2v-flash.

Important missed facts:
- MiniMax-H3 weights are on Hugging Face, but its license excludes the USA, so there is no self-host fallback for San Francisco without a separate license.
- Alibaba uses an undefined 'long-tail' retirement class, emails only accounts that called the model in the last 3 months, and has postponed retirements.
- OpenAI offers dedicated capacity to keep a model after its shutdown date.
- BFL changed a limit on the FLUX 3 `latest` endpoint the same day it announced it.
- The Gemini API restricted 2.5 models to prior users without deprecating them.
- Kling's new API names models by URL path, e.g. /omni-video/kling-o1.

All dates, IDs and notice periods in the researcher's table were confirmed. The Vertex veo-3.1 date of 'November 17, 2026 or later' is 54 days away. The Vertex 12-month versus 336-day inconsistency stays unresolved, since both statements are on the same first-party page.

Checks not marked "supported":
- **partially_supported**: Snapshots lock model version for consistent behavior → Quote verbatim on gpt-image-2.md: "Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent." But https://developers.openai.com/api/docs/changelog.md Aug 20 shows the dated snapshot's API surface changed post-release: "Transparent backgrounds are n
- **partially_supported**: GCP Terms 1.4(e): 12 months notice unless materially similar replacement; excludes pre-GA → https://cloud.google.com/terms (Last modified September 2, 2026): quote verbatim present. Omitted carve-out in same clause: "Nothing in this Section 1.4(e) (Discontinuation of Services) limits Google's ability to make changes required to comply with applicable law, address a material security risk, 
- **partially_supported**: BFL flux-pro-1.0 endpoints and Finetuning API got 28 days (Oct 3 -> Oct 31, 2025), no migration path for finetuning → release-notes.md Oct 3, 2025: "The following endpoints will be deprecated" + "No migration path available. Finetuning functionality will be discontinued." Oct 31, 2025: "As of today, the Flux Pro 1.0 endpoints ... and the Finetuning API are officially deprecated." Docs say 'deprecated', not explicit
- **contradicted**: Higgsfield publishes no deprecation/notice policy; only 'Availability and access can change' → Quote is on https://docs.higgsfield.ai/docs/models.md: "The catalog covers 82 entries listed for sale as of September 22, 2026 ... Availability and access can change". But Higgsfield DOES publish a model-retirement clause: https://higgsfield.ai/terms-of-use-agreement (Last updated: July 26, 2026) §1
- **contradicted**: Answer summary: 'None of the notice periods above is a zero-notice guarantee except BFL's, whose ToS explicitly allows zero notice' → Higgsfield ToU https://higgsfield.ai/terms-of-use-agreement (Jul 26, 2026) §11.10: "Company may modify, update, or discontinue any aspect of Developer Access at any time." §11.11: "Any Developer Access features designated as \"beta,\" \"preview,\" \"experimental,\" or similar ... may be modified or 
- **unsupported**: Answer: 'Alibaba: 36 days for snapshots' (notice actually given) → No claim/URL attached; not found in any English notice fetched today. The Jun 08, 2026 snapshot notice (_79d) gives 124 days (Jun 8 -> Oct 10). Chinese notices (ids 1840/1873) are client-rendered and unreadable via curl.
- **partially_supported**: Answer: Alibaba '92–124 days for the Oct 10 batches' → Jul 10 (_7d9) -> 92 d, Jul 09 (_7d4) -> 93 d, Jun 08 (_79e/_79d) -> 124 d confirmed. But https://www.alibabacloud.com/en/notice/model_studionotice_on_the_decommissioning_of_certain_historical_mainline_models_731?_p_lc=1 dated "Apr 13, 2026" also targets Oct 10: "Model Studio will decommission the ma
- **partially_supported**: Answer: Kling IDs 'kling-v3, -omni, o1' are version names only → updates/api.md: "Supported model ranges: `kling-v3-omni`, `kling-v3`"; "`kling-video-o1` model". But the new API (07/15/2026) addresses models by URL path segment, e.g. https://kling.ai/document-api/api/video/3-0-omni/image-to-video.md "Path: `/image-to-video/kling-3.0`", /omni-video/kling-3.0-omni,

Flagged as unconfirmed by the verifier:
- 'Alibaba: 36 days for snapshots' (Notice-actually-given section): no claim ID or URL. Not reproducible today from any English notice. The Jun 08, 2026 snapshot notice gives 124 days.
- '92–124 days for the Oct 10 batches' is incomplete: the Apr 13, 2026 notice (_731) for the same Oct 10 date gives 180 days.
- c57 source list names notices '_717/_718 Apr 03' and bare slug suffixes '_7d4/_79e/_7d0'. Slugs built from the base name model_studio_notice_of_retirement_for_selected_legacy_models_<suffix> return 'not found' for 7d4/79e/7d0. The real slugs are ..._legacy_longtail_models_7d4, ..._legacy_mainline_models_79e/_79d and ..._postponed_retirement_of_selected_legacy_models_7d0. '_717/_718' not located.
- Higgsfield 'None stated' / 'terms URLs all 404': a search miss, not a fabrication. The ToU exists at https://higgsfield.ai/terms-of-use-agreement (Last updated July 26, 2026) and has an explicit model-retirement clause.

---

## G4 — track MJ3: Two things are unresolved: whether MJ video depends on the image model, and which video model version is served. MJ3 says no doc ties video to an image version. But the first-party EU Public Summary (…

**Why it matters:** If the video model is tied to V8.x, or is silently retrained, new edges between existing V7 stills are not version-independent. That affects the hybrid path (non-MJ stills plus MJ edges) and any stockpile-now hedge. It also decides whether video drift, not V7 retirement, is the binding risk.

**Gap-fill confidence:** high

### Answer
## MJ3 gap: is MJ video tied to the image version, and which video version is served? (checked 2026-09-24)

### Verdict
- **Served video version: settled by first-party code.** The Midjourney web client names the video model "video 1" and sends the internal job type `vid_1.1_i2v_*` [c15][c16][c17].
  - `vid_1.1` already appears in the bundle from the day before the V1 launch (2025-06-17) [c20] and in the launch-day bundle (2025-06-18) [c19].
  - It is the only video identifier in every sampled bundle up to 2026-09-19 [c21].
  - So "1.1" is V1's own launch-day identifier, not an unannounced later "video 1.1".
  - The only video version the parser accepts is "1" [c16][c19].
  - No update post contains "1.1" [c13].
- **Coupling to the image version: tension between two first-party sources, not adjudicated. STOP.**
  - The EU summary lists the "Image and Video family" with "Model dependencies: Midjourney V8, V8.1, and V8.2" [c1]. The EC template defines that field as the models this one was modified or fine-tuned from [c9].
  - MJ's own client has used the same video job ID since June 2025 [c19][c21]. V8.0 launched on 2026-03-17 [c8], nine months later.
  - The two do not strictly contradict each other: an unchanged identifier does not prove unchanged weights. MJ has updated image weights under unchanged version strings before (MJ3 §5).
- **The web client never sends an image version with a video job.**
  - A video job carries: `f` (speed and visibility flags), `channelId`, UI `metadata`, `t:"video"`, `videoType`, `stitch`, `newPrompt`, `parentJob`, `animateMode` [c17].
  - The video prompt is parsed as version "video 1". That parser keeps only `--raw`, `--motion`, `--length` and `--end`, and silently skips every other flag, including `--v` [c18].
  - How the server routes video jobs is unknown.
- **EU summary history: cannot be reconstructed, but the body is stable.**
  - The Wayback Machine has zero captures of the page [c5].
  - Zendesk shows the body was created at 2026-08-11T21:20:22Z and last edited at 2026-08-11T21:29:00Z [c2][c3].
  - The 2026-08-17 `updated_at` is shared with 5 other articles in the policies section, while their `edited_at` dates differ, so it was not a body edit [c4].
  - Three fetches (2026-09-23, 2026-09-24 00:08, and today) returned byte-identical bodies [c6].
  - The summary labels itself "Version #1" [c1]. It is the only EU AI Act summary in the help center [c7].
- **The summary's dates.**
  - The placement date (March 17, 2026) equals the V8.0 alpha launch date [c8].
  - "Last update: March 17, 2026" is not the edit date [c2].
  - The body lists V8.1 and V8.2, which were released later [c8].

### What changes in MJ3
| MJ3 statement | Update |
|---|---|
| "No official video version named after V1" | Still true in docs. In client code the model is "video 1", internal `vid_1.1` since launch [c16][c19][c21]. |
| "Client sends a video model/version field: unknown" | The web client sends `videoType:"vid_1.1_i2v_start_end_480"` (SD) or `_720` (HD), and no image version [c17]. Secondary clients send the same value [c23]. What autogen's own client (only on hil) sends is still unknown. |
| "Video drift undetectable" | Still true. The identifier has not moved in 15 months [c21], so it will not reveal a retrain either. Only possible public signals: (a) a new identifier in the bundle; (b) a revised EU summary, due every 6 months or on a "materially significant" update [c11]. |

### Timeline of the web bundle (first-party code, Wayback captures)
| Capture (UTC) | Finding |
|---|---|
| 2025-06-17 | `vid_1.1_t2v_joint_video` and `vid_1.1_i2v_joint_video` exist. The display helper `guessVersion` returns "7" for them [c20]. This is a UI label, not evidence of lineage. |
| 2025-06-18 (launch day) | `videoType:"vid_1.1_i2v_480"`. `guessVersion` now returns "video 1". The `--video` parser accepts "1" or "" [c19]. |
| 2025-07-26 | First appearance of `vid_1.1_i2v_start_end_480` (it is not in the 2025-07-02 bundle) [c21]. |
| 2025-08-07 | First 480/720 template [c21]. `--length 2.5` or `5` parser appears [c25]. |
| 2026-06-11 → 07-15 | `vid_1.1_t2v_joint_video` disappears [c21]. |
| 2026-07-24 (V8.2 launch), 08-14, 08-28, 09-16, 09-19 | Still only `vid_1.1_*` and "video 1" [c15][c21]. |
| alpha.midjourney.com, 2026-03-19 → 08-23 | Also `vid_1.1`. By 08-23 alpha reads resolution from `videoSettings` instead of `videoVersions["1"]` [c22]. |

### Side findings
- `--length 2.5|5`, "video 1" and `--video 1` appear in none of the 105 help-center articles [c24].
- **Relevant to the V7-retirement tracks:** in the 2026-09-19 web bundle, when the version is 8.1 or 8.2 and the prompt has character references, the client forces version "7" (`forcedV7ForOref`) [c26]. The V7 `--oref` route was still wired into production on 2026-09-19.
- A feed helper filters video jobs by their parent image's version (7, 8, 8.1, 8.2, niji 6, niji 7) combined with personalization or `--sref`. It is not on the submission path [c27].

### Evidence files
Scratch folder: `<session scratch, not kept>/mj3gap/`

| File | Contents |
|---|---|
| `eu.json` | sha256 8fe27948… |
| `eu_tr.json` | EU summary translations |
| `all_articles.json` | All 105 help-center articles |
| `ec_118480.pdf` | EC template, sha256 be6cdf10… |
| `ec.txt` | Extracted template text |
| `posts/` | 92 update posts |
| `posts_text.json` | Post texts |
| `wb/cse_20260919_rx83xj3k.js` | sha256 18cd0cd4… |
| `wb/app_20250618194823__app-070036ba769bec08.js` | sha256 2b52e9a0… |
| `wb/app_20250617101301__app-9e2b77837ea73090.js` | sha256 1b1787fb… |
| `wb/alpha_20260823072935_clientSideEntry-9rg1vdzc.js` | sha256 571bc885… |
| `cdx_*.json` | Wayback CDX listings |
| `sec/` | Secondary clients (pointers only) |

### Claims
- [c1] FIRST-PARTY · created 2026-08-11T21:20:22Z; edited_at 2026-08-11T21:29:00Z; updated_at 2026-08-17T20:06:41Z; accessed 2026-09-24 · https://docs.midjourney.com/api/v2/help_center/en-us/articles/48067080311309.json — The current EU AI Act training summary names the 'Midjourney Image and Video family of models', lists 'Model dependencies: Midjourney V8, V8.1, and V8.2', labels itself 'Version #1', and gives 'Last update' and placement date as March 17, 2026. — "Version of Summary: Version #1 Last update: March 17, 2026 ... Versioned model name(s): Midjourney Image and Video family of models Model dependencies: Midjourney V8, V8.1, and V8.2 Date of placement of the model on the Union market: March 17, 2026"
- [c2] FIRST-PARTY · accessed 2026-09-24 · https://docs.midjourney.com/api/v2/help_center/articles/48067080311309/translations.json — Zendesk metadata shows the EU summary body was last edited 2026-08-11T21:29:00Z, 9 minutes after it was created. It has exactly one translation (en-us), whose updated_at is the same timestamp. — ""count": 1 ... en-us created_at 2026-08-11T21:20:22Z updated_at 2026-08-11T21:29:00Z outdated False draft False"
- [c3] FIRST-PARTY · accessed 2026-09-24 · https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/ — Zendesk defines edited_at as the time the article content was last edited in its locale, as distinct from updated_at. — "edited_at: The time the article was last edited in its displayed locale ... updated_at: The time the article was last updated"
- [c4] FIRST-PARTY · accessed 2026-09-24 · https://docs.midjourney.com/api/v2/help_center/en-us/articles.json — The EU summary's updated_at (2026-08-17T20:06:41Z) is shared by all 6 articles in the 'Midjourney Policies' section that carry that timestamp. Their edited_at values differ (e.g. Community Guidelines 2025-12-05, ToS 2026-05-27), so the 2026-08-17 change was a metadata update, not a body edit. — "32013696484109 Community Guidelines ... edited 2025-12-05T19:30:20Z ... 48067080311309 Public Summary of Training Content ... edited 2026-08-11T21:29:00Z (all updated_at 2026-08-17T20:06:41Z)"
- [c5] secondary · accessed 2026-09-24 · https://web.archive.org/cdx/search/cdx?url=docs.midjourney.com/hc/en-us/articles/48067080311309*&output=json&filter=statuscode:200&collapse=digest — The Wayback Machine holds no capture of the EU summary page or its API JSON. The CDX returns [] with and without filters, the availability API returns empty archived_snapshots, and the /web/2026/ timegate returns 404. The same CDX endpoint does return snapshots for other MJ articles. — "[] ... {"url": "docs.midjourney.com/hc/en-us/articles/48067080311309-Public-Summary-of-Training-Content", "archived_snapshots": {}, "timestamp": "20260924"}"
- [c6] FIRST-PARTY · accessed 2026-09-23 and 2026-09-24 · https://docs.midjourney.com/hc/en-us/articles/48067080311309-Public-Summary-of-Training-Content — The EU summary body fetched today is byte-identical to the MJ3 fetch (2026-09-23) and the critic's fetch (2026-09-24 00:08). — "cmp output: SAME_AS_CRITIC / SAME_AS_MJ3"
- [c7] FIRST-PARTY · created 2026-01-20; edited 2026-01-20T20:52:55Z; accessed 2026-09-24 · https://docs.midjourney.com/hc/en-us/articles/42829949256205-AB2013-Documentation — The help center has one EU AI Act summary. The only other training disclosure is the California AB2013 document, which names no model versions. — "Published pursuant to California Civil Code Section 3111 (AB2013) Last Updated: January 20, 2026 ... Midjourney models are trained on datasets comprised of billions of images, text, and audiovisual content. The exact number of data points vary depending on the model version and phase of training."
- [c8] FIRST-PARTY · updated 2026-09-01T17:26:08Z; accessed 2026-09-24 · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — The Version doc dates V8.0's alpha launch to March 17, 2026, the same date as the EU summary's placement date. It dates V8.1 to April 14, 2026 and V8.2 to July 24, 2026. — "V8.0 was an early access alpha version that launched on March 17, 2026 ... V8.1 released on April 14, 2026 ... V8.2 released as the default version on July 24, 2026."
- [c9] FIRST-PARTY · C(2025) 8311 final, Brussels, 5.12.2025; accessed 2026-09-24 · https://ec.europa.eu/newsroom/dae/redirection/document/118480 — The EC template defines 'Model dependencies' as the upstream model(s) the model was modified or fine-tuned from, and 'Versioned model name(s)' as the unique identifiers of the covered models. — "Model dependencies: If the model is the result of a modification, including fine-tuning, of one or more general-purpose AI models already placed on the Union market, specify the model (version) name(s) of that/those models and provide a link to their Summary(ies) where available. ... Versioned model"
- [c10] FIRST-PARTY · C(2025) 8311 final, 5.12.2025; accessed 2026-09-24 · https://ec.europa.eu/newsroom/dae/redirection/document/118480 — The EC template's header asks for the summary version with links to earlier versions, a 'Last update' date, and a placement date for each model version covered. — "Version of the Summary: Version of the summary, with link(s) to previous versions where applicable / Last update: DD/MM/YY ... (including the dates each model (version(s)) was placed on the market, if the Summary applies to more than one model or version"
- [c11] FIRST-PARTY · 5.12.2025; accessed 2026-09-24 · https://ec.europa.eu/newsroom/dae/redirection/document/118480 — The EC notice expects a provider to update its summary after further training, at 6-month intervals or sooner for a materially significant change. For models placed before 2 August 2025, the summary is due by 2 August 2027. — "the Summary should be updated at six-month intervanls or if in the meantime the additional data used to further train the model requires a materially significant update ... For models placed on the market before 2 August 2025, providers should take the necessary steps to make the corresponding Summa"
- [c12] FIRST-PARTY · 2025-06-18T16:35:15Z · https://updates.midjourney.com/introducing-our-v1-video-model/ — The launch post names the video model 'Version 1' (2025-06-18). This is the only public version name. — "We’re releasing Version 1 of our Video Model to the entire community"
- [c13] FIRST-PARTY · accessed 2026-09-24 · https://updates.midjourney.com/sitemap-posts.xml — None of the 92 posts in updates.midjourney.com/sitemap-posts.xml (re-fetched 2026-09-24, newest alpha-changelog-9-23-26) contains '1.1'. Only video-rating-party-1 and introducing-our-v1-video-model name a video model (V1). — "hits 1.1~video: 0 ; any "1.1" occurrences: (none)"
- [c14] secondary · accessed 2026-09-24 · https://index.commoncrawl.org/CC-MAIN-2026-39-index?url=www.midjourney.com/*&output=json — Live www.midjourney.com and alpha.midjourney.com return a Cloudflare 403 challenge to non-browser fetches. Common Crawl CC-MAIN-2026-39 and -34 hold only 403 robots.txt records, so the Wayback Machine is the only archive of MJ's bundles. — "<title>Just a moment... ; "url": "https://www.midjourney.com/robots.txt", ... "status": "403""
- [c15] FIRST-PARTY · Wayback capture 2026-09-19T07:53:37Z (referenced by https://web.archive.org/web/20260921042052/https://www.midjourney.com/); accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — MJ's production web bundle captured 2026-09-19 labels every vid_1.1 job type 'video 1' and every v8-2 job type '8.2'. The 2026-09-21 homepage capture still loads this bundle. — "case"v8-2_retexture":return"8.2";case"vid_1.1_i2v_joint_video":case"vid_1.1_i2v_extend_video":...case"vid_1.1_i2v_start_end_a_video":case"vid_1.1_i2v_start_end_b_video":return"video 1""
- [c16] FIRST-PARTY · Wayback capture 2026-09-19; accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — In the same bundle, the web prompt parser handles '--video' with a function that accepts only '1' or empty (both mean 'video 1') and rejects anything else as an unknown video version. — "function o03(w){switch(w){case"1":return"video 1";case"":return"video 1";default:return y0("error.promptParser.unknownVideoVersion",{version:w})}} ... case"video":{if(q!=null)continue;let P=o03(M); ... "error.promptParser.unknownVideoVersion":"Unknown video version: {version}""
- [c17] FIRST-PARTY · Wayback capture 2026-09-19; accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The web client builds start/end-frame video jobs with videoType vid_1.1_i2v_start_end_{480|720}, chosen by the videoVersions['1'] resolution setting. Uploads send parentJob null. The base payload holds only speed/visibility flags, channelId and UI metadata, with no image-version field. — "A={f:TN0(G.speed,G.visibility),channelId:O,metadata:{isMobile:...}} ... o=V.videoVersions["1"].resolution==="480p"?"480":"720";if($.parentJob)F={...A,t:"video",videoType:`vid_1.1_i2v_start_end_${o}`,...};else F={...A,t:"video",videoType:`vid_1.1_i2v_start_end_${o}`,stitch:null,newPrompt:p,parentJob:"
- [c18] FIRST-PARTY · Wayback capture 2026-09-19; accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The 'video 1' prompt parser keeps only --raw, --motion high|low, --length 2.5|5 and --end loop|URL, and skips every other flag. It also rejects aspect ratios. — "function Wz0(w,Z){let Q={...w,version:"video 1",styleRaw:!1,motion:null,length:null,end:null};for(let{flag:B,args:Y}of Z)if(B==="raw"){...}else if(B==="motion"){...}else if(B==="length"){...J!==2.5&&J!==5...}else if(B==="end"){...}else continue;return Q} ... case"video 1":return Error("Video 1 does "
- [c19] FIRST-PARTY · Wayback capture 2025-06-18T19:48:23Z; accessed 2026-09-24 · https://web.archive.org/web/20250618194823id_/https://www.midjourney.com/_next/static/chunks/pages/_app-070036ba769bec08.js — The bundle captured on V1 launch day (2025-06-18T19:48Z, about 3 hours after the launch post) already sends videoType 'vid_1.1_i2v_480', labels vid_1.1 job types 'video 1', and has the same '--video' parser. — "ep={...eS,t:"video",videoType:"vid_1.1_i2v_480",newPrompt:Q,parentJob:{...},animateMode:"auto"} ... case"vid_1.1_i2v_extend_b_video":return"video 1" ... case"video":{...switch(L){case"1":case"":return"video 1";default:return Error("Unknown video version: ".concat(L))}"
- [c20] FIRST-PARTY · Wayback capture 2025-06-17T10:13:01Z; accessed 2026-09-24 · https://web.archive.org/web/20250617101301id_/https://www.midjourney.com/_next/static/chunks/pages/_app-9e2b77837ea73090.js — In the pre-launch bundle (2025-06-17), a display helper named guessVersion returns '7' for vid_1.1 job types. On launch day it returns 'video 1'. This is a UI label heuristic, not evidence of which model video was built from. — "function guessVersion(L,H){switch(L){... case"v7_retexture":case"vid_1.1_t2v_joint_video":case"vid_1.1_i2v_joint_video":return"7";"
- [c21] FIRST-PARTY · Wayback captures 2025-06-17..2026-09-19; accessed 2026-09-24 · https://web.archive.org/cdx/search/cdx?url=www.midjourney.com/public/out/*&output=json&collapse=urlkey&from=2025 — Every sampled MJ web bundle from 2025-06-18 to 2026-09-19 (main site: 2025-06-18/19/20, 07-02, 07-26, 07-30, 08-07, 08-14, 11-21; 2026-01-09, 02-27, 03-24, 04-14, 05-15, 06-11, 07-15, 07-24, 08-14, 08-28, 09-16, 09-19) uses only vid_1.1_* video identifiers and the same parser that accepts only video version '1'. start_end_480 first appears 2025-07-26 (absent 2025-07-02). The 480/720 template first appears 2025-08-07. vid_1.1_t2v_joint_video is present through 2026-06-11 and absent from 2026-07-15. No vid_1.0, vid_1.2 or vid_2 string was found. — "20250730 ... ['vid_1.1_', 'vid_1.1_i2v_480', ... 'vid_1.1_i2v_start_end_480', ...] ... 20260916210848 ... templates: ['`vid_1.1_i2v_${V.videoVersions["1"].resolution==="480p"?"480":"720"}`', ...] | parser: function m03(w){switch(w){case"1":return"video 1";case"":return"video 1";..."
- [c22] FIRST-PARTY · Wayback capture 2026-08-23T07:29:35Z; accessed 2026-09-24 · https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js — The alpha.midjourney.com bundles (2026-03-19, 04-16, 07-25, 08-23) also emit vid_1.1. By 2026-08-23 alpha reads video resolution from a versionless videoSettings key. — "`vid_1.1_i2v_${U.videoSettings.resolution==="480p"?"480":"720"}` ... case"vid_1.1_i2v_start_end_b_video":return"video 1""
- [c23] secondary · commits 2025-08-02..2025-08-27; accessed 2026-09-24 · https://github.com/trueai-org/midjourney-proxy/blob/0f87175e28fbcd0d9c4459dd03245b87797f1ca8/src/Midjourney.Base/Dto/SubmitVideoDTO.cs — SECONDARY pointer: reverse-engineered clients hard-code vid_1.1_i2v_480/720 and vid_1.1_i2v_start_end_480. midjourney-proxy's video DTO history begins 2025-08-02. GitHub code search found no vid_1.0 or vid_2 hits from MJ clients. — "取值：vid_1.1_i2v_480 | vid_1.1_i2v_720 / SD: vid_1.1_i2v_480 / HD: vid_1.1_i2v_720 ... public string VideoType { get; set; } = "vid_1.1_i2v_480";"
- [c24] FIRST-PARTY · accessed 2026-09-24 · https://docs.midjourney.com/api/v2/help_center/en-us/articles.json — None of the 105 current help-center articles mentions '--length', '--video 1' or 'video 1'. — "(grep of all 105 article bodies for '--length', '--video 1', 'video 1', 'Video 1': 0 hits)"
- [c25] FIRST-PARTY · Wayback capture 2025-08-07T19:59:59Z; accessed 2026-09-24 · https://web.archive.org/web/20250807195959id_/https://www.midjourney.com/public/out/clientSideEntry-t9j5tm0j.js — The undocumented video '--length 2.5|5' parser has been in the web bundle since at least 2025-08-07. — "else if(B==="length"){if(Q.length!=null)continue;let H=W3(Y);if(Number.isNaN(H)||H!==2.5&&H!==5)return new Error("Length should be 2.5 or 5");"
- [c26] FIRST-PARTY · Wayback capture 2026-09-19; accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — Side finding: the 2026-09-19 production web client forces image version '7' when the version is 8.1 or 8.2 and character references are present (forcedV7ForOref). — "Y=(Z.version==="8.1"||Z.version==="8.2")&&B;return{prompt:Y?R2(Q):Q,version:Y?"7":Z.version,forcedV7ForOref:Y}"
- [c27] FIRST-PARTY · Wayback capture 2026-09-19; accessed 2026-09-24 · https://web.archive.org/web/20260919075337id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — A feed/UI helper filters video jobs by the parent image's version (7, 8.2, 8.1, 8, niji 6, niji 7) plus personalization or sref. It was seen only in feed and rendering code, not on the video submission path. — "function PL3(w){switch(w){case"7":case"8.2":case"8.1":case"8":case"niji 6":case"niji 7":return!0;default:return!1}} ... function NA(w){...return PL3(w.prompt.version)&&CL3(w)} ... if(D3.type==="video"){if(D3.prompt.version!=="video 1")continue;if(!NA(n0))continue}"

### Could not confirm
- Whether the EU summary's 'Model dependencies' or 'Last update' text was ever different. There are no Wayback captures, and Zendesk exposes no public revision history. Zendesk metadata only shows the body unchanged since 2026-08-11T21:29:00Z; the first 9 minutes after creation (21:20:22Z to 21:29:00Z) are unobservable.
- Whether the weights served under vid_1.1 / 'video 1' have ever been retrained, on V8.x or otherwise. The client-side identifier has not changed since 2025-06-17, and MJ has changed image weights under unchanged version strings before, so the client cannot reveal this.
- What the '.1' in 'vid_1.1' means. It predates the public V1 launch (2025-06-17 bundle), and no first-party text explains it.
- How the server routes video jobs, and whether routing depends on the image model or the start image's provenance. Only the client payload is visible, and it carries no image version.
- The live 2026-09-24 web bundle. midjourney.com returns a Cloudflare 403. The latest verified bundle is 2026-09-19 (clientSideEntry-rx83xj3k.js), which the 2026-09-21 homepage capture still loads.
- The Discord bot's video job type and version handling. Not accessible.
- What autogen's third-party midjourney.api client (only on hil) sends as videoType. Secondary reverse-engineered clients send 'vid_1.1_i2v_start_end_480' for start/end jobs, but that client itself is not verified.
- Semantics of the undocumented '--length 2.5|5' video flag, and whether it affects the server-side model.
- Whether a V7-era or video-V1-specific EU training summary exists outside docs.midjourney.com. None is in the help center. Under EC point 33, models placed before 2 August 2025 have until 2 August 2027.
- What the NA() helper (parent-image version 7/8/8.1/8.2/niji 6/niji 7 plus personalization or sref) gates in the UI. It was seen only in feed and rendering code, not on the submission path.

### Verification (combined lens)
I independently re-fetched every cited source on 2026-09-24. Where hashes were given, the files match the researcher's: Zendesk JSON 8fe27948, EC PDF be6cdf10, Wayback bundles 18cd0cd4, 2b52e9a0, 1b1787fb and 571bc885. I also pulled 10 more Wayback bundles to spot-check c21. 24 of 27 claims are supported, c23 is secondary-only, and c18 and c27 are partially supported.

Corrections and main findings:
- **c18:** the mechanism is wrong. The shared parser keeps --bs and the speed/visibility flags. --v is actively stripped from video prompts by R2/W33/Sz0, and was already removed with MV('v',...,'remove') on launch day.
- **c17:** needs a caveat. newPrompt carries ' --video 1' as text.
- **c27:** NA() is a profile-picture/banner picker filter, not a feed helper.
- **Headline:** the 'settled' verdict should be read as the client-requested identifier only, not the served weights.

Important missed first-party facts:
- The Video doc says video works on images 'regardless of what version they were made in' and that source-image parameters 'will be automatically removed'.
- The EU summary says the family 'is continuously trained'.
- The single March 17, 2026 placement date conflicts with the V1 video launch 'to the entire community' on 2025-06-18.
- EC points 30, 32 and 33 support the 'loose field use' reading and explain the August 2026 publication timing.
- The 2025-04-30 V7 update post supports the uncited 'silent weight update' precedent.

No hallucinated versions or dates were found. The researcher's STOP on the EU-summary vs client-code tension stands.

Checks not marked "supported":
- **partially_supported**: 'video 1' parser keeps only --raw, --motion, --length, --end and skips every other flag, including --v; rejects aspect ratios. → Video-1 keeps --raw/--motion/--length/--end in its version-specific parser. The shared flags (--bs, speed, visibility, --seed etc.) are still honored. --ar returns an error. The client removes --v/--version/--niji/--test/--testp from video prompts before parsing; they are not silently skipped. First-party Video doc lists video params as '--motion low , --motion high , --raw , --loop , --end , and --bs #'.
- **secondary_only**: SECONDARY: midjourney-proxy hard-codes vid_1.1_i2v_480/720; history begins 2025-08-02. → gh api repos/trueai-org/midjourney-proxy/contents/src/Midjourney.Base/Dto/SubmitVideoDTO.cs?ref=0f87175e…: '/// 取值：vid_1.1_i2v_480 | vid_1.1_i2v_720' and 'public string VideoType { get; set; } = "vid_1.1_i2v_480";'. 3 commits: 2025-08-02T13:59:32Z, 2025-08-03, 2025-08-27. gh search code 'vid_1.1_i2v
- **partially_supported**: Feed/UI helper filters video jobs by parent-image version plus personalization or sref; not on the submission path. → NA() gates which jobs can be picked as a profile picture (square) or banner (11:3). It is not a general feed helper and has no bearing on video generation.
- **partially_supported**: Verdict headline: 'Served video version: settled by first-party code.' → Settled: the client-requested video identifier (vid_1.1_* / 'video 1', unchanged since 2025-06-17/18). Not settled: which weights the server serves.

Flagged as unconfirmed by the verifier:
- c18/answer: the params list 'keeps only --raw, --motion, --length and --end ... skips every other flag, including --v' is inaccurate. The first-party Video doc lists '--motion low, --motion high, --raw, --loop, --end, and --bs #'. The bundle's shared parser honors --bs and the speed/visibility flags, and R2 strips --v before parsing. This is a mechanism error, not a fabricated number.
- No fabricated version numbers, dates, sizes or hashes found. Every date and version in the answer (2025-06-17/18, 2025-07-02/26/30, 2025-08-07, 2026-03-17, 2026-04-14, 2026-06-11, 2026-07-15/24, 2026-08-11/17/23, 2026-09-16/19/21, 105 articles, 92 posts, 139 JS captures, sha256 prefixes) was re-confirmed this session.

---

## G5 — track MJ1: The mission asks about 'notice given for V6/V7', and the record has holes. No first-party notice was found before the V5.2 to V6 default switch on 2024-02-14, because the updates page predates it and …

**Why it matters:** 'How much warning would we get' has to rest on as many precedents as possible. At present the only positive-notice case is the alpha V8.0 ('two weeks', honoured at 43 days). One more production precedent in either direction would change the planning figure's confidence.

**Gap-fill confidence:** medium

### Answer
## MJ1 gap: notice given for V6/V7, and whether any version was ever made uncallable

**Result:** The gap is partly closed. The V7 record is firmer. No written first-party V6 notice was found, and absence is not proven. The version-retirement record now rests on dated first-party statements, not only on docs.

### 1. V5.2 → V6 default (2024-02-14): no first-party written notice found
- **X.** Only 7 @midjourney posts from 2023-12-15 to 2024-02-20 are recoverable [c31]:
  - V6 alpha launch, with no default timeline [c1];
  - V6 alpha update [c2];
  - pan/zoom on V6 (2024-01-25), Niji 6 (2024-01-29), style algorithm (2024-01-31), web alpha (2024-02-08).
  - None mentions a default switch. No @midjourney post between 2024-02-09 and 2024-03-06 was archived, so X silence cannot be proven.
- **Old docs.**
  - The model-versions and models pages never mentioned V6 in any capture from 2023-12-27, 2024-01-14, 2024-01-29, 2024-02-09, 2024-02-11 or 2024-02-15 [c4][c6].
  - They said "--v 5.2 is the current default model" until at least 2024-02-15T19:07:35Z, which is after the switch.
  - The "--version accepts" list left out 6 even though `--v 6` already worked [c4][c1].
  - The docs were updated after the fact, between 2024-02-15T19:07Z and 2024-02-26T15:46Z [c5].
- **Updates page.** No pre-switch post exists. The earliest Ghost post is dated 2024-03-07 (backdated), and midjourney.com/updates was first captured on 2024-03-24 [c7].
- **Pointers only (secondary).** Recap titles say office hours signalled "V6 will be the default version by the end of January 2024" (3 Jan 2024) and "V6 Beta will become the default soon" (7 Feb 2024) [c8]. These were spoken, the target slipped about 2 weeks, and the recaps could not be read.

### 2. V6.1 → V7 default (2025-06-17): written notice appeared only on updates.midjourney.com
- **Docs.** On 2025-06-13T11:17:11Z the Version doc said "Version 7 is our latest model, but version 6.1 remains the default", with no forecast [c9]. It was updated after the fact [c13].
- **X.** The switch post came at 2025-06-17T06:04:41Z [c10], 1h18m after the updates post (04:46:33Z, prior [12]).
  - The 2025-05-29 X post left out the "before making V7 default" line that the same day's updates post carried [c11].
  - 20 @midjourney posts were recovered for 2025-05-15 to 2025-06-16. None pre-announces the switch.
- **Office hours.** X Spaces sessions were held on 05-21, 05-29, 06-04 and 06-11. Midjourney deleted those posts afterwards; Wayback kept them as API JSON [c12]. Midjourney also linked a live "Hivemind v0.1" room tool; its content was not archived [c30]. Nothing said in those sessions can be recovered.
- **Wording discrepancy.** See Contradictions.

### 3. Was any production or test model ever made uncallable? No record found.
- **Docs, 2023-12 to 2026-09.**
  - V1–V3, `--hd`, Niji 4 and `--test/--testp` were always documented as callable through `--version` or as legacy parameters [c14][c15][c16].
  - Test models were described as "released temporarily" in 2023 [c14], but they still appear under Legacy Parameters in 2026 [c16].
  - The Version article across 24 captures (2025-02 to 2026-07) marks only V8.0 as "no longer available for use" [c17].
- **Dated first-party statements on X.**
  - 2026-03-01: "you can still use all our old models on our website - everything back to midjourney v1" [c18].
  - 2026-07-26: "you can always use the old version" [c19].
  - 2026-09-09, in reply to a request to preserve access: "right now almost every old visual model is still available" [c20]. "Almost" and "right now" mean this is not a commitment, and at least one old model (V8.0) is gone.
- So there is no production precedent for retirement notice in either direction. No numbered production model has been retired in about 4.5 years (2022-02 to 2026-09), per docs plus MJ's statements. The only retirement is still the V8.0 alpha. Its notice chain gains one item: 2026-04-15 "we plan on discontinuing v8 soon" [c25].

### 4. Retention policy: none stated
- Docs searches for "retire", "sunset" and "unavailable" return 0 articles [c29].
- The only statements are informal X replies [c18][c19][c20] and "(for now)" caveats [c26].
- On oref specifically:
  - 2026-08-28: oref "still available via v7" [c21][c22].
  - 2026-09-10: "we replaced omni with the new edit model" [c23], plus requests for "examples where omni works better than the new edit model" [c24].
  - That request resembles the V8.0 pre-retirement pattern ([c25], 2026-04-15). In the V8.0 case, the formal notice followed 57 days later and removal 100 days later. This is my inference, low confidence.

### Effect on the planning figure
| Precedent | Written first-party notice |
|---|---|
| V5.2→V6 default | none found (docs lagged; X not archived for 02-09..03-06) [c4][c5][c31] |
| V6→V6.1 default | 0 days (prior) |
| V6.1→V7 default | updates: about 25 days of undated hints; docs 0; X 0 [c9][c10][c11] |
| V7→V8.1, V8.1→V8.2 | 0 days (prior) |
| Production model retirement | never happened; last "still available" statement 2026-09-09 [c20] |
| V8.0 alpha retirement | informal from 2026-03-21 and 2026-04-15 [c25]; formal 2026-06-11; removed 2026-07-24 |

The guaranteed-warning planning figure stays at 0 days. Two findings raise confidence in it:
- Written advance notice has never been found for any default switch, beyond V7's undated hints.
- No production model has ever been retired, so the V8.0 alpha is still the only notice precedent.

### Claims
- [c1] FIRST-PARTY · 2023-12-21T17:56:52Z (read via cdn.syndication.twimg.com 2026-09-24) · https://x.com/midjourney/status/1737894922362192017 — The V6 alpha launch post on X gave no default-switch timeline. — "We're now alpha-testing our V6 models Midjourney. Just type /settings and click V6 or add --v 6 after your prompt."
- [c2] FIRST-PARTY · 2024-01-06T06:52:31Z · https://x.com/midjourney/status/1743525940217729110 — The first V6 alpha update post on X mentioned no default switch. — "Our first major update to V6 alpha is now live."
- [c4] FIRST-PARTY · snapshot 2024-02-15T19:07:35Z (identical text in 20240114132550, 20240209002720, 20240211233713) · https://web.archive.org/web/20240215190735/https://docs.midjourney.com/docs/model-versions — The old docs model-versions page still showed V5.2 as default the day after the switch, never mentioned V6, and left 6 out of the accepted --version values. — "--version accepts the values 1, 2, 3, 4, 5, 5.1, and 5.2 ... --v 5.2 is the current default model. ... Default Model 06/22/23–current"
- [c5] FIRST-PARTY · snapshot 2024-02-26T15:46:40Z · https://web.archive.org/web/20240226154640/https://docs.midjourney.com/docs/models — The docs recorded the V6 default only after the fact, by 2024-02-26. — "--v 6 is the current default model. ... Midjourney Model Version 6 was released on December 20, 2023, and became the default model on February 14, 2024."
- [c6] FIRST-PARTY · snapshot 2024-01-29T20:47:27Z (also 20231227000557) · https://web.archive.org/web/20240129204727/https://docs.midjourney.com/docs/models — The docs models page 15 days before the switch still showed V5.2 as current, with no V6 forecast. — "--v 5.2 is the current default model."
- [c7] FIRST-PARTY · accessed 2026-09-24; sitemap-posts.xml earliest lastmod 2024-03-14T06:13:34Z; Wayback CDX first capture www.midjourney.com/updates 20240324012943 · https://updates.midjourney.com/launching-v6-turbo/ — No updates-page post predates the V6 switch: the earliest Ghost post is dated 2024-03-07, and midjourney.com/updates was first captured 2024-03-24. — "<meta property="article:published_time" content="2024-03-07T00:00:00.000Z""
- [c8] secondary · 2024-02-07 (title via search); companion: https://medium.com/design-bootcamp/midjourney-weekly-update-3rd-january-2024-v6-will-be-the-default-version-by-the-end-of-january-3865fbc77303 · https://medium.com/design-bootcamp/midjourney-weekly-update-7th-feb-2024-midjourney-v6-beta-will-become-the-default-soon-a754fd9de635 — POINTER ONLY: third-party office-hours recaps say V6 default was signalled verbally as 'by end of January' (3 Jan 2024) and 'soon' (7 Feb 2024). — "Midjourney Weekly Update (7th Feb 2024): Midjourney V6 Beta will become the default soon (title only; page returned 403, not in Wayback)"
- [c9] FIRST-PARTY · snapshot 2025-06-13T11:17:11Z · https://web.archive.org/web/20250613111711/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — Four days before the V7 default switch, the Version doc said V6.1 remained default and gave no forecast. — "Version 7 is our latest model, but version 6.1 remains the default. This means you'll need to manually set our new model to use it."
- [c10] FIRST-PARTY · 2025-06-17T06:04:41Z · https://x.com/midjourney/status/1934854695157420119 — The V7 default was announced on X on the day of the switch, 1h18m after the updates post. — "we are making V7 the default model for all new and existing members of Midjourney. Have fun!"
- [c11] FIRST-PARTY · 2025-05-29T23:15:39Z · https://x.com/midjourney/status/1928228774451269830 — The 2025-05-29 X post left out the V7-default heads-up that the same day's updates post included. — "Three updates today: 1) Midjourney V7 rendering is now ~40% faster! 2) Our image editor's AI moderator is now much smarter. 3) We're beginning our second community roadmap  voting period."
- [c12] FIRST-PARTY · 2025-05-29T19:07:22Z (Wayback capture of API JSON) · https://web.archive.org/web/20250529190722/https://twitter.com/midjourney/status/1928166294211166657 — Weekly office-hours X Spaces were held in the V7 window (05-29, 06-04, 06-11 confirmed); MJ later deleted those posts, and their spoken content is not accessible. — ""title":"Happening now: Midjourney Weekly Office Hours - May 29" (also 1930343514250064163 'June 4', 1932876980237877754 'June 11'; all TweetTombstone on syndication today)"
- [c13] FIRST-PARTY · snapshot 2025-07-11T08:39:54Z · https://web.archive.org/web/20250711083954/https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — The Version doc recorded the V7 switch after the fact. — "Version 7 was released on April 3, 2025, and became the default model on June 17, 2025. ... Version 6.1 was released on July 30, 2024, and was the default model until June 16, 2025."
- [c14] FIRST-PARTY · snapshot 2023-12-08T20:50:41Z · https://web.archive.org/web/20231208205041/https://docs.midjourney.com/legacy/docs/models — The 2023 legacy docs documented V1–V3, --hd, Niji 4 and the test models as callable, and described test models as released 'temporarily'. — "Occasionally new models are released temporarily for community testing and feedback. There are currently two available test models: --test and --testp ... You can access earlier midjourney models by using the --version or --v parameter"
- [c15] FIRST-PARTY · snapshot 2024-03-03T21:06:44Z (early-models 20240303210653 same substance, captures to 2024-09-20) · https://web.archive.org/web/20240303210644/https://docs.midjourney.com/docs/legacy-model-parameters — After the V6 switch, the early-models and legacy-parameters pages still documented V1–V5 and the test models as usable. — "The parameters on this page only work with legacy Midjourney Model Versions. ... Test --test Use the Midjourney special test model. ... Version --version <1, 2, 3, 4, or 5>"
- [c16] FIRST-PARTY · edited_at 2026-09-01T17:19:52Z; accessed 2026-09-24 via Zendesk API (same list in Wayback captures 2025-02-26..2026-03-15) · https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features — Current Legacy Features still lists the test models under Legacy Parameters and marks no production version unavailable. — "Test Models --test --testp Creative --creative Sameseed --sameseed Uplight --uplight Stop --stop Character Reference --cref --cw Deprecated Parameters"
- [c17] FIRST-PARTY · edited_at 2026-09-01T17:26:08Z; captures via https://web.archive.org/cdx/search/cdx?url=docs.midjourney.com/hc/en-us/articles/32199405667853* · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — Across 24 Version-article captures (2025-02-26 to 2026-07-31) and the live page, only V8.0 is ever marked unavailable. — "Images generated in V8.0 are still available in your website gallery, but the version is no longer available for use."
- [c18] FIRST-PARTY · 2026-03-01T02:40:07Z (quote-post, top level) · https://x.com/midjourney/status/2027936894789755252 — MJ stated on X that all old models back to V1 were still usable on the website. — "you can still use all our old models on our website - everything back to midjourney v1"
- [c19] FIRST-PARTY · 2026-07-26T18:32:44Z (reply to 2080918810169692660) · https://x.com/midjourney/status/2081447646397698293 — In an informal X reply, MJ said users can always use the old version. — "every new version has its own style you can always use the old version"
- [c20] FIRST-PARTY · 2026-09-09T19:58:00Z (parent 2097766443299328492: 'Preserve /access/ to old models whenever you can, please') · https://x.com/midjourney/status/2097776556836090015 — Replying to a request to preserve access to old models, MJ gave a hedged present-tense statement, not a commitment. — "right now almost every old visual model is still available"
- [c21] FIRST-PARTY · 2026-08-28T17:31:51Z · https://x.com/midjourney/status/2093391121267540131 — After the Edit Model launched, MJ said oref remains available via V7, and that V8 oref had always fallen back to V7. — "if you want to use the old one though for some reason it is still available via v7 (if you used it last week with v8 it always just fell back to v7 anyway)"
- [c22] FIRST-PARTY · 2026-08-28T17:30:22Z · https://x.com/midjourney/status/2093390750851686780 — A second MJ reply the same day confirms oref is still usable on V7. — "omni reference with v8 would just fall back to v7 , so you can still use it if you switch to v7."
- [c23] FIRST-PARTY · 2026-09-10T15:15:51Z · https://x.com/midjourney/status/2098067938771382630 — MJ describes omni-reference as replaced by the Edit Model. — "we replaced omni with the new edit model have you tried it?"
- [c24] FIRST-PARTY · 2026-09-10T17:38:40Z · https://x.com/midjourney/status/2098103877933613345 — MJ is asking for evidence that omni beats the Edit Model; this resembles the V8.0 pre-retirement solicitation (inference). — "can you show any examples where omni works better than the new edit model? this would help us improve things"
- [c25] FIRST-PARTY · 2026-04-15T05:29:12Z · https://x.com/midjourney/status/2044286899163181465 — An extra informal V8.0 retirement signal on X, 57 days before the formal notice and 100 days before removal. — "we plan on discontinuing v8 soon, if you have good prompts that show something v8 is doing that v8.1 can't do please let us know."
- [c26] FIRST-PARTY · 2025-05-02T21:06:27Z · https://x.com/midjourney/status/1918411790637252762 — The fallback to the old in-place V7 model was offered only 'for now'. — "If you want to disable optimizations you can type --q 2 (for now)."
- [c27] FIRST-PARTY · 2025-06-18T17:43:30Z · https://x.com/midjourney/status/1935392945907319020 — Around the V7 default switch, MJ said the V7 base model had not been changed apart from adding oref and the new sref. — "V7 is a image quality improvement over V6.1 and hasn't 'taken a hit' lately we haven't changed it outside of adding oref and new sref"
- [c28] FIRST-PARTY · 2025-04-30T23:04:57Z · https://x.com/midjourney/status/1917716836415856955 — About a day before oref launched, MJ gave informal notice that cref would be replaced on V7. — "Will be replaced by omni-reference which is coming very soon"
- [c29] FIRST-PARTY · accessed 2026-09-24 (105 articles scanned via /api/v2/help_center/en-us/articles.json) · https://docs.midjourney.com/api/v2/help_center/articles/search.json?query=retire — MJ docs contain no retention or deprecation-notice policy; searches for 'retire', 'sunset' and 'unavailable' return 0 articles. — "retire: 0 results; sunset: 0; unavailable: 0; 'deprecated' -> only Discord Command List and Legacy Features"
- [c30] FIRST-PARTY · 2025-05-29T19:21:42Z · https://web.archive.org/web/20250529192142/https://twitter.com/midjourney/status/1928169899379020003 — MJ posted links to a live office-hours 'Hivemind' room tool during office hours; room content is dynamic and was not archived (live URL returns 404). — "expanded_url https://midjourneyofficehours.onrender.com/room/f9c347af, title 'Hivemind v0.1'; root page meta: 'a new collective decision-making tool'"
- [c31] secondary · accessed 2026-09-24 · https://web.archive.org/cdx/search/cdx?url=twitter.com/midjourney/status/&matchType=prefix&output=txt&fl=original&collapse=urlkey&limit=20000 — Method note (coverage): 1,709 status IDs under twitter.com/x.com/midjourney were found in Wayback; 1,519 are @midjourney-authored and readable via syndication. Only 7 fall in 2023-12-15..2024-02-20, none after 2024-02-08T22:04Z until 2024-03-07. — "window 2023-12-15..2024-02-20 ids: 1737894922362192017, 1740088661033808162, 1743525940217729110, 1750353362774855765, 1752115495065755798, 1752843530576543906, 1755714302152225253"

### Could not confirm
- Any first-party written advance notice of the 2024-02-14 V5.2->V6 default switch. Discord #announcements was not accessible; no @midjourney X post from 2024-02-09 to 2024-03-06 is archived in Wayback, so absence on X is unproven; the docs said nothing until after the switch; the updates page did not exist yet.
- Exact time on 2024-02-14 that V6 became default.
- Office-hours statements (spoken X Spaces) for Jan–Feb 2024 and 2025-05-21/05-29/06-04/06-11. The Spaces posts were deleted, the Hivemind room pages are dynamic and not archived (live 404), and third-party recaps are secondary (Medium returned 403 and is not in Wayback).
- Discord #announcements content for the V6 and V7 default switches (needs login; not attempted).
- Completeness of the X record: only Wayback-captured status IDs could be enumerated (1,519 @midjourney posts), and uncaptured posts are unknown. The archive.md capture of twitter.com/midjourney from 2024-01-31 was blocked (HTTP 429).
- Which 'old visual model(s)' are not available, given 'almost every' (2026-09-09); V8.0 is the only one documented.
- Whether --v 1–5.2, --niji 4/5, --test/--testp or legacy --hd actually accept jobs today. Not tested; the latest positive first-party statement is 2026-03-01 ('everything back to midjourney v1').
- Any formal first-party model-retention or deprecation-notice policy: none exists in docs, updates posts or recovered X posts.

### Verification (combined lens)
I re-checked every citation live today (X syndication, Wayback id_ captures, the Zendesk API, Ghost meta). All 29 quoted claims check out verbatim: 22 fully, 6 partially (counts, framing, or the ToS clause omitted from c29), and c8 is secondary only. The core conclusions hold. No written first-party notice exists before the 2024-02-14 V6 default: docs showed V5.2 as default through 2024-02-15, no @midjourney post is archived between 2024-02-08T22:04Z and 2024-03-07T06:34Z, and the updates site was backdated from 2024-03-07. V7's only written hints are dated updates posts on 2025-05-23 and 2025-05-29; X and docs gave 0 days. No numbered production model is documented as uncallable; only V8.0 is.

Errors found:
- The V7-window count is 28 readable posts plus 8 author-deleted, not 20.
- The Version article has 26 captures, not 24.
- The '05-21' office hours is inferred, not seen.
- The V7 hints are dated, not 'undated'.
- The V8.0 notice chain is misframed. It was written and first-party from 2026-03-21, with a written 2026-04-14 decommission notice and a docs 'limited time' notice by 2026-05-18. The stated '2 weeks' ran 43 days.

Significant misses:
1. A written 2026-06-11 condition that V7 omni-reference stays available only 'while we finish training the improved version for V8'. The V8.2 Edit Model, launched 2026-08-27, is described in writing as 'replacing omni-reference'. This is the strongest first-party signal for the project's --oref --v 7 pipeline.
2. The ToS clause 'We reserve the right to modify or discontinue any aspect of the Service ... at any time', which contradicts 'no policy stated'.
3. First-party lines saying changes may come without notice or suddenly: 2024 V6 alpha 'may change suddenly', 2026 'Perhaps without notice!', and '--preview ... not guaranteed to run consistently'.
4. A live first-party docs contradiction: Legacy Features says the current default is V7, while the Version article says V8.2.
5. Beta Upscale, the only upscaler for test models, is documented as deprecated and unreliable.
6. V7 was changed in place under the same pin (2025-04-30 and 2025-05-02).

Scratch: <session scratch, not kept>/mj1-verify/

Checks not marked "supported":
- **secondary_only**: POINTER: third-party recaps say office hours signalled V6 default 'by end of January' (3 Jan) and 'soon' (7 Feb). → WebSearch confirms the Medium titles only: 'Midjourney Weekly Update (7th Feb 2024): Midjourney V6 Beta will become the default soon' and '(3rd January 2024): V6 will be the default version by the end of January 2024'. WebFetch returned 403. CDX has 0 Wayback captures of either. Secondary; it cannot
- **partially_supported**: Across 24 Version-article captures (2025-02-26..2026-07-31) and live, only V8.0 is ever marked unavailable. → 26 captures (20250226174030..20260731111048 incl. 5 utm-param variants); substance unchanged.
- **partially_supported**: Extra informal V8.0 retirement signal on X 2026-04-15, 57 days before formal notice and 100 before removal. → The V8.0 notice chain is written and first-party from 2026-03-21, not informal. 2026-03-21 updates post; 2026-04-14 updates post; 2026-04-15 X reply; the Version doc says 'still available for a limited time' by the 2026-05-18 capture; 2026-06-11 updates post and X: 'in two weeks'; actual removal 2026-07-24 (43 days after the two-week notice).
- **partially_supported**: MJ docs contain no retention or deprecation-notice policy; retire/sunset/unavailable return 0. → MJ does state a policy. It is the ToS clause that reserves the right to discontinue any feature at any time (https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service). There is no positive retention or notice commitment.
- **contradicted**: 20 @midjourney posts were recovered for 2025-05-15 to 2025-06-16; none pre-announces the switch. → 28 readable posts plus 8 deleted; the 'none pre-announces' conclusion stands.
- **partially_supported**: X Spaces office hours were held on 05-21, 05-29, 06-04 and 06-11. → 05-29, 06-04 and 06-11 have Spaces titles in Wayback JSON. The 05-21 session is inferred: 1925271753858900058 (2025-05-21T19:25:30Z) is a deleted Hivemind-link reply to 1925267445033639988. That parent is 'deleted by the Post author' and has no Wayback capture, so no 05-21 Spaces title was seen.
- **partially_supported**: V6.1→V7: 'updates: about 25 days of undated hints'. → About 24 days of dated but non-specific hints (2025-05-23 and 2025-05-29).

Flagged as unconfirmed by the verifier:
- '20 @midjourney posts were recovered for 2025-05-15 to 2025-06-16': the actual count is 28 readable plus 8 author-deleted (the researcher's own mj_tweets.json has 28).
- 'The Version article across 24 captures': CDX shows 26 captures with status 200 (21 canonical plus 5 utm variants).
- 'updates: about 25 days of undated hints': the hints are dated posts (2025-05-23T23:15:17Z, 24.2 days before the switch; 2025-05-29T23:03:25Z, 18.2 days before). They are 'undated' only in that neither gives a switch date.
- 'X Spaces sessions were held on 05-21': no 05-21 Spaces post or title was seen. This is inferred from a deleted Hivemind reply whose parent is deleted and uncaptured.
- 'the target slipped about 2 weeks' (V6 default): rests only on unreadable secondary Medium recap titles.
- 'V8.0 alpha retirement: informal from 2026-03-21': the 2026-03-21 item is a written updates.midjourney.com post, and a written 2026-04-14 decommission notice was omitted. The 57/100-day analogy is anchored on the X reply, not on the first written notice.
- '1,709 status IDs': a fresh CDX run today gives 1,710 (drift, not an error).

---

## G6 — track MJ2: The native Midjourney V8.x identity route is underexplored. The alpha changelog of 2026-08-20 (https://updates.midjourney.com/changelog-8-20-26/, re-fetched today) says '"Use Subject" no longer errors…

**Why it matters:** If V8.x has an identity-reference role or weight that nobody has documented, the MJ-native 'edit from anchor' option (Edit Model on the uploaded V7 canonical) could be a closer analogue to --oref --ow than the docs suggest. That changes how that row of the migration table is ranked.

**Gap-fill confidence:** high

### Answer
## MJ2 gap: "Use Subject", Edit Model weight, `--edit` on web, Relax and resolution (checked 2026-09-24)

**Bottom line:** "Use Subject" is not a hidden V8.x identity role. It is the alpha site's label for the old Omni Reference or Character Reference role. The Edit reference on the production web client has no strength control you can set. This is from the UI code: weights are switched off and the strength is fixed at 100 with a setter that does nothing. So the Edit-Model-from-anchor row in the migration table keeps its rank: no tunable weight exists.

**Evidence types used:**
- **Docs:** first-party documentation and posts.
- **UI code:** first-party JavaScript bundles and UI text taken from Wayback captures. These are first-party but they are UI copy and code, not documentation. Nothing below comes from a live test.

### (1) What "Use Subject" does
- **Where it appears in posts.** It is only in the 8/20 changelog, published 2026-08-21, under "Prompt bar and pills": "Use Subject" no longer errors out [c1].
  - All 92 posts in the updates sitemap were downloaded and searched. Only 3 contain "subject", and the other 2 are unrelated [c2].
  - That changelog also introduced "drop targets for each reference role" [c1].
- **Help center.** No help-center article (all 105, searched in full) mentions a subject reference role [c3].
- **Alpha bundle, 2026-08-23 (before the Edit Model launched on 8/27):**
  - Toggle labels: "Use subject" / "Use as subject". Unsupported-model message: "Subject references aren't supported on this model." [c4]
  - The toggle is wired to `isCharOrOmniRef`: `case"subject":if(g.isCharOrOmniRef)…` [c5].
  - Dropping an image on the subject role adds it to Omni References on versions 7, 8.1 and 8.2 (`w2`), and to Character References otherwise: `w2(B)?{…addToOmniReferences:!0}:{…addToCharacterReferences:!0}`, with `function w2(w){return w==="7"||w==="8.1"||w==="8.2"}` [c6].
  - The prompt serializer emits `--oref` then `--ow`. The V8.1 and V8.2 parsers in that bundle accept neither `--edit` nor `--oref` [c7].
- **Production site, 2026-09-21.** "Subject" is still the Omni drop label (`w==="OR"?"imagePrompts.dropToAddSubject"`). The Edit slot's drop label is "Reference" [c8].
- **Earlier alpha bundle, 2026-07-25.** It has no "Use subject" toggle, so the toggle appeared between 7/25 and 8/23 [c9].
- **Not checked:** no alpha bundle from after 8/27 is archived, so the alpha's current subject role was not inspected (see could_not_confirm).

### (2) Edit Model weight, strength or slider
**None exists in first-party docs, posts or production UI code.**
- **Production bundles, 8/28 and 9/21.** The "Attach to prompt" (Edit) slot is rendered with `disableWeights:!0,strengthHook:mF3`, and `mF3={strength:100,setStrength:()=>{}}` [c10].
  - The Omni slot, by contrast, has a live "Omni Strength" slider: default 100, minimum 1, maximum 1000 on V7 [c11].
- **Saved web settings.** They store strengths only for image prompt (0–3), style reference (0–1000), character reference (0–100) and Omni (0–1000). There is no Edit entry [c12].
- **Prompt parsers.** The V8.1 and V8.2 parsers accept `edit` and `ev`, but not `oref`, `ow`, `cref` or `cw`. The V7 parser accepts `oref` and `ow` but not `edit` [c13].
- **A new undocumented flag, `--ev`.**
  - UI label "Edit Variation"; it accepts only `1` or `2` ("--ev must be 1 or 2"). It has been in the production bundle since the 8/28 capture [c14].
  - No help-center article mentions it [c3].
  - It is a two-value switch, not a continuous weight. What it actually does is unknown.
- **Help-center screenshot.** The Edit Model article's Imagine-bar screenshot (uploaded 2026-08-28) shows an attached image with no slider. The Omni article's screenshot shows an inline Omni slider [c15].
- **Posts after 2026-09-24T01:59Z.** There are none. The newest sitemap and RSS entry is the 9/23 changelog, rechecked at 07:27Z today [c16].
- **"The weird slider" in the 9/23 changelog.** "The weird slider is fixed: 50% now means 228, not 1500" [c17] is the `--weird` slider, not an edit slider. `--weird` goes up to 3000 [c18], and 1500 is 50% of that (this link is an inference).

### (3) Whether `--edit <url>` works as web prompt text
- **Docs.** They give only the Discord how-to [c19]. The Parameter List lists `--edit` without naming a platform [c20].
- **Production UI code, 2026-09-21:**
  - The V8.1 and V8.2 web prompt parsers parse `--edit`, with a maximum of 4 images (`Ow=4`) and the errors "Edit Reference is missing" / "Edit Reference supports at most {max} images" [c21].
  - On submit, a prompt with Edit references goes out as `t:"edit_diffusion"`. Its prompt string is rebuilt as ` --edit <urls>` (plus `--ev`) [c22]. A prompt without them goes out as `t:"imagine"`.
  - Wrong-version flags produce "Version {version} doesn't support --{flag}." [c23].
- **Alpha changelog, 9/23:** "Pasted prompts keep their image prompts instead of turning into edit references" [c24]. So the alpha prompt bar turns pasted text into Edit references.
- **Verdict.** Per the UI code, midjourney.com treats `--edit` as prompt syntax on V8.1 and V8.2. Server acceptance was not tested live.
- **Risk for the repo's third-party client.** The web client sends edits as a separate `edit_diffusion` job type. That is a risk for any client that only sends `imagine` jobs (inference).

### (4) Relax mode and output pixel size
- **Relax.** No document says Relax is allowed or blocked for Edit Model jobs.
  - The GPU doc gives Edit Model costs, and its list of Relax limitations does not mention the Edit Model [c25].
  - In the production client, V8.x image jobs are downgraded from Turbo to Fast. Relax is downgraded only when the plan lacks it (`can_relax`). Nothing in the client blocks Relax for Edit jobs [c26].
  - What the server does is unknown.
- **Output pixel size.** There is no first-party figure for Edit Model output.
  - The Edit Model matches the first image's aspect ratio unless `--ar` is given, and it works with `--hd` [c19].
  - V8.2 at 1:1 is "HD images that are 2048 x 2048 pixels (px) and SD images that are 1024 x 1024px" [c27].
  - Inpainting and outpainting on HD images downscale the result to SD [c28]. The alpha editor, however, "can run in HD" [c24]. That is drift between the alpha site and the docs, not a strict contradiction.

### Contradictions
There are no new first-party vs first-party contradictions. The existing `--ow` minimum split (doc "between 1 and 1,000" vs launch post "0 to 100 to 1000") remains unresolved. The production UI slider's `minStrength:1` [c11] is UI code, not documentation, so it does not settle it.

### Claims
- [c1] FIRST-PARTY · 2026-08-21 (article:published_time 2026-08-21T16:48:58Z) · https://updates.midjourney.com/changelog-8-20-26/ — The only first-party post mentioning 'Use Subject' is the 8/20 alpha changelog (published 2026-08-21T16:48:58Z), under 'Prompt bar and pills'; the same post introduced per-reference-role drop targets. — ""Use Subject" no longer errors out … Dragging an image now opens the Images sidebar with drop targets for each reference role"
- [c2] FIRST-PARTY · accessed 2026-09-24 · https://updates.midjourney.com/sitemap-posts.xml — All 92 URLs in the updates sitemap were downloaded and full-text searched; only 3 contain 'subject'. The other two use it generically (video 'the subject moves'; sref 'subject leakage'). — "Much less likely to get any undesired 'subject leakage' into your images"
- [c3] FIRST-PARTY · accessed 2026-09-24 (latest article updated_at 2026-09-17T15:53:41Z) · https://docs.midjourney.com/api/v2/help_center/en-us/articles.json?per_page=100 — No help-center article (105 fetched via the Zendesk API and searched in full) contains 'Use Subject', a subject reference role, '--ev' or 'Edit Variation'. The only 'Subject' in prompting docs is generic prompt advice. Zendesk search for 'Use Subject' returns 97 loose keyword matches with no relevant hit. — "Subject: Who or what? (person, animal, character, location, object)"
- [c4] FIRST-PARTY · Wayback capture 2026-08-23T07:29:35Z (sha256 d89dabb2…) · https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js — The alpha.midjourney.com JS bundle captured 2026-08-23 contains the 'Use subject' role toggle and its unsupported-model message (UI copy, not documentation). — ""prompt.imageRef.useAsSubject":"Use as subject","prompt.imageRef.useSubject":"Use subject" … "imagesSidebar.subjectRefUnsupported":"Subject references aren't supported on this model.""
- [c5] FIRST-PARTY · Wayback capture 2026-08-23 · https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js — In that alpha bundle the 'subject' role toggle maps to the Character/Omni reference flag (isCharOrOmniRef); in Omni mode only 1 subject image is allowed. — "case"subject":if(g.isCharOrOmniRef)z(c);else if(w2(Z))U(c);else $(c);break … case"isCharOrOmniRef":return Z?1:20"
- [c6] FIRST-PARTY · Wayback capture 2026-08-23 · https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js — In the alpha bundle, dropping an image as 'subject' adds it to Omni References on V7/8.1/8.2 and to Character References on V6/6.1/niji 6. — "w2(B)?{skipImagePrompts:!0,addToOmniReferences:!0}:{skipImagePrompts:!0,addToCharacterReferences:!0} … function w2(w){return w==="7"||w==="8.1"||w==="8.2"}function pw(w){return w==="6.1"||w==="6"||w==="niji 6"}"
- [c7] FIRST-PARTY · Wayback capture 2026-08-23 · https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js — The alpha serializer on 2026-08-23 emits --oref/--ow for the omni role. That bundle has no --edit; its V8.1 and V8.2 parsers accept neither 'edit' nor 'oref'. — "if(w.omniRef.length>0&&Z)k+=` --oref ${wJ(w.omniRef)}`;if(w.ow!=null)k+=` --ow ${w.ow}`"
- [c8] FIRST-PARTY · Wayback capture 2026-09-21T04:20:52Z (sha256 4aededa6…) · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — In the production midjourney.com bundle (2026-09-21), 'Subject' is the drop label of the Omni (OR) slot; the Edit (ED) slot is labelled 'Reference'. — "id:w==="ED"?"imagePrompts.dropToAddReference":w==="OR"&&H.length>0?"imagePrompts.dropToSwapSubject":…w==="OR"?"imagePrompts.dropToAddSubject""
- [c9] FIRST-PARTY · Wayback capture 2026-07-25 (sha256 3b65aac4…) · https://web.archive.org/web/20260725123008id_/https://alpha.midjourney.com/public/out/clientSideEntry-sjxd3gs2.js — The alpha bundle captured 2026-07-25 has 'Drop to add Subject' but no 'useSubject' toggle string, so the toggle appeared between 7/25 and 8/23. — ""imagePrompts.dropToAddSubject":`Drop to add Subject`"
- [c10] FIRST-PARTY · Wayback capture 2026-09-21; same pattern (QA3) in 20260828123524 capture of clientSideEntry-s0gvcc8g.js · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — In production (captures 2026-08-28 and 2026-09-21), the Edit 'Attach to prompt' slot has weights disabled and a fixed strength of 100 whose setter is a no-op (UI code). — "category:"ED",title:J.formatMessage({id:"imagePrompts.attachToPrompt"}) … disableWeights:!0,strengthHook:mF3 … mF3={strength:100,setStrength:()=>{}}"
- [c11] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The production Omni slot keeps a real 'Omni Strength' slider: default 100, minimum 1, maximum 1000 on V7 (100 otherwise). — "defaultStrength:100,minStrength:1,maxStrength:D.effectiveVersion==="7"?1000:100,strengthHook:D.orStrengthHook,singularValue:!0,strengthTitle:J.formatMessage({id:"imagePrompts.omniStrength"})"
- [c12] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The web settings schema stores reference strengths only for image prompt, style reference, character reference and omni reference; there is no edit-reference strength. — "imageStrengths:c0({imagePrompt:j1(J1(Z3,0),3),styleReference:j1(J1(Z3,0),1000),characterReference:j1(J1(Z3,0),100),omniReference:j1(J1(Z3,0),1000)})"
- [c13] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The production web prompt parser dispatches by version. The V8.2 (zz0) and V8.1 (qz0) parsers accept 'edit' and 'ev' but not oref/ow/cref/cw; the V7 parser (Vz0) accepts oref/ow/cref but not edit. — "case"7":return Vz0(q,W,V);case"8.2":return zz0(W,V);case"8.1":return qz0(W,V) … function zz0(w,Z){…version:"8.2",…editRef:[],ev:null}"
- [c14] FIRST-PARTY · Wayback captures 2026-08-28 and 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — An undocumented V8.x parameter --ev ('Edit Variation') accepts only 1 or 2. It is present since the 2026-08-28 production capture. The UI never sets it, only parses and displays it. Its meaning is undocumented. — ""prompt.flags.ev":"Edit Variation" … "error.promptParser.evInvalid":"--ev must be 1 or 2" … else if(B==="ev"){if(Q.ev!=null)continue;if(Y!=="1"&&Y!=="2")return y0("error.promptParser.evInvalid");Q.ev=Y}"
- [c15] FIRST-PARTY · attachment created 2026-08-28T20:52:17Z · https://docs.midjourney.com/hc/article_attachments/48495453455117 — The Edit Model doc's UI screenshot (uploaded 2026-08-28) shows 'Attach to prompt' with an image attached and no slider. The Omni doc's UI screenshot (2025-05-01) shows an inline slider on the Omni Reference section. — "Attach to prompt — Edit or combine images, like "make this car red" or "put this hat on this cat" (screenshot text; web-ui-imagine-bar-edit.png, created_at 2026-08-28T20:52:17Z; compare omni-ref-ui https://docs.midjourney.com/hc/article_attachments/36285130549389 'Omni Reference — Use a person's lik"
- [c16] FIRST-PARTY · accessed 2026-09-24T07:27Z · https://updates.midjourney.com/sitemap-posts.xml — No updates post exists after the 9/23 changelog (published 2026-09-24T01:59:23Z); sitemap and RSS were rechecked at 2026-09-24T07:27Z. — "<lastmod>2026-09-24T01:59:23.000Z</lastmod>"
- [c17] FIRST-PARTY · 2026-09-24T01:59:23Z · https://updates.midjourney.com/alpha-changelog-9-23-26/ — The 9/23 alpha changelog's slider fix is under 'PROMPT BAR & PILLS' and says nothing about edit weight. The EDITING section adds v8.1/v8.2 edit types and HD edit canvases, with no weight. — "The weird slider is fixed: 50% now means 228, not 1500. … The editor now supports v8.1 and v8.2 edit types, and edit canvases can run in HD."
- [c18] FIRST-PARTY · updated 2026-07-27T16:18:41Z · https://docs.midjourney.com/hc/en-us/articles/32390120435085-Weird — The --weird range is 0–3000, so 1500 is its linear midpoint; this identifies the 'weird slider' as the Weird parameter (inference). — "By default, weird is set to 0, but you can add values up to 3000."
- [c19] FIRST-PARTY · updated 2026-09-04T18:46:32Z · https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model — The Edit Model doc documents the --edit prompt syntax only for Discord. Aspect ratio follows the first image unless --ar is given; the model is compatible with --hd; --raw is the only documented balance control. — "To use the Edit model in Discord, start by adding the --edit parameter to the end of your prompt, then pasting your image URL. … The Edit model will automatically try to match the aspect ratio of the first image you upload."
- [c20] FIRST-PARTY · updated 2026-09-01T17:18:30Z · https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List — The Parameter List lists --edit with no platform restriction and gives V8.1 SD/HD pixel sizes. — "Generate V8.1 images at higher resolution (2048px) using --hd or in standard resolution (1024px) using --sd Edit Model Create and modify images using written instructions and up to four reference images using --edit"
- [c21] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The production web prompt parser parses --edit from prompt text on V8.1 and V8.2, with a maximum of 4 references (UI code, not a live test). — "else if(B==="edit"){if(Q.editRef.length>0)continue;if(Y==="")return y0("error.promptParser.editRefMissing");…if(J.length>Ow)return y0("error.promptParser.editRefTooMany",{max:Ow});Q.editRef=J} … var b9="8.2",pc="niji 7",Ow=4"
- [c22] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The web client submits prompts that carry edit references as job type 'edit_diffusion' (otherwise 'imagine'), with the prompt string serialized as ' --edit <urls>' plus ' --ev'. The thumbnail label is 'Edit Reference (--edit)'. — "if("editRef"in Z0&&Z0.editRef.length>0)F={...A,t:"edit_diffusion",prompt:t3(Z0),…};else F={...A,t:"imagine",prompt:t3(Z0)} … if(w.editRef.length>0&&Z)Y+=` --edit ${GB(w.editRef)}`;if(w.ev!=null)Y+=` --ev ${w.ev}`"
- [c23] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — Typing a known flag that the selected version does not support produces a version error on the web (for example --oref on 8.2). — ""error.promptParser.versionDoesNotSupportFlag":"Version {version} doesn't support --{flag}.""
- [c24] FIRST-PARTY · 2026-09-24T01:59:23Z · https://updates.midjourney.com/alpha-changelog-9-23-26/ — The alpha prompt bar parses pasted prompt text into edit references, and alpha edit canvases can run in HD. — "Pasted prompts keep their image prompts instead of turning into edit references."
- [c25] FIRST-PARTY · updated 2026-08-28T23:10:23Z · https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo — The GPU Speed doc prices Edit Model SD and HD jobs, and its Relax limitations list does not mention the Edit Model (silence, not permission). — "Edit Model SD Prompt | 1 minute | Edit Model HD Prompt | 2.3 minutes … Permutation prompts, the repeat parameter, HD resolution videos, and Max Upscale (a legacy upscaler) are not available while using Relax mode."
- [c26] FIRST-PARTY · Wayback capture 2026-09-21 · https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js — The production client downgrades Turbo to Fast for V8/8.1/8.2 image jobs, and Relax to Fast only when the account lacks can_relax. There is no Edit-specific Relax downgrade in the client; server behaviour is unknown. — "!R&&(V.version==="8"||V.version==="8.1"||V.version==="8.2")&&G.speed==="turbo")G={...G,speed:"fast"};if(!R&&G.speed==="relaxed"&&!Z.firebase.abilities.can_relax)G={...G,speed:"fast"}"
- [c27] FIRST-PARTY · updated 2026-07-27T16:00:45Z · https://docs.midjourney.com/hc/en-us/articles/33329374594957-Image-Size-Resolution — V8.2 generic image sizes at 1:1 (not Edit-Model-specific). — "Midjourney version 8.2 creates HD images that are 2048 x 2048 pixels (px) and SD images that are 1024 x 1024px."
- [c28] FIRST-PARTY · updated 2026-09-01T17:26:08Z · https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — Inpainting and outpainting on HD images downscale the result to SD (main-site doc). This drifts from the later alpha note that edit canvases can run in HD. — "Using any of our inpainting or outpainting tools (Pan, Zoom Out, Edit/Vary Region) on HD images will downscale the resulting images to SD."
- [c29] FIRST-PARTY · 2026-08-27T23:32:15Z · https://updates.midjourney.com/edit-model-for-v8/ — The Edit Model launch post describes the web entry points and the Discord text syntax only; it mentions no weight. — "Drag images into the prompt bar under "attach to prompt" … Type --edit url... on Discord"
- [c30] secondary · Aug 28, 2026 · https://geekycuriosity.substack.com/p/midjourneys-new-editing-model-does — A secondary blog says that copying a web prompt back out shows the attached images behind --edit. This agrees with the UI-code finding but is not used as fact. — "Copy the prompt back out afterwards and you'll see your four images sitting behind a '--edit' parameter."

### Could not confirm
- What the alpha 'Use subject' toggle does after the Edit Model launch (2026-08-27). The only archived alpha bundle is from 2026-08-23, where subject means Omni (V7/8.1/8.2) or Character Reference (V6/6.1/niji 6). The bundle the alpha home page loaded on 2026-09-06 (clientSideEntry-y2kswza0.js) is not in Wayback, and the live site returns 403.
- How the 8/23 alpha actually routed an Omni 'subject' on V8.1/V8.2: its V8.x parsers do not accept --oref, and the effectiveVersion override was not traced.
- The meaning of the undocumented --ev ('Edit Variation', values 1|2). It may be the 'v8.1 and v8.2 edit types' from the 9/23 alpha changelog, or something else; no first-party text explains it and the UI never sets it.
- Whether the server accepts '--edit <url>' typed as prompt text. The UI code shows the web client parses it and serializes to it, but no live submission was made.
- Whether '--edit' works inside a plain 'imagine' job, as the repo's third-party midjourney.api client would likely send it. The web client uses a separate 'edit_diffusion' job type.
- Whether Edit Model jobs run in Relax mode on the server. Docs are silent; the client code does not downgrade Relax for edit jobs.
- Edit Model output pixel dimensions at non-1:1 aspect ratios, and whether edit outputs match the generic V8.2 SD/HD sizes. No first-party figure exists.
- Any first-party measurement or claim of face or identity fidelity for the Edit Model.
- Discord #alpha-news and #announcements were not read (they require auth).

### Verification (combined lens)
I re-checked every citation on 2026-09-24 between 07:31Z and 07:40Z. Sources: all 92 update posts, the sitemap and RSS, all 105 Zendesk articles, the attachment screenshots, and five Wayback JS bundles (alpha 7/25 and 8/23, production 8/27, 8/28 and 9/21). The raw-gzip hashes of the three hashed bundles match the researcher's.

Every verbatim quote in claims c1–c30 was found. There are no hallucinated versions, dates, prices or sizes.

Verdicts:
- 26 claims supported.
- c6, c8 and c24 partially supported. c6 and c8 leave out that V8.x Omni/"subject" references are silently submitted as V7. c24 misreads a bug fix as a feature.
- c30 is secondary only.
- The bottom line is partially supported.

The most important missed fact is in the same 8/23 alpha bundle. On V8.1/V8.2, "Use subject" rewrote the job to V7 with omni refs and showed the message "Submitted with v7 — omni references are v7-only". Production 9/21 still silently forces V7 when character refs are present on V8.x, and its Omni ("Subject") slot is V7-only. So "Use Subject" never was a V8 identity route.

Other missed first-party facts:
- The Edit Model doc says Edit references replace Omni and Character Reference, on V8.1 and V8.2 only.
- The V8.2 edit model was updated in place on 2026-08-29 with no version bump. This matters for a face graph that cannot be changed back.
- The Version doc chart marks Relax as supported for V8.1/V8.2 at version level only; no doc speaks to Edit jobs.
- The UI copy for --ev is inconsistent: English "Edit Variation", Swedish "edit preset".
- An undocumented --dref/--dw Depth Reference role exists in the web parsers.

No first-party vs first-party contradiction was found beyond the known --ow 1–1,000 vs 0–1000 split.

Still unresolved: the alpha subject role after 8/27 (no archived bundle), server acceptance of --edit and Relax for edit jobs, edit output pixel sizes, and what --ev means.

Scratch files: <session scratch, not kept>/verify-mj2gap/

Checks not marked "supported":
- **partially_supported**: Dropping as 'subject' adds to Omni on V7/8.1/8.2 and Character on V6/6.1/niji 6. → On 8/23 alpha, 'Use subject' on V8.1/V8.2 submitted a V7 job with omni refs (UI toast 'Submitted with v7 — omni references are v7-only'); source https://web.archive.org/web/20260823072935id_/https://alpha.midjourney.com/public/out/clientSideEntry-9rg1vdzc.js
- **partially_supported**: Prod 2026-09-21: 'Subject' is the Omni (OR) drop label; Edit (ED) slot labelled 'Reference'. → https://web.archive.org/web/20260921042052id_/https://www.midjourney.com/public/out/clientSideEntry-rx83xj3k.js (raw sha256 4aededa6bd19..., matches). Strings present: 'id:w==="ED"?"imagePrompts.dropToAddReference":w==="OR"&&H.length>0?"imagePrompts.dropToSwapSubject"' and 'w==="OR"?"imagePrompts.dr
- **partially_supported**: The alpha prompt bar parses pasted prompt text into edit references; alpha edit canvases can run in HD. → The 9/23 changelog reports a fix: pasted prompts' image prompts no longer get converted into edit references. It does not document --edit parsing on alpha.
- **secondary_only**: Substack says copied web prompts show images behind --edit. → https://geekycuriosity.substack.com/p/midjourneys-new-editing-model-does (Aug 28, 2026): 'Copy the prompt back out afterwards and you'll see your four images sitting behind a `--edit` parameter.' Secondary; consistent with UI code.
- **partially_supported**: 'Use Subject' is the alpha label for old Omni/Character role; Edit reference has no settable strength; 'no tunable weight exists'. → First half supported as of the 8/23 alpha capture only (no post-8/27 alpha bundle archived; alpha home 20260906211419 loads clientSideEntry-y2kswza0.js, CDX returns [] for it). No-settable-strength supported for the web client (mF3 no-op, no edit key in imageStrengths, no edit-weight flag in zz0/qz0

Flagged as unconfirmed by the verifier:
- (none)

---

## G7 — track MJ4: There is a cross-track licensing conflict in the identity gate that any migration pilot would use. MJ4 disqualifies InsightFace models ('available for non-commercial research purposes only', insightfa…

**Why it matters:** The one-way-door rule says to A/B about 10 transitions and 10 idles and audit face drift before re-rendering 251 clips. That audit needs an identity metric the project may legally use and that is meaningful on Old-Master-style painted faces. Otherwise the go/no-go on any vendor cannot be measured.

**Gap-fill confidence:** high

### Answer
## MJ4 gap: an identity metric the project may legally use on painted faces

**Verdict:** Part of the gap is closed and part is not.
- **Licence side: closed.** buffalo_l cannot be used, even for internal QA. There is a clean replacement stack.
- **Accuracy on painted faces: not closed.** No source evaluates AuraFace, SFace or dlib on paintings. The only published painting results are for InsightFace-family or other models, and they show large degradation.

### (1) The InsightFace buffalo_l licence
- **Licence text.** The main README says "the models trained with these data ... are available for non-commercial research purposes only" [c1]. The python-package README repeats this [c2]. The model-zoo README says "ALL models are available for non-commercial research purposes only" [c3].
- **No licence file in the pack.** buffalo_l.zip (release asset updated 2026-09-03) has no licence file. It holds det_10g, w600k_r50, 1k3d68, 2d106det and genderage [c4]. The new raccoon packs are signed `"grant": "non-commercial"` [c5].
- **Training data.** The recogniser is ResNet50@WebFace600K [c6]. WebFace260M's rules say it "can only be used for academic research" [c7].
- **Internal QA is not covered.** A user asked about buffalo_l for login in "internal applications only". The maintainer Jia Guo (nttstar) replied: "No, all open source models from our repo are for non-commercial research purposes only" [c8]. Asked about detection models, he said: "ALL models." [c9]. My inference: a gate that decides which clips reach a permanent public wall is production use, not research. The licence has no carve-out for internal use.
- **The detector is also restricted.** verify.py:204 calls `FaceAnalysis(name="buffalo_l")`, so the gate also uses InsightFace's non-commercial SCRFD detector [c10]. Swapping only the recogniser does not fix this.
- **Commercial licence.** Contact recognition-oss-pack@insightface.ai for buffalo_l [c11]. insightface.ai lists "Face recognition model commercial license (buffalo_l, antelopev2, buffalo_s, etc.)" at "Custom" pricing [c12]. No price is published.

### (2) Commercially licensed alternatives
| Model | Weight licence (checked at the weight host) | Published benchmarks | Caveat |
|---|---|---|---|
| fal/AuraFace-v1 `glintr100.onnx` | apache-2.0 [c13] | LFW 0.99650, CFP-FP 0.95186, AGEDB 0.96100, CALFW 0.94700, CPLFW 0.90933 [c14]. Scores below ArcFace [c15] | See the three notes below this table [c16][c17][c18] |
| OpenCV Zoo SFace 2021dec | Apache-2.0 on GitHub and the HF mirror, same SHA-256 `0ba9fbfa…` [c19][c20] | LFW 0.9940 (zoo) vs 99.60% (tutorial), a conflict. Cosine threshold 0.363 [c21][c22] | Upstream zhongyy/SFace has no licence [c23]. The paper trains on CASIA-WebFace, VGGFace2 and MS-Celeb-1M [c23]. A July 2026 issue asking about commercial use and training data has no maintainer reply [c24]. Already ships in OpenCV, so verify.py needs no new dependency |
| OpenCV Zoo YuNet detector | MIT [c25] | WIDER Face AP (see contradictions) | Detects faces of "around 10x10 to 300x300" pixels, so large portraits must be downscaled [c25] |
| dlib_face_recognition_resnet_model_v1 | Public domain / CC0 [c26] | LFW 0.993833 (the README calls it "mean error") [c26] | Pair it with shape_predictor_5. The 68-point predictor cannot be used commercially [c27] |
| AWS Rekognition CompareFaces | Commercial API | None published. SimilarityThreshold defaults to 80 [c28] | Says nothing about non-photographic faces |

**AuraFace notes:**
- **Four of its files are InsightFace's own.** `scrfd_10g_bnkps`, `2d106det`, `genderage` and `1k3d68` have SHA-256 hashes identical to buffalo_l and antelopev2 [c16]. The README's `FaceAnalysis(name="auraface")` therefore runs InsightFace's non-commercial detector.
- **Provenance question unanswered.** A 2025-09-29 question about where `glintr100.onnx` came from is still unanswered, as is a separate question about commercial use [c17].
- **Not a drop-in for ArcFace.** fal says it is not in ArcFace's latent space [c18], so verify.py's 0.55 threshold does not carry over. No threshold is published.

**Disqualified:**
- EdgeFace: code is BSD-3 but the HF weights are cc-by-nc-sa-4.0 [c29].
- CVLface/AdaFace HF weights: no licence, and the card says "follow the license of the training dataset" [c30].
- StyleID: "non-commercial research use" [c31].
- InsightFace raccoon packs: non-commercial [c5].

**Clean stack for the pilot (my inference):** YuNet (MIT) + 5-point alignment + SFace (Apache) or AuraFace `glintr100.onnx` only. Recalibrate the threshold on the project's own accepted stills. Or buy the InsightFace licence.

### (3) Evaluations on paintings and artwork
- **ArtFace (Idiap, arXiv 2508.20626, 2025-08-28).** Historical Faces dataset: 766 paintings, 210 sitters.
  - AntelopeV2 (IResNet100 on Glint360k, used as-is): EER 14.0%, TAR@0.1%FAR 29.9%, TAR@1%FAR 55.1%.
  - A commercial off-the-shelf system: 12.6% / 34.3% / 58.1%.
  - Best fusion: EER 9.9%, TAR@1%FAR 65.9% [c32][c33].
- **Huber et al., ICPR 2022.** Built the dataset: "over 760 ... paintings of over 250 different artists", 210 identities [c34]. I could not retrieve its results.
- **Gupta et al., ICME 2018.** Hypothesis-testing accuracy: VGG-Art 91.253% vs VGG-Face 87.29% [c35].
- **StyleID (SIGGRAPH 2026 / TOG, arXiv 2604.21689).**
  - Photo-trained encoders "exhibit severe brittleness under stylization ... mistake changes in texture or color palette for identity drift" [c36].
  - ArcFace TPR@FPR=1e-2: 0.7649 Cross-ID, 0.8511 Cross-Style, 0.3721 Cross-Method [c37].
  - AntelopeV2: TPR 0.7756, AUROC 0.9566 on StyleBench-H [c38].
- **Stylized-Face (ICCV 2025).** 80 styles, including "Classical Art Styles". IResNet-50 trained on Glint360k: TAR@FAR 1e-2 / 1e-3 / 1e-4 = 95.0 / 87.0 / 74.7. Trained on MS1MV3: 85.1 / 68.0 / 49.7 [c39].
- **iCartoonFace (arXiv 1907.13394).** "ArcFace performs over 95% on all human datasets while only 83.34% on cartoon faces" [c40].
- **What none of these test.** No source tests AuraFace, SFace or dlib on paintings. No source tests re-render drift from a single generator anchor, which is this project's actual case.

### Claims
- [c1] FIRST-PARTY · last commit 2026-09-08 (317d3349); accessed 2026-09-24 · https://github.com/deepinsight/insightface/blob/master/README.md — InsightFace main README: models trained with InsightFace data are for non-commercial research only; applies to manual and auto-downloaded models — "The training data containing the annotation (and the models trained with these data) are available for non-commercial research purposes only. Both manual-downloading models from our github repo and auto-downloading models with our python-library follow the above license policy(which is for non-comme"
- [c2] FIRST-PARTY · last commit 2026-09-08; accessed 2026-09-24 · https://github.com/deepinsight/insightface/blob/master/python-package/README.md — python-package README (InsightFace 2.0): library MIT, pretrained models non-commercial research only — "The pretrained models provided with this library are for non-commercial research only, whether downloaded automatically or manually."
- [c3] FIRST-PARTY · last commit 2026-09-09 (4559ddfe); accessed 2026-09-24 · https://github.com/deepinsight/insightface/blob/master/model_zoo/README.md — model_zoo README: all models non-commercial research only — "ALL models are available for non-commercial research purposes only."
- [c4] FIRST-PARTY · asset updated 2026-09-03; release published 2026-09-03 · https://github.com/deepinsight/insightface/releases/tag/model-zoo — buffalo_l.zip in the model-zoo release contains five ONNX files and no licence file (listed via ZIP central directory over HTTP range requests) — "genderage.onnx, 2d106det.onnx, det_10g.onnx, 1k3d68.onnx, w600k_r50.onnx (buffalo_l.zip, 288621354 bytes)"
- [c5] FIRST-PARTY · asset updated 2026-09-03 · https://github.com/deepinsight/insightface/releases/download/model-zoo/raccoon_l.zip — InsightFace 2.0 raccoon_s / raccoon_l packs ship a signed MODEL.LICENSE granting non-commercial use only — ""license_id": "raccoon_l-public-v1", "issuer": "InsightFace", "grant": "non-commercial", "valid_from": "2026-08-29T00:00:00Z""
- [c6] FIRST-PARTY · last commit 2026-09-08; accessed 2026-09-24 · https://github.com/deepinsight/insightface/blob/master/python-package/docs/model_zoo.md — buffalo_l = SCRFD-10GF detector + ResNet50@WebFace600K recogniser; LFW 99.83, CFP-FP 99.33, AgeDB-30 98.23 — "| **buffalo_l** | SCRFD-10GF | ResNet50@WebFace600K | 2d106 & 3d68 | Gender&Age | 326MB |"
- [c7] FIRST-PARTY · Wayback snapshot 2024-09-19 (live site DNS fails 2026-09-24) · https://web.archive.org/web/20240919071423/https://www.face-benchmark.org/download.html — WebFace260M (and subsets) dataset rules: academic research only, no commercial use — "1. This dataset and its subsets can only be used for academic research. 2. Applicants are not allowed to use this dataset and its subsets for any commercial purposes."
- [c8] FIRST-PARTY · 2023-12-03 (question: 'login purpose(internal applications only)') · https://github.com/deepinsight/insightface/issues/2486 — InsightFace maintainer (nttstar = Jia Guo, named maintainer) says buffalo_l may not be used in production even for internal-only applications — "No, all open source models from our repo are for non-commercial research purposes only."
- [c9] FIRST-PARTY · 2024-07-28 · https://github.com/deepinsight/insightface/issues/2469 — Maintainer confirms the non-commercial restriction covers detection models too, not only inswapper — "[@commenter] ALL models."
- [c10] FIRST-PARTY · local last commit 2026-07-11; accessed 2026-09-24 · https://github.com/Wenjix/living-portraits/blob/master/pipeline/verify.py — Project identity gate loads the full buffalo_l pack (detector + recogniser) with threshold 0.55; local and upstream match — "app = FaceAnalysis(name="buffalo_l") ... IDENTITY_THRESHOLD = 0.55     # InsightFace cosine: same-actor floor (ArcFace embeddings)"
- [c11] FIRST-PARTY · '2025-11-24 Update' section; accessed 2026-09-24 · https://github.com/deepinsight/insightface/blob/master/README.md — Commercial licensing contact for open-sourced recognition models such as buffalo_l — "2. For open-sourced face recognition models (e.g., buffalo_l package), please contact recognition-oss-pack@insightface.ai for licensing."
- [c12] FIRST-PARTY · accessed 2026-09-24 · https://www.insightface.ai/ — insightface.ai sells a commercial licence covering buffalo_l/antelopev2 at unpublished custom pricing — "Model Licensing Custom Commercial licensing for face recognition and face swapping models Face recognition model commercial license (buffalo_l, antelopev2, buffalo_s, etc.)"
- [c13] FIRST-PARTY · lastModified 2024-08-26 · https://huggingface.co/fal/AuraFace-v1 — AuraFace-v1 HF repo is tagged Apache-2.0 and states it was trained for commercial use — "license: apache-2.0 ... has been trained on commercially and publicly available data sources to enable its usage in commercial setting"
- [c14] FIRST-PARTY · lastModified 2024-08-26 · https://huggingface.co/fal/AuraFace-v1/raw/main/README.md — AuraFace published benchmarks; the model card says nothing about non-photographic or painted faces — "LFW: 0.99650 - CFP-FP: 0.95186 - AGEDB: 0.96100 - CALFW: 0.94700 - CPLFW: 0.90933"
- [c15] FIRST-PARTY · 2024-08-26 (HF community article) · https://huggingface.co/blog/isidentical/auraface — fal staff (isidentical, fal HF org member) state that AuraFace underperforms original ArcFace; comparison table given — "AuraFace does not match the performance of the original ArcFace ... CFP-FP 95.18 98.87 AGEDB 96.10 98.38 CALFW 94.70 96.10 CPLFW 90.93 93.43"
- [c16] FIRST-PARTY · HF LFS oids vs SHA-256 computed 2026-09-24 from model-zoo zips · https://huggingface.co/api/models/fal/AuraFace-v1/tree/main — Four of AuraFace-v1's six ONNX files are byte-identical to InsightFace's non-commercial buffalo_l/antelopev2 files; only glintr100.onnx differs (260,694,151 vs 260,665,334 bytes) — "scrfd_10g_bnkps.onnx 16923827 5838f7fe053675b1c7a08b633df49e7af5495cee0493c7dcf6697200b85b5b91 (== InsightFace det_10g.onnx sha256 5838f7fe...); 2d106det f001b856...; genderage 4fde69b1...; 1k3d68 df5c06b8... all identical"
- [c17] FIRST-PARTY · opened 2025-09-29; last comment 2026-04-13; no fal reply · https://huggingface.co/fal/AuraFace-v1/discussions/8 — Public requests to fal for glintr100.onnx provenance and commercial-use confirmation remain unanswered by fal — "Are the glintr100.onnx weights in this repo your own original weights ... and not copied from or derived from InsightFace's antelopev2 / glintr100 ... ? (follow-ups 2026-01-06, 2026-04-13: 'Can you please reply.')"
- [c18] FIRST-PARTY · 2024-08-26 · https://huggingface.co/fal/AuraFace-v1/discussions/3 — fal org member Warlord-K says AuraFace is not in ArcFace's latent space, so ArcFace thresholds do not transfer — "No, This does not operate in the same latent space as ArcFace since its trained on a different set of commercial images."
- [c19] FIRST-PARTY · last dir commit 2024-11-06; accessed 2026-09-24 · https://github.com/opencv/opencv_zoo/blob/main/models/face_recognition_sface/README.md — OpenCV Zoo SFace directory is Apache-2.0 — "All files in this directory are licensed under [Apache 2.0 License](./LICENSE)."
- [c20] FIRST-PARTY · lastModified 2025-06-20 · https://huggingface.co/opencv/face_recognition_sface — HF mirror opencv/face_recognition_sface has an Apache 2.0 LICENSE and the same weight hash as the GitHub LFS pointer — "face_recognition_sface_2021dec.onnx 38696353 0ba9fbfa01b5270c96627c4ef784da859931e02f04419c829e83484087c34e79; LICENSE: Apache License Version 2.0"
- [c21] FIRST-PARTY · accessed 2026-09-24 · https://github.com/opencv/opencv_zoo/blob/main/models/face_recognition_sface/README.md — OpenCV Zoo reports SFace LFW accuracy 0.9940 using its own eval tool (YuNet-detected boxes) — "| SFace       | 0.9940   |"
- [c22] FIRST-PARTY · last commit 2022-01-10 · https://github.com/opencv/opencv/blob/4.x/doc/tutorials/dnn/dnn_face/dnn_face.markdown — OpenCV tutorial gives SFace per-benchmark accuracy and cosine thresholds — "| LFW      | 99.60%   | 1.128              | 0.363              | ... | CFP-FP   | 94.80%   | 1.253              | 0.212              |"
- [c23] FIRST-PARTY · pushed 2021-07-27 · https://github.com/zhongyy/SFace — Upstream SFace repo has no licence; the paper trained on CASIA-WebFace, VGGFace2 and MS-Celeb-1M — "Extensive experiments of models trained on CASIA-WebFace, VGGFace2, and MS-Celeb-1M databases (GitHub license: null)"
- [c24] FIRST-PARTY · opened 2026-07-22; updated 2026-09-17; state OPEN · https://github.com/opencv/opencv_zoo/issues/313 — Open issue asking which dataset trained the SFace 2021dec weights and whether commercial use is allowed; only non-maintainer comments — "Commercial-use and training-data clarification for SFace 2021dec ONNX weights"
- [c25] FIRST-PARTY · accessed 2026-09-24 · https://github.com/opencv/opencv_zoo/blob/main/models/face_detection_yunet/README.md — YuNet detector is MIT-licensed and trained to detect faces of about 10x10 to 300x300 pixels — "This model can detect **faces of pixels between around 10x10 to 300x300** due to the training scheme. ... All files in this directory are licensed under [MIT License](./LICENSE)."
- [c26] FIRST-PARTY · last commit 2025-05-28 · https://github.com/davisking/dlib-models/blob/master/README.md — dlib face-recognition model is released into the public domain (repo CC0-1.0); LFW figure given — "anyone can do whatever they want with these model files as I've released them into the public domain ... obtains a mean error of 0.993833 with a standard deviation of 0.00272732 on the LFW benchmark"
- [c27] FIRST-PARTY · last commit 2025-05-28 · https://github.com/davisking/dlib-models/blob/master/README.md — dlib 68-point landmark models cannot be used commercially (iBUG 300-W licence) — "The license for this dataset excludes commercial use and Stefanos Zafeiriou ... asked me to include a note here saying that the trained model therefore can't be used in a commercial product."
- [c28] FIRST-PARTY · accessed 2026-09-24 · https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html — AWS Rekognition CompareFaces is a commercial verification API with default similarity cut-off 80; no accuracy figures or non-photo statement in the API reference — "By default, only faces with a similarity score of greater than or equal to 80% are returned in the response."
- [c29] FIRST-PARTY · lastModified 2026-05-21 · https://huggingface.co/api/models/Idiap/EdgeFace-Base — EdgeFace weights on HF are non-commercial even though the GitHub code is BSD-3 — "license: cc-by-nc-sa-4.0"
- [c30] FIRST-PARTY · lastModified 2025-07-17 · https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m — CVLface AdaFace HF weights carry no licence and defer to training-dataset licences (WebFace = academic only) — "Please cite the orignal paper and follow the license of the training dataset."
- [c31] FIRST-PARTY · README last commit 2026-08-16; HF card license: other · https://github.com/kwanyun/StyleID — StyleID model is non-commercial research only — "StyleID is released for non-commercial research use."
- [c32] FIRST-PARTY · v1 2025-08-28 (ArtMetrics @ ICCV 2025, non-archival) · https://arxiv.org/abs/2508.20626 — ArtFace: face recognition trained on photos struggles on paintings; Historical Faces dataset = 766 paintings, 210 sitters; AntelopeV2 used as base — "while traditional facial recognition models perform well on photographs, they struggle with paintings due to domain shift and high intra-class variation"
- [c33] FIRST-PARTY · v1 2025-08-28 · https://arxiv.org/html/2508.20626v1 — ArtFace Table 3 on paintings: COTS EER 12.6% / TAR@0.1%FAR 34.3% / TAR@1%FAR 58.1%; IResNet100(AntelopeV2)-Base 14.0% / 29.9% / 55.1%; best fusion 9.9% / 39.7% / 65.9% — "COTS FR system | 12.6% | 34.3% | 58.1% ... IResNet100-Base | 14.0% | 29.9% | 55.1% ... CLIP-LoRA + IResNet100-Base + IResNet100-Tuned | 9.9% | 39.7% | 65.9%"
- [c34] FIRST-PARTY · repo pushed 2022-08-02 · https://github.com/marcohuber/HistoricalFaces/blob/main/README.md — Huber et al. ICPR 2022 Historical Faces dataset composition (results not retrieved) — "The dataset consists of over 760 authentic historic portrait paintings of over 250 different artists. 210 different identities are present in the dataset."
- [c35] FIRST-PARTY · ICME 2018; author-hosted PDF (path 2019-02); accessed 2026-09-24 · https://vlg.engr.ucr.edu/sites/default/files/2019-02/ICME.pdf — Gupta et al. ICME 2018: style-transfer fine-tuned VGG-Art beats VGG-Face on Renaissance portrait verification (hypothesis-testing accuracy) — "Hypothesis testing on portrait validation dataset with VGG-Art model has shown accuracy of 91.253 % whereas the accuracy of VGG-Face was found to be 87.29%."
- [c36] FIRST-PARTY · v1 2026-04-23 (SIGGRAPH 2026 / ACM TOG) · https://arxiv.org/abs/2604.21689 — StyleID: identity encoders trained on photos are brittle under stylization, including paintings — "current identity encoders, which are typically trained and calibrated on natural photographs, exhibit severe brittleness under stylization. They often mistake changes in texture or color palette for identity drift or fail to detect geometric exaggerations."
- [c37] FIRST-PARTY · v1 2026-04-23 · https://arxiv.org/html/2604.21689v1 — StyleID Table 1 (StyleBench-H, TPR@FPR=1e-2 / AUROC): ArcFace Cross-ID 0.7649/0.9418, Cross-Style 0.8511/0.9690, Cross-Method 0.3721/0.8697 — "ArcFace | 0.7649 | 0.7925 | 0.7266 | 0.6449 | 0.9418 | | 0.8511 | 0.8511 | 0.7739 | 0.6729 | 0.9690 | | 0.3721 | 0.5031 | 0.5000 | 0.5000 | 0.8697"
- [c38] FIRST-PARTY · v1 2026-04-23 · https://arxiv.org/html/2604.21689v1 — StyleID Table 10: AntelopeV2 on StyleBench-H TPR 0.7756 / Acc 0.7871 / AUROC 0.9566; on SKSF-A 0.7633 / 0.5597 / 0.9704 (text says frozen encoder; caption says fine-tuned) — "AntelopeV2 | 0.7756 | 0.7871 | 0.9566 | 0.7633 | 0.5597 | 0.9704"
- [c39] FIRST-PARTY · ICCV 2025 open access; accessed 2026-09-24 · https://openaccess.thecvf.com/content/ICCV2025/papers/Peng_Stylized-Face_A_Million-level_Stylized_Face_Dataset_for_Face_Recognition_ICCV_2025_paper.pdf — Stylized-Face (ICCV 2025): photo-trained IResNet-50 degrades on stylized faces (80 styles incl. Classical Art / renaissance); TAR@FAR 1e-2/1e-3/1e-4 — "MS1MV3 [13] 85.1 68.0 49.7 / Gint360k [6] 95.0 87.0 74.7 ... there is a significant performance degradation compared to real face scenarios"
- [c40] FIRST-PARTY · v3 2020-06-27 · https://arxiv.org/pdf/1907.13394v3 — iCartoonFace: ArcFace accuracy drops from >95% on human datasets to 83.34% (Rank@1) on cartoon faces — "For example, the ArcFace performs over 95% on all human datasets while only 83.34% on cartoon faces."

### Could not confirm
- Accuracy of AuraFace-v1, SFace or dlib on paintings, Old-Master-style or other non-photographic faces: no first-party or peer-reviewed evaluation found. The AuraFace card and blog say nothing on it.
- Any evaluation of a face metric on this project's actual case: re-render drift of one generator-made character from a single anchor. All painting studies measure cross-artist sitter identity or diffusion stylization.
- Provenance and training data of AuraFace glintr100.onnx: fal has not answered HF discussion #8 (opened 2025-09-29) or #9.
- Training dataset of the OpenCV Zoo SFace 2021dec weights: opencv_zoo issue #313 has no maintainer answer. Upstream zhongyy/SFace has no licence.
- A cosine threshold for AuraFace: none is published. verify.py's 0.55 is buffalo_l-specific and does not transfer (different latent space).
- InsightFace commercial licence price for buffalo_l: listed only as 'Custom'.
- Numeric results of Huber et al. ICPR 2022: the IEEE/CSDL pages would not render and Semantic Scholar returned 429. Only the dataset description was confirmed.
- The weight licence for timesler/facenet-pytorch: the repo is MIT, but no separate weight licence was found and the VGGFace2 / CASIA-WebFace terms were not checked. Not recommended.
- Whether YuNet (trained on WIDER Face photos) reliably detects faces in painted portraits: not evaluated in any source found. This matters because verify.py fails a clip when no face is detected.

### Verification (combined lens)
All 40 cited claims were re-checked against their first-party sources today. 35 are supported verbatim. That includes the InsightFace licence text, maintainer replies #2486/#2469, the buffalo_l ZIP contents and hashes, the four AuraFace files byte-identical to InsightFace (re-hashed today, 1k3d68 included), the unanswered fal provenance threads, the SFace/YuNet licences and hashes, AWS CompareFaces, and every painting/stylization metric (ArtFace, Gupta ICME 2018, StyleID, Stylized-Face, iCartoonFace). Five are partially supported: c20 (HF SFace has no licence tag), c22 (wrong commit date), c26 (dlib training data omitted), c29 (EdgeFace GitHub ships weights under BSD-3), and A2 (OpenCV ships the API, not the weights). The main error is the verdict 'Licence side: closed / clean replacement stack'. YuNet is trained on WIDER FACE (CC BY-NC-ND), and dlib's recogniser is about half VGG Face (CC BY-NC 4.0). SFace and AuraFace training data are unresolved. So no proposed stack is clean by the answer's own training-data standard, and a paid InsightFace licence is the only fully cleared route. A first-party EdgeFace licence conflict (GitHub BSD-3 checkpoints vs HF CC BY-NC-SA) went unreported. Also missed: LivePortrait's LICENSE says InsightFace detectors must be removed for commercial use, while the project's installer pulls buffalo_l det_10g/2d106det from the MIT-tagged KlingTeam/LivePortrait mirror and antelopev2 from an untagged third-party mirror. Other misses: InsightFace's pre-licence Enterprise Evaluation Mode, the uncited arXiv 2609.04151 (the closest analogue: generative identity drift measured with antelopev2), and the first-party proof that WebFace600K is a WebFace260M subset. No invented version numbers or figures were found. The one date error is c22 (2022-02-22, not 2022-01-10).

Checks not marked "supported":
- **partially_supported**: HF mirror opencv/face_recognition_sface has an Apache LICENSE and the same weight hash → HF tree: face_recognition_sface_2021dec.onnx 38696353, oid 0ba9fbfa...4e79, which matches the GitHub LFS pointer 'oid sha256:0ba9fbfa01b5270c96627c4ef784da859931e02f04419c829e83484087c34e79 size 38696353'. The LICENSE file is Apache 2.0. However, the HF model metadata has NO licence tag (cardData.li
- **partially_supported**: OpenCV tutorial: SFace LFW 99.60%, cosine threshold 0.363; last commit 2022-01-10 → https://raw.githubusercontent.com/opencv/opencv/4.x/doc/tutorials/dnn/dnn_face/dnn_face.markdown L29: '| LFW      | 99.60%   | 1.128              | 0.363              |' and L33 CFP-FP 94.80% / 0.212. The quote is correct, but the source_date is wrong: the latest commit touching the file is 899b4d14
- **partially_supported**: dlib face-recognition model is public domain (CC0); LFW 0.993833 → https://raw.githubusercontent.com/davisking/dlib-models/master/README.md: 'anyone can do whatever they want with these model files as I've released them into the public domain' and 'obtains a mean error of 0.993833 ... on the LFW benchmark'. Repo licence CC0-1.0; last commit 2025-05-28. The answer o
- **partially_supported**: EdgeFace code is BSD-3 but HF weights are cc-by-nc-sa-4.0 → HF API: Idiap/EdgeFace-Base license cc-by-nc-sa-4.0, lastModified 2026-05-21; EdgeFace-XXS also cc-by-nc-sa-4.0. The HF card says 'EdgeFace is released under [CC BY-NC-SA 4.0]' and 'EdgeFace-Base was trained on [Webface260M] dataset (12M and 4M subsets)'. The answer omits that the GitHub repo otrosh
- **contradicted**: Answer verdict: 'Licence side: closed ... There is a clean replacement stack' (YuNet MIT + SFace Apache or AuraFace glintr100 + dlib public domain) → The weight licences are permissive, but the answer applies its training-data test (SFace, CVLface, EdgeFace, buffalo_l/WebFace260M) inconsistently. YuNet is trained on WIDER Face (https://raw.githubusercontent.com/ShiqiYu/libfacedetection.train/master/README.md: 'YuNet face detection training on WID
- **partially_supported**: SFace 'already ships in OpenCV, so verify.py needs no new dependency' → The API ships: the OpenCV tutorial says 'we introduce cv::FaceDetectorYN class ... and cv::FaceRecognizerSF class' with 'Compatibility | OpenCV >= 4.5.4'. The weights do not: 'There are two models (ONNX format) pre-trained and required for this module', to be fetched from opencv_zoo. verify.py alrea

Flagged as unconfirmed by the verifier:
- c22 source_date 'last commit 2022-01-10' is wrong: the latest commit touching opencv/doc/tutorials/dnn/dnn_face/dnn_face.markdown is 899b4d14 at 2022-02-22T19:55:26Z.
- Answer's EdgeFace line ('code is BSD-3 but the HF weights are cc-by-nc-sa-4.0') implies the weights exist only on HF. The GitHub repo also ships the weights under BSD-3. The claim is incomplete, though nothing in it is invented.
- c20 implies the HF mirror is licence-tagged Apache. The HF metadata has no licence tag; only the LICENSE file and README line say Apache 2.0.
- Overall 'confidence: high' and 'Licence side: closed' are not supported. Training-data licences for YuNet (WIDER FACE CC BY-NC-ND) and dlib (VGG Face CC BY-NC 4.0) were not checked, and SFace and AuraFace provenance is unresolved.

---

## G8 — track A: Lip-sync timing for the chosen voices is unresolved across tracks (also affects B1 and B2). B1 picks VoxCPM2 and B2 picks Chatterbox, and neither emits phoneme timings. A's only GPL-free duration rout…

**Why it matters:** Whichever voice is picked, visemes need timings. If the aligner chain or its English model carries a non-commercial or GPL component, lip-sync falls back to the letter-fabricated visemes, or forces a Kokoro voice the TTS tracks rated lower.

**Gap-fill confidence:** high

### Answer
## Gap A (lip-sync timing): licence chain for forced alignment of cached TTS wavs (checked 2026-09-24)

### Verdict
1. **The Montreal Forced Aligner (MFA) 3.4.2 toolchain has no non-commercial parts.** The GPL items are the GCC runtime libraries, which carry the GCC runtime exception, plus GPL executables that conda installs but MFA does not call.
   - MFA itself is MIT [c1], kalpy is MIT [c4], Kaldi is Apache-2.0 [c5].
   - OpenFst, pynini, baumwelch and ngram are all Apache-2.0 [c6][c7][c8][c9].
   - Code loaded into the MFA process:
     - The `_kalpy` extension links libkaldi-* and libfst.so.26, both Apache [c10].
     - OpenBLAS is BSD-3.
     - libstdc++, libgcc_s and libgfortran are "GPL-3.0-only WITH GCC-exception-3.1" [c14].
     - librosa loads soxr (LGPL-2.1+) as soon as it is imported. soundfile loads libsndfile (LGPL-2.1+) [c11][c12][c13].
     - psycopg2 (LGPL-3.0+) is loaded only with `--use_postgres`. The default is sqlite [c17].
   - GPL executables that conda installs:
     - The conda-forge recipe still requires `sox` (GPL-2.0-only) and `ffmpeg`, which resolves to a GPL build by default [c3][c14].
     - The 3.4.2 source contains no sox or ffmpeg invocation [c17]. MFA's own changelog says both dependencies were removed in 3.0.7 [c16]. This conflicts with the recipe (see Contradictions).
     - `ffmpeg=*=lgpl*` resolves cleanly to an LGPL build [c15]. sox cannot be removed from the conda package.
2. **The default English model, `english_mfa`, is BLOCKED.** This is an unresolved first-party conflict, the same shape as the lessac problem.
   - Both v3.1.0 (GitHub, 2024) and v3.3.0 (Hugging Face (HF), trained 2026-05-12) are labelled CC BY 4.0 [c19][c20].
   - 4 of its 10 training corpora are non-commercial on their own first-party pages: CORAAL CC BY-NC-SA 4.0 [c24], ICE-Nigeria CC BY-NC-SA 3.0 DE [c29], ASR-SPakEDuSC CC BY-NC-ND 4.0 [c30], L2-ARCTIC CC BY-NC 4.0 [c31].
   - Together that is 208.68 of the 3,614.20 hours listed.
   - Google UK and Ireland English [c26] and Google Nigerian English [c25] are CC BY-SA 4.0. Commercial use is allowed; share-alike applies.
   - VCTK is **not** a training corpus.
3. **Clean MFA model: `english_us_arpa`.**
   - v3.0.0 (GitHub) and v3.3.0 (HF, tag v3.3.0) are trained on **LibriSpeech only** (CC BY 4.0) and licensed CC BY 4.0 [c34][c23].
   - Its dictionary lists "Source: wikipron". Wiktionary text is CC BY-SA 4.0 plus GFDL [c33]. Share-alike applies; no non-commercial term.
   - It uses the US ARPAbet phone set. How well it aligns British TTS voices was not measured.
4. **Alternatives**

| Route | Code licence | Weights licence | Status |
|---|---|---|---|
| torchaudio `forced_align` + **MMS_FA** | BSD-2 [c42] | CC-BY-NC 4.0 on Meta's fairseq MMS page [c38]; mms-300m card is cc-by-nc-4.0 [c39] | **DISQUALIFIED** |
| torchaudio `forced_align` + **WAV2VEC2_ASR_BASE_960H** | BSD-2 | torchaudio says MIT [c40]; Meta's HF card says apache-2.0 [c41]; LibriSpeech-only | Allowed. Aligns characters, not phonemes. |
| `facebook/wav2vec2-lv-60-espeak-cv-ft` (phoneme CTC) | – | apache-2.0 [c41] | Allowed. Needs a transcript in espeak phonemes; its pretraining data licence was not checked. |
| Gentle | MIT [c43] | Model zip has no licence file; the model folder name matches Kaldi's ASpIRE recipe, which trains on Fisher English (LDC) [c43][c44] | **DISQUALIFIED** (no-licence model) |
| aeneas | AGPL-3.0; runs eSpeak "via a Python C extension"; aligns text fragments, not phonemes; last release 2017 [c45] | – | Copyleft, and does not give phoneme timing |
| charsiu | MIT repo | HF weights have no licence [c46] | **DISQUALIFIED** |
| NeMo Forced Aligner | Apache-2.0 | parakeet-ctc cc-by-4.0 [c47] | Only the licence tags were checked |

- torchaudio 2.11.0 (2026-03-23) still ships `forced_align` on CPU and CUDA, although the library is in "maintenance phase" [c36].

### Practical chain with no non-commercial parts and no GPL code loaded into the process
- MFA 3.4.2 from conda-forge, pinned to `ffmpeg=*=lgpl*`, on sqlite (the default).
- `mfa align_one` [c18].
- `english_us_arpa` v3.3.0 acoustic model, dictionary and G2P.
- sox (GPL-2.0-only) is still installed as an executable that is never called.
- Otherwise: torchaudio `forced_align` with WAV2VEC2_ASR_BASE_960H gives character timings, and you would need your own G2P to get visemes.

### Details
- **Resolved environment:** conda dry-run for linux-64, MFA 3.4.2, python 3.12, 285 packages, against conda-forge repodata from 2026-09-24. win-64 gives 207 packages with the same GPL set: sox, ffmpeg (GPL build), libmad, x264, x265 [c14].
- **Other licences in the environment:**
  - readline (GPL-3.0-only) is a dependency of python, sqlite and postgresql, but MFA and kalpy never import it.
  - graphviz (EPL-1.0) is a dependency of pynini.
- **Feedstock repo licence:** the conda-forge feedstock repos are BSD-3-Clause. That covers the recipes, not the packages.
- **The released dictionaries are not independent of the training corpora.** The v3.1.0 README says the released `english_mfa` / `english_uk_mfa` dictionaries have "pronunciation and silence probabilities estimated as part acoustic model training" [c32]. That is the same training that used the non-commercial corpora.
- **Alignment resolution:** MFA features use `frame_shift 10` ms [c35].

### Claims
- [c1] FIRST-PARTY · 2026-08-20 · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/tag/v3.4.2 — MFA latest release is v3.4.2 (published 2026-08-20); repository licence MIT; PyPI 3.4.2 licence MIT — "Version 3.4.2 ... published 2026-08-20T00:18:52Z; LICENSE: "Copyright (c) 2016 Montreal Corpus Tools ... Permission is hereby granted, free of charge""
- [c2] FIRST-PARTY · v3.4.2 (2026-08-20) · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/v3.4.2/docs/source/installation.rst — MFA is distributed and installed through conda-forge — "conda create -n aligner -c conda-forge montreal-forced-aligner -y"
- [c3] FIRST-PARTY · commit ed7addc2d7 2026-08-20 · https://github.com/conda-forge/montreal-forced-aligner-feedstock/blob/main/recipe/meta.yaml — The conda-forge montreal-forced-aligner 3.4.2 recipe (maintainer mmcauliffe) is MIT and its run requirements include kaldi 5.5.1172, pynini, openfst, baumwelch, ngram, sox, ffmpeg, postgresql, psycopg2 and kalpy >=0.10 — "run: - kaldi {{ kaldi_version }} - pynini - openfst - baumwelch - ngram - sox - ffmpeg ... - psycopg2 ... - kalpy >=0.10 ... license: MIT"
- [c4] FIRST-PARTY · 2026-08-20 · https://github.com/mmcauliffe/kalpy/releases/tag/v0.10.5 — kalpy 0.10.5 (pybind11 bindings for Kaldi) is MIT in the sdist, the GitHub repo and conda-forge. It pins openfst ==1.8.4 and kaldi 5.5.1172. PyPI has an sdist only. — "MIT License

Copyright (c) 2023 Michael McAuliffe; conda-forge: summary: 'Pybind11 bindings for Kaldi for use with the Montreal Forced Aligner' license: MIT"
- [c5] FIRST-PARTY · commit 2025-07-22; accessed 2026-09-24 · https://github.com/kaldi-asr/kaldi/blob/f4007661023b98b8081fd875029f0dee62242fd1/COPYING — Kaldi at the commit conda-forge builds (f4007661, 2025-07-22) is Apache-2.0. The gst-plugin, whose file declares LGPL, is not in the CMake build. — "Each of the files comprising Kaldi v1.0 have been separately licensed by their respective author(s) under the terms of the Apache License v 2.0"
- [c6] FIRST-PARTY · accessed 2026-09-24 · http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.8.4.tar.gz — OpenFst 1.8.4 (tarball sha256 a8ebbb6f… matches the conda-forge recipe) is Apache-2.0 — "Licensed under the Apache License, Version 2.0 ... Copyright 2005-2024 Google LLC."
- [c7] FIRST-PARTY · accessed 2026-09-24 · https://www.opengrm.org/twiki/pub/GRM/PyniniDownload/pynini-2.1.7.tar.gz — pynini 2.1.7 (sha256 matches the recipe) is Apache-2.0 — "Apache License Version 2.0, January 2004 (LICENSE); conda-forge: license: Apache-2.0"
- [c8] FIRST-PARTY · accessed 2026-09-24 · https://www.opengrm.org/twiki/pub/GRM/BaumWelchDownload/baumwelch-0.3.11.tar.gz — baumwelch 0.3.11 is Apache-2.0 — "Apache License Version 2.0, January 2004 (LICENSE); conda-forge: license: Apache-2.0"
- [c9] FIRST-PARTY · accessed 2026-09-24 · https://www.opengrm.org/twiki/pub/GRM/NGramDownload/ngram-1.3.17.tar.gz — OpenGrm ngram 1.3.17 is Apache-2.0 — "Apache License Version 2.0, January 2004 (LICENSE); conda-forge: license: Apache-2.0"
- [c10] FIRST-PARTY · accessed 2026-09-24 (empirical) · https://conda.anaconda.org/conda-forge/linux-64/kalpy-0.10.5-py312ha5105d2_0.conda — The _kalpy extension module links the Kaldi and OpenFst shared libraries into the Python process (read from DT_NEEDED of the conda-forge linux-64 build) — "_kalpy.cpython-312-x86_64-linux-gnu.so -> ['libkaldi-base.so', ... 'libkaldi-feat.so', ... 'libfst.so.26', 'libstdc++.so.6', ... 'libgcc_s.so.1']"
- [c11] FIRST-PARTY · v0.10.5 (2026-08-20) · https://github.com/mmcauliffe/kalpy/blob/v0.10.5/kalpy/data.py — kalpy loads audio through librosa at 16 kHz — "y, _ = librosa.load(
            self.file_path,
            sr=16000,"
- [c12] FIRST-PARTY · 1.0.0 released 2026-08-11 · https://github.com/librosa/librosa/blob/1.0.0/librosa/core/audio.py — librosa 1.0.0 imports soxr when the module is imported and uses soxr_hq by default. It depends on soundfile and soxr (no audioread). — "import soxr ... res_type: str = "soxr_hq"; PyPI requires_dist ['soundfile>=0.12.1', 'soxr>=1.0.0']"
- [c13] FIRST-PARTY · accessed 2026-09-24 · https://pypi.org/project/soxr/ — soxr (python-soxr) is LGPL-2.1-or-later and libsndfile is LGPL-2.1; both are loaded into the process — "soxr 1.1.0 license_expression: LGPL-2.1-or-later; github libsndfile/libsndfile license LGPL-2.1"
- [c14] FIRST-PARTY · repodata mod Thu, 24 Sep 2026 06:58:55 GMT · https://conda.anaconda.org/conda-forge/linux-64/repodata.json — Copyleft packages in a conda-forge solve of MFA 3.4.2 (linux-64 and win-64), with licences from conda-forge repodata — "sox 14.4.2 GPL-2.0-only; ffmpeg 9.0.0 gpl_h95e667c_900 GPL-2.0-or-later; mad GPL; x264/x265 GPL-2.0-or-later; readline 8.3 GPL-3.0-only; psycopg2 2.9.12 LGPL-3.0-or-later; libstdcxx 16.2.0 GPL-3.0-only WITH GCC-exception-3.1; libopenblas 0.3.34 BSD-3-Clause"
- [c15] FIRST-PARTY · accessed 2026-09-24 (empirical dry-run) · https://conda.anaconda.org/conda-forge/linux-64/repodata.json — Pinning the LGPL ffmpeg build solves cleanly with MFA 3.4.2; sox stays GPL-2.0-only — "ffmpeg 9.0.0 lgpl_hdabad70_800 (LGPL-2.1-or-later); sox 14.4.2 h8c9d6be_1021"
- [c16] FIRST-PARTY · v3.4.2 tree (2026-08-20) · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/v3.4.2/docs/source/changelog/changelog_3.0.rst — MFA's changelog says sox and ffmpeg were dropped in 3.0.7 — "Removed dependencies on :code:`sox` and :code:`ffmpeg` as audio loading is done through :code:`librosa` in :code:`kalpy`"
- [c17] FIRST-PARTY · v3.4.2 (grep of the sdist, sha256 421f8cf3…) · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/v3.4.2/montreal_forced_aligner/config.py — The MFA 3.4.2 source contains no sox or ffmpeg invocation (sox appears only in a legacy enum, a DB column and error parsing). The default database is sqlite; psycopg2 is used only with postgres. — "USE_POSTGRES = False ... return f"sqlite:///{self.db_path}" ... SOX = 2  #: Needs to use SoX to preprocess"
- [c18] FIRST-PARTY · v3.4.2 · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/v3.4.2/montreal_forced_aligner/command_line/align_one.py — MFA 3.4.2 has an align_one command for aligning a single file — "name="align_one", ... short_help="Align a single file""
- [c19] FIRST-PARTY · commit 153c489946 2024-06-16 · https://github.com/MontrealCorpusTools/mfa-models/blob/main/acoustic/english/mfa/v3.1.0/README.md — english_mfa acoustic v3.1.0 is CC BY 4.0 (trained 2024-06-12, released 2024-06-16) and trained on 10 corpora: Common Voice English 17.0, LibriSpeech, CORAAL 2021.07, Google Nigerian English, Google UK and Ireland English, NCHLT English, ARU, ICE-Nigeria, ASR-SPakEDuSC and L2-ARCTIC — "**License:** [CC BY 4.0] ... This model was trained on the following corpora: ... [Corpus of Regional African American Language] ... [ICE-Nigeria] ... [A Scripted Pakistani English Daily-use Speech Corpus] ... [L2-ARCTIC]"
- [c20] FIRST-PARTY · 2026-05-13 · https://huggingface.co/MontrealCorpusTools/english_mfa — The newer HF english_mfa v3.3.0 (train_date 2026-05-12, last modified 2026-05-13) is cc-by-4.0, lists the same 10 corpora, and names 4 non-commercial licences itself — "license: cc-by-4.0 ... Corpus of Regional African American Language ... **License:** CC BY-NC-SA 4.0 ... ICE-Nigeria ... CC BY-NC-SA 3.0 ... L2-ARCTIC ... CC BY-NC 4.0 ... A Scripted Pakistani English Daily-use Speech Corpus ... CC BY-NC-ND 4.0; title={Global English MFA acoustic model v3.3.0}"
- [c21] FIRST-PARTY · v3.4.2 tree · https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/blob/v3.4.2/docs/source/changelog/changelog_3.4.rst — MFA 3.4.0 introduced a model format distributed on Hugging Face — "Introduced new MFA model format for distribution on HuggingFace"
- [c22] FIRST-PARTY · snapshot 2024-06-22 · https://web.archive.org/web/20240622123213/https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0 — Common Voice 17.0 is CC0 (Mozilla's own HF card, archived). It adds a condition: do not try to identify speakers. Since Oct 2025 the data is served only through the Mozilla Data Collective. — "License: cc0-1.0 ... you also agree to not attempt to determine the identity of speakers ... Licensing Information Public Domain, CC-0"
- [c23] FIRST-PARTY · accessed 2026-09-24 · https://openslr.org/12/ — LibriSpeech (SLR12) is CC BY 4.0 — "Identifier: SLR12 ... License: CC BY 4.0"
- [c24] FIRST-PARTY · page source last commit 2024-09-07 · https://oraal.github.io/coraal — CORAAL is non-commercial share-alike (page covers v2023.06; MFA trained on v2021.07) — "CORAAL is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike (4.0) International license"
- [c25] FIRST-PARTY · accessed 2026-09-24 · https://openslr.org/70/ — Google Nigerian English (SLR70) is CC BY-SA 4.0 — "License: Attribution-ShareAlike 4.0 International"
- [c26] FIRST-PARTY · accessed 2026-09-24 · https://openslr.org/83/ — Google UK and Ireland English (SLR83) is CC BY-SA 4.0; commercial use is allowed and share-alike applies — "License: Attribution-ShareAlike 4.0 International (resources/83/LICENSE header: "Attribution-ShareAlike 4.0 International")"
- [c27] FIRST-PARTY · item date 2014-07-08 · https://repo.sadilar.org/handle/20.500.12185/274 — NCHLT English is CC BY 3.0 — "License Creative Commons Attribution 3.0 Unported License (CC BY 3.0)"
- [c28] FIRST-PARTY · Last Modified: 04 Oct 2024 · http://datacat.liverpool.ac.uk/681/ — The ARU English corpus archive is CC BY 3.0; its README PDF in the same deposit is CC BY 4.0 — "ARU_Speech_Corpus_v1_0.zip ... License: Creative Commons: Attribution 3.0 ... Read me ... License: Creative Commons: Attribution 4.0"
- [c29] FIRST-PARTY · Manual_ICE-Nigeria.pdf in zip dated 2015-11-03 · https://sourceforge.net/projects/ice-nigeria/files/ICE-Nigeria-txt-and-xml-files_version_Nov_03_2015.zip/download — ICE-Nigeria is CC BY-NC-SA 3.0 Germany according to its own manual; SourceForge lists 'Other License' — "ICE Nigeria by Prof. Dr. Ulrike Gut is licensed under a Creative Commons Attribution-Non- Commercial-Share Alike 3.0 Germany License."
- [c30] FIRST-PARTY · accessed 2026-09-24 · https://magichub.com/datasets/pakistani-english-scripted-speech-corpus-daily-use-sentence/ — ASR-SPakEDuSC (MagicHub) is CC BY-NC-ND 4.0 — "This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License"
- [c31] FIRST-PARTY · accessed 2026-09-24 · https://psi.engr.tamu.edu/l2-arctic-corpus/ — L2-ARCTIC is CC BY-NC 4.0 — "The corpus is released under the CC BY-NC 4.0 license ... For any usage that is not covered by the CC BY-NC 4.0 license, please contact Dr. Ricardo Gutierrez-Osuna"
- [c32] FIRST-PARTY · 2024-06-16 · https://github.com/MontrealCorpusTools/mfa-models/blob/main/dictionary/english/uk_mfa/v3.1.0/README.md — The english_mfa and english_uk_mfa dictionaries v3.1.0 are CC BY 4.0 (released 2024-06-16). The released files carry probabilities estimated during acoustic model training. — "**License:** [CC BY 4.0] ... The dictionary available from the release page and command line installation has pronunciation and silence probabilities estimated as part acoustic model training"
- [c33] FIRST-PARTY · 2026-05-13 · https://huggingface.co/MontrealCorpusTools/english_mfa — MFA English dictionaries list WikiPron as their source; WikiPron's data inherits Wiktionary's terms (CC BY-SA 4.0 plus GFDL) — "Details for english_uk_mfa dictionary and G2P model - **Source:** wikipron | WikiPron README: "Wiktionary data in the data/ directory has its own licensing terms" | Wiktionary:Copyrights: "dual-licensed ... Creative Commons Attribution-ShareAlike 4.0 International License (CC-BY-SA) and the GNU Free"
- [c34] FIRST-PARTY · 2026-06-09 · https://huggingface.co/MontrealCorpusTools/english_us_arpa — english_us_arpa acoustic model (v3.0.0 GitHub, released 2024-02-24; v3.3.0 HF, trained 2026-05-14, tag v3.3.0) is trained on LibriSpeech only and licensed CC BY 4.0; dictionary source is wikipron, 266,823 words — "license: cc-by-4.0 ... #### LibriSpeech English - **Source:** https://openslr.org/12/ - **License:** [CC BY 4.0] ... title={English (US) ARPA acoustic model v3.3.0}"
- [c35] FIRST-PARTY · asset 2024-06-16 (sha256 2c08bd4f…) · https://github.com/MontrealCorpusTools/mfa-models/releases/download/acoustic-english_mfa-v3.1.0/english_mfa.zip — meta.json inside english_mfa.zip v3.1.0 has no licence field and uses a 10 ms frame shift — "'features': {'type': 'mfcc', ... 'frame_shift': 10, ...}; 'version': '3.1.0'"
- [c36] FIRST-PARTY · 2026-03-23 · https://github.com/pytorch/audio/blob/v2.11.0/src/torchaudio/functional/_alignment.py — torchaudio 2.11.0 (2026-03-23) still ships forced_align on CPU and CUDA; the library is in maintenance mode — "def forced_align( ... .. devices:: CPU CUDA; README: "We have transitioned TorchAudio into a maintenance phase.""
- [c37] FIRST-PARTY · 2026-03-23 · https://github.com/pytorch/audio/blob/v2.11.0/src/torchaudio/pipelines/_wav2vec2/impl.py — torchaudio's MMS_FA bundle points to the MMS alignment model and states it is CC-BY-NC 4.0 — "https://dl.fbaipublicfiles.com/mms/torchaudio/ctc_alignment_mling_uroman/model.pt ... Published by the authors of *Scaling Speech Technology to 1,000+ Languages* ... under [`CC-BY-NC 4.0 License"
- [c38] FIRST-PARTY · last README commit 2024-01-08; same text at 100cd91 (2023-07-07) · https://github.com/facebookresearch/fairseq/blob/main/examples/mms/README.md — Meta's fairseq MMS page puts the MMS code and weights, including the multilingual alignment model, under CC-BY-NC 4.0. The fairseq repo itself is MIT and archived. — "We also open source a multilingual alignment model trained on 31K hours of data in 1,130 languages ... The MMS code and model weights are released under the CC-BY-NC 4.0 license."
- [c39] FIRST-PARTY · lastModified 2023-06-05 · https://huggingface.co/facebook/mms-300m — Meta's HF card for facebook/mms-300m is CC-BY-NC 4.0 — "license: cc-by-nc-4.0 ... - **License:** CC-BY-NC 4.0 license"
- [c40] FIRST-PARTY · 2026-03-23 · https://github.com/pytorch/audio/blob/v2.11.0/src/torchaudio/pipelines/_wav2vec2/impl.py — torchaudio's WAV2VEC2_ASR_BASE_960H is trained on LibriSpeech 960h and redistributed under MIT — "pre-trained on 960 hours of unlabeled audio from *LibriSpeech* ... fine-tuned for ASR on the same audio ... Originally published by the authors of *wav2vec 2.0* ... under MIT License and redistributed with the same license."
- [c41] FIRST-PARTY · lastModified 2022-11-14 · https://huggingface.co/facebook/wav2vec2-base-960h — Meta's HF cards give apache-2.0 for wav2vec2-base-960h (LibriSpeech), wav2vec2-large-960h-lv60-self and wav2vec2-lv-60-espeak-cv-ft (phoneme CTC) — "datasets:
- librispeech_asr ... license: apache-2.0"
- [c42] FIRST-PARTY · accessed 2026-09-24 · https://github.com/pytorch/audio — torchaudio's repo licence is BSD-2-Clause — "license: BSD-2-Clause (GitHub API)"
- [c43] FIRST-PARTY · last commit 2025-02-16; zip last-modified 2025-02-16 · https://github.com/strob/gentle/blob/master/install_models.sh — Gentle's code is MIT (last release 0.11.0, 2023-03-05). Its model zip (kaldi-models-0.04.zip, 161,246,499 bytes, directory exp/tdnn_7b_chain_online) contains no licence or README file. — "VERSION="0.04" ... local url="https://rmozone.com/gentle/$filename"; COPYING: "The MIT License (MIT) Copyright (c) 2015 Robert M Ochshorn""
- [c44] FIRST-PARTY · model date 2016-10-15 · https://kaldi-asr.org/models/m1 — Kaldi's ASpIRE chain model (recipe egs/aspire, dir tdnn_7b) is trained on Fisher English (LDC) and its page states no licence. Linking Gentle's model to ASpIRE is an inference from the directory name only. — "ASpIRE Chain Model A chain model trained on Fisher English that has been augmented with impulse responses and noises ... Recipe egs/aspire/s5; run.sh: "local/fisher_data_prep.sh /export/corpora3/LDC/LDC2004T19""
- [c45] FIRST-PARTY · release v1.7.3 2017-03-16 · https://github.com/readbeyond/aeneas — aeneas is AGPL-3.0, runs eSpeak in-process by default, aligns at fragment level, and was last released as v1.7.3 in 2017 — "**aeneas** is released under the terms of the GNU Affero General Public License Version 3 ... Default TTS (eSpeak) called via a Python C extension ... not designed with word-level alignment in mind"
- [c46] FIRST-PARTY · lastModified 2021-10-03 · https://huggingface.co/charsiu/en_w2v2_fc_10ms — charsiu's repo is MIT, but its HF weights have no licence or README — "cardData license: None; files ['.gitattributes','config.json','pytorch_model.bin']; github lingjzhu/charsiu license MIT"
- [c47] FIRST-PARTY · lastModified 2026-08-05 · https://huggingface.co/nvidia/parakeet-ctc-1.1b — NeMo is Apache-2.0 and nvidia/parakeet-ctc-1.1b is tagged cc-by-4.0; training data was not checked — "license: cc-by-4.0 (tag license:cc-by-4.0); NVIDIA/NeMo license Apache-2.0"

### Could not confirm
- Licence of CORAAL v2021.07, the version MFA lists, from a page for that version. The current first-party page covers v2023.06 (CC BY-NC-SA 4.0). The Wayback Machine went offline mid-session and lingtools.uoregon.edu was unreachable.
- Whether non-commercial or share-alike terms on training corpora bind the CC BY 4.0 english_mfa model. This is a legal question and was not resolved.
- Provenance of Gentle's kaldi-models-0.04 acoustic model. The folder name matches Kaldi's ASpIRE tdnn_7b recipe (Fisher English, LDC), but nothing first-party names it.
- Whether english_uk_mfa / english_mfa v3.1.0 dictionaries (GitHub) come from WikiPron. Only the HF v3.3.0 card states 'Source: wikipron'; the v3.1.0 README is silent.
- A runtime trace that MFA 3.4.2 never calls sox or ffmpeg on wav input. This is based on grep of the MFA and kalpy source only.
- MFA was not run end to end, and alignment accuracy on synthetic British TTS audio (VoxCPM2, Chatterbox, Kokoro) was not measured, for either english_us_arpa (US ARPAbet) or english_mfa.
- Pretraining data licence of wav2vec2-lv-60 checkpoints (Libri-Light), and training data of NVIDIA parakeet CTC models (only HF licence tags checked).
- Licences of MFA English G2P models beyond the HF card metadata. They are needed only for words missing from the dictionary.
- Whether the deploy host 'hil' is Windows. A win-64 solve was run in case it is; its GPL set matches linux-64.

### Verification (combined lens)
Fidelity is high. All 47 claims were re-opened on 2026-09-24. 42 are supported and 3 are only partly supported (c5 gst-plugin wording, c17 quote attributed to the wrong file, c34 dictionary provenance and missing LICENSE file). Nothing is contradicted or unreachable. I re-ran both linux-64 conda solves (285 packages, ffmpeg 9.0.0 gpl_h95e667c_900 by default; lgpl_hdabad70_800 when pinned) and the win-64 solve (207 packages, same GPL set). I also re-checked every tarball sha256, the _kalpy DT_NEEDED list, the english_mfa.zip meta.json, the corpus licence pages (L2-ARCTIC via WebFetch because curl hit a Cloudflare block) and the ICE-Nigeria manual. I found no invented version numbers.

Errors are in the practical recommendation, not the licence chain:
- The HF v3.3.0 models need `align_one_hf`, not `align_one`.
- Tag v3.3.0 has no G2P. The G2P on main is v3.2.0.
- mad (GPL) stays installed next to sox after the LGPL ffmpeg pin.
- The GPL package list is incomplete: ld_impl_linux-64, hicolor-icon-theme, and dual-licensed freetype and dbus are missing.

New findings:
- CORAAL 2021.07 is confirmed CC BY-NC-SA 4.0 from its July 2021 user guide (Wayback). This strengthens the english_mfa BLOCKED verdict.
- MFA's GitHub pages and HF card disagree on where the english_us_arpa dictionary comes from: Prosodylab-aligner (MIT) vs WikiPron. Not resolved.
- parakeet-ctc-1.1b lists Fisher, Switchboard and WSJ (LDC) in its training data under CC-BY-4.0.
- MFA's own environment.yml agrees with the changelog that sox and ffmpeg are gone.

The core conclusions hold:
- The MFA toolchain has no non-commercial parts. The GPL code is in executables or carries the GCC runtime exception.
- english_mfa is blocked by 4 non-commercial corpora totalling 208.68 of 3,614.20 hours.
- english_us_arpa is trained on LibriSpeech only, CC BY 4.0.
- MMS_FA is disqualified (CC-BY-NC).
- wav2vec2-base-960h is permissive.
- Gentle's model and charsiu's HF weights have no licence.
- aeneas is AGPL-3.0.

Scratch files: <session scratch, not kept>/verifyA-align/ (solve_linux.json, solve_linux_lgpl.json, solve_win.json, coraal_ug_2022.pdf, mfa/ clone).

Checks not marked "supported":
- **partially_supported**: Kaldi at f4007661 (2025-07-22) is Apache-2.0; gst-plugin, whose file declares LGPL, is not in the CMake build → Kaldi f4007661 is Apache-2.0 (COPYING). src/gst-plugin files carry Apache-2.0 headers; gst-online-gmm-decode-faster.cc only registers the plugin with the metadata string "LGPL" (line 886) to satisfy GStreamer; not built by CMake. https://github.com/kaldi-asr/kaldi/blob/f4007661023b98b8081fd875029f0dee62242fd1/src/gst-plugin/gst-online-gmm-decode-faster.cc
- **partially_supported**: MFA 3.4.2 source has no sox/ffmpeg invocation; default DB sqlite; psycopg2 only with postgres → sqlite string is in montreal_forced_aligner/abc.py:378 and SOX enum in montreal_forced_aligner/data.py:360; only USE_POSTGRES = False is in config.py.
- **partially_supported**: english_us_arpa v3.0.0 (GitHub, 2024-02-24) and v3.3.0 (HF, trained 2026-05-14, tag v3.3.0) LibriSpeech-only, CC BY 4.0; dictionary source wikipron, 266,823 words → Dictionary provenance is reported inconsistently by the same maintainer: HF v3.3.0 card 'Source: wikipron' (266,823 words) vs GitHub v3.0.0 README citing Prosodylab-aligner (199,858 words). Both first-party; not resolved.
- **partially_supported**: GPL items are only GCC runtime libs (with exception) plus GPL executables MFA does not call → Reproduced linux-64 solve also contains ld_impl_linux-64 2.46.1 'GPL-3.0-only', hicolor-icon-theme 0.17 'GPL-2.0-or-later', libgomp 16.2.0 (GCC exception), freetype/libfreetype 'GPL-2.0-only OR FTL', dbus 'AFL-2.1 OR GPL-2.0-or-later', and GPL libraries (mad, x264, x265) that are libraries, not exec
- **partially_supported**: Practical chain: MFA 3.4.2 + ffmpeg lgpl pin + 'mfa align_one' + english_us_arpa v3.3.0 acoustic model, dictionary and G2P; only sox remains GPL → Use 'mfa align_one_hf <wav> <txt> MontrealCorpusTools/english_us_arpa <out>' (from_pretrained -> snapshot_download revision=None, i.e. main) or 'mfa align_one' with legacy english_us_arpa v3.0.0 files; G2P on HF is v3.2.0 and absent at tag v3.3.0; GPL sox AND mad remain installed.

Flagged as unconfirmed by the verifier:
- Practical chain says 'english_us_arpa v3.3.0 acoustic model, dictionary and G2P': there is no v3.3.0 G2P. Tag v3.3.0 contains no g2p/; the G2P on main is version 3.2.0 (meta.json).
- Practical chain says 'mfa align_one' for the HF v3.3.0 model. In MFA 3.4.2 HF models load through 'align_one_hf'; 'align_one' takes legacy files (GitHub v3.0.0).
- c5: 'gst-plugin, whose file declares LGPL'. The file header is Apache-2.0; only a GStreamer registration string says "LGPL".
- c17: the quote is attributed to config.py, but 'sqlite:///' is in abc.py:378 and 'SOX = 2' is in data.py:360.
- c34: 'dictionary source is wikipron, 266,823 words' holds only for the HF main card. GitHub v3.0.0 cites Prosodylab-aligner (199,858 words). The tag v3.3.0 card also gives different LibriSpeech hours (976.90 vs 982.10).

---


# MIGRATION.md -- moving the Living Portraits show from supercommons2 to hil08rd

The architecture v4 picture: `living-portraits-architecture-v4.svg`.

## What is moving, and what is not

The **show** (player + director + rig + cross-frame walk -> the two LED panels)
relocates to **hil08rd**, the machine physically wired to the panels. The **GPU
bakery** (SD1.5 portrait gen + the verify gate + qwen3) stays on
**supercommons2**, which has the RTX 2080 Ti.

| | machine | tailnet | role after migration |
|---|---|---|---|
| **A (destination)** | `desktop-hil08rd` | `100.71.118.128` | the panel machine: runs the show, drives both LED panels |
| **B (source)** | `supercommons2` | `100.123.185.12` (`immer@`) | the GPU backend: bakes assets, optionally serves qwen3 |

Two cross-machine seams over the tailnet:
1. **Assets** (portraits / cutouts / bg plates / rigs / clip manifest) sync
   **SC2 -> hil** via `install/sync_assets.ps1`.
2. **qwen3** -- if hil has **no GPU**, hil's director calls SC2's Ollama over the
   tailnet (`LP_OLLAMA`). If hil **has a GPU**, Ollama runs locally on hil and
   SC2 can drop out entirely (the **all-on-hil** variant).

### The branch that decides everything: does hil08rd have an NVIDIA GPU?

You do not need to answer this by hand -- step (b) (`bringup_host.ps1`) detects it
and picks the path. But the whole runbook forks on the answer, so hold both in
mind:

- **hil HAS a GPU (all-on-hil):** hil becomes self-contained. `bringup_host.ps1`
  builds `.venv-gen`, installs torch+SD+piper+insightface, pulls qwen3 + the VL
  model locally, and can bake portraits on hil itself. **Skip step (d)** (no
  cross-tailnet asset sync, no `LP_OLLAMA`). SC2 is then optional.
- **hil has NO GPU (two-machine, the assumed case):** hil runs the lean `.venv`
  (player + director + watchdog + GrabCut re-rig). Portraits are baked on SC2 and
  **synced in** (step d), and hil's director reaches **SC2's** qwen3 via
  `LP_OLLAMA` (step d). This is the default topology v4 draws.

---

## Conductor pre-reqs (run once, on the dev box `jtole`)

All remote PowerShell goes through the base64-EncodedCommand helper (never inline
PS over SSH -- see memory `feedback_ps_over_ssh_b64`). Dot-source it into the
session **first**; `deploy_host.ps1` and `sync_assets.ps1` both call
`Invoke-RemotePS` and fail fast if it is absent.

```powershell
# from the life repo root
. C:\Users\jtole\Documents\2026\life\scripts\invoke-remote-ps.ps1
```

The dev box already holds SSH keys to SC2 (`ssh immer@100.123.185.12` is
key-auth). It must also reach hil08rd over the tailnet with the same key once
step (a) is done. The two scp legs in `sync_assets.ps1` both originate here.

> Throughout, `<HIL>` = the hil08rd login as `user@host`, e.g. `immer@hil08rd`
> or `immer@100.71.118.128`. If hil's interactive user is **not** `immer`, read
> the **Known gaps -> task principal** note before step (c).

---

## (a) Enable SSH on hil08rd (OpenSSH server + tailnet firewall)

hil needs an SSH server the dev box can reach over the tailnet. Run this **once,
at the hil08rd console** (or via any existing remote shell) in an **elevated**
PowerShell. It installs the OpenSSH Server feature, starts + auto-starts the
service, and opens the firewall to TCP 22 **scoped to the tailnet CGNAT range**
(`100.64.0.0/10`) so SSH is never exposed to the LAN or the internet.

```powershell
# ELEVATED PowerShell on hil08rd
# 1. Install + enable the OpenSSH server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Set-Service -Name sshd -StartupType Automatic
Start-Service sshd

# 2. Firewall: allow SSH ONLY from the Tailscale CGNAT range (not 0.0.0.0/0).
#    Remove the default rule the feature drops in (it allows from Any), then add
#    a tailnet-scoped one.
Get-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -ErrorAction SilentlyContinue |
    Remove-NetFirewallRule
New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP-Tailnet' `
    -DisplayName 'OpenSSH Server (TCP 22, tailnet only)' `
    -Enabled True -Direction Inbound -Protocol TCP -Action Allow `
    -LocalPort 22 -RemoteAddress 100.64.0.0/10

# 3. Default shell to PowerShell so Invoke-RemotePS lands in PS, not cmd.
New-Item -Path 'HKLM:\SOFTWARE\OpenSSH' -Force | Out-Null
New-ItemProperty -Path 'HKLM:\SOFTWARE\OpenSSH' -Name DefaultShell `
    -Value 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' `
    -PropertyType String -Force
```

Then authorize the dev box's key. Copy the dev box's **public** key into hil's
`administrators_authorized_keys` (admin users on Windows OpenSSH read that file,
not `~/.ssh/authorized_keys`). From the **dev box**:

```powershell
# dev box -- push your public key to hil's admin authorized_keys
$pub = Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub -Raw
$remote = @"
`$f = 'C:\ProgramData\ssh\administrators_authorized_keys'
Add-Content -Path `$f -Value '$($pub.Trim())'
icacls `$f /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F' | Out-Null
"@
# (run on hil via the console once, OR via an existing session; after this, SSH key-auth works)
```

> If hil is not yet on the tailnet at all, join it first with the
> `windows-bootstrap` skill (USB build + tailnet auto-join) or
> `tailscale up` on the box. Confirm `100.71.118.128` answers before continuing.

**Verify (a) from the dev box:**

```powershell
ssh -o BatchMode=yes -o ConnectTimeout=10 <HIL> "hostname"
# expect: desktop-hil08rd  (key-auth, no password prompt)
```

If that prints the hostname with no prompt, the link is good and every later
step's `Invoke-RemotePS`/`scp` will work.

---

## (b) Bring up the host: GPU-detect + install deps (`bringup_host.ps1`)

`install/bringup_host.ps1` is host-adaptive: it detects hil's GPU
(`nvidia-smi` OR an NVIDIA `Win32_VideoController`) and takes one of two paths,
no edits. Each step prints `OK`/`SKIP`/`FAIL`; it is idempotent.

```powershell
# dev box -- scp the script to hil (pure ASCII, no BOM -- straight scp is fine)
scp C:\Users\jtole\Documents\2026\life\projects\living-portraits\install\bringup_host.ps1 `
    "<HIL>:C:/Users/immer/living-portraits/install/bringup_host.ps1"

# dev box -- run it on hil (auto-detects GPU, streams every step's verdict)
Invoke-RemotePS -Host_ <HIL> -Script @'
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\immer\living-portraits\install\bringup_host.ps1
'@
```

- **GPU PRESENT** -> builds `.venv-gen`, installs torch(cu121)+diffusers+piper+
  insightface+SAM-pip deps, pulls `qwen3:8b` + `qwen2.5vl:7b`, runs the producer
  backfill. hil is now a self-contained producer.
- **GPU ABSENT** -> builds the lean `.venv` (pygame/opencv/numpy/imageio-ffmpeg/
  Pillow + piper). NO torch/SD. It prints the exact `setx LP_OLLAMA ...` line you
  apply in step (d).

Read the **`PATH SELECTED`** line and the **capability summary** in the
transcript -- that is hil's ground truth, and it determines whether you run step
(d). Overrides for testing: `-ForceCpu` / `-ForceGpu`; `-SkipBackfill` (GPU path,
install deps without baking).

> `bringup_host.ps1` creates the **same `.venv`** that the scheduled tasks in (c)
> target, so on the GPU-absent path (c) finds its interpreter. On the GPU path,
> note `deploy_host.ps1` in (c) will *also* create `.venv` (the lean runtime) --
> that is fine and idempotent; the two venvs (`.venv` runtime, `.venv-gen`
> producer) coexist exactly as on SC2.

---

## (c) Deploy the runtime show + register tasks (`deploy_host.ps1`)

`install/deploy_host.ps1` is one command to stand up the **runtime** show on any
Windows tailnet host: it stages the runtime code (robocopy, excluding
`.venv*`/`data`/media/caches), scps it to hil, creates the lean `.venv` with
`py -3.12`, then runs `install_tasks.ps1` on hil to register `lp-player` /
`lp-director` / `lp-watchdog` **at-logon** (reboot-survivable).

```powershell
# dev box -- helper already dot-sourced (pre-reqs). From the life repo root:
.\projects\living-portraits\install\deploy_host.ps1 -Target <HIL>

# non-default project root on hil:
.\projects\living-portraits\install\deploy_host.ps1 -Target <HIL> -RemoteRoot D:\shows\living-portraits
```

It self-verifies (pythonw present + 3 tasks registered) and prints a summary. It
deliberately does **not** sync `data\`/clips (that is step d) and does **not**
wire the Ollama endpoint (also step d).

> **Task principal gap (read this):** `install_tasks.ps1` pins
> `RUN_USER='immer'`. If hil's interactive user is **not** `immer`, the at-logon
> tasks register against the wrong principal and the player window will not land
> on hil's console session. `deploy_host.ps1` *warns* but does not fix it. If
> hil's user differs, edit `RUN_USER` in `install/install_tasks.ps1` to hil's
> interactive user before this step (or deploy as `immer`). See **Known gaps**.

---

## (d) Two-machine wiring -- ONLY if hil has NO GPU (sync assets + `LP_OLLAMA`)

**Skip this entire step on the all-on-hil (GPU-present) path** -- hil bakes its
own assets and runs Ollama locally.

### (d.1) Sync the baked assets SC2 -> hil

`install/sync_assets.ps1` pulls the per-slug gen files + the clip manifest from
SC2 and pushes them to hil. Default mode stages via the dev box (two hops, both
legs from the dev box -- no SC2->hil SSH trust required).

```powershell
# dev box -- preview first (lists what would sync, copies nothing)
powershell -NoProfile -ExecutionPolicy Bypass `
    -File .\projects\living-portraits\install\sync_assets.ps1 -Target <HIL> -DryRun

# then the real sync (discovers slugs from SC2's data\gen, or pin them):
powershell -NoProfile -ExecutionPolicy Bypass `
    -File .\projects\living-portraits\install\sync_assets.ps1 -Target <HIL> -Slugs phineas,seraphina
```

Per slug it syncs `data/gen/<slug>_{portrait,cutout,bg}.png` +
`data/gen/<slug>_rig.json`, plus the shared `data/clips/manifest.json`. It is
overwrite-only (no prune); re-run after any fresh SC2 bake. `-Direct` attempts a
single SC2->hil hop but needs SC2->hil SSH trust -- leave it off unless you have
set that up.

> If a slug shows per-file FAILs for `_cutout`/`_bg`/`_rig`, SC2 has a portrait
> but the bake is incomplete -- run `install/sc2_bringup.ps1` on SC2 (the
> producer backfill) first, then re-sync.

### (d.2) Point hil's director at SC2's qwen3 (the 2-line code edit + env var)

`director/stage_manager.py:24` hardcodes the local endpoint:

```python
OLLAMA = "http://127.0.0.1:11434/api/chat"
```

Make it env-overridable. This is a **conductor code edit** (neither
`sync_assets.ps1` nor `bringup_host.ps1` touches `stage_manager.py`). Replace
line 24 with:

```python
import os                                                       # with the other imports
OLLAMA = os.environ.get("LP_OLLAMA", "http://127.0.0.1:11434/api/chat")
```

Re-run `deploy_host.ps1` (step c) after the edit so hil gets the patched file, or
scp just `director/stage_manager.py` across. Then set the env var on hil so its
director calls SC2's Ollama, at a scope the scheduled task can see (Machine):

```powershell
# dev box -- set LP_OLLAMA on hil (Machine scope)
Invoke-RemotePS -Host_ <HIL> -Script @'
[Environment]::SetEnvironmentVariable("LP_OLLAMA","http://100.123.185.12:11434/api/chat","Machine")
'@
```

With `LP_OLLAMA` unset (the all-on-hil / SC2-local case) the constant falls back
to `127.0.0.1` and nothing changes.

### (d.3) SC2-side / ACL prerequisites for the remote qwen3 call

For hil to reach SC2's Ollama, two things must already be true on the SC2 / ACL
side (`sync_assets.ps1` neither checks nor changes them):

1. **SC2's Ollama binds beyond loopback.** Set `OLLAMA_HOST=0.0.0.0` on SC2 (a
   Machine env var) and restart Ollama, so `100.123.185.12:11434` answers from
   off-box (by default it only listens on `127.0.0.1`).
2. **Tailnet ACL permits hil -> SC2:11434.** Confirm the tailnet policy allows
   the hil node to reach SC2 on 11434 (see memory `reference_tailscale_api` /
   `project_tailnet_isolation` for the tagged-ACL model).

**Verify (d) from hil:**

```powershell
# dev box -- prove hil can hit SC2's Ollama over the tailnet
Invoke-RemotePS -Host_ <HIL> -Script @'
(Invoke-WebRequest -UseBasicParsing http://100.123.185.12:11434/api/tags -TimeoutSec 8).StatusCode
'@
# expect: 200  (and the body lists qwen3:8b)
```

---

## (e) Fit the panel geometry to hil's display (`panels.yaml`)

The panel layout is now a **config edit, not a code change**: `player.py` reads
its `PANELS` dict + window size from `panels.yaml` via
`runtime/panels.py:load_panels()`. The conductor wires it in `player.py` with one
line replacing the old hardcoded `PANELS`/`WINDOW_W`/`WINDOW_H` block:

```python
from panels import load_panels            # runtime/ is already on sys.path
PANELS, WINDOW_W, WINDOW_H = load_panels()
```

The shipped `panels.yaml` reproduces SC2's exact layout (A `0,0 256x256` maroon/
gold, B `256,0 192x192` teal/mint), and the window size is **derived** (bounding
box of every rect) -- there is no window size to edit. If hil's desktop
resolution or its LED sending-card's frame-grab origin differs, re-measure and
edit the rects here on hil:

```yaml
# C:\Users\immer\living-portraits\panels.yaml  (on hil)
version: 1
panels:
  - name: "A"
    rect: [0, 0, 256, 256]      # [x, y, w, h] in desktop pixels, sub-rect the card grabs
    bg: [38, 14, 16]
    accent: [210, 170, 90]
    char: "phineas"
  - name: "B"
    rect: [256, 0, 192, 192]
    bg: [12, 26, 28]
    accent: [120, 200, 190]
    char: "seraphina"
```

`runtime/panels.py` **degrades to today's layout** on any failure (yaml missing /
malformed / a single bad panel), announcing it on stderr but never crashing the
show -- a bad edit renders the SC2 layout, not a black screen. Validate the edit
on hil without launching the show:

```powershell
# dev box -- run the offline self-test on hil (no pygame/numpy/network)
Invoke-RemotePS -Host_ <HIL> -Script @'
C:\Users\immer\living-portraits\.venv\Scripts\python.exe C:\Users\immer\living-portraits\runtime\panels.py
'@
# expect: "self-test OK ..."; if you customized rects, eyeball the printed window box.
```

> `deploy_host.ps1` excludes `data\` but **does** ship the repo's `panels.yaml`
> (it lives at the project root, not under `data\`). Edit the copy **on hil**
> after deploy; a later `deploy_host.ps1` re-run will overwrite it with the repo
> default, so keep hil's measured values in the repo's `panels.yaml` if they
> become canonical.

---

## (f) Start the show and verify it on the real panels

The at-logon tasks fire when `immer` signs in. To start the show now without a
sign-out/in, trigger the launch tasks on hil (the watchdog would also restart
them within 5 min, but do not wait):

```powershell
# dev box -- start player + director on hil now
Invoke-RemotePS -Host_ <HIL> -Script @'
schtasks /Run /TN lp-player
schtasks /Run /TN lp-director
Start-Sleep -Seconds 3
Get-ScheduledTask -TaskName lp-player,lp-director,lp-watchdog |
    Select-Object TaskName,State,@{N="RunAs";E={$_.Principal.UserId}} | Format-Table -AutoSize
'@
```

Verify the processes are alive and the director is writing beats:

```powershell
# dev box -- confirm both pythonw processes + a fresh stage_state.json on hil
Invoke-RemotePS -Host_ <HIL> -Script @'
Get-CimInstance Win32_Process -Filter "Name='pythonw.exe'" |
    Where-Object { $_.CommandLine -match "player.py|stage_manager.py" } |
    Select-Object ProcessId,CommandLine | Format-Table -AutoSize -Wrap
$state = "C:\Users\immer\living-portraits\data\stage_state.json"
if (Test-Path $state) {
    "stage_state.json age (min): {0:N1}" -f ((Get-Date)-(Get-Item $state).LastWriteTime).TotalMinutes
    Get-Content $state -Raw
} else { "stage_state.json NOT present yet -- director has not written a first beat" }
'@
```

Then **look at hil's screen / the panels** (per memory
`feedback_playwright_verify_first` -- "build green != correct"; the equivalent
here is "tasks running != the panels show the play"). The player pins a
borderless `448x256` window at `(0,0)`. Confirm: the maroon Phineas frame (A) and
teal Seraphina frame (B) render, the liveness marker + wall clock move, and the
fourth-wall asides update each beat. If the window is mis-positioned or sized
wrong for hil's monitor, return to step (e) and re-measure `panels.yaml`.

> Watchdog sanity: `data\watchdog.log` on hil logs an hourly heartbeat + any
> restart. A live director that has paused writing `stage_state.json` during a
> render is **not** a fault (the watchdog only restarts on process *absence*).

---

## (g) Confirm the LED sending-card mapping (on-site, the last physical seam)

Everything above is verifiable over the tailnet. The **only** thing that needs a
human at the panels is the LED sending card's frame grab: confirm the card grabs
the window's region from hil's desktop and maps each sub-rect to the right
physical panel.

Walk it on-site:

1. The player paints **panel A** (the larger, `256x256`, maroon/gold, Phineas) at
   desktop `(0,0)`, and **panel B** (`192x192`, teal/mint, Seraphina) at
   `(256,0)`. Confirm the **physical** large panel shows A and the small panel
   shows B -- if they are swapped, swap the card's two source rects (or swap the
   `name:` order / rects in `panels.yaml`, then re-run the step-e self-test).
2. Confirm the card's grab **origin + size** matches `panels.yaml`'s bounding box
   (`448x256` for the shipped A+B). A card grabbing from a different origin is the
   classic "portraits are half-off the panel" symptom -- re-measure the grab
   origin and set the rects in `panels.yaml` (step e) to match, **not** the code.
3. Confirm there is no stray console window or taskbar in the grabbed region (the
   player runs windowless via `pythonw`; nothing else should paint into
   `0,0..448,256`).

When A and B land on the correct physical panels at the right size, the migration
is complete: the show lives on hil08rd, durable across reboots, with SC2 as the
(optional, no-GPU-case) bakery + qwen3 backend over the tailnet.

---

## Quick reference -- the ordered conductor commands

```powershell
# --- pre-reqs (dev box) ---
. C:\Users\jtole\Documents\2026\life\scripts\invoke-remote-ps.ps1

# --- (a) verify SSH to hil (after enabling it on hil; see step a) ---
ssh -o BatchMode=yes -o ConnectTimeout=10 <HIL> "hostname"

# --- (b) bring up hil (GPU-detect) ---
scp ...\install\bringup_host.ps1 "<HIL>:C:/Users/immer/living-portraits/install/bringup_host.ps1"
Invoke-RemotePS -Host_ <HIL> -Script '& powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\immer\living-portraits\install\bringup_host.ps1'

# --- (c) deploy runtime + register tasks ---
.\projects\living-portraits\install\deploy_host.ps1 -Target <HIL>

# --- (d) NO-GPU ONLY: sync assets + LP_OLLAMA (after editing stage_manager.py:24) ---
powershell -File .\projects\living-portraits\install\sync_assets.ps1 -Target <HIL> -Slugs phineas,seraphina
Invoke-RemotePS -Host_ <HIL> -Script '[Environment]::SetEnvironmentVariable("LP_OLLAMA","http://100.123.185.12:11434/api/chat","Machine")'

# --- (e) fit panels.yaml on hil, then self-test ---
Invoke-RemotePS -Host_ <HIL> -Script 'C:\Users\immer\living-portraits\.venv\Scripts\python.exe C:\Users\immer\living-portraits\runtime\panels.py'

# --- (f) start + verify ---
Invoke-RemotePS -Host_ <HIL> -Script 'schtasks /Run /TN lp-player; schtasks /Run /TN lp-director'

# --- (g) confirm LED-card mapping ON-SITE (no remote command) ---
```

---

## Known gaps / things to watch

1. **Task principal pinned to `immer`.** `install_tasks.ps1` hardcodes
   `RUN_USER='immer'`. If hil's interactive user differs, the at-logon player/
   director tasks register against the wrong principal and the window will not
   land on hil's console session. `deploy_host.ps1` warns but does not fix it --
   edit `RUN_USER` (or deploy as `immer`) before step (c). *(Surfaced by the
   deployer; this file owns flagging it, not fixing `install_tasks.ps1`.)*
2. **The `LP_OLLAMA` code edit is manual.** Making `stage_manager.py:24`
   env-overridable is a 2-line conductor edit; the tooling deliberately does not
   patch `stage_manager.py`. Forgetting it on a no-GPU hil leaves the director
   pointed at a non-existent local Ollama (it will fail every beat).
3. **SC2 Ollama bind + ACL are out-of-band.** The remote qwen3 call needs SC2's
   `OLLAMA_HOST=0.0.0.0` **and** a tailnet ACL allowing hil -> SC2:11434. Neither
   is set or checked by any migration script -- verify with the step-(d) probe.
4. **Asset sync is overwrite-only (no prune).** Retiring a character on SC2 does
   not delete its stale files on hil; clean up manually. Only
   `data/clips/manifest.json` is synced for clips -- when real clip *media* lands
   on SC2, `sync_assets.ps1`'s `$relPaths` must be extended to pull it (today the
   library is synthetic-placeholder, so the manifest alone is the whole library).
5. **`panels.yaml` lives in the repo and re-deploys.** Edit it **on hil** for
   hil-specific geometry, but a later `deploy_host.ps1` overwrites it with the
   repo default. If hil's measured layout becomes canonical, commit it to the
   repo's `panels.yaml`.
6. **All-on-hil (GPU on hil) is the lighter end state but unverified here.** If
   hil has a GPU, `bringup_host.ps1` covers the producer install, but the
   end-to-end bake-on-hil path has not been exercised in this migration -- run a
   single `orchestrate.py --all <slug> --allow-generate` on hil and confirm a
   clean clip-row before declaring SC2 fully detachable.
7. **The LED-card grab is the one un-remoteable step.** Steps (a)-(f) are
   verifiable over the tailnet; (g) requires eyes on the panels. Nothing in the
   tooling can confirm the physical A/B mapping.

---

*`projects/living-portraits/MIGRATION.md` + `living-portraits-architecture-v4.svg`
. 2026-05-26 . supersedes the single-host (SC2) deploy assumption in `README.md`
and `install/BRINGUP.md`.*

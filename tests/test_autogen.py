"""test_autogen.py -- the no-cost autogen layer: proposal queue, budget, lint+labels,
and the atomic graph merge. No MJ, no network (the MJ client is imported lazily)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline import autogen
from runtime import video_graph


def test_add_proposal_dedup_and_status(tmp_path, monkeypatch):
    monkeypatch.setattr(autogen, "PROPOSALS", tmp_path / "proposals.json")
    p = {"character": "phineas", "label": "reading", "still_prompt": "x", "proposed_at": 100}
    id1 = autogen.add_proposal(p)
    id2 = autogen.add_proposal(p)                 # same (char,label) while pending -> dedup
    assert id1 == id2
    assert len(autogen.load_proposals()["proposals"]) == 1
    autogen.set_status(id1, "approved")
    assert [x["id"] for x in autogen._by_status("approved")] == [id1]


def test_budget_caps_per_day(tmp_path, monkeypatch):
    monkeypatch.setattr(autogen, "BUDGET", tmp_path / "budget.json")
    monkeypatch.setattr(autogen, "DAILY_CAP", 2)
    assert autogen.budget_left("phineas") == 2
    autogen._spend("phineas")
    assert autogen.budget_left("phineas") == 1
    autogen._spend("phineas")
    assert autogen.budget_left("phineas") == 0


def test_plan_lints_and_derives_labels():
    v, lab = autogen.plan({
        "character": "phineas", "label": "reading", "hub": "anchor",
        "still_prompt": "a tragedian reading a letter by candlelight",
        "transition_motion": "he lifts and unfolds a letter",
        "idles": [{"id": "reading_0", "motion": "he reads intently"}],
        "negatives": ["text", "naked"]})
    assert v["ok"] is True
    assert "naked" not in v["safe_negatives"]            # body word stripped from negatives
    assert lab["fwd"] == "anchor_to_reading" and lab["rev"] == "reading_to_anchor"


def test_plan_rejects_unsafe_still():
    v, _ = autogen.plan({"character": "phineas", "label": "x", "hub": "anchor",
                         "still_prompt": "a nude figure reclining", "transition_motion": "", "idles": []})
    assert v["ok"] is False


def test_autogen_additions_is_atomic(monkeypatch):
    spec = {"characters": {"phineas": {"poses": {
        "reading": {"node_image": "data/gen/phineas_reading.png", "still_prompt": "x", "hub": "anchor",
                    "transition": {"label": "anchor_to_reading", "reverse_label": "reading_to_anchor", "motion": "m"},
                    "idles": [{"id": "reading_0", "motion": "i"}]}}}}}
    monkeypatch.setattr(video_graph, "_load_autogen", lambda: spec)
    # every declared edge has a gif -> pose is READY and merges
    monkeypatch.setattr(video_graph, "_variant_gifs",
                        lambda c, l: [(0, "data/clips/_proto/%s_%s_v0.gif" % (c, l))])
    nodes, edges, skipped = video_graph._autogen_additions()
    assert "reading" in nodes.get("phineas", {})
    assert {"anchor_to_reading", "reading_to_anchor", "reading_0"} <= {e[2] for e in edges}
    assert skipped == []
    # a missing gif -> the WHOLE pose is skipped (never half-merged -> never strands the walk)
    monkeypatch.setattr(video_graph, "_variant_gifs", lambda c, l: [])
    nodes2, edges2, skipped2 = video_graph._autogen_additions()
    assert nodes2 == {} and edges2 == [] and "phineas:reading" in skipped2


# --------------------------------------------------------------- web-not-star connectivity

def _gif_all(c, l):
    return [(0, "data/clips/_proto/%s_%s_v0.gif" % (c, l))]


def _reading_spec(extra=None):
    pose = {"node_image": "data/gen/phineas_reading.png", "still_prompt": "x", "hub": "anchor",
            "transition": {"label": "anchor_to_reading", "reverse_label": "reading_to_anchor", "motion": "m"},
            "idles": [{"id": "reading_0", "motion": "i"}]}
    if extra is not None:
        pose["extra_links"] = extra
    return {"characters": {"phineas": {"poses": {"reading": pose}}}}


def test_plan_lints_extra_link_motions():
    """An unsafe motion in the OPTIONAL second path must fail the whole proposal (same mj_safe
    pass as the hub motions) -- the web link can't smuggle an unsafe submit past the gate."""
    v, _ = autogen.plan({
        "character": "phineas", "label": "reading", "hub": "anchor",
        "still_prompt": "a tragedian reading a letter", "transition_motion": "he lifts a letter",
        "idles": [{"id": "reading_0", "motion": "he reads"}],
        "extra_links": [{"sibling": "glower", "motion": "he strips off his nude clothing", "reverse_motion": ""}]})
    assert v["ok"] is False


def test_autogen_additions_emits_extra_links(monkeypatch):
    """A merged pose with a present, non-dangling sibling link emits BOTH extra transition edges
    -- this is the star->web mesh (glower<->reading, on top of the anchor<->reading spoke)."""
    extra = [{"sibling": "glower", "label": "glower_to_reading",
              "reverse_label": "reading_to_glower", "motion": "lm"}]
    monkeypatch.setattr(video_graph, "_load_autogen", lambda: _reading_spec(extra))
    monkeypatch.setattr(video_graph, "_variant_gifs", _gif_all)   # every label has a gif
    nodes, edges, skipped = video_graph._autogen_additions()
    labels = {e[2] for e in edges}
    assert {"anchor_to_reading", "reading_to_anchor", "glower_to_reading", "reading_to_glower"} <= labels
    # the extra edges run between the real sibling pose and the new pose (both directions)
    by_label = {e[2]: (e[3], e[4]) for e in edges}
    assert by_label["glower_to_reading"] == ("glower", "reading")
    assert by_label["reading_to_glower"] == ("reading", "glower")
    assert skipped == []


def test_autogen_additions_extra_link_optional_when_gif_missing(monkeypatch):
    """If the sibling-link clips never landed (gif missing) the pose STILL merges on its core
    hub edges -- a failed second path never costs us the whole pose."""
    extra = [{"sibling": "glower", "label": "glower_to_reading",
              "reverse_label": "reading_to_glower", "motion": "lm"}]
    core = {"anchor_to_reading", "reading_to_anchor", "reading_0"}
    monkeypatch.setattr(video_graph, "_load_autogen", lambda: _reading_spec(extra))
    monkeypatch.setattr(video_graph, "_variant_gifs", lambda c, l: _gif_all(c, l) if l in core else [])
    nodes, edges, skipped = video_graph._autogen_additions()
    labels = {e[2] for e in edges}
    assert "reading" in nodes.get("phineas", {})          # core pose merged
    assert core <= labels                                  # core edges present
    assert "glower_to_reading" not in labels and "reading_to_glower" not in labels


def test_autogen_additions_extra_link_dangling_sibling_dropped(monkeypatch):
    """A link to a sibling that is NOT a real node is dropped -- one bad link can never emit a
    dangling edge that would fail build()'s walk-safety and sink the whole graph."""
    extra = [{"sibling": "ghost", "label": "ghost_to_reading",
              "reverse_label": "reading_to_ghost", "motion": "lm"}]
    monkeypatch.setattr(video_graph, "_load_autogen", lambda: _reading_spec(extra))
    monkeypatch.setattr(video_graph, "_variant_gifs", _gif_all)
    nodes, edges, skipped = video_graph._autogen_additions()
    assert "reading" in nodes.get("phineas", {})          # core pose still merges
    assert not any("ghost" in (e[3], e[4]) for e in edges)   # no edge touches the phantom node


def test_extra_link_is_walk_safe():
    """Two leaves cross-linked by an extra edge stay walk-safe (no ERRORs): the mesh only ADDS
    edges, so reach + return invariants still hold."""
    g = video_graph.VideoGraph()
    for pose in ("anchor", "reading", "glower"):
        g.add_node("phineas:%s" % pose, character="phineas", pose=pose,
                   image="x.png", gen_prompt="p")
    def tr(label, fr, to):
        g.add_edge(id="phineas/%s/v0" % label, character="phineas", kind="transition",
                   label=label, **{"from": "phineas:%s" % fr, "to": "phineas:%s" % to})
    def idle(label, at):
        g.add_edge(id="phineas/%s/v0" % label, character="phineas", kind="idle",
                   label=label, **{"from": "phineas:%s" % at, "to": "phineas:%s" % at})
    # anchor hub <-> two leaf poses
    tr("anchor_to_reading", "anchor", "reading"); tr("reading_to_anchor", "reading", "anchor")
    tr("anchor_to_glower", "anchor", "glower");   tr("glower_to_anchor", "glower", "anchor")
    for n in ("anchor", "reading", "glower"):
        idle("%s_idle" % n, n)
    # the WEB edge: reading <-> glower directly
    tr("glower_to_reading", "glower", "reading"); tr("reading_to_glower", "reading", "glower")
    errs = [m for lvl, m in g.validate() if lvl == "ERROR"]
    assert errs == []


def test_record_pose_persists_extra_links(tmp_path, monkeypatch):
    monkeypatch.setattr(autogen, "AUTOGEN", tmp_path / "autogen_poses.json")
    p = {"character": "phineas", "label": "reading", "still_prompt": "x",
         "transition_motion": "m", "idles": [{"id": "reading_0", "motion": "i"}]}
    links = [{"sibling": "glower", "label": "glower_to_reading",
              "reverse_label": "reading_to_glower", "motion": "lm"}]
    autogen._record_pose(p, "anchor", "anchor_to_reading", "reading_to_anchor", links)
    saved = autogen._load(autogen.AUTOGEN, {})["characters"]["phineas"]["poses"]["reading"]
    assert saved["extra_links"] == links


# ------------------------------------------------------------ proposal-side connectivity

def _fake_graph():
    """anchor hub + two leaf poses (each degree 1) so siblings exist and are leaves-first."""
    g = video_graph.VideoGraph()
    for pose in ("anchor", "glower", "swoon"):
        g.add_node("phineas:%s" % pose, character="phineas", pose=pose, image="x.png")
    for label, fr, to in (("a2g", "anchor", "glower"), ("g2a", "glower", "anchor"),
                          ("a2s", "anchor", "swoon"), ("s2a", "swoon", "anchor")):
        g.add_edge(id="phineas/%s/v0" % label, character="phineas", kind="transition",
                   label=label, **{"from": "phineas:%s" % fr, "to": "phineas:%s" % to})
    return g


def test_sibling_candidates_leaves_first_and_excludes():
    from director import heartbeat
    g = _fake_graph()
    cands = heartbeat._sibling_candidates(g, "phineas", hub="anchor")
    assert "anchor" not in cands                       # hub excluded
    assert set(cands) == {"glower", "swoon"}           # the two leaves offered
    cands2 = heartbeat._sibling_candidates(g, "phineas", hub="anchor", exclude={"swoon"})
    assert cands2 == ["glower"]                         # bedtime/excluded pose dropped


def test_propose_pose_authors_idle_count_and_link(tmp_path, monkeypatch):
    from director import heartbeat
    monkeypatch.setattr(autogen, "PROPOSALS", tmp_path / "proposals.json")
    monkeypatch.setattr(heartbeat.video_graph.VideoGraph, "load", staticmethod(_fake_graph))
    monkeypatch.setattr(heartbeat, "_current_pose", lambda g, c: ("phineas:anchor", 0, None))
    monkeypatch.setattr(heartbeat, "_load_char_spec", lambda c: {})
    monkeypatch.setattr(heartbeat.circadian, "bedtime_poses", lambda spec, c: set())
    monkeypatch.setattr(heartbeat.mj_safe, "check",
                        lambda *a, **k: {"ok": True, "hard": [], "soft": [], "safe_negatives": []})
    monkeypatch.setattr(heartbeat.llm, "complete_json", lambda *a, **k: {
        "label": "reading", "still_prompt": "a tragedian reading", "transition_motion": "t",
        "reverse_motion": "r", "idles": ["i1", "i2", "i3", "i4", "i5"],   # over-supplied
        "link_to": "glower", "link_motion": "lm", "link_reverse_motion": "lr", "reason": "why"})
    pid = heartbeat.propose_pose("phineas", model="m", dry_run=False, log=lambda *a: None)
    assert pid
    saved = autogen.load_proposals()["proposals"][0]
    assert len(saved["idles"]) == heartbeat.IDLE_COUNT          # capped to the named constant
    assert len(saved["extra_links"]) == 1 and saved["extra_links"][0]["sibling"] == "glower"
    assert saved["extra_links"][0]["motion"] == "lm"


def test_propose_pose_falls_back_to_hub_only_on_bad_link(tmp_path, monkeypatch):
    """If the LLM names a link_to that isn't an offered candidate, we ship hub-only (fail-safe to
    today's behavior) instead of inventing an edge to a pose that doesn't exist."""
    from director import heartbeat
    monkeypatch.setattr(autogen, "PROPOSALS", tmp_path / "proposals.json")
    monkeypatch.setattr(heartbeat.video_graph.VideoGraph, "load", staticmethod(_fake_graph))
    monkeypatch.setattr(heartbeat, "_current_pose", lambda g, c: ("phineas:anchor", 0, None))
    monkeypatch.setattr(heartbeat, "_load_char_spec", lambda c: {})
    monkeypatch.setattr(heartbeat.circadian, "bedtime_poses", lambda spec, c: set())
    monkeypatch.setattr(heartbeat.mj_safe, "check",
                        lambda *a, **k: {"ok": True, "hard": [], "soft": [], "safe_negatives": []})
    monkeypatch.setattr(heartbeat.llm, "complete_json", lambda *a, **k: {
        "label": "reading", "still_prompt": "a tragedian reading", "transition_motion": "t",
        "reverse_motion": "r", "idles": ["i1", "i2"],
        "link_to": "does_not_exist", "link_motion": "lm", "reason": "why"})
    pid = heartbeat.propose_pose("phineas", model="m", dry_run=False, log=lambda *a: None)
    assert pid
    saved = autogen.load_proposals()["proposals"][0]
    assert saved["extra_links"] == []


# --------------------------------------------------------------------------- video takes
class _FakeClient:
    """Stands in for the hil-only MJ client. `available` is how many of the 4-up grid's
    video variants this account actually returns."""

    def __init__(self, available=4):
        self.available = available
        self.asked = []

    def download_video(self, job_id, variant=0, out_path=None):
        self.asked.append(variant)
        if variant >= self.available:
            raise RuntimeError("no variant %d on job %s" % (variant, job_id))
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        Path(out_path).write_bytes(b"mp4")


def _stub_gif(monkeypatch, tmp_path):
    """Skip the real decode (imageio/PIL): just drop a file where the gif would land,
    creating the parent dir the way the real _mp4_to_gif does."""
    monkeypatch.setattr(autogen, "MIND", tmp_path / "mind")
    (tmp_path / "mind").mkdir(parents=True, exist_ok=True)

    def _fake(mp4, gif, **kw):
        Path(gif).parent.mkdir(parents=True, exist_ok=True)
        Path(gif).write_bytes(b"gif")
        return 1

    monkeypatch.setattr(autogen, "_mp4_to_gif", _fake)


def test_video_to_gif_pulls_every_paid_for_take(tmp_path, monkeypatch):
    # MJ bills a 4-up grid; video_graph globs <char>_<label>_v*.gif into one edge row per take.
    _stub_gif(monkeypatch, tmp_path)
    client = _FakeClient(available=4)
    dst = tmp_path / "proto" / "phineas_a2g_v0.gif"
    landed = autogen._video_to_gif(client, "job1", dst)

    assert landed == 4
    assert client.asked == [0, 1, 2, 3]
    assert sorted(p.name for p in (tmp_path / "proto").glob("*.gif")) == [
        "phineas_a2g_v0.gif", "phineas_a2g_v1.gif", "phineas_a2g_v2.gif", "phineas_a2g_v3.gif"]


def test_video_to_gif_degrades_to_one_take_without_raising(tmp_path, monkeypatch):
    # An account/API that only ever returns one video must behave EXACTLY as before this
    # change -- the edge still lands, nothing raises, and we stop asking after the first gap.
    _stub_gif(monkeypatch, tmp_path)
    client = _FakeClient(available=1)
    dst = tmp_path / "proto" / "phineas_a2g_v0.gif"
    landed = autogen._video_to_gif(client, "job1", dst)

    assert landed == 1
    assert client.asked == [0, 1]                      # asked once more, then gave up
    assert [p.name for p in (tmp_path / "proto").glob("*.gif")] == ["phineas_a2g_v0.gif"]


def test_video_to_gif_still_fails_when_the_edge_itself_is_lost(tmp_path, monkeypatch):
    # Take 0 IS the edge. Its loss must stay fatal so the caller records no half-built pose.
    _stub_gif(monkeypatch, tmp_path)
    client = _FakeClient(available=0)
    try:
        autogen._video_to_gif(client, "job1", tmp_path / "proto" / "phineas_a2g_v0.gif")
    except RuntimeError:
        return
    raise AssertionError("a missing variant 0 must raise, not degrade")


def test_video_takes_become_interchangeable_edge_rows(tmp_path, monkeypatch):
    # The whole point: four takes on disk -> four edge rows the walk can pick between.
    _stub_gif(monkeypatch, tmp_path)
    # _variant_gifs reports paths relative to the project root, so the fake proto dir has to
    # live under a root it can subtract -- point BOTH at tmp.
    monkeypatch.setattr(video_graph, "ROOT", tmp_path)
    monkeypatch.setattr(video_graph, "PROTO", tmp_path / "proto")
    autogen._video_to_gif(_FakeClient(available=4), "job1", tmp_path / "proto" / "phineas_a2g_v0.gif")

    found = video_graph._variant_gifs("phineas", "a2g")
    assert [v for v, _g in found] == [0, 1, 2, 3]
    assert found[2][1] == "proto/phineas_a2g_v2.gif"


def test_video_takes_one_is_the_revert_switch(tmp_path, monkeypatch):
    # VIDEO_TAKES = 1 must reproduce the pre-change behaviour exactly: one download, one gif.
    _stub_gif(monkeypatch, tmp_path)
    client = _FakeClient(available=4)
    landed = autogen._video_to_gif(client, "job1", tmp_path / "proto" / "phineas_a2g_v0.gif", takes=1)

    assert landed == 1
    assert client.asked == [0]                         # never even asks for a second variant
    assert [p.name for p in (tmp_path / "proto").glob("*.gif")] == ["phineas_a2g_v0.gif"]

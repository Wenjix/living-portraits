"""test_heartbeat.py -- the slow brain's WRITE side: urgency->route, arrival, and the
journalled gap on an LLM blip. Pure + offline (the LLM and the graph are stubbed).

Covers the three contracts the walker and the next tick depend on:
  * route      -- intent.json carries "route", which _preview_graph.py feeds to
                  policy.ROUTE_PULL (beeline 7.0 vs wander 2.0). Unparseable -> "wander",
                  which is the behaviour that shipped, so a confused model changes nothing.
  * arrived    -- the journal records whether the body reached the goal it last announced,
                  and stays SILENT (None) when the question is meaningless: nothing was set,
                  or the goal already aged past the walker's release TTL.
  * the gap    -- an LLM error still appends a line, so a dead gateway can never freeze the
                  character's memory clock while the body keeps walking. That line is marked
                  err and must never reach the character's own inner monologue.
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from director import heartbeat as hb
from director import llm
from runtime import mind


# --------------------------------------------------------------------------- fakes
class _Graph:
    """The slice of VideoGraph the heartbeat actually touches."""

    def __init__(self):
        self.nodes = {
            "phineas:anchor": {"character": "phineas", "pose": "anchor", "gen_prompt": "the hub"},
            "phineas:glower": {"character": "phineas", "pose": "glower", "gen_prompt": "the glower"},
        }
        self.edges = [
            {"id": "phineas/breathe/v0", "kind": "idle", "label": "breathe",
             "from": "phineas:anchor", "to": "phineas:anchor"},
            {"id": "phineas/a2g/v0", "kind": "transition", "label": "a2g",
             "from": "phineas:anchor", "to": "phineas:glower"},
            {"id": "phineas/g2a/v0", "kind": "transition", "label": "g2a",
             "from": "phineas:glower", "to": "phineas:anchor"},
        ]

    def poses(self, character):
        return [n for n in self.nodes if n.startswith(character + ":")]

    def edges_from(self, node):
        return [e for e in self.edges if e.get("from") == node]


def _offline(monkeypatch, tmp_path, reply=None, error=False):
    """Point the journal + pose dirs at tmp, silence the weather line, stub the LLM."""
    monkeypatch.setattr(hb, "JOURNAL_DIR", tmp_path / "journal")
    monkeypatch.setattr(hb, "POSE_DIR", tmp_path / "pose")
    monkeypatch.setattr(hb, "INTENT_PATH", tmp_path / "intent.json")
    monkeypatch.setattr(hb.ctx, "context_line", lambda *a, **k: "")

    def _complete_json(system, user, **kw):
        if error:
            raise llm.LLMError("gateway timeout")
        return reply or {}

    monkeypatch.setattr(hb.llm, "complete_json", _complete_json)


def _pose(tmp_path, node, character="phineas", **extra):
    """Write the walker's pose file (the walker is its sole writer in production)."""
    d = tmp_path / "pose"
    d.mkdir(parents=True, exist_ok=True)
    payload = {"node": node, "dwell": 0}
    payload.update(extra)
    (d / (character + ".json")).write_text(json.dumps(payload), encoding="utf-8")


def _journal(tmp_path, character="phineas"):
    p = tmp_path / "journal" / (character + ".jsonl")
    if not p.exists():
        return []
    return [json.loads(ln) for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def _log(_msg):
    pass


# --------------------------------------------------------------------------- _norm_route
def test_route_exact_values_pass_through():
    assert hb._norm_route("beeline") == "beeline"
    assert hb._norm_route("wander") == "wander"
    assert hb._norm_route("  BEELINE ") == "beeline"


def test_route_keyword_cascade_catches_natural_answers():
    # a model asked how urgently it wants something does not answer "beeline"
    for phrase in ("desperately, now", "at once", "I must go immediately", "straight there"):
        assert hb._norm_route(phrase) == "beeline", phrase


def test_route_survives_a_non_string_answer():
    # "urgency" is the field most likely to make a model answer on a 1-10 scale, and an
    # unguarded .strip() here aborts the WHOLE tick -- discarding the other character's good
    # decision and writing no intent at all. policy._mood_bias coerces with str() for this reason.
    for raw in (7, 0, True, False, 0.5, ["urgent"], {"a": 1}):
        assert hb._norm_route(raw) in hb.ROUTES, raw


def test_as_text_flattens_whatever_json_hands_back():
    assert hb._as_text("x") == "x"
    assert hb._as_text(None) == ""
    assert hb._as_text(7) == "7"
    assert hb._as_text(["a"]) == "['a']"        # a string -> hashable -> the set lookup degrades


def test_route_defaults_to_the_shipped_behaviour():
    # wander (pull 2.0) is what every goal walk did before this key existed -- an empty,
    # missing or unrecognised answer must not change the wall.
    for raw in (None, "", "   ", "languid", "{}"):
        assert hb._norm_route(raw) == hb.DEFAULT_ROUTE == "wander"


# --------------------------------------------------------------------------- _arrival
def test_arrival_is_silent_when_nothing_was_being_pursued():
    assert hb._arrival(None, "phineas:anchor") is None
    assert hb._arrival({}, "phineas:anchor") is None


def test_arrival_true_when_standing_on_the_goal():
    now = time.time()
    assert hb._arrival({"goal": "phineas:glower", "set_at": now - 60}, "phineas:glower") is True


def test_arrival_stays_silent_when_the_walker_cannot_say():
    # The policy walk only WEIGHTS the goal (GOAL_HOLD_BOOST in, AWAY_PENALTY out) -- it never
    # pins -- so "not standing there now" does not mean "never got there". With no `reached`
    # stamp we genuinely cannot tell, and accusing the character of failing would be a lie.
    now = time.time()
    assert hb._arrival({"goal": "phineas:glower", "set_at": now - 60}, "phineas:anchor") is None


def test_arrival_uses_the_walkers_reached_stamp():
    now = time.time()
    prev = {"goal": "phineas:glower", "set_at": now - 60}
    # arrived, held a while, then drifted back to anchor -> still an arrival
    assert hb._arrival(prev, "phineas:anchor", reached="phineas:glower") is True
    # the last place it landed was somewhere else -> it really did not get there
    assert hb._arrival(prev, "phineas:anchor", reached="phineas:swoon") is False


def test_arrival_is_silent_once_the_goal_outlived_the_walkers_ttl():
    # past mind.DEFAULT_MAX_AGE the walker has RELEASED the goal, so "did not arrive" would
    # blame the character for something nothing was chasing.
    stale = time.time() - (mind.DEFAULT_MAX_AGE + 60)
    assert hb._arrival({"goal": "phineas:glower", "set_at": stale}, "phineas:anchor") is None


# --------------------------------------------------------------------------- _journal_tail
def test_journal_tail_never_shows_the_character_its_own_silence(monkeypatch, tmp_path):
    monkeypatch.setattr(hb, "JOURNAL_DIR", tmp_path / "journal")
    for entry in ({"pose": "anchor", "mood": "grand", "reason": "I hold the room."},
                  {"pose": "anchor", "mood": "", "reason": "", "err": 1},
                  {"pose": "anchor", "mood": "wry", "reason": "Again, then."}):
        hb._append_journal("phineas", entry)
    tail = hb._journal_tail("phineas")
    assert len(tail) == 2
    assert all("feeling ?" not in line for line in tail)
    assert "I hold the room." in tail[0] and "Again, then." in tail[1]


def test_journal_tail_marks_a_goal_the_body_did_not_reach(monkeypatch, tmp_path):
    monkeypatch.setattr(hb, "JOURNAL_DIR", tmp_path / "journal")
    hb._append_journal("phineas", {"pose": "anchor", "mood": "thwarted",
                                   "reason": "I meant to be elsewhere.", "arrived": False})
    hb._append_journal("phineas", {"pose": "glower", "mood": "smug",
                                   "reason": "And here I am.", "arrived": True})
    tail = hb._journal_tail("phineas")
    assert "did not get there" in tail[0]
    assert "did not get there" not in tail[1]


def test_journal_tail_still_returns_at_most_n_after_filtering(monkeypatch, tmp_path):
    monkeypatch.setattr(hb, "JOURNAL_DIR", tmp_path / "journal")
    for i in range(40):
        hb._append_journal("phineas", {"pose": "anchor", "mood": "m", "reason": "line %d" % i})
    tail = hb._journal_tail("phineas")
    assert len(tail) == hb.JOURNAL_TAIL
    assert "line 39" in tail[-1]            # the widened read window still ends at the newest


# --------------------------------------------------------------------------- decide_character
def test_decide_records_route_and_arrival(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path,
             reply={"goal": "phineas:glower", "mood": "restless",
                    "urgency": "beeline", "reason": "Enough of this wall."})
    # asked for glower; the walker last landed on anchor, so it really did not get there
    _pose(tmp_path, "phineas:anchor", reached="phineas:anchor")
    prev = {"goal": "phineas:glower", "set_at": time.time() - 60}
    goal, mood, route = hb.decide_character(_Graph(), {}, "phineas", 14, "m", False, _log, prev=prev)

    assert (goal, mood, route) == ("phineas:glower", "restless", "beeline")
    line = _journal(tmp_path)[-1]
    assert line["route"] == "beeline"
    assert line["arrived"] is False


def test_decide_omits_arrived_when_there_was_no_prior_goal(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path,
             reply={"goal": "phineas:glower", "mood": "idle", "reason": "Why not."})
    hb.decide_character(_Graph(), {}, "phineas", 14, "m", False, _log, prev=None)
    line = _journal(tmp_path)[-1]
    assert "arrived" not in line             # silent, not a guess
    assert line["route"] == "wander"         # no urgency offered -> the shipped default


def test_llm_error_keeps_the_intent_but_never_the_silence(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path, error=True)
    prev = {"goal": "phineas:glower", "set_at": time.time() - 60}
    goal, mood, route = hb.decide_character(_Graph(), {}, "phineas", 14, "m", False, _log, prev=prev)

    assert goal == "__keep__"                # the walker keeps the last good goal
    line = _journal(tmp_path)[-1]
    assert line["err"] == 1                  # ...but the memory clock still ticked
    assert line["goal"] == "phineas:glower"
    assert hb._journal_tail("phineas") == []  # and the character never reads its own outage


def test_dry_run_writes_no_journal_on_either_path(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path, reply={"goal": "phineas:glower", "mood": "m", "reason": "r"})
    hb.decide_character(_Graph(), {}, "phineas", 14, "m", True, _log, prev=None)
    assert _journal(tmp_path) == []
    _offline(monkeypatch, tmp_path, error=True)
    hb.decide_character(_Graph(), {}, "phineas", 14, "m", True, _log, prev=None)
    assert _journal(tmp_path) == []


def test_a_non_string_urgency_does_not_kill_the_decision(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path,
             reply={"goal": "phineas:glower", "mood": "restless", "urgency": 7, "reason": "Now."})
    goal, mood, route = hb.decide_character(_Graph(), {}, "phineas", 14, "m", False, _log, prev=None)
    assert goal == "phineas:glower" and route in hb.ROUTES


def test_a_structured_goal_degrades_instead_of_raising(monkeypatch, tmp_path):
    # json.loads can hand back a list for any key; `goal not in allowed` would raise TypeError
    # on an unhashable value, so coercion has to happen before the membership test.
    _offline(monkeypatch, tmp_path,
             reply={"goal": ["phineas:glower"], "mood": {"x": 1}, "urgency": None, "reason": 3})
    goal, mood, route = hb.decide_character(_Graph(), {}, "phineas", 14, "m", False, _log, prev=None)
    assert goal == "phineas:anchor"          # not on the menu -> stay put, the designed degrade
    assert route == hb.DEFAULT_ROUTE


# --------------------------------------------------------------------------- tick
def test_tick_publishes_route_into_intent(monkeypatch, tmp_path):
    _offline(monkeypatch, tmp_path,
             reply={"goal": "phineas:glower", "mood": "restless",
                    "urgency": "at once", "reason": "Now."})
    monkeypatch.setattr(hb.video_graph.VideoGraph, "load", staticmethod(lambda *a, **k: _Graph()))
    monkeypatch.setattr(hb, "_ensure_player", lambda *a, **k: None)
    # tick() reads the wall clock, and at night circadian owns the body and the heartbeat
    # correctly writes no goal -- pin daytime so this asserts the route contract, not the hour.
    monkeypatch.setattr(hb.circadian, "is_night", lambda *a, **k: False)

    hb.tick(["phineas"], "m", False, _log)

    intent = json.loads((tmp_path / "intent.json").read_text(encoding="utf-8"))
    entry = intent["characters"]["phineas"]
    assert entry["route"] == "beeline"       # the key _preview_graph.py has always read
    assert entry["mood"] == "restless"
    assert entry["goal"] == "phineas:glower"


def test_one_characters_bad_reply_never_discards_the_others_goal(monkeypatch, tmp_path):
    """The whole tick writes intent.json ONCE, after every character has decided -- so a crash on
    the second character throws away the first one's good goal AND leaves no journal trace."""
    _offline(monkeypatch, tmp_path)
    replies = {"phineas": {"goal": "phineas:glower", "mood": "restless",
                           "urgency": "wander", "reason": "Fine."},
               "maxx": {"goal": "phineas:glower", "mood": "loud", "urgency": 7, "reason": "GO."}}
    seen = []

    def _complete_json(system, user, **kw):
        seen.append(len(seen))
        return replies["phineas"] if len(seen) == 1 else replies["maxx"]

    monkeypatch.setattr(hb.llm, "complete_json", _complete_json)
    monkeypatch.setattr(hb.video_graph.VideoGraph, "load", staticmethod(lambda *a, **k: _Graph()))
    monkeypatch.setattr(hb, "_ensure_player", lambda *a, **k: None)
    monkeypatch.setattr(hb.circadian, "is_night", lambda *a, **k: False)

    hb.tick(["phineas", "maxx"], "m", False, _log)

    intent = json.loads((tmp_path / "intent.json").read_text(encoding="utf-8"))
    assert intent["characters"]["phineas"]["goal"] == "phineas:glower"
    assert intent["characters"]["phineas"]["route"] == "wander"

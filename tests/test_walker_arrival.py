"""Exercise arrival across the real walker, pose files, and consecutive heartbeats."""
import ast
import datetime
import json
import os
import random
from collections import deque
from pathlib import Path

from director import heartbeat as hb
from runtime import circadian, mind, policy
from test_heartbeat import _Graph, _journal, _log, _offline

ROOT = Path(__file__).resolve().parent.parent


def _walker_class(tmp_path):
    # Load the actual class without the player's pygame imports or process-wide log redirect.
    source = ROOT / "_preview_graph.py"
    tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "GraphCycler")
    scope = dict(ROOT=ROOT, GRAPH=tmp_path / "graph.json", POSE_DIR=tmp_path / "pose",
                 INTENT_PATH=tmp_path / "intent.json", FPS=10, _context=None,
                 mind=mind, policy=policy, circadian=circadian, random=random,
                 datetime=datetime, json=json, os=os, deque=deque, Path=Path)
    exec(compile(ast.Module(body=[cls], type_ignores=[]), str(source), "exec"), scope)
    return scope["GraphCycler"]


def _intent(tmp_path, goal, stamp):
    entry = {"goal": goal, "set_at": stamp} if goal else None
    characters = {"phineas": entry} if entry else {}
    path = tmp_path / "intent.json"
    path.write_text(json.dumps({"characters": characters}), encoding="utf-8")
    os.utime(path, (stamp, stamp))  # deterministic mtime change for the real reader's cache
    return entry


def _setup(monkeypatch, tmp_path, start="glower", policy_on=True):
    _offline(monkeypatch, tmp_path)
    monkeypatch.setattr(hb.time, "time", lambda: 1100.0)
    graph = _Graph()
    graph.nodes["phineas:swoon"] = {"character": "phineas", "pose": "swoon"}
    graph.edges.extend([
        {"id": "phineas/a2s/v0", "kind": "transition", "label": "a2s",
         "from": "phineas:anchor", "to": "phineas:swoon"},
        {"id": "phineas/s2a/v0", "kind": "transition", "label": "s2a",
         "from": "phineas:swoon", "to": "phineas:anchor"},
    ])
    # Legal deterministic choices: transition from glower, then idle at anchor.
    monkeypatch.setattr(policy, "choose", lambda node, out, all_edges, **kw: out[0])
    _intent(tmp_path, "phineas:" + start, 1000.0)
    walker = _walker_class(tmp_path)({"edges": graph.edges}, "phineas", (1, 1), 1,
                                   start_pose=start, hour_override=14,
                                   mind_on=not policy_on, policy_on=policy_on)
    monkeypatch.setattr(walker, "_frames", lambda: [None])
    return walker, graph


def _arrival(graph, prev):
    node, _, receipt = hb._current_pose(graph, "phineas")
    return hb._arrival(prev, node, receipt, now=1100.0)


def test_renewed_goal_cannot_reuse_an_old_arrival(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path)
    original = {"goal": "phineas:glower", "set_at": 1000.0}
    walker.frame()  # Arrive at anchor after visiting glower.
    assert _arrival(graph, original) is True  # Drifting away still counts for this pursuit.

    renewed = _intent(tmp_path, "phineas:glower", 1001.0)
    assert _arrival(graph, renewed) is None  # The heartbeat may read before the walker polls.
    pose_before = (walker.node, walker.pose_dwell)
    walker._pick()
    assert (walker.node, walker.pose_dwell) == pose_before
    assert _arrival(graph, renewed) is False  # Must republish even without pose/dwell changes.

    walker.cur = next(e for e in graph.edges if e["label"] == "a2g")
    walker.frame()
    walker.frame()  # Reach glower on the new pursuit, then drift away again.
    assert walker.node == "phineas:anchor"
    assert _arrival(graph, renewed) is True


def test_switching_goals_and_releasing_clears_arrival(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path)
    walker.frame()
    for goal, stamp in (("phineas:swoon", 1001.0), ("phineas:glower", 1002.0)):
        prev = _intent(tmp_path, goal, stamp)
        walker._pick()
        assert _arrival(graph, prev) is False
    _intent(tmp_path, None, 1003.0)
    walker._pick()
    assert hb._current_pose(graph, "phineas")[2] is None
    prev = _intent(tmp_path, "phineas:glower", 1004.0)
    walker._pick()
    assert _arrival(graph, prev) is False


def test_goal_identity_is_republished_while_still_on_target(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path)
    prev = _intent(tmp_path, "phineas:glower", 1001.0)
    assert _arrival(graph, prev) is None
    walker._pick()  # Same node and dwell, but a new goal identity and arrival.
    assert _arrival(graph, prev) is True
    receipt = hb._current_pose(graph, "phineas")[2]
    assert receipt == dict(prev, arrived=True)


def test_mind_only_walker_also_reports_goal_arrival(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path, start="anchor", policy_on=False)
    prev = _intent(tmp_path, "phineas:glower", 1001.0)
    walker._pick()
    assert _arrival(graph, prev) is False
    walker.frame()
    assert _arrival(graph, prev) is True


def test_restart_does_not_invent_a_failed_pursuit(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path)
    walker.frame()
    # The new walker cannot know whether this already-active pursuit arrived before restart.
    restarted = _walker_class(tmp_path)({"edges": graph.edges}, "phineas", (1, 1), 1,
                                      start_pose="anchor", hour_override=14, policy_on=True)
    assert restarted.node == "phineas:anchor"
    prev = {"goal": "phineas:glower", "set_at": 1000.0}
    assert _arrival(graph, prev) is None


def test_previous_goal_outcome_is_separate_from_the_next_thought(monkeypatch, tmp_path):
    walker, graph = _setup(monkeypatch, tmp_path, start="anchor")
    replies = iter([
        {"goal": "phineas:glower", "mood": "restless", "urgency": "wander",
         "reason": "I want to glower."},
        {"goal": "phineas:anchor", "mood": "calm", "urgency": "wander",
         "reason": "I will stay at the anchor."},
    ])
    monkeypatch.setattr(hb.llm, "complete_json", lambda *a, **k: next(replies))
    goal, _, _ = hb.decide_character(graph, {}, "phineas", 14, "m", False, _log)
    prev = _intent(tmp_path, goal, 1001.0)
    walker._pick()  # Still at anchor; did not reach the previous goal.
    hb.decide_character(graph, {}, "phineas", 14, "m", False, _log, prev=prev)

    thought = "I will stay at the anchor."
    tail = hb._journal_tail("phineas")
    assert thought + " -- and did not get there" not in "\n".join(tail)
    outcome_line, thought_line = tail[-1].splitlines()
    assert "phineas:glower" in outcome_line and "did not get there" in outcome_line
    assert thought in thought_line and "did not get there" not in thought_line
    entry = _journal(tmp_path)[-1]
    assert entry["goal"] == "phineas:anchor"
    assert entry["outcome"] == dict(prev, arrived=False)

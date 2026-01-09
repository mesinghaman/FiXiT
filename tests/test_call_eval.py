from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_call_eval_response_shape() -> None:
    payload = {
        "call_id": "C-test-1",
        "lead_id": "L-test-9",
        "duration_seconds": 310,
        "transcript": "Agent: Hello. Buyer: Just checking options right now.",
    }

    res = client.post("/api/v1/call-eval", json=payload)

    assert res.status_code == 200

    body = res.json()

    assert "quality_score" in body
    assert 0.0 <= body["quality_score"] <= 1.0

    assert "labels" in body
    assert isinstance(body["labels"], dict)

    for key in [
        "rapport_building",
        "need_discovery",
        "closing_attempt",
        "compliance_risk",
    ]:
        assert key in body["labels"]
        assert isinstance(body["labels"][key], bool)

    assert "summary" in body
    assert isinstance(body["summary"], str)

    assert "next_actions" in body
    assert isinstance(body["next_actions"], str)

    assert "model_metadata" in body
    assert "model_name" in body["model_metadata"]
    assert "latency" in body["model_metadata"]

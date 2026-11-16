
from fastapi.testclient import TestClient

from app.backend.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["api_status"] == "running"


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_question_endpoint():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "What causes iron deficiency anemia?"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "pipeline_pending"


def test_short_question_rejected():
    response = client.post(
        "/api/v1/ask",
        json={"question": "Hi"}
    )

    assert response.status_code == 422

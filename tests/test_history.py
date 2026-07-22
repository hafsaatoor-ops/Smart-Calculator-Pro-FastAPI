from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_history_requires_login():
    response = client.get("/history")

    assert response.status_code in [401, 403]
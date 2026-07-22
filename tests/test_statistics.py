from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_statistics_requires_login():
    response = client.get("/statistics")

    assert response.status_code in [401, 403]
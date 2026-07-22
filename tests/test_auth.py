from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_signup_endpoint_exists():
    response = client.post(
        "/auth/signup",
        json={}
    )
    assert response.status_code in [200, 400, 422]


def test_login_endpoint_exists():
    response = client.post(
        "/auth/login",
        data={}
    )
    assert response.status_code in [200, 400, 401, 422]
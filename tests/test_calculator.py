from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculator_without_token():
    response = client.post(
        "/calculator/calculate",
        json={
            "operation": "add",
            "number1": 5,
            "number2": 2
        }
    )

    assert response.status_code in [401, 403]
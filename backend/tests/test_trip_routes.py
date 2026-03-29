from fastapi.testclient import TestClient

from app.main import app


def test_create_trip_route_returns_structured_trip() -> None:
    client = TestClient(app)

    response = client.post(
        "/trips",
        json={
            "destination": "Tokyo",
            "duration_days": 3,
            "pace": "balanced",
            "preferences": ["food", "culture"],
        },
    )

    assert response.status_code == 200
    assert "days" in response.json()

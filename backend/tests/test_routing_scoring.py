from app.schemas.routing import RouteStop
from app.services.routing import score_route_order


def test_score_penalizes_reordering_locked_stop() -> None:
    stops = [
        RouteStop(stop_id="1", locked=True, travel_minutes_from_previous=0, opening_hours_ok=True),
        RouteStop(stop_id="2", locked=False, travel_minutes_from_previous=20, opening_hours_ok=True),
    ]

    score = score_route_order(stops=stops, reordered_locked_stops=1, backtracking_penalty=10)

    assert score > 100

from app.schemas.routing import RouteStop


def score_route_order(
    stops: list[RouteStop],
    reordered_locked_stops: int,
    backtracking_penalty: int,
) -> int:
    travel_score = sum(stop.travel_minutes_from_previous for stop in stops)
    hours_penalty = sum(50 for stop in stops if not stop.opening_hours_ok)
    lock_penalty = reordered_locked_stops * 100
    return travel_score + hours_penalty + backtracking_penalty + lock_penalty

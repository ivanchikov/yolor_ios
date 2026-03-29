from app.schemas.planner import PlannerTripDraft
from app.schemas.routing import RouteStop
from app.services.routing import score_route_order


def validate_planner_output(payload: dict) -> PlannerTripDraft:
    return PlannerTripDraft.model_validate(payload)


def score_planner_route(
    stops: list[RouteStop],
    reordered_locked_stops: int = 0,
    backtracking_penalty: int = 0,
) -> int:
    return score_route_order(
        stops=stops,
        reordered_locked_stops=reordered_locked_stops,
        backtracking_penalty=backtracking_penalty,
    )

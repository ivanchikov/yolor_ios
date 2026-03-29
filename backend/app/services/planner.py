from app.schemas.planner import PlannerTripDraft


def validate_planner_output(payload: dict) -> PlannerTripDraft:
    return PlannerTripDraft.model_validate(payload)

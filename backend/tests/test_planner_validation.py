import pytest
from pydantic import ValidationError

from app.schemas.planner import PlannerDay, PlannerStop, PlannerTripDraft


def test_planner_rejects_stop_without_poi_id() -> None:
    with pytest.raises(ValidationError):
        PlannerTripDraft(
            days=[
                PlannerDay(
                    day_index=1,
                    stops=[
                        PlannerStop(
                            title="Shibuya Crossing",
                            poi_id="",
                            duration_minutes=60,
                        )
                    ],
                )
            ]
        )

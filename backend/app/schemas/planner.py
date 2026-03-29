from pydantic import BaseModel, Field, field_validator


class PlannerStop(BaseModel):
    title: str
    poi_id: str = Field(min_length=1)
    duration_minutes: int = Field(gt=0)


class PlannerDay(BaseModel):
    day_index: int = Field(ge=1)
    stops: list[PlannerStop]


class PlannerTripDraft(BaseModel):
    days: list[PlannerDay]

    @field_validator("days")
    @classmethod
    def require_days(cls, days: list[PlannerDay]) -> list[PlannerDay]:
        if not days:
            raise ValueError("trip draft must include at least one day")
        return days

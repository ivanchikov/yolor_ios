from pydantic import BaseModel


class CreateTripRequest(BaseModel):
    destination: str
    duration_days: int
    pace: str
    preferences: list[str]


class TripDayResponse(BaseModel):
    day_index: int
    stops: list[dict]


class TripResponse(BaseModel):
    trip_id: str
    days: list[TripDayResponse]

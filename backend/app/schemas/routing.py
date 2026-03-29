from pydantic import BaseModel


class RouteStop(BaseModel):
    stop_id: str
    locked: bool
    travel_minutes_from_previous: int
    opening_hours_ok: bool

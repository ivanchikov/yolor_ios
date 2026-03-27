from pydantic import BaseModel


class POICandidate(BaseModel):
    name: str
    latitude: float
    longitude: float
    region_code: str

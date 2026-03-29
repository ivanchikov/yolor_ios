from fastapi import APIRouter

from app.schemas.trips import CreateTripRequest, TripDayResponse, TripResponse

router = APIRouter(prefix="/trips", tags=["trips"])


@router.post("", response_model=TripResponse)
def create_trip(payload: CreateTripRequest) -> TripResponse:
    return TripResponse(
        trip_id="trip_dev_001",
        days=[TripDayResponse(day_index=1, stops=[{"title": payload.destination}])],
    )

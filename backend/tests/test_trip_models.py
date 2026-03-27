from app.models.day import Day
from app.models.stop import Stop
from app.models.trip import Trip


def test_trip_day_stop_relationships_are_explicit() -> None:
    trip = Trip(title="Tokyo")
    day = Day(day_index=1, trip=trip)
    stop = Stop(order_index=0, day=day, poi_id="poi_123", locked=False)

    assert trip.days[0] is day
    assert day.stops[0] is stop
    assert stop.poi_id == "poi_123"

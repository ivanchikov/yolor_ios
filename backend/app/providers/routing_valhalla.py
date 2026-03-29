from app.schemas.routing import RouteStop


class ValhallaRoutingProvider:
    provider_name = "valhalla"

    async def score(self, stops: list[RouteStop]) -> int:
        return sum(stop.travel_minutes_from_previous for stop in stops)

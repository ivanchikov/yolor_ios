from app.schemas.routing import RouteStop


class VroomOptimizerProvider:
    provider_name = "vroom"

    async def optimize(self, stops: list[RouteStop]) -> list[RouteStop]:
        return stops

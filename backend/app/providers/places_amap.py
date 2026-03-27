from app.providers.base import PlacesProvider
from app.schemas.poi import POICandidate


class AmapPlacesProvider:
    provider_name = "amap"

    async def resolve(self, query: str) -> list[POICandidate]:
        return []


amap_places_provider: PlacesProvider = AmapPlacesProvider()

from app.providers.base import PlacesProvider
from app.schemas.poi import POICandidate


class GooglePlacesProvider:
    provider_name = "google_places"

    async def resolve(self, query: str) -> list[POICandidate]:
        return []


google_places_provider: PlacesProvider = GooglePlacesProvider()

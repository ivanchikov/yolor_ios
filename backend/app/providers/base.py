from typing import Protocol

from app.schemas.poi import POICandidate


class PlacesProvider(Protocol):
    provider_name: str

    async def resolve(self, query: str) -> list[POICandidate]: ...

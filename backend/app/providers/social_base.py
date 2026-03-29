from typing import Protocol


class SocialImportProvider(Protocol):
    provider_name: str

    async def extract_places(self, url: str) -> list[str]: ...

from typing import Protocol


class LLMProvider(Protocol):
    async def generate_structured_trip(self, prompt: str) -> dict: ...

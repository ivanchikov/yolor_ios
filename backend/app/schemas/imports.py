from pydantic import BaseModel


class ImportSummary(BaseModel):
    accepted_count: int
    dropped_count: int
    message: str

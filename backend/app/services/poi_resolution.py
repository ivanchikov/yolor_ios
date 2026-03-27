from app.schemas.poi import POICandidate


def select_places_provider(candidate: POICandidate) -> str:
    if candidate.region_code.upper() == "CN":
        return "amap"
    return "google_places"

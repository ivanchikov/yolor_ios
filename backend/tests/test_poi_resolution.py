from app.schemas.poi import POICandidate
from app.services.poi_resolution import select_places_provider


def test_select_places_provider_uses_amap_for_mainland_china() -> None:
    candidate = POICandidate(name="外滩", latitude=31.2400, longitude=121.4900, region_code="CN")

    provider_name = select_places_provider(candidate)

    assert provider_name == "amap"

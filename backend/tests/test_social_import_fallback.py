from app.services.social_import import summarize_import_result


def test_partial_import_keeps_verified_places_and_reports_dropped_items() -> None:
    result = summarize_import_result(
        verified_places=["Tokyo Tower", "Meiji Shrine"],
        dropped_places=["Unknown cafe from video caption"],
    )

    assert result.accepted_count == 2
    assert result.dropped_count == 1
    assert "Unknown cafe from video caption" in result.message

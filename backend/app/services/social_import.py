from app.schemas.imports import ImportSummary


def summarize_import_result(verified_places: list[str], dropped_places: list[str]) -> ImportSummary:
    message = f"Imported {len(verified_places)} verified places."
    if dropped_places:
        message += " Dropped: " + ", ".join(dropped_places)
    return ImportSummary(
        accepted_count=len(verified_places),
        dropped_count=len(dropped_places),
        message=message,
    )

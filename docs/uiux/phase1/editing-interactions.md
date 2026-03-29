# Editing Interactions

Editing principles:
- The backend remains the source of truth for itinerary structure.
- The client can acknowledge intent immediately, but final trip state comes back from the backend.
- Regeneration must stay scoped. Do not silently rewrite the whole trip when the user changes one day.

Supported Phase 1 actions:
- Reorder stops within a day
- Delete a stop
- Lock or unlock a stop
- Add a POI
- Regenerate a day or a local segment

Interaction rules:
- `Reorder`: show the provisional new order immediately, then reconcile with the backend response.
- `Delete`: remove the stop from the visible list only after user confirmation.
- `Lock`: a locked stop must display an obvious pinned state and be preserved during regeneration.
- `Add Stop`: launch a focused add-stop surface from the review screen, not a full-screen context switch.
- `Regenerate`: clearly indicate scope such as `Regenerate Day 2` or `Regenerate around Lunch`.

Failure handling:
- If an edit fails, restore the last valid itinerary state.
- If a stop cannot be verified, explain that the place could not be matched rather than pretending it was added.
- If regeneration returns a lower-confidence result, preserve locked stops and show what changed.

Trust cues:
- Always show when a stop is user-added, imported, or generated.
- Keep route changes diffable at the day level so users understand what moved.

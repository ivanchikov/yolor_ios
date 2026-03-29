# Design System

Core tone:
- Calm, precise, map-first
- Travel utility before decoration
- Strong hierarchy over novelty

Layout rules:
- Prefer generous horizontal padding and stable vertical rhythm.
- Keep the map prominent on review screens.
- Use cards and grouped sections sparingly; the itinerary itself should provide most of the structure.

Typography:
- Use a clean humanist sans for app text with strong weight contrast between labels and timing metadata.
- Titles should feel directional and operational, not editorial.
- Secondary metadata such as travel times and offline status should remain compact and low-noise.

Color:
- Use a light default surface for Phase 1.
- Reserve the primary accent for active day selection, primary calls to action, and important route state.
- Use neutral grays for passive controls and muted metadata.
- Error and fallback states should use warm warning tones, not alarming red by default.

Component guidance:
- Day chips should read as segmented navigation, not filter tags.
- Stop rows should foreground name and time, with travel segments visually lighter.
- Toolbar actions should be few and explicit: add stop, regenerate, save.
- Profile/menu actions should stay secondary in the visual hierarchy.

Motion:
- Use short transitions when switching days to keep map and list synchronized.
- Progress states can animate between backend stages, but avoid decorative motion during planning.
- Editing confirmations should be immediate and restrained.

Accessibility:
- Preserve strong contrast for map overlays and day controls.
- Controls in the review flow must be reachable with Dynamic Type without collapsing the stop list into noise.
- Avoid relying on color alone for lock state or fallback warnings.

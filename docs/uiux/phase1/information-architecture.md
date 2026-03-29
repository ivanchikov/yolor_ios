# Information Architecture

Primary navigation:
- Plan
- Saved
- Profile

Primary flow:
1. Enter a destination or supported social URL.
2. Answer only the minimum follow-up questions.
3. Watch backend generation progress.
4. Review one itinerary day at a time.
5. Make bounded edits to stops or regenerate a scoped section.
6. Save and sign in if persistence is needed.

Entry points:
- `Plan` is the default root and must remain visually dominant.
- `Saved` is available from the profile menu and later can become a first-class tab if usage justifies it.
- `Profile` is always reachable from the top bar so login, account, and settings are never trapped behind `Save`.

Screen ownership:
- `InputView`: destination/social URL capture and lightweight follow-up prompts.
- `GenerationView`: progress stages, retries, and fallback explanations.
- `TripReviewView`: map-first review of a selected day and its ordered stops.
- `EditToolbarView` and related sheets: add stop, lock/unlock, delete, regenerate.
- `SavedTripsView`: offline-readable saved trip list and entry to saved trip detail.
- `ProfileMenuView`: sign in/out, saved trips, later settings and account actions.

State boundaries:
- Anonymous planning is first-class.
- Authentication is required for save and sync, not for previewing value.
- Offline access is read-only and uses the last saved snapshot.

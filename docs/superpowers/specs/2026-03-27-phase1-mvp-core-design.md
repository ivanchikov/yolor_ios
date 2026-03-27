# Yolor Phase 1 MVP Core Design

Date: 2026-03-27
Status: Approved in brainstorming, pending final user review
Source PRD: `docs/master/phase1/MASTER_PRD.md`

## 1. Goal

Define the Phase 1 MVP system design for Yolor as a map-first AI trip planner with a real planning core. This design prioritizes:

- real AI-driven itinerary generation
- real POI and routing providers
- a clean backend architecture that can scale later
- an iOS app that exercises the planning core without owning planning logic

This spec covers the first build slice:

- input to POI-backed itinerary generation
- map-first trip review
- bounded itinerary editing
- login on save plus proactive account access
- saved-trip offline viewing

## 2. Product Boundaries

Phase 1 decisions locked during brainstorming:

- Build slice: real planning core first, not a mocked end-to-end shell
- AI strategy: real LLM plus real POI/map providers from the start
- Backend shape: iOS app plus a thin but clean custom backend
- Geography: dual-track global plus mainland China compatibility from day one
- Social import: direct URL ingestion with graceful fallback
- Auth: anonymous planning is allowed; login is required only when saving
- Editing scope: reorder, delete, lock, add a POI, and regenerate a day or segment
- Offline scope: saved itineraries can be viewed offline, including day details and cached/basic map assets

Out of scope for Phase 1:

- deep cross-day editing such as drag-and-drop across days
- full freeform natural-language trip rewriting
- heavy platform decomposition into multiple services
- community, booking, OCR, or monetization features

## 3. System Architecture

Phase 1 uses a 3-layer architecture.

### 3.1 iOS App

The iOS app owns the user experience:

- destination or social-link input
- minimal follow-up questions
- generation progress
- map-first trip review
- bounded edit actions
- save/login prompts
- offline viewing of saved trips

The app does not own provider-specific planning logic. It sends intent and edit commands to the backend and renders the returned structured trip model.

### 3.2 Yolor Backend

The backend is a modular monolith with one app-facing API. It owns:

- provider credentials and secrets
- LLM orchestration
- POI resolution and deduplication
- route optimization
- planning validation and repair
- trip persistence
- save/sync
- offline payload preparation

The backend returns structured trip data only. Freeform itinerary text is never the source of truth.

### 3.3 External Providers

External providers are adapters behind backend interfaces:

- LLM provider(s)
- POI/place providers
- routing/matrix providers
- auth and storage infrastructure as needed

Provider differences must be hidden behind backend contracts so the iOS app remains stable when providers vary by region.

## 4. Data and Storage

Phase 1 uses three storage concerns behind the backend.

### 4.1 Primary Relational Database

System of record for:

- users
- trips
- days
- stops
- route segments
- canonical POIs
- import sessions
- provider/generation metadata needed for regeneration and debugging

### 4.2 Cache Layer

Used for expensive but repeatable results:

- POI lookups
- normalized place details
- route or matrix queries
- generation artifacts keyed by stable input when useful

### 4.3 Object Storage

Used for binary or packaged artifacts such as:

- offline map snapshots
- cached static assets for offline trip viewing
- persisted import artifacts if retained

Avoid in Phase 1:

- event sourcing
- graph databases
- provider-specific schemas leaking into the core domain

## 5. Core Domain Model

The canonical model follows the Master PRD.

### 5.1 User

Account identity used for saved trips, sync, and account management.

### 5.2 Trip

Top-level travel plan storing:

- destination context
- duration
- preferences
- pace
- source type (`manual`, `social_import`)
- planning status
- provider/generation metadata

### 5.3 Day

Belongs to one trip and stores:

- day index
- geographic cluster summary
- start and end planning window
- regeneration metadata

### 5.4 Stop

Trip-specific POI instance storing:

- day association
- order
- arrival window
- planned duration
- role such as meal or attraction
- locked flag
- provenance (`generated`, `imported`, `user_added`)

### 5.5 POI

Canonical reusable place record storing:

- normalized name
- coordinates
- provider IDs
- category
- address metadata
- opening hours when available
- source provider
- confidence and verification state
- freshness metadata

### 5.6 RouteSegment

Explicit connection between consecutive stops storing:

- origin stop
- destination stop
- travel mode if known
- estimated duration
- distance
- optional geometry or snapshot references

### 5.7 ImportSession

Tracks a social-link ingestion attempt:

- source URL and platform
- extraction status
- extracted place candidates
- fallback reason if any
- mapping results into canonical POIs

### 5.8 Data Rules

- `POI` is reusable across trips; `Stop` is trip-specific
- route segments are stored explicitly
- locking lives on `Stop`
- AI outputs must map into this schema before a trip is accepted
- app DTOs are derived from this model; they do not define competing truth

## 6. POI Freshness and Update Model

POI updates are backend-controlled and opportunistic.

### 6.1 Stable vs Volatile Fields

Mostly stable:

- name
- coordinates
- category
- address

Volatile:

- opening hours
- temporary closures
- ratings/counts if used
- contact details

### 6.2 Freshness Metadata

Each canonical POI stores:

- `last_verified_at`
- `source_provider`
- `source_provider_id`
- `data_confidence`
- `refresh_policy`

### 6.3 Update Paths

`Read-through refresh`

- when planning or viewing needs stale volatile data, refresh it on demand or immediately after serve

`Background refresh`

- upcoming saved trips get refreshed ahead of travel to reduce stale-hours risk

`On-demand repair`

- when planning detects a closure, mismatch, or invalid record, re-resolve or re-verify the POI

### 6.4 Merge Rules

Provider data must merge by policy, not by last write wins:

- core identity fields anchor to the canonical source
- volatile fields can refresh from the best regional provider
- conflicting data is tracked with confidence

### 6.5 Offline Consistency

When a trip is saved, POI details used by that trip are snapshotted into the offline payload so offline viewing stays stable even if the canonical POI changes later.

## 7. Backend Modules

The modular monolith should be separated internally into these modules.

### 7.1 API Layer

Single app-facing contract for:

- trip creation
- trip editing
- save/sync
- auth/account actions
- offline payload retrieval

### 7.2 Social Import Module

Responsibilities:

- accept supported social URLs
- extract candidate places where possible
- normalize extracted content into structured place candidates
- return graceful fallback states when extraction is incomplete or blocked

### 7.3 POI Resolution Module

Responsibilities:

- resolve raw place mentions into canonical POIs
- deduplicate candidates
- choose provider path by geography
- persist reusable POIs and caches

### 7.4 Planner Module

Responsibilities:

- combine trip intent, duration, preferences, pace, and resolved POIs
- call the LLM with schema-constrained output
- apply business rules
- reject vague or invalid outputs

### 7.5 Routing and Optimization Module

Responsibilities:

- compute travel-time truth
- score route coherence
- reduce backtracking
- check opening-hours feasibility where data exists
- repair bad itineraries

### 7.6 Trip Module

Responsibilities:

- own the persistent `Trip -> Day -> Stop -> RouteSegment` model
- support edit operations
- preserve locked stops
- support partial regeneration
- handle save/load behavior

### 7.7 Offline Packaging Module

Responsibilities:

- build saved-trip offline payloads
- package POI details and map assets
- provide the app with offline-safe content

## 8. Planning and Optimization Workflow

Planning is a backend workflow, not one opaque LLM call.

### 8.1 Input Assembly

The backend gathers:

- destination or imported social input
- trip duration
- preferences
- pace
- explicit user constraints

If essential information is missing, request only the minimum additional input.

### 8.2 POI Candidate Set

All raw place mentions must be resolved into canonical POIs before planning. The planner works only on structured POIs.

### 8.3 LLM Draft Planning

The LLM generates a schema-constrained draft itinerary from the resolved POI set and trip constraints. Its role is to propose sequencing, pacing, and category balance within hard structural rules.

### 8.4 Validation and Repair

The backend validates the draft:

- every stop maps to a real POI
- route order is geographically reasonable
- duplicates are handled intentionally
- opening-hours constraints are checked where available
- day density fits pace
- locked stops are preserved during edits

If the draft fails validation, the backend first repairs it with routing/optimization logic. If the repaired plan still violates core constraints, the backend runs one additional constrained AI pass against the validated POI set and re-validates the result. Invalid itineraries are not returned as accepted truth.

### 8.5 Routing and Route Optimization

The routing module should optimize by scoring candidate sequences, not by shortest distance alone.

Phase 1 flow:

1. Build a resolved POI set.
2. Cluster POIs geographically into day-sized groups.
3. Request travel-time matrices from the routing provider.
4. Score candidate stop orders using weighted factors:
   - travel time
   - backtracking penalty
   - opening-hours feasibility
   - pace fit
   - category balance
   - lock preservation
   - time-slot plausibility
5. Repair poor plans by reordering stops, moving stops across days when necessary, replacing weak stops, or trimming overloaded days.
6. Persist explicit `RouteSegment` records for the accepted order.

The system should not build a deep custom route solver in Phase 1. Instead, Yolor owns the orchestration and scoring logic while external routing infrastructure supplies travel-time truth.

### 8.6 Partial Regeneration

Supported scopes:

- one day
- one day segment
- around a newly added or removed stop

Locked stops act as anchors. Unchanged days remain untouched unless the user explicitly requests broader regeneration.

## 9. Provider Strategy

### 9.1 iOS Map Rendering

Use `Apple MapKit` in the iOS app for rendering and interaction.

Rule:

- the map SDK renders; it is not the planning source of truth

### 9.2 POI Providers

Use a backend abstraction with:

- `Google Places` as the global/default POI provider
- `Amap` as the mainland China provider

The backend chooses the provider path by geography and normalization policy.

### 9.3 Routing Providers

Use a backend routing abstraction with:

- `VROOM + Valhalla` as the recommended Phase 1 routing stack

Reason:

- stronger optimization ownership
- cleaner long-term moat
- more flexibility than a pure managed route API

The routing adapter must remain replaceable so a managed-routing provider can be added later without changing the app contract or the canonical trip model.

## 10. iOS App Structure and UX

The app should stay thin in logic but strong in interaction.

### 10.1 Input Flow

One primary input accepts:

- destination text
- supported social URL

After submission, ask only the minimum follow-up questions needed to generate a defensible itinerary.

### 10.2 Generation State

Show real progress with plain-language stages such as:

- resolving places
- optimizing days
- building route

### 10.3 Trip Review

Core screen is map-first:

- one selected day on the map at a time
- day selector
- stop list for the selected day
- timing and route segments
- POI detail access

Map and list remain synchronized around the same canonical day model.

### 10.4 Editing Scope

Phase 1 supports:

- reorder stops within a day
- delete a stop
- lock or unlock a stop
- add a POI
- regenerate a day or segment

The app sends structured edit commands to the backend. The backend remains the source of truth for accepted itinerary changes.

### 10.5 Auth and Menu Entry Points

Auth should be available in two ways:

- primary contextual trigger: `Save`
- secondary global trigger: a lightweight profile/menu entry

This preserves low-friction anonymous planning while supporting proactive sign-in, account access, and future settings growth.

### 10.6 Offline View

Saved trips remain readable offline with:

- day details
- POI data
- cached/static map assets prepared by the backend

### 10.7 Suggested App Modules

- `Input`
- `TripReview`
- `TripEdit`
- `Auth`
- `OfflineTrips`
- `SharedUI`
- networking layer
- local persistence layer

## 11. Error Handling and Fallbacks

Failures must be structured by stage:

- input validation failure
- social import extraction failure
- POI resolution failure
- itinerary generation failure
- routing/optimization failure
- save/auth failure
- offline packaging failure

The app should render clear outcomes rather than generic errors.

Graceful degradation rules:

- if some imported POIs are valid, continue with the valid set and explain what was dropped
- if hours data is missing, plan with reduced confidence rather than false precision
- if route geometry is unavailable, still return ordered stops with travel estimates if possible
- if offline map assets fail, saved trip text/details should still remain offline-available
- if an edit/regeneration fails, preserve the last valid itinerary

## 12. Testing Strategy

Testing should emphasize backend correctness first.

### 12.1 Backend Tests

- schema validation for LLM outputs
- POI normalization and deduplication
- POI freshness and refresh-path behavior
- routing score and repair logic
- locked-stop preservation during edits
- partial regeneration boundaries
- provider adapter contract tests
- social import fallback behavior

### 12.2 iOS Tests

- input flow and minimal follow-up questions
- generation-state rendering
- map/day synchronization
- edit command dispatch
- auth-on-save flow
- proactive profile login flow
- offline saved-trip rendering

### 12.3 End-to-End Tests

- destination-only trip generation
- social-link import with partial fallback
- save and reload in a later session
- offline viewing of a saved trip
- day regeneration while preserving locked stops

## 13. Implementation Guidance

Phase 1 should optimize for a clean modular monolith, not a premature service mesh. Internal interfaces must be explicit so that the following future splits stay feasible:

- planner service
- POI service
- routing service
- trip/user service

The app-backend contract and the canonical trip model should remain stable as the internal deployment topology evolves.

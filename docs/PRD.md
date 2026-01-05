# Project Tracker – Product Requirements Document (PRD)

## 1. Overview

### Purpose
Build a small, production-like project tracking application to evaluate backend and frontend development independently but against a shared, immutable API contract.

This project is intentionally minimal while still exercising:
- Correct state modeling
- Idempotent backend behavior
- Safe database evolution
- Real frontend UX flows
- Test quality and engineering judgment

### In Scope
- Viewing projects
- Archiving projects (soft state change)

### Out of Scope
- Authentication / authorization
- Project creation or editing
- Deletion (hard delete)
- Pagination, filtering, or search
- Role-based access control

---

## 2. Goals

### Primary Goals
- Allow users to archive a project safely
- Ensure archive behavior is idempotent
- Enable backend and frontend teams to work in parallel
- Provide a stable contract for integration and testing

### Evaluation Goals
- Measure correctness over speed
- Detect hallucinated assumptions
- Enforce minimal diffs and repo awareness
- Assess test quality and risk reduction

---

## 3. User Personas

### Primary User
- Internal user managing a list of projects
- Wants to archive completed or inactive projects

---

## 4. Functional Requirements

### FR-1: View Projects
- User can view a list of projects
- Both active and archived projects are visible
- Archived projects are clearly distinguishable

### FR-2: Archive Project
- User can archive an active project
- Archiving is irreversible via UI
- Archiving does not delete data
- Re-archiving an already archived project is safe (idempotent)

---

## 5. UX Requirements

### Archive Action
- Archive action must be explicit
- Requires confirmation via modal
- Modal must clearly state irreversibility

### Loading & State
- Archive action must disable while request is in-flight
- Double submission must be prevented

### Success
- User sees a success notification
- Project list refreshes to reflect archived state

### Error
- User sees an error notification
- UI state must not change on failure

---

## 6. Accessibility Requirements

- Modal must trap keyboard focus
- Actions must be keyboard-accessible
- Screen-reader friendly labels and roles

---

## 7. Non-Functional Requirements

| Area | Requirement |
|----|------------|
| Safety | No destructive operations |
| Reliability | Idempotent archive behavior |
| Maintainability | Minimal diffs, no unnecessary abstractions |
| Observability | Explicit, user-visible errors |
| Testability | Deterministic behavior |

---

## 8. Testing Requirements

### Backend
- Unit tests for archive logic
- Integration tests for API behavior
- Explicit idempotency test

### Frontend
- Component tests for modal behavior
- End-to-end test for archive flow
- Stable selectors (`data-testid`)
- No time-based waits

---

## 9. Constraints & Assumptions

- API contract is frozen once work begins
- Backend and frontend are developed in parallel
- Any deviation from contract is considered a failure during evaluation

---

## 10. Ownership

- Backend implementation: Uday Bhardwaj
- Frontend implementation: Friend
- Product & API contract ownership: Shared

---

**End of PRD**

# Project Tracker – API Contract (Frozen)

## 1. Contract Principles

- This document is the single source of truth for backend–frontend integration.  
- Behavior defined here must not be inferred or extended.  
- All responses are deterministic.  
- Idempotency is a core requirement.  

---

## 2. Domain Model

### Project

| Field        | Type                      | Description          |
|---------------|---------------------------|----------------------|
| id            | string (UUID)             | Unique identifier    |
| name          | string                    | Project name         |
| archived_at   | string (ISO 8601) \| null | Archive timestamp    |
| created_at    | string (ISO 8601)         | Creation timestamp   |

### State Rules

- `archived_at == null` → active project  
- `archived_at != null` → archived project  
- Archived projects are read-only  

---

## 3. Endpoints

### 3.1 List Projects

**Request**  
`GET /projects`

**Response: 200 OK**

```json
[
  {
    "id": "uuid",
    "name": "Project Alpha",
    "archived_at": null,
    "created_at": "2024-01-01T10:00:00Z"
  }
]

3.2 Archive Project
Request
POST /projects/{id}/archive

Path Parameters

Name	Type	Required
id	string (UUID)	Yes
4. Success Responses
Case A: Project archived successfully
Response: 200 OK

json
{
  "id": "uuid",
  "archived_at": "2024-02-01T12:00:00Z"
}
Case B: Project already archived (Idempotent)
Response: 200 OK

json
{
  "id": "uuid",
  "archived_at": "2024-02-01T12:00:00Z"
}
Frontend must treat Case A and Case B identically.

5. Error Responses
Project Not Found
Response: 404 Not Found

json
{
  "error": {
    "code": "PROJECT_NOT_FOUND",
    "message": "Project does not exist"
  }
}
Invalid Project ID
Response: 400 Bad Request

json
{
  "error": {
    "code": "INVALID_PROJECT_ID",
    "message": "Invalid project identifier"
  }
}
Internal Server Error
Response: 500 Internal Server Error

json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Unexpected error occurred"
  }
}
6. Idempotency Rules (Critical)
Multiple POST requests must not change state after the first archive.

archived_at must remain stable across repeated requests.

Backend must not return 409 or 422 for already archived projects.

Frontend must assume retries are possible.

7. Frontend Integration Rules
Do not infer undocumented states.

Do not treat idempotent success as error.

Do not optimistically update without server confirmation.

Errors must be surfaced using API-provided messages.

8. Change Policy
This contract is frozen once backend and frontend work begins.

Any change requires explicit agreement.

Undocumented behavior is considered a defect.

9. Ownership
Backend owner: Uday Bhardwaj

Frontend owner: Friend

API contract owner: Shared

End of API Contract

text

***

Would you like me to add an auto-generated Markdown table of contents (with anchor links for quick navigation) at the top of this file?
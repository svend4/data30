# Entity history and rollback API

## 1) Methods

### `GET /entities/{id}/history`
Returns the change history for an entity ordered by `changedAt` descending (latest first).

### `POST /entities/{id}/rollback`
Rolls back an entity to a previous version (snapshot) by re-applying a historical state.

### `GET /entities/{id}/compare?from=&to=`
Returns a diff between two versions of the same entity. `from` and `to` are history version identifiers (or timestamps, if supported).

---

## 2) Behavior details

### Pagination of history
`GET /entities/{id}/history` supports cursor-based pagination:

* **Query params**
  * `limit` (int, optional, default: 50, max: 200)
  * `cursor` (string, optional): opaque cursor from a previous response
* **Response**
  * `items`: array of history entries
  * `nextCursor`: string or `null` if no more items
  * `hasMore`: boolean

### Diff format
`GET /entities/{id}/compare` returns **field-by-field** diffs by default, and supports **JSON Patch** when requested:

* **Query params**
  * `format` (optional): `field` (default) or `json-patch`

**Field-by-field format** includes `field`, `from`, `to` per change.
**JSON Patch format** follows RFC 6902 (`op`, `path`, `value`).

### Rollback strategy
Rollback uses **full snapshot** restoration by default:

* The target history version contains a full snapshot of the entity.
* The rollback operation writes a new history entry representing the rollback action.
* Optional future extension: allow rollback via reverse operations when snapshots are not available.

---

## 3) Authorization & audit requirements

* **Auth**: All endpoints require a valid bearer token.
* **Permissions**
  * `history:read` for history and compare endpoints.
  * `entity:rollback` for rollback endpoint.
* **Audit**
  * Log actor `userId`, `ip`, `userAgent`, `entityId`, `versionId`/`from`/`to`, `timestamp`.
  * Rollback must emit an audit event with reason (optional `reason` field in request).

---

## 4) DTO contracts and examples

### DTOs

```json
// HistoryEntryDTO
{
  "versionId": "string",
  "entityId": "string",
  "changedAt": "2024-01-14T12:34:56Z",
  "changedBy": "user-123",
  "changeType": "CREATE|UPDATE|ROLLBACK",
  "summary": "string",
  "snapshot": { "any": "json" }
}
```

```json
// HistoryResponseDTO
{
  "items": [ /* HistoryEntryDTO */ ],
  "nextCursor": "string|null",
  "hasMore": true
}
```

```json
// CompareResponseDTO (field-by-field)
{
  "fromVersionId": "string",
  "toVersionId": "string",
  "format": "field",
  "changes": [
    { "field": "status", "from": "draft", "to": "published" }
  ]
}
```

```json
// CompareResponseDTO (json-patch)
{
  "fromVersionId": "string",
  "toVersionId": "string",
  "format": "json-patch",
  "changes": [
    { "op": "replace", "path": "/status", "value": "published" }
  ]
}
```

```json
// RollbackRequestDTO
{
  "targetVersionId": "string",
  "reason": "string (optional)"
}
```

```json
// RollbackResponseDTO
{
  "entityId": "string",
  "rolledBackToVersionId": "string",
  "newVersionId": "string",
  "rolledBackAt": "2024-01-14T13:00:00Z"
}
```

### Examples

**GET /entities/abc/history?limit=2**
```json
{
  "items": [
    {
      "versionId": "v3",
      "entityId": "abc",
      "changedAt": "2024-01-14T12:34:56Z",
      "changedBy": "user-123",
      "changeType": "UPDATE",
      "summary": "Changed status",
      "snapshot": { "status": "published", "title": "Hello" }
    },
    {
      "versionId": "v2",
      "entityId": "abc",
      "changedAt": "2024-01-14T11:20:00Z",
      "changedBy": "user-123",
      "changeType": "UPDATE",
      "summary": "Initial update",
      "snapshot": { "status": "draft", "title": "Hello" }
    }
  ],
  "nextCursor": "eyJvZmZzZXQiOjJ9",
  "hasMore": true
}
```

**GET /entities/abc/compare?from=v2&to=v3&format=field**
```json
{
  "fromVersionId": "v2",
  "toVersionId": "v3",
  "format": "field",
  "changes": [
    { "field": "status", "from": "draft", "to": "published" }
  ]
}
```

**POST /entities/abc/rollback**
```json
{
  "targetVersionId": "v2",
  "reason": "Reverted unintended change"
}
```

**Response**
```json
{
  "entityId": "abc",
  "rolledBackToVersionId": "v2",
  "newVersionId": "v4",
  "rolledBackAt": "2024-01-14T13:00:00Z"
}
```

### Error responses

```json
// 401 Unauthorized
{
  "error": "unauthorized",
  "message": "Missing or invalid token"
}
```

```json
// 403 Forbidden
{
  "error": "forbidden",
  "message": "Insufficient permissions"
}
```

```json
// 404 Not Found
{
  "error": "not_found",
  "message": "Entity or version not found"
}
```

```json
// 409 Conflict
{
  "error": "conflict",
  "message": "Rollback target version is not compatible with current state"
}
```

```json
// 422 Unprocessable Entity
{
  "error": "validation_error",
  "message": "Invalid version range or request payload"
}
```

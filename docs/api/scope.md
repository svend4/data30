# API scope

This document defines CRUD operations, endpoints, data contracts, and API requirements for:

- Function
- Module
- UseCase
- Macro

## 1. CRUD operations
All resources support the following base operations:

- Create: add a new entity.
- Read: fetch a single entity by id.
- Update: replace or partially update an entity by id.
- Delete: remove an entity by id (soft-delete by default).

## 2. Endpoints (REST)
Base path: `/api/v1`

### Functions
- `POST /functions`
- `GET /functions`
- `GET /functions/{functionId}`
- `PUT /functions/{functionId}`
- `PATCH /functions/{functionId}`
- `DELETE /functions/{functionId}`

### Modules
- `POST /modules`
- `GET /modules`
- `GET /modules/{moduleId}`
- `PUT /modules/{moduleId}`
- `PATCH /modules/{moduleId}`
- `DELETE /modules/{moduleId}`

### Use Cases
- `POST /use-cases`
- `GET /use-cases`
- `GET /use-cases/{useCaseId}`
- `PUT /use-cases/{useCaseId}`
- `PATCH /use-cases/{useCaseId}`
- `DELETE /use-cases/{useCaseId}`

### Macros
- `POST /macros`
- `GET /macros`
- `GET /macros/{macroId}`
- `PUT /macros/{macroId}`
- `PATCH /macros/{macroId}`
- `DELETE /macros/{macroId}`

## 3. Data contracts (OpenAPI-like JSON schemas)
All entities share these common fields:

```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Function
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "moduleId": "uuid",
  "signature": "string",
  "returnType": "string",
  "parameters": [
    {
      "name": "string",
      "type": "string",
      "required": true
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Module
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "owner": "string",
  "version": "string",
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### UseCase
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "moduleIds": ["uuid"],
  "functionIds": ["uuid"],
  "steps": [
    {
      "order": 1,
      "summary": "string",
      "macroId": "uuid|null"
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Macro
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "inputs": [
    {
      "name": "string",
      "type": "string",
      "required": true
    }
  ],
  "outputs": [
    {
      "name": "string",
      "type": "string"
    }
  ],
  "steps": [
    {
      "order": 1,
      "action": "string",
      "functionId": "uuid|null"
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

#### Request/response conventions
- Create request: omit `id`, `createdAt`, `updatedAt`, `deletedAt`.
- Update request (PUT): full resource without immutable fields (`id`, `createdAt`).
- Update request (PATCH): only fields to modify.
- Responses return the full resource.
- Errors use a standard envelope:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {}
  }
}
```

## 4. Filtering, pagination, sorting, versioning

### Filtering
Common query parameters for list endpoints:
- `ids`: comma-separated list of ids.
- `name`: substring match.
- `tags`: comma-separated list; matches any tag.
- `createdFrom`, `createdTo`: date-time range.
- `updatedFrom`, `updatedTo`: date-time range.
- `deleted`: boolean; include soft-deleted records if `true`.

Resource-specific filters:
- Functions: `moduleId`, `returnType`, `parameterType`.
- Modules: `owner`, `version`.
- UseCases: `moduleId`, `functionId`, `macroId`.
- Macros: `inputType`, `outputType`.

### Pagination
- `limit`: integer, default 25, max 100.
- `cursor`: opaque cursor for forward pagination.
- Response includes:
  - `items`: array of resources
  - `nextCursor`: string|null
  - `total`: integer (optional for performance-sensitive endpoints)

### Sorting
- `sort`: field name, prefix with `-` for descending.
  - Example: `sort=-updatedAt`
- Allowed fields: `name`, `createdAt`, `updatedAt`.

### API versioning
- URI versioning: `/api/v1`.
- Backward-incompatible changes require a new major version.
- Deprecations are announced with `Deprecation` and `Sunset` headers.

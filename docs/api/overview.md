# data30 API Documentation (Markdown)

## Format
This document is written in **Markdown**.

## API Versioning
* **Current version:** `v1`
* **Base URL:** `https://api.example.com/v1`
* **Versioning strategy:** URL prefix (`/v1/...`).

## Authentication
* **Scheme:** Bearer token (JWT or opaque token).
* **Header:** `Authorization: Bearer <token>`
* **Unauthenticated endpoints:** `GET /health`.

## Endpoints

### Health Check
**GET** `/health`  
Returns service status.

**Response (200)**
```json
{
  "status": "ok",
  "timestamp": "2025-01-01T12:00:00Z"
}
```

### List Items
**GET** `/items`  
Returns a paginated list of items.

**Query Parameters**
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | integer | no | Page number (default: 1). |
| `page_size` | integer | no | Items per page (default: 20, max: 100). |

**Response (200)**
```json
{
  "data": [
    {
      "id": "item_123",
      "name": "Example Item",
      "created_at": "2025-01-01T12:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total": 1
  }
}
```

### Create Item
**POST** `/items`  
Creates a new item. **Requires authentication.**

**Request Body**
```json
{
  "name": "New Item"
}
```

**Response (201)**
```json
{
  "id": "item_124",
  "name": "New Item",
  "created_at": "2025-01-01T12:30:00Z"
}
```

### Get Item
**GET** `/items/{item_id}`  
Returns a single item by ID.

**Path Parameters**
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | Unique item identifier. |

**Response (200)**
```json
{
  "id": "item_123",
  "name": "Example Item",
  "created_at": "2025-01-01T12:00:00Z"
}
```

### Update Item
**PATCH** `/items/{item_id}`  
Updates an item. **Requires authentication.**

**Request Body**
```json
{
  "name": "Updated Item"
}
```

**Response (200)**
```json
{
  "id": "item_123",
  "name": "Updated Item",
  "updated_at": "2025-01-01T13:00:00Z"
}
```

### Delete Item
**DELETE** `/items/{item_id}`  
Deletes an item. **Requires authentication.**

**Response (204)**
No content.

## Schemas

### Item
```json
{
  "id": "string",
  "name": "string",
  "created_at": "RFC3339 timestamp",
  "updated_at": "RFC3339 timestamp (optional)"
}
```

### Error
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object (optional)"
  }
}
```

## Errors and Status Codes
| Status | Meaning | Example Scenario |
| --- | --- | --- |
| 200 | OK | Successful read. |
| 201 | Created | Successful create. |
| 204 | No Content | Successful delete. |
| 400 | Bad Request | Invalid query or payload. |
| 401 | Unauthorized | Missing/invalid token. |
| 403 | Forbidden | Insufficient permissions. |
| 404 | Not Found | Item does not exist. |
| 409 | Conflict | Duplicate resource. |
| 429 | Too Many Requests | Rate limit exceeded. |
| 500 | Internal Server Error | Unexpected server error. |

**Error Response Example (400)**
```json
{
  "error": {
    "code": "INVALID_PAYLOAD",
    "message": "The field 'name' is required."
  }
}
```

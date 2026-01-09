# Architecture Overview

## Interfaces

The Data30 service exposes the following external interfaces:

- **REST/HTTP API**: The primary client-facing interface for health checks and dataset management. The formal contract is defined in [`docs/api/openapi.yaml`](../api/openapi.yaml).

If future event-driven integrations are added, an AsyncAPI specification will be published alongside the OpenAPI document.

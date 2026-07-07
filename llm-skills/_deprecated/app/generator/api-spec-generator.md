---
name: api-spec-generator
description: Generates the design-time API specification (controllers, endpoints, request/response DTOs, routing, security, and error models) from the domain model and architecture design. Produces api_spec as part of the application blueprint; distinct from backend/api-generator, which generates runtime API code.
version: 1.0.0
author: OpenAI
category: generator
tags:
  - api
  - rest
  - controller
  - dto
  - http
tools: []
model: inherit

priority: 85
entrypoint: false
parallel: true
timeout: 300
retry: 1

inputs:
  - domain_model
  - architecture_design

outputs:
  - api_spec

invokes: []
---

# api-spec-generator

## Goal

Generate a clean API layer that exposes domain capabilities through RESTful interfaces.

The API layer must be thin and must not contain business logic.

---

# Inputs

```yaml
domain_model:

architecture_design:
```

---

# Outputs

```yaml
api_spec:
  controllers:
  endpoints:
  request_dtos:
  response_dtos:
  routes:
  authentication:
  authorization:
  error_models:
```

---

# Workflow

## Step 1 — Map Domain to API

Convert:

- aggregates → resources
- domain services → endpoints
- domain events → async endpoints (if needed)

---

## Step 2 — Define Controllers

Create controllers per domain module.

Example:

- UserController
- OrderController

---

## Step 3 — Define Endpoints

Design RESTful endpoints:

- GET
- POST
- PUT
- DELETE

---

## Step 4 — Define DTOs

Create:

- Request DTOs
- Response DTOs

Ensure no domain leakage.

---

## Step 5 — Define Routing

Map endpoints to:

- controller methods
- URL structure
- versioning strategy

---

## Step 6 — Define Security Layer

Specify:

- authentication method (JWT, session, etc.)
- authorization rules
- role mapping

---

## Step 7 — Define Error Models

Standardize API errors:

- validation error
- not found
- unauthorized
- internal error

---

# Rules

## Thin API Principle

- No business logic in controllers
- Only orchestration + mapping

---

## DTO Isolation

- DTOs must never leak domain internals
- No entity exposure

---

## REST Consistency

- Use resource-based naming
- Avoid verb-based endpoints

---

## Traceability

Every API element must reference:

- domain model
- requirement
- architecture module

---

## Completion Criteria

API generation is complete only when:

- all aggregates are exposed correctly
- endpoints are defined
- DTOs are mapped
- security rules are defined
- error models are standardized

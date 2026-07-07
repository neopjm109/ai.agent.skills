---
name: api-client-generator
description: Generate type-safe API clients for Next.js applications using fetch/axios with TanStack Query compatibility, DTO separation, and clean architecture principles.
category: frontend
tags:
  - nextjs
  - api-client
  - axios
  - fetch
  - typescript
  - tanstack-query
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate type-safe API client layer for frontend applications.

Focus on isolating HTTP communication from UI and state logic.

# Inputs

- Resource name
- Base URL
- Endpoints (CRUD or custom)
- Request/Response DTO
- Auth requirements
- Error handling strategy

Example:

Resource: User

Endpoints:
- GET /users
- POST /users
- DELETE /users/:id

# Output

Generate:

- API Client class or module
- Request/Response types
- Endpoint functions
- Error handler
- Base client (fetch/axios wrapper)
- Optional interceptors

# Rules

## General
- Never mix API logic with UI or state.
- Always use typed DTOs.
- Keep API layer framework-agnostic if possible.

## HTTP Layer
- Use fetch or axios (configurable).
- Centralize base URL.
- Add timeout handling.
- Add retry logic only if requested.

## DTO
- Do not reuse backend entities directly.
- Separate Request/Response models.

## Error Handling
- Normalize API errors.
- Never expose raw HTTP errors to UI.

## Auth
- Support token injection via interceptor.

## Naming

UserApiClient
OrderApiClient
AuthApiClient

# Output

Production-ready API client layer only.
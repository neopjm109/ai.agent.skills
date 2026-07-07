---
name: api-generator
description: Generate the API layer including Controller, Request DTO, Response DTO and API mapping from business requirements.
category: backend
tags:
  - spring-boot
  - controller
  - dto
  - rest-api
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate a complete REST API layer for a Spring Boot application while keeping business logic inside the Domain layer.

# Inputs

The user should provide:

- API requirements
- Route information
- HTTP methods
- Existing Domain (optional)
- Authentication requirements (optional)

Example:

GET /users

POST /users

PUT /users/{id}

DELETE /users/{id}

# Output

Generate:

Controller

Request DTO

Response DTO

Validation

API mappings

Exception handling integration

The generated API should be production-ready.

# Workflow

1. Analyze API requirements.
2. Identify required endpoints.
3. Design Request DTOs.
4. Design Response DTOs.
5. Design Controller mappings.
6. Build an API specification.
7. Delegate implementation to `spring-senior-programmer`.
8. Validate API consistency.

# Rules

- Controllers should contain minimal business logic.
- Delegate all business processing to Services.
- Use Bean Validation.
- Follow RESTful API conventions.
- Return consistent response structures.
- Avoid exposing Entities directly.
- Keep DTOs immutable when appropriate.
- Generate production-ready code only.
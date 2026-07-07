---
name: backend-orchestrator
description: Orchestrates backend implementation for a feature by coordinating domain, API, service, security, and test generators.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - backend
  - domain
  - api
  - spring
tools: []
model: inherit

priority: 60
entrypoint: false
parallel: true
timeout: 600
retry: 1

inputs:
  - feature
  - application_blueprint
  - target_stack

outputs:
  - backend_artifact

invokes:
  - domain-generator
  - api-generator
  - service-generator
  - validation-generator
  - event-generator
  - security-generator
  - test-generator
---

# backend-orchestrator

## Goal

Generate the complete backend implementation for a Feature by orchestrating domain modeling, API design, business logic, security, and test generation.

This Skill is responsible for backend orchestration only.

It never generates implementation code directly.

---

# Inputs

```yaml
feature:
  id:
  name:
  stories:
  tasks:

application_blueprint:

target_stack:
  backend: Spring Boot
```

---

# Outputs

```yaml
backend_artifact:
  domain:
  api:
  services:
  validations:
  events:
  security:
  tests:
```

---

# Workflow

## Step 1 — Analyze Backend Scope

Analyze Feature to determine:

- Domain boundaries
- API requirements
- Business logic rules
- Security constraints
- Event-driven needs

---

## Step 2 — Generate Domain Layer

Invoke:

- domain-generator

Generate:

```text
Entities
Value Objects
Domain Services
Aggregates
Domain Rules
```

---

## Step 3 — Generate API Layer

Invoke:

- api-generator

Generate:

```text
Controllers
DTOs
Request/Response Models
API Routes
Mapping Layer
```

---

## Step 4 — Generate Service Layer

Invoke:

- service-generator

Generate:

```text
Application Services
Use Cases
Transaction Logic
Business Workflows
```

---

## Step 5 — Generate Validation

Invoke:

- validation-generator

Generate:

```text
Input Validation Rules
Domain Validation Rules
Custom Constraints
```

---

## Step 6 — Generate Events

Invoke:

- event-generator

Generate:

```text
Domain Events
Integration Events
Event Handlers
```

---

## Step 7 — Generate Security

Invoke:

- security-generator

Generate:

```text
Authentication Logic
Authorization Rules
Role/Permission Model
Security Configuration
```

---

## Step 8 — Generate Tests

Invoke:

- backend-test-generator

Generate:

```text
Unit Tests
Integration Tests
API Tests
```

---

## Step 9 — Assemble Backend Artifact

Merge all outputs into backend_artifact.

---

# Backend Artifact Structure

```text
Backend Artifact
│
├── Domain
│   ├── Entities
│   ├── Value Objects
│   └── Domain Services
│
├── API
│   ├── Controllers
│   ├── DTOs
│   └── Mappers
│
├── Services
│
├── Validation
│
├── Events
│
├── Security
│
└── Tests
```

---

# Invocation Flow

```text
Feature
│
├── domain-generator
├── api-generator
├── service-generator
├── validation-generator
├── event-generator
├── security-generator
└── test-generator
↓
Backend Artifact
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Domain required | domain-generator |
| API required | api-generator |
| Business logic required | service-generator |
| Validation required | validation-generator |
| Event-driven system | event-generator |
| Security required | security-generator |
| Testing enabled | test-generator |

---

# Rules

## General

- Never generate implementation code directly.
- Always delegate to specialized generators.
- Maintain strict separation between Domain and API layers.

---

## Domain Layer

- Must contain all business rules
- Must be independent of frameworks
- Must not depend on API layer

---

## API Layer

- Must be thin
- Must only map requests ↔ domain/service
- Must not contain business logic

---

## Consistency

Ensure alignment between:

- Domain ↔ API DTOs
- Service ↔ Domain Rules
- API ↔ External Contracts

---

## Traceability

Every artifact must reference:

- Requirement
- Blueprint Component
- Feature
- Story
- Task

---

## Completion Criteria

Backend orchestration is complete only when:

- Domain generation is complete
- API generation is complete
- Service layer is complete
- Validation, Events, Security, Tests are complete (if required)
- All outputs are merged into backend_artifact
---
name: blueprint-orchestrator
description: Builds a complete application blueprint from unified requirements by orchestrating architecture, domain, database, and API design skills.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - blueprint
  - architecture
  - design
  - planning
tools: []
model: inherit

priority: 90
entrypoint: false
parallel: true
timeout: 300
retry: 1

inputs:
  - unified_requirements
  - target_stack

outputs:
  - application_blueprint

invokes:
  - architecture-generator
  - domain-model-generator
  - database-generator
  - api-spec-generator
---

# blueprint-orchestrator

## Goal

Transform unified requirements into a complete application blueprint.

The blueprint becomes the single source of truth for every downstream generator. It describes **what the application should look like**, not how individual components are implemented.

This Skill never generates source code.

---

# Inputs

```yaml
unified_requirements:
  functional_requirements:
  non_functional_requirements:
  ui_requirements:
  business_rules:

target_stack:
  backend: Spring Boot
  frontend: Next.js
  database: MariaDB
```

---

# Outputs

```yaml
application_blueprint:
  architecture:
  modules:
  domain_model:
  database:
  apis:
  integrations:
  security:
```

---

# Workflow

## Step 1 — Analyze Requirements

Read and classify all requirements into:

- Functional
- Non-functional
- UI
- Business Rules
- External Integrations

---

## Step 2 — Design Architecture

Invoke:

- architecture-generator

Generate:

```text
Architecture Style

Layers

Packages

Modules

Technology Decisions
```

---

## Step 3 — Build Domain Model

Invoke:

- domain-model-generator

Generate:

```text
Aggregates

Entities

Value Objects

Relationships

Business Rules
```

---

## Step 4 — Design Database

Invoke:

- database-generator

Generate:

```text
Tables

Collections

Indexes

Relationships

Constraints
```

---

## Step 5 — Design APIs

Invoke:

- api-spec-generator

Generate:

```text
REST Endpoints

Request Models

Response Models

Authentication

Authorization
```

---

## Step 6 — Assemble Blueprint

Merge all generated outputs into a single Application Blueprint.

---

# Blueprint Structure

```text
Application Blueprint
│
├── Architecture
├── Modules
├── Domain Model
├── Database
├── APIs
├── Integrations
├── Security
└── Technology Stack
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Requirements loaded | architecture-generator |
| Architecture completed | domain-model-generator |
| Domain completed | database-generator |
| Domain completed | api-spec-generator |

---

# Rules

## General

- Never generate implementation code.
- Focus on system design only.
- Ensure every blueprint component is traceable to a requirement.

---

## Architecture

- Keep architecture technology-agnostic where possible.
- Respect the selected target stack.
- Prefer modular design.

---

## Domain

- Domain Model is the source of truth.
- Avoid duplicate entities.
- Normalize relationships.

---

## Database

- Database design must be derived from the Domain Model.
- Avoid redundant schemas.
- Define primary and foreign keys explicitly.

---

## API

- APIs must map directly to business capabilities.
- Follow RESTful naming conventions.
- Ensure consistency between request and response models.

---

## Traceability

Every blueprint element must contain references to:

- originating requirement
- originating feature
- originating document

---

## Completion Criteria

Blueprint generation is complete only when:

- Architecture is defined.
- Domain Model is complete.
- Database schema is designed.
- APIs are defined.
- All outputs have been merged into a single Application Blueprint.
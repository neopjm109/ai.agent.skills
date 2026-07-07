---
name: domain-model-generator
description: Generates domain model structures including entities, value objects, aggregates, and domain rules based on unified requirements and architecture design.
version: 1.0.0
author: OpenAI
category: generator
tags:
  - domain
  - ddd
  - model
  - entity
  - aggregate
tools: []
model: inherit

priority: 90
entrypoint: false
parallel: true
timeout: 300
retry: 1

inputs:
  - unified_requirements
  - architecture_design

outputs:
  - domain_model

invokes: []
---

# domain-model-generator

## Goal

Generate a complete domain model based on business requirements and architecture design.

Focus on core business concepts and domain boundaries.

No infrastructure or API concerns should be included.

---

# Inputs

```yaml
unified_requirements:

architecture_design:
```

---

# Outputs

```yaml
domain_model:
  aggregates:
  entities:
  value_objects:
  domain_services:
  domain_events:
  relationships:
  invariants:
```

---

# Workflow

## Step 1 — Identify Core Domains

Extract:

- core business domains
- subdomains
- bounded contexts

---

## Step 2 — Define Aggregates

Identify aggregate roots and boundaries.

Example:

- User Aggregate
- Order Aggregate
- Payment Aggregate

---

## Step 3 — Define Entities

Define entities inside each aggregate.

- Identity-based objects
- Lifecycle-managed objects

---

## Step 4 — Define Value Objects

Extract immutable concepts:

- Money
- Email
- Address
- Status

---

## Step 5 — Define Domain Services

Define domain logic that does not belong to a single entity.

---

## Step 6 — Define Domain Events

Capture business events:

- UserCreated
- OrderPlaced
- PaymentCompleted

---

## Step 7 — Define Invariants

Define business rules that must always hold true.

---

## Step 8 — Build Relationships

Define relationships between:

- aggregates
- entities
- value objects

---

# Rules

## Domain Purity

- Must not depend on API layer
- Must not depend on database schema
- Must be framework-agnostic

---

## Aggregate Rules

- One aggregate root per transaction boundary
- No direct cross-aggregate entity mutation
- Use IDs for cross references only

---

## Invariants

- Must be enforceable within domain layer
- Must not rely on external systems

---

## Traceability

Each domain element must reference:

- requirement
- architecture module
- business rule

---

## Completion Criteria

Domain model is complete only when:

- all core domains are identified
- aggregates are defined
- entities are assigned
- value objects are extracted
- domain events are defined
- invariants are specified
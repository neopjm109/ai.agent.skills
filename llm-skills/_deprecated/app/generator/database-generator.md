---
name: database-generator
description: Generates database schema design including tables, relationships, indexes, constraints, and persistence mapping based on domain model and architecture design.
version: 1.0.0
author: OpenAI
category: generator
tags:
  - database
  - schema
  - sql
  - erd
  - persistence
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
  - database_schema

invokes: []
---

# database-generator

## Goal

Convert the domain model into a physical database schema design.

Ensure alignment with aggregates and persistence strategy.

---

# Inputs

```yaml
domain_model:

architecture_design:
```

---

# Outputs

```yaml
database_schema:
  tables:
  relationships:
  indexes:
  constraints:
  migrations:
  mapping_rules:
```

---

# Workflow

## Step 1 — Identify Persistence Strategy

Determine:

- relational vs NoSQL
- normalization level
- aggregate persistence boundaries

---

## Step 2 — Generate Tables

Map:

- entities → tables
- value objects → embedded fields or tables

---

## Step 3 — Define Relationships

Define:

- one-to-one
- one-to-many
- many-to-many

---

## Step 4 — Define Constraints

Include:

- primary keys
- foreign keys
- unique constraints
- not null rules

---

## Step 5 — Define Indexes

Optimize for:

- query patterns
- performance hotspots
- join efficiency

---

## Step 6 — Define Migrations

Describe schema evolution strategy.

---

## Step 7 — Define Mapping Rules

Map:

- domain model ↔ database schema
- aggregate boundaries ↔ tables

---

# Rules

## Domain Alignment

- Must strictly follow domain model
- No extra tables without domain justification

---

## Performance Awareness

- Avoid unnecessary joins
- Prefer aggregate-aligned design

---

## Traceability

Each schema element must reference:

- domain entity
- requirement
- architecture module

---

## Completion Criteria

Database design is complete only when:

- all aggregates are mapped
- all entities have persistence representation
- relationships are defined
- indexes and constraints are specified
---
name: project-planner
description: Decomposes an application blueprint into epics, features, stories, tasks, and dependency graphs to create an executable development plan.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - planner
  - project
  - roadmap
  - feature
  - dependency
tools: []
model: inherit

priority: 80
entrypoint: false
parallel: false
timeout: 300
retry: 1

inputs:
  - application_blueprint

outputs:
  - execution_plan

invokes: []
---

# project-planner

## Goal

Transform an Application Blueprint into an executable development plan.

The execution plan becomes the source of truth for downstream orchestrators, defining the order, priority, and dependencies of implementation work.

This Skill never generates source code.

---

# Inputs

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

# Outputs

```yaml
execution_plan:
  epics:
  features:
  stories:
  tasks:
  dependency_graph:
  execution_order:
```

---

# Workflow

## Step 1 — Analyze Blueprint

Analyze the complete Application Blueprint.

Identify:

- Business Domains
- Modules
- APIs
- Database Objects
- UI Screens
- External Integrations

---

## Step 2 — Generate Epics

Group related functionality into Epics.

Example:

```text
Authentication

User Management

Order Management

Administration
```

---

## Step 3 — Generate Features

Split every Epic into Features.

Example:

```text
Authentication

├── Login

├── Logout

├── Refresh Token

└── Password Reset
```

---

## Step 4 — Generate Stories

Break every Feature into implementation Stories.

Example:

```text
Login

├── Login API

├── Login Screen

├── JWT Generation

└── Session Management
```

---

## Step 5 — Generate Tasks

Generate implementation Tasks for every Story.

Example:

```text
Create Entity

Create Repository

Create Service

Create Controller

Create UI Page

Create API Client

Create Tests
```

---

## Step 6 — Resolve Dependencies

Build dependency relationships.

Determine:

- prerequisite tasks
- blocking tasks
- independent tasks
- parallel execution groups

---

## Step 7 — Calculate Execution Order

Produce an execution order based on the dependency graph.

Prefer parallel execution whenever dependencies allow.

---

# Execution Plan Structure

```text
Execution Plan
│
├── Epics
│
├── Features
│
├── Stories
│
├── Tasks
│
├── Dependency Graph
│
└── Execution Order
```

---

# Dependency Rules

Examples:

```text
Database

↓

Backend

↓

API

↓

Frontend

↓

Integration

↓

Testing
```

Another example:

```text
Entity

↓

Repository

↓

Service

↓

Controller
```

---

# Rules

## Planning

- Every Feature must belong to exactly one Epic.
- Every Story must belong to exactly one Feature.
- Every Task must belong to exactly one Story.

---

## Dependencies

- Never create circular dependencies.
- Minimize blocking tasks.
- Maximize opportunities for parallel execution.

---

## Granularity

Tasks should be:

- independently executable
- measurable
- reviewable
- idempotent

---

## Prioritization

Priority should consider:

- business value
- dependency order
- implementation complexity
- technical risk

---

## Traceability

Every Epic, Feature, Story, and Task must reference:

- originating requirement
- originating blueprint component
- originating module

---

## Completion Criteria

Planning is complete only when:

- every blueprint component has been assigned to an Epic
- every Epic contains Features
- every Feature contains Stories
- every Story contains Tasks
- dependency graph is valid
- execution order has been generated
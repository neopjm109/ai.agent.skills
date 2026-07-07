---
name: feature-orchestrator
description: Orchestrates the complete implementation of a single feature by coordinating backend, frontend, and integration orchestrators.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - feature
  - backend
  - frontend
  - integration
tools: []
model: inherit

priority: 70
entrypoint: false
parallel: true
timeout: 600
retry: 1

inputs:
  - feature
  - application_blueprint
  - target_stack

outputs:
  - feature_artifact

invokes:
  - backend-orchestrator
  - frontend-orchestrator
  - integration-orchestrator
---

# feature-orchestrator

## Goal

Generate a complete implementation for a single Feature by coordinating all required implementation orchestrators.

Each Feature should become an independently deliverable unit of functionality.

This Skill never generates implementation code directly.

---

# Inputs

```yaml
feature:
  id:
  name:
  description:
  stories:
  tasks:

application_blueprint:

target_stack:
  backend:
  frontend:
  database:
```

---

# Outputs

```yaml
feature_artifact:
  backend:
  frontend:
  integration:
  status:
```

---

# Workflow

## Step 1 — Analyze Feature

Read:

- Feature
- Stories
- Tasks

Determine:

- backend scope
- frontend scope
- integration scope

---

## Step 2 — Generate Backend

Invoke:

- backend-orchestrator

Generate:

```text
Entities

Repositories

Services

Controllers

DTOs

Security

Tests
```

---

## Step 3 — Generate Frontend

Invoke:

- frontend-orchestrator

Generate:

```text
Pages

Components

Forms

Dialogs

Tables

API Clients

State

Tests
```

---

## Step 4 — Generate Integration

Invoke:

- integration-orchestrator

Generate:

```text
API Contracts

OpenAPI

Frontend Client

Events

Redis

Messaging

External Integrations
```

---

## Step 5 — Merge Outputs

Merge Backend, Frontend, and Integration outputs into a Feature Artifact.

---

# Feature Artifact Structure

```text
Feature Artifact
│
├── Backend
│
├── Frontend
│
├── Integration
│
└── Metadata
```

---

# Invocation Flow

```text
Feature

│

├── backend-orchestrator

├── frontend-orchestrator

└── integration-orchestrator

↓

Merge Outputs

↓

Feature Artifact
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Backend implementation required | backend-orchestrator |
| Frontend implementation required | frontend-orchestrator |
| API or external integration required | integration-orchestrator |

---

# Rules

## General

- Never generate implementation code directly.
- Delegate implementation to specialized orchestrators.
- Generate only artifacts required by the current Feature.

---

## Backend

Invoke backend generation only if the Feature requires:

- business logic
- persistence
- APIs
- authentication
- background processing

---

## Frontend

Invoke frontend generation only if the Feature requires:

- pages
- UI components
- forms
- tables
- dialogs
- state management

---

## Integration

Invoke integration generation only if the Feature requires:

- REST APIs
- OpenAPI
- API Client
- Redis
- Messaging
- External Services
- Event Processing

---

## Parallel Execution

Backend, Frontend, and Integration may execute in parallel whenever dependencies permit.

---

## Traceability

Every generated artifact must reference:

- Feature
- Story
- Task
- Requirement
- Blueprint Component

---

## Completion Criteria

Feature orchestration is complete only when:

- Backend generation has completed (if required)
- Frontend generation has completed (if required)
- Integration generation has completed (if required)
- Outputs have been merged into a Feature Artifact
- Status has been reported
---
name: frontend-orchestrator
description: Orchestrates frontend implementation for a feature by coordinating page, layout, component, form, table, dialog, state, API client, and frontend test generators.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - frontend
  - nextjs
  - react
  - ui
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
  - frontend_artifact

invokes:
  - layout-generator
  - page-generator
  - component-generator
  - form-generator
  - table-generator
  - dialog-generator
  - hook-generator
  - state-generator
  - api-client-generator
  - test-generator
---

# frontend-orchestrator

## Goal

Generate the complete frontend implementation for a Feature by orchestrating specialized frontend generators.

This Skill is responsible for coordinating frontend generation only.

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
  frontend: Next.js
```

---

# Outputs

```yaml
frontend_artifact:
  layouts:
  pages:
  components:
  forms:
  tables:
  dialogs:
  hooks:
  state:
  api_clients:
  tests:
```

---

# Workflow

## Step 1 — Analyze Frontend Scope

Analyze the Feature and determine:

- User Flows
- Screens
- Layouts
- Components
- Forms
- Tables
- Dialogs
- State Management
- API Communication

---

## Step 2 — Generate Layouts

Invoke:

- layout-generator

Generate:

```text
Application Layouts

Navigation

Sidebar

Header

Footer
```

---

## Step 3 — Generate Pages

Invoke:

- page-generator

Generate:

```text
Pages

Routes

Loading Pages

Error Pages
```

---

## Step 4 — Generate Components

Invoke:

- component-generator

Generate:

```text
Reusable Components

Feature Components

Shared Components
```

---

## Step 5 — Generate Forms

Invoke:

- form-generator

Generate:

```text
Input Forms

Validation Rules

Submission Logic
```

---

## Step 6 — Generate Tables

Invoke:

- table-generator

Generate:

```text
Data Tables

Pagination

Sorting

Filtering
```

---

## Step 7 — Generate Dialogs

Invoke:

- dialog-generator

Generate:

```text
Modal Dialogs

Confirmation Dialogs

Alert Dialogs
```

---

## Step 8 — Generate Hooks

Invoke:

- hook-generator

Generate:

```text
Custom Hooks

Data Fetching Hooks

Mutation Hooks
```

---

## Step 9 — Generate State

Invoke:

- state-generator

Generate:

```text
Global State

Feature State

Store

Actions
```

---

## Step 10 — Generate API Client

Invoke:

- api-client-generator

Generate:

```text
REST Client

Request Models

Response Models

Error Handling
```

---

## Step 11 — Generate Tests

Invoke:

- test-generator

Generate:

```text
Component Tests

Page Tests

Integration Tests

Mock APIs
```

---

## Step 12 — Assemble Frontend Artifact

Merge all outputs into a Frontend Artifact.

---

# Frontend Artifact Structure

```text
Frontend Artifact
│
├── Layouts
│
├── Pages
│
├── Components
│
├── Forms
│
├── Tables
│
├── Dialogs
│
├── Hooks
│
├── State
│
├── API Clients
│
└── Tests
```

---

# Invocation Flow

```text
Frontend Feature

│

├── layout-generator

├── page-generator

├── component-generator

├── form-generator

├── table-generator

├── dialog-generator

├── hook-generator

├── state-generator

├── api-client-generator

└── frontend-test-generator

↓

Frontend Artifact
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Layout required | layout-generator |
| Screen required | page-generator |
| UI component required | component-generator |
| User input required | form-generator |
| Data grid required | table-generator |
| Modal interaction required | dialog-generator |
| Custom logic required | hook-generator |
| State management required | state-generator |
| Backend API required | api-client-generator |
| Testing enabled | test-generator |

---

# Rules

## General

- Never generate implementation code directly.
- Delegate all implementation to specialized generators.
- Generate only frontend artifacts.

---

## Dependency Order

Generation should generally follow:

```text
Layout

↓

Page

↓

Component

↓

Form / Table / Dialog

↓

Hook

↓

State

↓

API Client

↓

Tests
```

---

## Parallel Execution

The following generators may execute in parallel whenever dependencies allow:

- component-generator
- form-generator
- table-generator
- dialog-generator
- hook-generator

---

## UI Consistency

Ensure consistency across:

- Layouts
- Navigation
- Components
- Design System
- Naming Conventions

---

## API Consistency

Frontend API Clients must match:

- API Specification
- Backend DTOs
- Authentication Strategy
- Error Response Format

---

## Traceability

Every generated frontend artifact must reference:

- Requirement
- Blueprint Component
- Feature
- Story
- Task

---

## Completion Criteria

Frontend orchestration is complete only when:

- Layout generation has completed.
- Page generation has completed.
- Component generation has completed.
- Form generation has completed (if required).
- Table generation has completed (if required).
- Dialog generation has completed (if required).
- Hook generation has completed.
- State generation has completed.
- API Client generation has completed.
- Test generation has completed (if enabled).
- All outputs have been merged into a Frontend Artifact.
---
name: validation-orchestrator
description: Validates the generated application by coordinating architecture, backend, frontend, integration, security, and quality validation skills before project completion.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - validation
  - quality
  - review
  - verification
tools: []
model: inherit

priority: 40
entrypoint: false
parallel: true
timeout: 600
retry: 1

inputs:
  - application_blueprint
  - execution_result
  - generated_artifacts

outputs:
  - validation_report

invokes:
  - architecture-validator
  - backend-validator
  - frontend-validator
  - integration-validator
  - security-validator
  - test-validator
---

# validation-orchestrator

## Goal

Validate every generated artifact to ensure consistency, completeness, correctness, and quality before the project is considered complete.

This Skill coordinates validation activities across architecture, backend, frontend, integration, security, and testing.

This Skill never modifies implementation artifacts.

---

# Inputs

```yaml
application_blueprint:

execution_result:

generated_artifacts:
```

---

# Outputs

```yaml
validation_report:
  overall_status:
  passed:
  warnings:
  errors:
  metrics:
  recommendations:
```

---

# Workflow

## Step 1 — Load Project Artifacts

Load:

- Application Blueprint
- Generated Artifacts
- Execution Result

Verify all required artifacts are available.

---

## Step 2 — Validate Architecture

Invoke:

- architecture-validator

Validate:

```text
Architecture Layers

Module Dependencies

Package Structure

Naming Conventions

Circular Dependencies
```

---

## Step 3 — Validate Backend

Invoke:

- backend-validator

Validate:

```text
Entities

Repositories

Services

Controllers

DTOs

Validation Rules

Event Flow
```

---

## Step 4 — Validate Frontend

Invoke:

- frontend-validator

Validate:

```text
Layouts

Pages

Components

Forms

Tables

Dialogs

Routing

State Management
```

---

## Step 5 — Validate Integration

Invoke:

- integration-validator

Validate:

```text
API Contracts

OpenAPI

Redis

Messaging

External Services

Contract Consistency
```

---

## Step 6 — Validate Security

Invoke:

- security-validator

Validate:

```text
Authentication

Authorization

Permissions

Secrets

Sensitive Data

Security Configuration
```

---

## Step 7 — Validate Tests

Invoke:

- test-validator

Validate:

```text
Unit Tests

Integration Tests

End-to-End Tests

Coverage

Missing Tests
```

---

## Step 8 — Aggregate Results

Merge all validation results.

Calculate:

- Overall Status
- Error Count
- Warning Count
- Validation Metrics

---

## Step 9 — Generate Validation Report

Generate:

```text
Passed Checks

Warnings

Errors

Recommendations

Quality Metrics
```

---

# Validation Categories

```text
Validation
│
├── Architecture
├── Backend
├── Frontend
├── Integration
├── Security
└── Testing
```

---

# Validation Levels

```text
PASS

WARNING

ERROR
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Blueprint available | architecture-validator |
| Backend generated | backend-validator |
| Frontend generated | frontend-validator |
| Integration generated | integration-validator |
| Security enabled | security-validator |
| Tests generated | test-validator |

---

# Rules

## General

- Never generate implementation code.
- Never modify generated artifacts.
- Perform read-only validation.

---

## Completeness

Verify:

- No missing components
- No missing APIs
- No missing database objects
- No missing screens
- No missing tests

---

## Consistency

Verify consistency between:

- Blueprint ↔ Backend
- Blueprint ↔ Frontend
- Backend ↔ API
- API ↔ Frontend
- Events ↔ Messaging
- Redis ↔ Cache Strategy

---

## Dependency Validation

Detect:

- Circular Dependencies
- Broken References
- Invalid Imports
- Missing Relationships

---

## Security Validation

Verify:

- Authentication
- Authorization
- Sensitive Data Handling
- Secret Management
- Security Configuration

---

## Quality Metrics

Calculate:

- Test Coverage
- Module Coupling
- Dependency Count
- API Coverage
- Validation Success Rate

---

## Traceability

Every validation finding must reference:

- Requirement
- Blueprint Component
- Feature
- Story
- Task
- Generated Artifact

---

## Failure Policy

Validation must continue even if errors are detected.

Collect all findings into a single Validation Report.

---

## Completion Criteria

Validation is complete only when:

- Every validation category has finished.
- Every generated artifact has been evaluated.
- Overall project status has been determined.
- Validation Report has been generated.
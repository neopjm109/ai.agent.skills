---
name: app-orchestrator
description: Orchestrates the complete software generation pipeline from project documents by invoking analysis, planning, generation, validation, and review skills.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - application
  - software-generation
  - planning
  - architecture
  - automation
tools: []
model: inherit

priority: 100
entrypoint: true
parallel: false
timeout: 600
retry: 1

inputs:
  - documents
  - target_stack
  - options

outputs:
  - application_blueprint
  - execution_plan
  - generated_artifacts
  - validation_report
  - review_summary
  - remaining_tasks

invokes:
  - docs-analyze-pptx
  - docs-analyze-docx
  - docs-analyze-xlsx
  - docs-analyze-markdown
  - blueprint-orchestrator
  - project-planner
  - feature-orchestrator
  - execution-orchestrator
  - validation-orchestrator
  - remediation-orchestrator
  - review-orchestrator
---

# app-orchestrator

## Goal

Receive one or more project documents, understand the application requirements, build an application blueprint, and orchestrate the complete software generation workflow.

This Skill **never generates implementation code directly**. It delegates all work to specialized Skills while managing execution order, dependency resolution, validation, and reporting.

---

# Inputs

```yaml
documents:
  - requirements.docx
  - ui-design.pptx
  - api-spec.xlsx

target_stack:
  backend: Spring Boot
  frontend: Next.js
  database: MariaDB

options:
  generate_tests: true
  generate_docker: true
  generate_ci: true
  max_remediation_iterations: 2
```

---

# Outputs

```yaml
application_blueprint

execution_plan

generated_artifacts

validation_report

review_summary

remaining_tasks
```

---

# Workflow

## Step 1 — Analyze Documents

Invoke:

- docs-analyze-pptx
- docs-analyze-docx
- docs-analyze-xlsx
- docs-analyze-markdown

Output:

```text
Unified Requirements
```

---

## Step 2 — Build Blueprint

Invoke:

- blueprint-orchestrator

Generate:

```text
Architecture

Modules

Domain Model

Database Design

API Overview

Technology Stack
```

---

## Step 3 — Plan Development

Invoke:

- project-planner

Generate:

```text
Epics

Features

Stories

Tasks

Dependency Graph

Execution Priority
```

---

## Step 4 — Generate Features

For each Feature:

Invoke:

- feature-orchestrator

---

## Step 5 — Generate Implementation

Each Feature invokes:

- backend-orchestrator
- frontend-orchestrator
- integration-orchestrator

---

## Step 6 — Resolve Execution

Invoke:

- execution-orchestrator

Purpose:

- Resolve dependency graph
- Determine execution order
- Schedule parallel execution

---

## Step 7 — Validate

Invoke:

- validation-orchestrator

Validate:

```text
Architecture

API Consistency

Database

Dependencies

Security

Naming Rules

Missing Components

Test Coverage
```

---

## Step 8 — Remediate (conditional)

If validation reported errors, invoke:

- remediation-orchestrator

Loop:

```text
map errors → tasks

re-execute affected tasks

re-validate

repeat until pass or max_remediation_iterations reached
```

Unresolved errors are promoted to Remaining Tasks.

If validation passed, skip this step.

---

## Step 9 — Review

Invoke:

- review-orchestrator

Generate:

```text
Project Summary

Coverage Report

Warnings

Improvement Suggestions

Remaining Tasks
```

---

# Invocation Flow

```text
app-orchestrator
│
├── docs-analyze-*
│
├── blueprint-orchestrator
│
├── project-planner
│
├── feature-orchestrator
│   ├── backend-orchestrator
│   ├── frontend-orchestrator
│   └── integration-orchestrator
│
├── execution-orchestrator
│
├── validation-orchestrator
│
├── remediation-orchestrator   (loops back to execution + validation on failure)
│
└── review-orchestrator
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| Documents uploaded | docs-analyze-* |
| Requirements extracted | blueprint-orchestrator |
| Blueprint completed | project-planner |
| Feature discovered | feature-orchestrator |
| Feature generation | backend-orchestrator |
| Feature generation | frontend-orchestrator |
| Feature generation | integration-orchestrator |
| All Features completed | execution-orchestrator |
| Execution completed | validation-orchestrator |
| Validation failed | remediation-orchestrator |
| Validation passed or remediation exhausted | review-orchestrator |

---

# Rules

## General

- Never generate implementation code.
- Never skip required Skills.
- Always delegate work to specialized Skills.
- Maintain clear separation of responsibilities.
- Preserve traceability between requirements and generated artifacts.

---

## Dependency Management

- Respect execution dependencies.
- Never execute downstream Skills before prerequisites.
- Execute independent branches in parallel whenever possible.

---

## Traceability

Every generated artifact must reference:

- source document
- requirement identifier
- originating feature

---

## Incremental Execution

When rerunning:

- detect changed requirements
- regenerate only affected artifacts
- preserve unchanged outputs

---

## Error Handling

If a Skill fails:

- stop dependent Skills
- continue independent branches
- collect failures
- include failure summary in final review

---

## Validation

Validation is mandatory before Review.

Review must never execute if Validation has not completed.

---

## Remediation

- When validation reports errors, remediation runs before Review.
- Remediation re-executes only the tasks mapped from errors, never the whole pipeline.
- Remediation is bounded by `max_remediation_iterations`; unresolved errors are promoted to Remaining Tasks and surfaced in the final Review.

---

## Completion Criteria

The orchestration is complete only when:

- every required Skill has executed
- validation has finished
- review has been generated
- remaining work has been reported
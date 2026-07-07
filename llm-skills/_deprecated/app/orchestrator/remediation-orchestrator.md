---
name: remediation-orchestrator
description: Closes the validation feedback loop by mapping validation errors back to their responsible tasks, re-executing only the affected work, and re-validating until the project passes or the remediation budget is exhausted.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - remediation
  - feedback-loop
  - validation
  - self-healing
tools: []
model: inherit

priority: 35
entrypoint: false
parallel: false
timeout: 600
retry: 1

inputs:
  - validation_report
  - execution_plan
  - execution_result
  - application_blueprint
  - max_remediation_iterations

outputs:
  - remediation_result

invokes:
  - execution-orchestrator
  - validation-orchestrator
---

# remediation-orchestrator

## Goal

Turn the one-way `validate → review` flow into a closed loop.

When validation reports errors, map each error back to the task that produced the faulty artifact, re-execute only those tasks, and re-validate. Repeat until the project passes or the remediation budget is exhausted.

This Skill **never generates implementation code directly**. It re-invokes existing orchestrators against a targeted subset of work.

---

# Inputs

```yaml
validation_report:
  overall_status:
  errors:
  warnings:
  recommendations:

execution_plan:
  tasks:
  dependency_graph:

execution_result:
  completed_tasks:
  failed_tasks:

application_blueprint:

max_remediation_iterations: 2
```

---

# Outputs

```yaml
remediation_result:
  final_status:          # passed | unresolved
  iterations_used:
  remediated_tasks:
  unresolved_errors:     # promoted to review remaining_tasks
  remediation_log:
```

---

# Workflow

## Step 1 — Check Entry Condition

If `validation_report.overall_status == passed`:

- skip remediation entirely
- return `final_status: passed`, `iterations_used: 0`

---

## Step 2 — Map Errors to Tasks

For every error in `validation_report.errors`, resolve the responsible unit using the traceability chain:

```text
error → artifact → task → feature → story
```

Produce a de-duplicated set of tasks that must be regenerated.

Errors that cannot be mapped to any task are collected as `unmappable_errors`.

---

## Step 3 — Build Remediation Subset

From the affected tasks, construct a partial re-execution plan:

- include the affected tasks
- include downstream tasks that depend on them (dependency_graph)
- exclude unaffected, already-passing tasks

---

## Step 4 — Re-Execute (Targeted)

Invoke:

- execution-orchestrator

Scope execution to the remediation subset only. Preserve all unchanged outputs.

---

## Step 5 — Re-Validate

Invoke:

- validation-orchestrator

Re-validate the regenerated artifacts (and any artifacts affected by them).

---

## Step 6 — Loop or Exit

```text
if overall_status == passed        → exit, final_status: passed
else if iterations >= max          → exit, final_status: unresolved
else                               → iterations++, return to Step 2
```

---

## Step 7 — Promote Unresolved

On exit with `unresolved`:

- collect remaining errors + unmappable_errors into `unresolved_errors`
- these are handed to review-orchestrator as `remaining_tasks`

---

# Remediation Loop

```text
validation_report (fail)
        │
        ▼
   map errors → tasks
        │
        ▼
   partial re-execution ──► re-validation
        │                        │
        │        pass ◄──────────┤
        │                        │ fail & budget left
        └────────────◄───────────┘
                     │
              budget exhausted
                     ▼
            promote to remaining_tasks
```

---

# Rules

## Convergence

- Never loop more than `max_remediation_iterations` times.
- Each iteration must reduce the error set; if it does not, exit as `unresolved`.
- Never retry validation failures caused by requirement gaps — promote them instead.

## Targeting

- Re-execute only tasks mapped from errors plus their dependents.
- Never regenerate passing artifacts.
- Preserve traceability across every regenerated artifact.

## Isolation

- Never generate or modify implementation code directly.
- Only re-invoke execution-orchestrator and validation-orchestrator.

---

# Completion Criteria

Remediation is complete only when:

- validation passes, or
- the remediation budget is exhausted and unresolved errors are promoted
- a remediation log has been recorded

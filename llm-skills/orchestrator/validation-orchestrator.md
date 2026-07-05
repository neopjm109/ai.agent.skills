---
name: validation-orchestrator
description: Validates the generated application by coordinating architecture, backend, frontend, integration, security, and test validators. Read-only; runs before review and gates remediation.
version: 1.0.0
category: orchestrator
tags:
  - orchestrator
  - validation
  - quality
  - verification
model: inherit
invokes:
  - architecture-validator
  - backend-validator
  - frontend-validator
  - integration-validator
  - security-validator
  - performance-validator
  - dependency-license-validator
  - test-validator
inputs:
  - application_blueprint
  - execution_result
  - generated_artifacts
outputs:
  - validation_report
---

# Goal

Validate every generated artifact for completeness, consistency, correctness, and quality
before the project is considered done. This skill coordinates validators across
architecture, backend, frontend, integration, security, and testing. It is strictly
**read-only** and **never modifies artifacts**.

# Inputs

```yaml
application_blueprint: {...}
execution_result: {...}
generated_artifacts: {...}
```

# Output

```yaml
validation_report:
  overall_status: PASS | WARNING | ERROR
  passed: [...]
  warnings: [...]
  errors: [...]
  metrics: {...}
  recommendations: [...]
```

# Workflow

## Step 1 — Load artifacts
Load the blueprint, generated artifacts, and execution result. Verify all required inputs are present.

## Step 2 — Validate architecture
Invoke `architecture-validator` → layers, module dependencies, package structure, naming, circular dependencies.

## Step 3 — Validate backend
Invoke `backend-validator` → entities, repositories, services, controllers, DTOs, validation rules, event flow.

## Step 4 — Validate frontend
Invoke `frontend-validator` → layouts, pages, components, forms, tables, dialogs, routing, state.

## Step 5 — Validate integration
Invoke `integration-validator` → API contracts, external services, contract consistency.

## Step 6 — Validate security
Invoke `security-validator` → authentication, authorization, permissions, secrets, sensitive data, config.

## Step 7 — Validate performance
Invoke `performance-validator` → N+1 queries, pagination, timeouts, indexing, caching, bundle/image/render anti-patterns.

## Step 8 — Validate dependencies
Invoke `dependency-license-validator` → known CVEs, license policy, version pinning, duplicates (Gradle + npm).

## Step 9 — Validate tests
Invoke `test-validator` → unit, integration, end-to-end tests, coverage, missing tests.

## Step 10 — Aggregate and report
Merge results; compute overall status, error/warning counts, and metrics; emit the `validation_report`.

# Rules

- Never generate or modify artifacts; perform read-only validation only.
- Only `invokes` listed in frontmatter may be called; they must exist in INVENTORY.md.
- Verify consistency across blueprint ↔ backend ↔ API ↔ frontend and events ↔ messaging ↔ Redis.
- Detect circular dependencies, broken references, invalid imports, and missing relationships.
- Continue validation even when errors are found; collect all findings into one report.
- Every finding must reference its requirement, blueprint component, feature, story, task, and artifact.
- `overall_status` is ERROR if any category reports an error; this gates remediation before review.
- Complete only when every category finishes, every artifact is evaluated, and the report is generated.

# Examples

Input:

```yaml
application_blueprint: {...}
generated_artifacts: { backend: 12 files, frontend: 14 files }
```

Output (abridged):

```
✔ architecture → PASS
✔ backend      → 1 error (OrderMapper missing field: currency)
✔ frontend     → PASS, 1 warning (unused import)
✔ integration  → PASS
✔ security     → PASS
✔ test         → coverage 88%, 1 error (no test for PlaceOrderForm)
validation_report: overall_status=ERROR, errors=2, warnings=1, coverage=88%
```

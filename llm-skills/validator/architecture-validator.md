---
name: architecture-validator
description: Validate the generated codebase against the architecture blueprint for layer separation, module boundaries, and dependency direction, returning a structured pass/fail result.
version: 1.0.0
category: validator
tags:
  - validation
  - architecture
  - layering
  - dependencies
model: inherit
invokes: []
inputs:
  - generated_artifacts
  - architecture_blueprint
outputs:
  - validation_result
---

# Goal

Statically validate the generated codebase against the architecture blueprint. This
skill **only analyzes** — it never modifies code. Findings are reported for the
remediation loop.

# Inputs

Validated inputs (produced upstream): `generated_artifacts`, `architecture_blueprint`.

# Scope

- Layer separation (presentation / application / domain / infrastructure)
- Module boundaries and inter-module coupling
- Dependency direction vs the blueprint (inner layers must not depend on outer)
- Circular dependency detection
- Architecture-style consistency (declared monolith/modular structure honored)
- Missing modules declared in the blueprint but not generated

# Checks

| id | check | severity |
|----|-------|----------|
| AR-01 | Domain layer has no import of infrastructure/framework packages | error |
| AR-02 | Dependency direction matches blueprint (no inner→outer references) | error |
| AR-03 | No circular dependency between modules/packages | error |
| AR-04 | Every module declared in the blueprint exists in the codebase | error |
| AR-05 | Cross-module access goes through declared public API, not internal packages | error |
| AR-06 | Actual layering matches the blueprint's declared architecture style | warning |
| AR-07 | Module coupling (fan-out) stays within the blueprint's stated limit | warning |

# Pass/Fail Criteria

- **pass**: zero `error`-severity findings.
- **fail**: one or more `error` findings. `warning` findings do not fail the run but are reported.

# Output Schema

```yaml
validation_result:
  status: pass | fail
  errors:
    - { id: string, file: string, message: string }
  warnings:
    - { id: string, file: string, message: string }
  metrics:
    checked_modules: int
    checked_files: int
    error_count: int
    warning_count: int
```

# Examples

Input: generated codebase for `order-service` + architecture blueprint declaring
`domain`, `application`, `infrastructure` layers and 4 modules.

Output:

```yaml
validation_result:
  status: fail
  errors:
    - { id: AR-01, file: domain/order/Order.java, message: "domain imports jakarta.persistence infrastructure package" }
    - { id: AR-03, file: module: billing<->catalog, message: "circular dependency detected" }
  warnings:
    - { id: AR-07, file: application/OrderFacade.java, message: "fan-out 9 exceeds blueprint limit 6" }
  metrics: { checked_modules: 4, checked_files: 58, error_count: 2, warning_count: 1 }
```

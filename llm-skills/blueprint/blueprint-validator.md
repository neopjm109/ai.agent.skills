---
name: blueprint-validator
description: Validate the blueprint spec set for internal consistency — every DB table and API resource traces to a domain entity, every event references a defined domain event and module, and architecture modules are coherent — returning a deterministic pass/fail report. Design-time spec gate (distinct from validator/architecture-validator, which checks generated code against the blueprint).
version: 1.0.0
category: blueprint
tags:
  - blueprint
  - validation
  - consistency
  - spec-gate
model: inherit
invokes: []
inputs:
  - blueprint
outputs:
  - validation_result
---

# Goal

Verify that the blueprint specs agree with each other before any code is generated from
them, returning a deterministic pass/fail verdict with specific violations. This validates
the **spec set** (architecture, domain model, database, API, event topology) for internal
consistency; it does not generate specs, and it does not validate generated code — that is
`validator/architecture-validator`. Catching a cross-spec mismatch here prevents rippling a
broken contract into code.

# Scope

- Domain↔database alignment (every persisted entity has a table; every table maps to an entity)
- Domain↔API alignment (every API resource/DTO traces to a domain entity/aggregate)
- Domain↔event alignment (every event references a defined domain event/entity)
- Architecture coherence (every module referenced by other specs is declared; no dangling module)
- Producer/consumer validity (every event producer/consumer is a declared module)

Out of scope: generated-code conformance (see `validator/*`), runtime behavior, requirement
completeness.

# Checks

1. Every entity in `domain_model` marked persistent has a `database` table, and every table
   maps back to a domain entity (no orphan table).
2. Every resource/endpoint in `api_specification` references a domain entity/aggregate that
   exists in `domain_model`.
3. Every event in `event_topology` references a domain event/entity defined in `domain_model`.
4. Every module named across specs is declared in `architecture`; no dangling module reference.
5. Every event producer/consumer is a declared architecture module.

# Pass-Fail Criteria

- **pass**: all checks succeed.
- **fail**: any orphan table, API resource with no domain entity, event with no domain source,
  dangling module, or undefined producer/consumer.

# Output Schema

```yaml
validation_result:
  result: pass | fail
  violations:
    - { area: db | api | event | module, ref: <name>, issue: <what failed> }
  stats: { entities: <n>, tables: <n>, endpoints: <n>, events: <n>, dangling: <n> }
```

# Rules

- Report violations only; never modify the blueprint.
- Deterministic verdict: any single violation forces `fail`.
- Check specs against each other, not against generated code or outside assumptions.
- Do not judge requirement completeness or code conformance — out of scope.

# Examples

Input:

```yaml
blueprint:
  domain_model: { entities: [User, Order] }         # no Coupon entity
  database: { tables: [users, orders, coupons] }     # orphan table
  api_specification: { resources: [User, Order, Coupon] }   # Coupon has no entity
  event_topology: { events: [OrderPlaced], producers: [OrderModule] }
  architecture: { modules: [UserModule, OrderModule] }
```

Output:

```yaml
validation_result:
  result: fail
  violations:
    - { area: db, ref: coupons, issue: "table maps to no domain entity" }
    - { area: api, ref: Coupon, issue: "API resource references undefined domain entity" }
  stats: { entities: 2, tables: 3, endpoints: 3, events: 1, dangling: 2 }
```

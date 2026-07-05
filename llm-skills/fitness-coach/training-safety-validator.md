---
name: training-safety-validator
description: Validate the training plan for safety and balance — injury-constraint compliance, weekly volume sanity, muscle-group balance, and recovery spacing — returning a pass/fail report. Final check of the fitness-coach pipeline.
version: 1.0.0
category: fitness-coach
tags:
  - fitness-coach
  - safety
  - balance
  - validation
model: inherit
invokes: []
inputs:
  - program
  - workouts
  - progression
  - fitness_spec
outputs:
  - safety_report
---

# Goal

Check the plan for safety and balance problems before use, returning a deterministic
pass/fail verdict with fixes. Educational validation; it does not give medical clearance.

# Inputs

Validated inputs (produced upstream): `program`, `workouts`, `progression`, `fitness_spec`.

# Scope

- Constraint compliance (no movement contraindicated by injuries/limits)
- Volume sanity (weekly sets per group within a reasonable range for the level)
- Balance (no neglected antagonist group; push/pull and upper/lower reasonably even)
- Recovery (same muscle group not trained on consecutive days without recovery)

Out of scope: individual medical clearance, precise 1RM prescription.

# Checks

1. No exercise violates a stated injury constraint.
2. Weekly volume per muscle group is within a sane range for the level.
3. Opposing muscle groups are reasonably balanced across the week.
4. Recovery spacing respects at least ~48h for the same group where feasible.

# Pass-Fail Criteria

- **pass**: constraints honored, volume/balance/recovery reasonable.
- **fail**: any contraindicated movement, excessive/insufficient volume, major imbalance, or
  inadequate recovery spacing.

# Output Schema

```yaml
safety_report:
  result: pass | fail
  issues:
    - { area: constraint | volume | balance | recovery, detail: <what>, fix: <suggestion> }
  note: "일반 교육용 — 의료적 우려는 전문가 상담"
  stats: { sessions: <n>, issues: <n> }
```

# Rules

- Report issues and fixes only; never rewrite the plan.
- Deterministic verdict: any contraindicated movement or unsafe volume/recovery forces `fail`.
- Always include the educational-use note; never present as medical advice.
- Judge against the trainee's stated level and constraints, not assumptions.

# Examples

Input:

```yaml
fitness_spec: { level: 초급, constraints: [허리 주의] }
workouts: [ { day: 월, exercises: [ { name: 바벨 데드리프트, target: 등 } ] } ]
program: { days: [ { day: 월 } ] }
```

Output:

```yaml
safety_report:
  result: fail
  issues:
    - { area: constraint, detail: "'허리 주의'인데 바벨 데드리프트(고 척추부하) 포함", fix: "힙 힌지 변형/루마니안 대체 또는 제거" }
  note: "일반 교육용 — 의료적 우려는 전문가 상담"
  stats: { sessions: 1, issues: 1 }
```

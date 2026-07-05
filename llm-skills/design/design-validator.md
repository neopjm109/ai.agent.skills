---
name: design-validator
description: Validate the design spec set for internal consistency — every design-system component references defined tokens, every wireframe/UX-flow screen references defined components, tokens have no duplicate/conflicting definitions, and flow nodes connect to real screens — returning a deterministic pass/fail report. Design-time spec gate (distinct from validator/frontend-validator, which checks generated UI code).
version: 1.0.0
category: design
tags:
  - design
  - validation
  - consistency
  - spec-gate
model: inherit
invokes: []
inputs:
  - design_system_bundle
outputs:
  - validation_result
---

# Goal

Verify that the design specs agree with each other before any UI code is generated from
them, returning a deterministic pass/fail verdict with specific violations. This validates
the **spec set** (tokens, design system, UX flows, wireframes, component specs) for internal
consistency; it does not generate specs, and it does not validate generated UI code — that is
`validator/frontend-validator`. Catching a mismatch here prevents rippling a broken design
contract into frontend code.

# Scope

- Component↔token alignment (every component style references a token defined in `design_tokens`)
- Screen↔component alignment (every wireframe/flow screen references a defined system component)
- Token integrity (no duplicate or conflicting token definitions)
- Flow connectivity (every UX-flow node connects to a defined screen; no dangling node)

Out of scope: visual aesthetics/quality, generated-code conformance (see `validator/frontend-validator`),
accessibility audit.

# Checks

1. Every component in `design_system` references only tokens that exist in `design_tokens`.
2. Every screen in `wireframe` / `ux_flow` references components defined in `design_system`.
3. No token name is defined twice with conflicting values.
4. Every `ux_flow` transition points at a screen that exists; no dangling flow node.

# Pass-Fail Criteria

- **pass**: all checks succeed.
- **fail**: any undefined token reference, undefined component reference, conflicting token,
  or dangling flow node.

# Output Schema

```yaml
validation_result:
  result: pass | fail
  violations:
    - { area: token | component | flow, ref: <name>, issue: <what failed> }
  stats: { tokens: <n>, components: <n>, screens: <n>, dangling: <n> }
```

# Rules

- Report violations only; never modify the design specs.
- Deterministic verdict: any single violation forces `fail`.
- Check specs against each other, not against generated code or outside assumptions.
- Do not judge visual quality or code conformance — out of scope.

# Examples

Input:

```yaml
design_system_bundle:
  design_tokens: { color: [primary, surface] }              # no "danger" token
  design_system: { components: [Button(uses: primary), Alert(uses: danger)] }
  wireframe: { screens: [Checkout(uses: Button, Modal)] }   # Modal undefined
  ux_flow: { nodes: [Cart -> Checkout -> Confirm] }
```

Output:

```yaml
validation_result:
  result: fail
  violations:
    - { area: token, ref: danger, issue: "Alert references undefined token 'danger'" }
    - { area: component, ref: Modal, issue: "Checkout screen references undefined component 'Modal'" }
  stats: { tokens: 2, components: 2, screens: 1, dangling: 2 }
```

---
name: proposal-validator
description: Validate an assembled proposal for RFP requirement coverage, scope↔estimate↔pricing consistency, pricing arithmetic, and required-section completeness, returning a deterministic pass/fail report. Final structured gate of the proposal pipeline (prose style is checked separately by doc-style-checker).
version: 1.0.0
category: proposal
tags:
  - proposal
  - validation
  - coverage
  - final-output
model: inherit
invokes: []
inputs:
  - proposal
  - rfp_analysis
  - proposal_request
outputs:
  - validation_result
---

# Goal

Verify that a proposal is complete and internally consistent before it goes to a client,
returning a deterministic pass/fail verdict with specific violations. This validates the
proposal's structure and coverage against the analyzed RFP; it does not scope, estimate,
price, draft, or judge win-rate. Prose tone/terminology is out of scope — that is
`doc-style-checker`.

# Scope

- RFP coverage (every RFP requirement is addressed in-scope or explicitly out-of-scope)
- Scope↔estimate consistency (every in-scope item has an effort estimate)
- Estimate↔pricing consistency (every estimated item has a price line, when pricing included)
- Pricing arithmetic (breakdown sums to the stated total, in the stated currency)
- Section completeness (required sections present: exec summary, approach, scope, schedule,
  pricing when included, team)

Out of scope: price reasonableness, competitiveness/win-rate, prose quality (see
`doc-style-checker`), execution planning.

# Checks

1. Every requirement in `rfp_analysis` maps to an in-scope or explicit out-of-scope item.
2. Every in-scope item has a corresponding effort estimate; no unsized item.
3. If `include_pricing`, every estimated item has a pricing line, and none is orphaned
   (a price for a non-scoped item).
4. The pricing breakdown sums to the stated total in the target currency.
5. All required proposal sections are present and non-empty.

# Pass-Fail Criteria

- **pass**: all checks succeed.
- **fail**: any unaddressed RFP requirement, unsized in-scope item, missing/orphan price
  line, arithmetic mismatch, or missing required section.

# Output Schema

```yaml
validation_result:
  result: pass | fail
  violations:
    - { area: coverage | estimate | pricing | arithmetic | section, ref: <id/name>, issue: <what failed> }
  stats: { requirements: <n>, uncovered: <n>, unsized: <n>, price_mismatch: <amount|0> }
```

# Rules

- Report violations only; never modify the proposal.
- Deterministic verdict: any single violation forces `fail`.
- Check coverage against `rfp_analysis`, not against outside assumptions.
- Do not judge price levels, competitiveness, or prose — out of scope.

# Examples

Input:

```yaml
proposal:
  scope: { in_scope: [Portal UI, SSO], out_of_scope: [Mobile app] }
  estimate: { by_item: [ { item: Portal UI, pd: 40 } ] }          # SSO unsized
  pricing: { total: 40000000, breakdown: [ { item: Portal UI, amount: 32000000 } ] }
rfp_analysis: { requirements: [Portal UI, SSO, Reporting] }        # Reporting unaddressed
proposal_request: { include_pricing: true, currency: KRW }
```

Output:

```yaml
validation_result:
  result: fail
  violations:
    - { area: coverage, ref: Reporting, issue: "RFP requirement neither in-scope nor out-of-scope" }
    - { area: estimate, ref: SSO, issue: "in-scope item has no effort estimate" }
    - { area: arithmetic, ref: total, issue: "breakdown sums to 32,000,000 but total is 40,000,000" }
  stats: { requirements: 3, uncovered: 1, unsized: 1, price_mismatch: 8000000 }
```

---
name: pricing-generator
description: Convert an effort estimate into a costed pricing breakdown using a rate card, with per-item and total amounts in the target currency. Optional pricing stage of the proposal pipeline.
version: 1.0.0
category: proposal
tags:
  - proposal
  - pricing
  - cost
  - rate-card
model: inherit
invokes: []
inputs:
  - estimate
  - options
outputs:
  - pricing
---

# Goal

Turn a person-day effort estimate into a monetary pricing breakdown using a provided rate
card. This skill only computes cost from effort and rates; it does not re-estimate effort.

# Inputs

```yaml
estimate: { by_item: [ { scope_id, person_days, roles } ], total_person_days: <n> }
options:
  currency: KRW
  rate_card: { senior: 800000, mid: 600000 }   # per person-day
  discount_pct: 0        # optional
  tax_pct: 10            # optional (e.g. VAT)
```

# Output

```yaml
pricing:
  currency: <ccy>
  breakdown: [ { scope_id, amount }, ... ]
  subtotal: <amount>
  discount: <amount>
  tax: <amount>
  total: <amount>
```

# Workflow

## Step 1 — Cost each item
Multiply each item's role-days by the matching rate; sum to the item amount.

## Step 2 — Subtotal, discount, tax
Sum item amounts; apply `discount_pct`, then `tax_pct`, to reach the total.

## Step 3 — Return
Return `pricing`. Stop.

# Rules

- Requires a `rate_card`; if absent, return nothing priced and report that pricing was
  skipped for lack of rates.
- Compute strictly from provided effort and rates; never re-estimate person-days.
- Show every line (subtotal, discount, tax, total) so the math is auditable.
- Currency and rounding follow `options.currency`; state the rounding used.

# Examples

Input:

```yaml
estimate:
  by_item:
    - { scope_id: S-01, person_days: 10, roles: { senior: 4, mid: 6 } }
  total_person_days: 11.5
options: { currency: KRW, rate_card: { senior: 800000, mid: 600000 }, tax_pct: 10 }
```

Output:

```yaml
pricing:
  currency: KRW
  breakdown:
    - { scope_id: S-01, amount: 6800000 }   # 4×800000 + 6×600000
  subtotal: 6800000
  discount: 0
  tax: 680000
  total: 7480000
```

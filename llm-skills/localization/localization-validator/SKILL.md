---
name: localization-validator
description: Validate translated catalogs for missing keys, placeholder/ICU mismatches, untranslated entries, and format validity across locales, returning a pass/fail report. Final stage of the localization pipeline.
version: 1.0.0
category: localization
tags:
  - localization
  - validation
  - i18n
  - final-output
model: inherit
invokes: []
inputs:
  - formatted_catalogs
  - source_catalog
  - l10n_request
outputs:
  - validation_result
---

# Goal

Verify that every locale's catalog is complete, placeholder-safe, and syntactically valid
before use, returning a deterministic pass/fail verdict. This validates catalogs; it does not
translate or fix.

# Scope

- Key completeness (every source key present in every target locale)
- Placeholder parity (same placeholders/tokens as source, none added/dropped)
- Untranslated detection (target string identical to source where it should differ)
- Format validity (well-formed ICU/target message syntax)

Out of scope: translation quality/nuance, prose documents, runtime i18n code.

# Checks

1. Each target locale contains every translatable source key.
2. Each entry's placeholder set matches the source entry exactly.
3. No translatable entry is left equal to the source (excluding legitimate identical terms).
4. Messages parse as valid `format` (e.g. balanced ICU braces/plural forms).

# Pass/Fail Criteria

- **pass**: all checks succeed for all locales.
- **fail**: any missing key, placeholder mismatch, untranslated entry, or invalid syntax.

# Output Schema

```yaml
validation_result:
  result: pass | fail
  issues:
    - { locale, key, issue: missing-key | placeholder-mismatch | untranslated | invalid-format }
  stats: { locales: <n>, keys: <n>, issues: <n> }
```

# Rules

- Report issues only; never translate or edit catalogs.
- Deterministic verdict: any single issue forces `fail`.
- Placeholder parity is exact — extra or missing tokens are always failures.
- Do not judge translation nuance/quality; only the checkable properties above.

# Examples

Input:

```yaml
formatted_catalogs: { en: { "cart.count": "{count} items" }, ja: { "cart.count": "{cnt}個" } }
source_catalog: { entries: [ { key: "cart.count", placeholders: ["{count}"], translatable: true } ] }
l10n_request: { target_locales: [en, ja] }
```

Output:

```yaml
validation_result:
  result: fail
  issues:
    - { locale: ja, key: "cart.count", issue: placeholder-mismatch }   # {cnt} ≠ {count}
  stats: { locales: 2, keys: 1, issues: 1 }
```

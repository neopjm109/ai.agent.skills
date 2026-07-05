---
name: dependency-license-validator
description: Statically validate backend (Gradle) and frontend (npm) dependencies for known CVEs, license compatibility, pinned versions, and duplicates, returning a pass/fail result.
version: 1.0.0
category: validator
tags:
  - validation
  - dependencies
  - security
  - license
  - supply-chain
model: inherit
invokes: []
inputs:
  - generated_backend_artifacts
  - generated_frontend_artifacts
  - policy
outputs:
  - validation_result
---

# Goal

Statically validate the project's declared dependencies (Spring Boot / Gradle and Next.js / npm)
for supply-chain and compliance risks: known CVEs, license compatibility against policy, unpinned
versions, and duplicate/conflicting versions. This skill **only analyzes** manifests — it never
modifies build files or upgrades dependencies. Failures are reported for the remediation loop.

# Inputs

Validated inputs (produced upstream): `generated_backend_artifacts`, `generated_frontend_artifacts`, `policy`.

# Scope

- Backend: `build.gradle` / lockfile dependency versions and licenses
- Frontend: `package.json` / `package-lock.json` dependency versions and licenses
- Cross-cutting: version pinning, duplicate/conflicting versions, disallowed licenses

# Checks

| id | check | severity |
|----|-------|----------|
| DL-01 | No dependency with a known critical/high CVE | error |
| DL-02 | No license that violates the policy allowlist (e.g. GPL in a proprietary product) | error |
| DL-03 | Direct dependencies are version-pinned (no floating `+` / `latest` / `^` on criticals) | warning |
| DL-04 | No duplicate/conflicting versions of the same library | warning |
| DL-05 | No unmaintained/abandoned dependency where a maintained alternative exists | warning |

# Pass/Fail Criteria

- **pass**: zero `error`-severity findings.
- **fail**: one or more `error` findings. `warning` findings do not fail the run but are reported.
- If no vulnerability/license data source is available, report DL-01/DL-02 as `unknown` in
  `metrics` rather than silently passing.

# Output Schema

```yaml
validation_result:
  status: pass | fail
  errors:
    - { id: string, dependency: string, version: string, message: string }
  warnings:
    - { id: string, dependency: string, version: string, message: string }
  metrics:
    backend_deps: int
    frontend_deps: int
    error_count: int
    warning_count: int
    cve_source: available | unknown
```

# Examples

Input: generated backend `build.gradle` (32 deps) + frontend `package.json` (57 deps) + policy `{ allow: [MIT, Apache-2.0, BSD-3-Clause], deny: [GPL-3.0] }`.

Output:

```yaml
validation_result:
  status: fail
  errors:
    - { id: DL-02, dependency: some-gpl-lib, version: 2.1.0, message: "GPL-3.0 violates policy allowlist" }
  warnings:
    - { id: DL-03, dependency: axios, version: "^1", message: "floating range on HTTP client; pin exact version" }
  metrics: { backend_deps: 32, frontend_deps: 57, error_count: 1, warning_count: 1, cve_source: available }
```

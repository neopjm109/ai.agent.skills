---
name: cicd-generator
description: Generate CI/CD pipelines and reusable build/test/deploy scripts (no containers) for the Spring Boot + Next.js monorepo, with a configurable deploy hook.
version: 1.0.0
category: deployment
tags:
  - deployment
  - ci-cd
  - github-actions
  - build
  - scripts
model: inherit
invokes: []
inputs:
  - cicd_requirements
outputs:
  - cicd_code
---

# Goal

Generate CI/CD pipeline definitions and reusable shell scripts that build, test, and deploy the
Spring Boot (Gradle) backend and Next.js (npm) frontend — **without containerization**. Deploy
runs through a configurable hook/script so the actual target (VM, PaaS, cloud) stays owned by the
user's infrastructure. This skill performs analysis + config generation only; it does not deploy.

# Inputs

```yaml
cicd_requirements:
  provider: github-actions        # github-actions | gitlab-ci
  monorepo: true
  apps:
    backend: { build: gradle, java: 21, tests: true }
    frontend: { build: npm, node: 20, tests: true }
  environments: [dev, staging, prod]
  deploy: script-hook             # scripts/deploy.sh <env>; target owned by user infra
  triggers: { push: [main], pull_request: [main] }
```

# Output

```yaml
cicd_code:
  - .github/workflows/ci.yml       # build + lint + test (both apps, per-app jobs/matrix)
  - .github/workflows/deploy.yml   # per-environment deploy via deploy hook
  - scripts/build.sh               # gradle bootJar + next build
  - scripts/test.sh                # gradle test + npm test
  - scripts/deploy.sh              # configurable deploy hook (rsync/scp/CLI placeholder)
```

# Workflow

## Step 1 — Analyze pipeline scope
Resolve provider, monorepo layout, per-app build/test commands, environments, and triggers.

## Step 2 — Design CI (build + test)
Define per-app jobs (or a matrix): backend `./gradlew build`, frontend `npm ci && npm run build`,
plus tests and lint. Cache Gradle/npm. Fail fast; upload build artifacts (JAR / .next).

## Step 3 — Design CD (deploy)
Define a per-environment deploy workflow gated by environment protection rules that runs
`scripts/deploy.sh <env>`. The script is a hook — it reads env/secrets and pushes the built
artifact to the user-owned target; keep the actual transport as a clearly-marked placeholder.

## Step 4 — Generate reusable scripts
Emit `build.sh`, `test.sh`, `deploy.sh` so the same commands run locally and in CI.

# Rules

- No Docker/containers — build native artifacts (`bootJar`, `next build`) and deploy via script hook.
- Deploy target belongs to user infrastructure; the deploy step must be a configurable hook, never a hardcoded host.
- Reference secrets from CI secret stores / environments only; never inline credentials.
- Keep local and CI commands identical by routing both through the generated scripts.
- Gate production deploys behind environment protection / manual approval where the provider supports it.
- Reference the environment keys produced by `env-config-generator`; do not redefine them here.

# Examples

Input:

```yaml
cicd_requirements:
  provider: github-actions
  apps: { backend: { build: gradle, java: 21 }, frontend: { build: npm, node: 20 } }
  environments: [dev, prod]
  deploy: script-hook
```

Output (abridged):

```yaml
# .github/workflows/ci.yml
name: ci
on: { push: { branches: [main] }, pull_request: { branches: [main] } }
jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { distribution: temurin, java-version: "21", cache: gradle }
      - run: ./gradlew build
  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: npm }
      - run: npm ci && npm run build && npm test
```

```bash
# scripts/deploy.sh
set -euo pipefail
ENV="${1:?usage: deploy.sh <env>}"
# build artifacts assumed present (bootJar / .next)
# TODO(user-infra): replace with your transport (rsync/scp/platform CLI)
echo "Deploying to ${ENV} using secrets from CI environment '${ENV}'"
```

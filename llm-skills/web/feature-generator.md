---
name: feature-generator
description: Generate a complete Next.js feature module (Feature-Sliced Design) — api, hooks, components, model, types, constants, utils — from business requirements.
version: 1.0.0
category: frontend
tags:
  - nextjs
  - react
  - typescript
  - feature
  - fsd
model: inherit
invokes:
  - typescript-senior-programmer
inputs:
  - feature_requirements
outputs:
  - feature_module
---

# Goal

Generate a production-ready Feature module following Feature-Sliced Design (FSD),
including only the files required by the requested functionality. Delegates
implementation to `typescript-senior-programmer`.

# Inputs

```yaml
feature_requirements:
  name: user
  requirements:
    - view user list
    - search by name
    - edit user
    - delete user
  api_spec: <optional>
```

# Output

```yaml
feature_module: |
  Canonical FSD folder layout:
  features/<name>/
  ├── api/          # endpoint functions (from api-client-generator)
  ├── hooks/        # data + orchestration hooks
  ├── components/   # feature UI
  ├── model/        # business logic / stores
  ├── types/        # feature types
  ├── constants/    # feature constants
  └── utils/        # feature helpers
```

# Workflow

## Step 1 — Define the boundary
Analyze requirements and identify the Feature boundary and required slices.

## Step 2 — Plan the slices
Decide which of `api / hooks / components / model / types / constants / utils` are needed
(generate only what the feature requires).

## Step 3 — Delegate to sub-generators and implementation
Delegate data to `data-generator`, forms/tables/etc. to the component-level generators, and
the remaining implementation to `typescript-senior-programmer`.

## Step 4 — Validate
Confirm consistency across slices and that UI, business logic, and data access are separated.

# Rules

- Follow the single canonical FSD layout: `features/<name>/{api,hooks,components,model,types,constants,utils}`.
- Generate only files required by the feature; avoid duplicated logic.
- Separate UI, business logic, and data access; reuse existing components where possible.
- Strict TypeScript; single-responsibility components; follow project naming conventions.

# Examples

Input:

```yaml
feature_requirements: { name: user, requirements: [view user list, delete user] }
```

Output (abridged):

```
features/user/
├── api/user-api.ts            # userApi.list(), userApi.remove()
├── hooks/use-users.ts         # useUsers(), useDeleteUser()
├── components/user-table.tsx
├── model/user-selection.ts
├── types/user.ts
├── constants/user-columns.ts
└── utils/format-user.ts
```

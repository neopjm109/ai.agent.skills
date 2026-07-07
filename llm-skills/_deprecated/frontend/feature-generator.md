---
name: feature-generator
description: Generate a complete Next.js feature including API layer, hooks, components, models, types, and supporting files from business requirements.
category: frontend
tags:
  - nextjs
  - react
  - typescript
  - feature
  - generator
  - fsd
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate a production-ready Feature module for a Next.js application.

The generated feature should follow the project's architecture and include only the files required by the requested functionality.

# Inputs

The user should provide:

- Feature or domain name
- Business requirements
- API specification (optional)
- Existing project structure (optional)
- Coding conventions (optional)

Example:

```text
Feature: User

Requirements:
- View user list
- Search by name
- Delete user
- Edit user
```

# Output

Generate a complete Feature module.

Example:

```text
features/user/

api/
hooks/
components/
model/
types/
constants/
utils/
```

Each generated file should:

- Follow project conventions
- Compile without errors
- Include necessary imports
- Avoid unused code
- Follow clean architecture principles

# Workflow

1. Analyze the business requirements.
2. Identify the Feature boundary.
3. Determine required files and directories.
4. Design component responsibilities.
5. Design API layer.
6. Design hooks.
7. Design models and types.
8. Delegate implementation to `nextjs-senior-programmer`.
9. Validate consistency across generated files.

# Rules

- Generate only files required by the feature.
- Follow Feature-based architecture.
- Separate UI, business logic, and data access.
- Prefer composition over inheritance.
- Reuse existing components when possible.
- Avoid duplicated logic.
- Use TypeScript strict typing.
- Keep components focused on a single responsibility.
- Follow project naming conventions.
- Generate production-ready code only.
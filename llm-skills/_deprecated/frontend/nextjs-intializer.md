---
name: nextjs-initializer
description: Initialize a production-ready Next.js project with the required frontend stack and project conventions.
category: frontend
tags:
  - nextjs
  - react
  - typescript
  - initializer
  - tailwindcss
  - shadcn
model: gemma-4-e4b
tools:
  - terminal
  - file
---

# Goal

Initialize a production-ready Next.js project using the selected technology stack and predefined project conventions.

# Inputs

The user may provide:

- Next.js version
- TypeScript
- Tailwind CSS
- shadcn/ui
- TanStack Query
- Zustand
- React Hook Form
- Zod
- ESLint
- Prettier
- Project architecture
- Additional libraries

# Output

Generate:

- Project structure
- Configuration files
- Shared layouts
- Providers
- Base components
- Development environment

The generated project should be immediately runnable.

# Workflow

1. Analyze requested technology stack.
2. Select compatible package versions.
3. Create project structure.
4. Configure development tools.
5. Configure providers.
6. Configure shared layouts.
7. Configure environment.
8. Verify project integrity.

# Rules

- Follow modern Next.js App Router conventions.
- Prefer Server Components by default.
- Enable TypeScript strict mode.
- Configure ESLint and Prettier.
- Minimize unnecessary dependencies.
- Keep the project production-ready.
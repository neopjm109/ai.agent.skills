---
name: component-generator
description: Generate reusable React components for a Next.js application following the project's design system and architecture.
category: frontend
tags:
  - nextjs
  - react
  - component
  - ui
  - shadcn
  - tailwindcss
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate reusable, maintainable, and production-ready React UI components.

Focus on presentation and composition while keeping business logic outside of components.

# Inputs

The user should provide:

- Component name
- Component purpose
- Props
- UI requirements
- Interaction requirements (optional)
- Existing design system (optional)

Example:

Component: UserCard

Props:
- name
- email
- avatar
- status

Requirements:
- Responsive
- Clickable
- Loading state
- Empty avatar fallback

# Output

Generate:

- Component
- Props interface
- Supporting types (if required)
- Styling
- Loading state (if applicable)
- Empty state (if applicable)
- Export definitions

The generated component should compile successfully and be reusable across multiple features.

# Workflow

1. Analyze component requirements.
2. Identify the component's responsibility.
3. Design the public Props interface.
4. Separate presentation from business logic.
5. Build the component specification.
6. Delegate implementation to `typescript-senior-programmer`.
7. Validate reusability and consistency.
8. Return the completed component.

# Rules

## General

- Generate reusable UI components.
- Keep components focused on a single responsibility.
- Do not include business logic.
- Avoid direct API calls.
- Avoid direct data fetching.
- Keep components composable.

## React

- Use functional components.
- Prefer composition over inheritance.
- Keep components stateless whenever possible.
- Extract reusable child components when appropriate.
- Avoid unnecessary re-renders.

## TypeScript

- Use strict typing.
- Avoid `any`.
- Define clear Props interfaces.
- Prefer readonly props when appropriate.

## Styling

- Use Tailwind CSS.
- Use shadcn/ui components when available.
- Follow the project's design system.
- Keep styling consistent.
- Avoid inline styles.

## Accessibility

- Use semantic HTML.
- Support keyboard navigation.
- Include appropriate ARIA attributes when required.
- Ensure accessible labels for interactive elements.

## Performance

- Minimize unnecessary rendering.
- Avoid unnecessary state.
- Lazy load heavy components when appropriate.

## Naming

- Use PascalCase for component names.
- Use meaningful prop names.
- Keep files organized by responsibility.

## Output

Generate production-ready, reusable, enterprise-quality React components only.
---
name: form-generator
description: Generate reusable React forms using React Hook Form, Zod, and the project's design system following modern Next.js best practices.
category: frontend
tags:
  - nextjs
  - react
  - form
  - react-hook-form
  - zod
  - validation
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate reusable, maintainable, and production-ready forms for a Next.js application.

Focus on user input, validation, and form interactions while keeping business logic outside of the form.

# Inputs

The user should provide:

- Form name
- Business purpose
- Fields
- Validation rules
- Initial values (optional)
- Submit behavior
- Existing API or Mutation Hook (optional)

Example:

Form: UserForm

Fields:

- name
- email
- phone
- status

Validation:

- name required
- email format
- phone optional

Submit:

Create User

# Output

Generate:

- Form Component
- Form Fields
- Props Interface
- Zod Schema
- Default Values
- Form Types
- Validation
- Submit Handler
- Loading State
- Error State
- Success State
- Barrel Export

The generated form should compile successfully and integrate with the project's data layer.

# Workflow

1. Analyze form requirements.
2. Identify input fields.
3. Design validation rules.
4. Design the Props interface.
5. Build the form specification.
6. Delegate implementation to `typescript-senior-programmer`.
7. Validate usability, accessibility, and consistency.
8. Return the completed form.

# Rules

## General

- Generate reusable forms.
- Keep forms focused on a single responsibility.
- Do not include business logic.
- Do not call APIs directly.
- Receive submit callbacks through Props.
- Keep validation centralized.

## React Hook Form

- Use React Hook Form.
- Use Controller only when necessary.
- Register fields directly whenever possible.
- Minimize unnecessary re-renders.

## Validation

- Use Zod.
- Keep validation rules declarative.
- Generate reusable schemas.
- Display validation errors consistently.

## UI

- Use shadcn/ui form components when available.
- Follow the project's design system.
- Support responsive layouts.
- Display loading and disabled states appropriately.

## Accessibility

- Associate labels with inputs.
- Display validation messages accessibly.
- Support keyboard navigation.
- Provide appropriate ARIA attributes.

## State

- Keep form state local.
- Avoid duplicated state.
- Support default values.
- Support reset behavior.

## Submission

- Receive submit callbacks through Props.
- Disable submission while pending.
- Prevent duplicate submissions.
- Handle submission errors gracefully.

## TypeScript

- Enable strict typing.
- Avoid `any`.
- Infer types from Zod schemas whenever possible.

## Naming

Use meaningful names.

Examples:

UserForm

LoginForm

ProfileForm

SettingsForm

ProductForm

SearchForm

## Output

Generate production-ready, reusable, enterprise-quality forms only.
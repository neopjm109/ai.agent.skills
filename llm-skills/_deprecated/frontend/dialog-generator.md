---
name: dialog-generator
description: Generate reusable dialog components for a Next.js application including modals, drawers, alerts, confirmation dialogs, and interactive overlays.
category: frontend
tags:
  - nextjs
  - react
  - dialog
  - modal
  - drawer
  - shadcn
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate reusable, accessible, and production-ready dialog components.

Focus on user interactions while keeping business logic outside of the dialog.

# Inputs

The user should provide:

- Dialog name
- Dialog type
- Purpose
- UI requirements
- Actions
- Form requirements (optional)

Supported dialog types:

- Alert Dialog
- Confirmation Dialog
- Modal
- Drawer
- Sheet
- Full Screen Dialog
- Wizard Dialog

Example:

Dialog: DeleteUserDialog

Type:
Confirmation Dialog

Requirements:

- Show warning message
- Confirm button
- Cancel button
- Loading state

# Output

Generate:

- Dialog Component
- Props Interface
- Supporting Types (if required)
- Action Definitions
- Loading State
- Empty State (if required)
- Barrel Export

The generated dialog should be reusable and compile successfully.

# Workflow

1. Analyze dialog requirements.
2. Identify interaction patterns.
3. Design Props interface.
4. Separate UI from business logic.
5. Build the dialog specification.
6. Delegate implementation to `typescript-senior-programmer`.
7. Validate accessibility and consistency.
8. Return the completed dialog.

# Rules

## General

- Generate reusable dialog components.
- Keep dialogs focused on a single responsibility.
- Do not include business logic.
- Avoid direct API calls.
- Avoid direct data fetching.
- Accept required data through Props.

## React

- Use functional components.
- Prefer composition.
- Keep dialogs stateless whenever possible.
- Extract reusable child components when appropriate.

## UI

- Use shadcn/ui Dialog or Drawer components when available.
- Follow the project's design system.
- Support responsive layouts.
- Prevent background interaction while open when appropriate.

## Accessibility

- Support keyboard navigation.
- Close with Escape key when appropriate.
- Trap keyboard focus inside the dialog.
- Restore focus when closed.
- Provide accessible titles and descriptions.
- Follow ARIA dialog best practices.

## State

- Keep open/close state controlled by the parent whenever possible.
- Do not manage unrelated application state.
- Expose callback events through Props.

## Performance

- Lazy render heavy dialog content when appropriate.
- Avoid unnecessary re-renders.

## Naming

Use meaningful names.

Examples:

DeleteUserDialog

UserFormDialog

SettingsDrawer

NotificationDrawer

AlertDialog

ConfirmDialog

## Output

Generate production-ready, reusable, enterprise-quality dialog components only.
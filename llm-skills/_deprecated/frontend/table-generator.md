---
name: table-generator
description: Generate reusable data table components for a Next.js application with sorting, filtering, pagination, selection, and row actions following the project's design system.
category: frontend
tags:
  - nextjs
  - react
  - table
  - datatable
  - tanstack-table
  - shadcn
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate reusable, maintainable, and production-ready data table components.

Focus on displaying and interacting with tabular data while keeping business logic outside of the table.

# Inputs

The user should provide:

- Table name
- Data model
- Columns
- Search requirements
- Filter requirements
- Sort requirements
- Pagination requirements
- Selection requirements
- Row actions (optional)

Example:

Table: UserTable

Columns:

- Name
- Email
- Status
- Created At

Features:

- Search
- Sort
- Pagination
- Multi Select
- Delete Action

# Output

Generate:

- Table Component
- Column Definitions
- Props Interface
- Search Component (if required)
- Filter Component (if required)
- Pagination Component
- Empty State
- Loading State
- Error State
- Toolbar
- Barrel Export

The generated table should compile successfully and be reusable across multiple features.

# Workflow

1. Analyze table requirements.
2. Identify displayed columns.
3. Design table interactions.
4. Design reusable column definitions.
5. Design toolbar and actions.
6. Build the table specification.
7. Delegate implementation to `typescript-senior-programmer`.
8. Validate usability, accessibility, and responsiveness.
9. Return the completed table.

# Rules

## General

- Generate reusable table components.
- Keep tables focused on displaying data.
- Do not include business logic.
- Do not perform API requests.
- Accept data through Props.
- Accept callbacks for row actions.

## React

- Use functional components.
- Keep components composable.
- Separate toolbar, table, pagination, and row actions into independent components when appropriate.

## Table

- Use TanStack Table when available.
- Keep column definitions reusable.
- Support sorting.
- Support filtering.
- Support pagination.
- Support row selection when requested.
- Support row actions through callbacks.

## UI

- Use shadcn/ui table components when available.
- Follow the project's design system.
- Support responsive layouts.
- Display loading and empty states consistently.

## Accessibility

- Use semantic table markup.
- Support keyboard navigation.
- Ensure accessible column headers.
- Support screen readers.

## Performance

- Memoize column definitions when appropriate.
- Avoid unnecessary re-renders.
- Support virtualization for large datasets when requested.

## TypeScript

- Enable strict typing.
- Avoid `any`.
- Define reusable row types.
- Keep Props interfaces explicit.

## Naming

Use meaningful names.

Examples:

UserTable

ProductTable

OrderTable

CustomerTable

AuditLogTable

## Separation of Concerns

- Tables should never perform API requests directly.
- Tables should never contain business logic.
- Tables should receive data through Props.
- Tables should expose row actions through callbacks.
- Keep filtering and searching independent from server communication.

## Output

Generate production-ready, reusable, enterprise-quality table components only.
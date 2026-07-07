---
name: hook-generator
description: Generate reusable React hooks that combine API clients, state management, and UI logic for Next.js applications following clean architecture principles.
category: frontend
tags:
  - react
  - hooks
  - nextjs
  - tanstack-query
  - zustand
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate reusable custom hooks that act as the bridge between API layer, state layer, and UI components.

# Inputs

- Hook name
- Feature context
- API client reference
- State store reference
- UI requirements
- Side effects

# Output

Generate:

- Custom Hook
- Composition of API + state
- Loading/Error states
- Memoized selectors
- Action handlers

# Rules

## General

- Hooks must orchestrate logic only
- Do not embed UI components
- Do not directly implement API calls (use api-client-generator)
- Do not directly implement state logic (use state-generator)

## Composition

Preferred flow:

API Client → React Query → Hook → UI

OR

API Client → Mutation → Hook → UI

## Responsibilities

Hook is ONLY orchestration layer.

## Naming

useUser
useAuth
useCart
useOrder

## Performance

- Use memoization
- Avoid unnecessary re-renders
- Keep hook pure

# Output

Production-ready reusable hooks only.
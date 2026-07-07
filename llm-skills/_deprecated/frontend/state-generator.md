---
name: state-generator
description: Generate frontend state management logic using Zustand, React Query, or local state patterns depending on state type (server state, UI state, global state).
category: frontend
tags:
  - state
  - zustand
  - react-query
  - frontend
  - cache
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate optimal state management architecture.

Decide automatically whether state should be:

- Server state (React Query)
- Global client state (Zustand)
- Local component state

# Inputs

- Feature name
- State type
- Data model
- Mutations
- Cache strategy
- Persistence requirement

# Output

Generate:

- Zustand store OR React Query hooks OR local state pattern
- State interface
- Actions
- Selectors
- Persistence config (if needed)
- Devtools integration (optional)

# Rules

## State classification

### Server State
- Use React Query
- Do NOT duplicate caching logic

### Client State
- Use Zustand
- Keep minimal global state

### Local State
- Prefer useState/useReducer

## Separation

- Never mix server state and UI state
- Do not call APIs directly unless using query/mutation layer

## Persistence

- Use localStorage only when necessary
- Avoid over-persisting state

## Performance

- Avoid unnecessary re-renders
- Use selectors

## Naming

useUserStore
useAuthStore
useCartStore

# Output

Clean state architecture only.
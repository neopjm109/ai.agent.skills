---
name: architecture-generator
description: Generates a system architecture design from unified requirements, including layers, modules, boundaries, and technology decisions.
version: 1.0.0
author: OpenAI
category: generator
tags:
  - architecture
  - system-design
  - blueprint
  - backend
  - frontend
tools: []
model: inherit

priority: 95
entrypoint: false
parallel: true
timeout: 300
retry: 1

inputs:
  - unified_requirements
  - target_stack

outputs:
  - architecture_design

invokes: []
---

# architecture-generator

## Goal

Generate a high-level system architecture from unified requirements.

This includes system structure, layers, modules, boundaries, and technology decisions.

This Skill does not generate code or domain logic.

---

# Inputs

```yaml
unified_requirements:
  functional_requirements:
  non_functional_requirements:
  ui_requirements:
  business_rules:

target_stack:
  backend:
  frontend:
  database:
```

---

# Outputs

```yaml
architecture_design:
  system_style:
  layers:
  modules:
  service_boundaries:
  data_flow:
  communication_style:
  scalability_strategy:
  deployment_model:
  technology_stack:
```

---

# Workflow

## Step 1 — Analyze Requirements

Understand system constraints:

- Functional scope
- Non-functional requirements
- Performance expectations
- Security requirements
- Scalability needs

---

## Step 2 — Define Architecture Style

Determine architecture type:

- Monolith
- Modular Monolith
- Microservices
- Event-driven
- Hybrid

---

## Step 3 — Define System Layers

Design system layers:

```text
Presentation Layer
Application Layer
Domain Layer
Infrastructure Layer
```

---

## Step 4 — Define Modules

Break system into modules:

- User Module
- Auth Module
- Core Business Modules
- Integration Modules

---

## Step 5 — Define Communication Model

Specify communication style:

- REST
- Event-driven
- RPC
- Hybrid

---

## Step 6 — Define Data Flow

Describe:

- Request flow
- Event flow
- Sync/Async boundaries

---

## Step 7 — Define Scalability Strategy

Include:

- Horizontal scaling
- Caching strategy
- Load balancing
- Async processing

---

## Step 8 — Define Deployment Model

Specify:

- Monolith deployment
- Container-based deployment
- Cloud-native architecture
- CI/CD compatibility

---

## Step 9 — Select Technology Stack

Map architecture to stack:

- Backend framework
- Frontend framework
- Database
- Cache
- Messaging system

---

## Step 10 — Assemble Architecture Design

Combine all outputs into final architecture blueprint.

---

# Architecture Structure

```text
Architecture Design
│
├── System Style
├── Layers
├── Modules
├── Service Boundaries
├── Data Flow
├── Communication Model
├── Scalability Strategy
├── Deployment Model
└── Technology Stack
```

---

# Rules

## General

- Never generate implementation code.
- Focus only on system-level design.
- Keep architecture technology-aware but implementation-agnostic.

---

## Design Principles

- Prefer modularity over monolith unless explicitly required
- Minimize coupling between modules
- Maximize cohesion within modules

---

## Boundaries

- Clearly define module boundaries
- Avoid cross-layer business logic leakage
- Ensure clean separation between domain and infrastructure

---

## Scalability

Always consider:

- horizontal scaling capability
- stateless services where possible
- async processing for heavy workloads

---

## Traceability

Every architecture decision must reference:

- Requirement
- Business constraint
- Non-functional requirement

---

## Completion Criteria

Architecture generation is complete only when:

- system style is defined
- layers are defined
- modules are defined
- communication model is defined
- scalability strategy is defined
- deployment model is defined
- technology stack is selected
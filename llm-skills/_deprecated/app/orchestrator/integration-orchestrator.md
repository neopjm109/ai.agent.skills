---
name: integration-orchestrator
description: Orchestrates system integration by coordinating API contracts, client generation, event messaging, Redis, external services, and integration tests.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - integration
  - api
  - messaging
  - redis
  - event
tools: []
model: inherit

priority: 60
entrypoint: false
parallel: true
timeout: 600
retry: 1

inputs:
  - feature
  - application_blueprint
  - target_stack

outputs:
  - integration_artifact

invokes:
  - openapi-generator
  - api-client-generator
  - event-generator
  - messaging-generator
  - redis-generator
  - integration-test-generator
---

# integration-orchestrator

## Goal

Generate all integration artifacts required for a Feature by coordinating specialized integration generators.

Integration includes communication between frontend and backend, internal services, asynchronous messaging, Redis, external APIs, and system contracts.

This Skill never generates implementation code directly.

---

# Inputs

```yaml
feature:
  id:
  name:
  stories:
  tasks:

application_blueprint:

target_stack:
  backend: Spring Boot
  frontend: Next.js
```

---

# Outputs

```yaml
integration_artifact:
  openapi:
  api_clients:
  events:
  messaging:
  redis:
  external_services:
  integration_tests:
```

---

# Workflow

## Step 1 — Analyze Integration Requirements

Analyze the Feature and determine:

- REST APIs
- Event Flows
- Redis Usage
- Messaging
- External Services
- Authentication
- Service Dependencies

---

## Step 2 — Generate API Contracts

Invoke:

- openapi-generator

Generate:

```text
OpenAPI Specification

Endpoints

Schemas

Security Definitions
```

---

## Step 3 — Generate API Clients

Invoke:

- api-client-generator

Generate:

```text
Frontend API Client

SDK

Request Models

Response Models

Error Handling
```

---

## Step 4 — Generate Events

Invoke:

- event-generator

Generate:

```text
Domain Events

Application Events

Event Payloads

Event Consumers
```

---

## Step 5 — Generate Messaging

Invoke:

- messaging-generator

Generate:

```text
Topics

Queues

Publishers

Consumers

Retry Policies
```

---

## Step 6 — Generate Redis

Invoke:

- redis-generator

Generate:

```text
Cache Keys

TTL Policies

Distributed Locks

Pub/Sub Channels
```

---

## Step 7 — Generate External Service Integration

If external systems exist:

Generate:

```text
HTTP Clients

Authentication

Retry Policies

Circuit Breakers

Rate Limiting
```

---

## Step 8 — Generate Integration Tests

Invoke:

- integration-test-generator

Generate:

```text
API Tests

Contract Tests

Messaging Tests

Redis Tests

End-to-End Tests
```

---

## Step 9 — Assemble Integration Artifact

Merge all outputs into a single Integration Artifact.

---

# Integration Artifact Structure

```text
Integration Artifact
│
├── OpenAPI
│
├── API Clients
│
├── Events
│
├── Messaging
│
├── Redis
│
├── External Services
│
└── Integration Tests
```

---

# Invocation Flow

```text
Feature

│

├── openapi-generator

├── api-client-generator

├── event-generator

├── messaging-generator

├── redis-generator

└── integration-test-generator

↓

Integration Artifact
```

---

# Invocation Contract

| Condition | Invoke |
|-----------|--------|
| REST API exists | openapi-generator |
| Frontend consumes API | api-client-generator |
| Event-driven architecture | event-generator |
| Queue or broker required | messaging-generator |
| Redis required | redis-generator |
| Integration testing enabled | integration-test-generator |

---

# Rules

## General

- Never generate implementation code directly.
- Delegate implementation to specialized generators.
- Generate only integration artifacts.

---

## API Contracts

OpenAPI Specification is the source of truth.

All API Clients must be generated from the OpenAPI Specification.

---

## Messaging

Ensure consistency between:

- Publishers
- Consumers
- Topics
- Queues
- Event Payloads

---

## Redis

Redis artifacts must define:

- Key naming conventions
- TTL strategy
- Cache invalidation policy
- Pub/Sub channels
- Lock strategy

---

## External Services

Every external integration should define:

- Authentication
- Timeout
- Retry policy
- Circuit breaker
- Error handling

---

## Testing

Integration Tests should validate:

- API Contracts
- Event Flow
- Messaging
- Redis Behavior
- External Service Integration

---

## Traceability

Every generated integration artifact must reference:

- Requirement
- Blueprint Component
- Feature
- Story
- Task

---

## Completion Criteria

Integration orchestration is complete only when:

- OpenAPI generation has completed.
- API Client generation has completed.
- Event generation has completed (if required).
- Messaging generation has completed (if required).
- Redis generation has completed (if required).
- External service integration has been defined (if required).
- Integration Test generation has completed.
- All outputs have been merged into an Integration Artifact.
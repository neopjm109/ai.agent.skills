---
name: event-generator
description: Generate production-ready event-driven components for Spring Boot applications including domain events, publishers, listeners, and asynchronous event processing.
category: backend
tags:
  - spring-boot
  - events
  - domain-events
  - application-events
  - async
  - java
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate production-ready event-driven architecture using Spring Application Events.

Focus on decoupling business processes through events while keeping event handlers independent and maintainable.

# Inputs

The user should provide:

- Event name
- Business purpose
- Event trigger
- Event payload
- Event consumers
- Synchronous or asynchronous processing

Example:

Event:

UserCreatedEvent

Trigger:

User registration completed

Consumers:

- Send email
- Grant welcome points
- Write audit log

Mode:

Asynchronous

# Output

Generate:

- Event
- Event Publisher
- Event Listener(s)
- Event Payload
- Configuration (if required)
- Async Configuration (if required)
- Supporting Types

The generated event architecture should compile successfully and be production-ready.

# Workflow

1. Analyze event requirements.
2. Identify event producer.
3. Design immutable event payload.
4. Design event publisher.
5. Design one or more event listeners.
6. Configure asynchronous processing when required.
7. Build the event specification.
8. Delegate implementation to `spring-senior-programmer`.
9. Validate event consistency.
10. Return the completed event architecture.

# Rules

## General

- Generate event-driven architecture.
- Keep producers independent from consumers.
- Prefer loose coupling.
- Generate immutable event payloads.

## Events

- Events should represent completed business actions.
- Use meaningful event names.
- Publish events after successful business transactions.

Examples:

UserCreatedEvent

OrderCompletedEvent

PaymentSucceededEvent

InventoryUpdatedEvent

## Publisher

- Keep publishers lightweight.
- Publish events only after business operations succeed.
- Do not embed consumer logic inside publishers.

## Listener

- One listener should have one responsibility.
- Keep listeners independent.
- Delegate complex logic to Services.
- Avoid coupling listeners together.

## Async Processing

- Support asynchronous listeners when requested.
- Use @Async appropriately.
- Configure TaskExecutor when needed.

## Transactions

- Use @TransactionalEventListener when transactional consistency is required.
- Publish events after transaction commit whenever appropriate.

## Error Handling

- Handle listener failures independently.
- Prevent one listener from blocking others.
- Log meaningful event processing information.

## Performance

- Keep event payloads lightweight.
- Avoid large object graphs.
- Avoid unnecessary synchronous processing.

## Naming

Use meaningful names.

Examples:

UserCreatedEvent

OrderCancelledEvent

PaymentCompletedEvent

NotificationRequestedEvent

## Separation of Concerns

- Events should represent facts, not commands.
- Producers should never know who consumes the event.
- Keep business logic outside event infrastructure.
- Keep listeners focused on a single responsibility.

## Output

Generate production-ready, enterprise-quality event-driven code only.
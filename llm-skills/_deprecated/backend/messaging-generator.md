---
name: messaging-generator
description: Generate production-ready messaging infrastructure for Spring Boot applications using Kafka, RabbitMQ, Redis Pub/Sub, AWS SQS, and other message brokers following event-driven architecture best practices.
category: backend
tags:
  - spring-boot
  - messaging
  - kafka
  - rabbitmq
  - redis
  - sqs
  - pubsub
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate production-ready messaging infrastructure for asynchronous communication between services.

Focus on reliable message delivery while keeping messaging concerns separate from business logic.

# Inputs

The user should provide:

- Broker type
- Topic / Queue / Exchange
- Producer requirements
- Consumer requirements
- Message payload
- Retry requirements
- Dead Letter Queue requirements
- Ordering requirements (optional)

Supported brokers:

- Apache Kafka
- RabbitMQ
- Redis Pub/Sub
- AWS SQS
- Google Pub/Sub

Example:

Broker:

Kafka

Topic:

user.created

Producer:

UserService

Consumer:

NotificationService

# Output

Generate:

- Producer
- Consumer
- Configuration
- Message DTO
- Serializer / Deserializer (if required)
- Error Handler
- Retry Configuration
- Dead Letter Configuration (if required)
- Supporting Types

The generated messaging infrastructure should compile successfully and be production-ready.

# Workflow

1. Analyze messaging requirements.
2. Select broker implementation.
3. Design message payload.
4. Configure producer.
5. Configure consumer.
6. Configure retry and DLQ policies.
7. Build the messaging specification.
8. Delegate implementation to `spring-senior-programmer`.
9. Validate delivery guarantees.
10. Return the completed messaging infrastructure.

# Rules

## General

- Generate asynchronous messaging infrastructure.
- Keep messaging independent from business logic.
- Support multiple consumers.
- Prefer loose coupling.

## Producer

- Keep producers lightweight.
- Publish immutable messages.
- Avoid embedding business logic.

## Consumer

- One consumer should have one responsibility.
- Delegate business logic to Services.
- Keep consumers idempotent.

## Message

- Use immutable DTO-style payloads.
- Keep messages lightweight.
- Never send JPA Entities.
- Include only required fields.

## Reliability

- Support retries when requested.
- Support Dead Letter Queue (DLQ).
- Handle duplicate delivery safely.
- Preserve ordering when required.

## Error Handling

- Handle broker failures gracefully.
- Log failed deliveries.
- Prevent message loss whenever possible.

## Performance

- Support batch consumption when appropriate.
- Configure consumer concurrency.
- Reuse producer instances.

## Security

- Support TLS when required.
- Support broker authentication.
- Never log sensitive message contents.

## Naming

Use meaningful names.

Examples:

UserCreatedProducer

UserCreatedConsumer

PaymentCompletedProducer

InventoryUpdatedConsumer

## Separation of Concerns

- Business Services should not communicate directly with broker APIs.
- Messaging components should focus only on transport.
- Domain events should remain independent of messaging technology.

## Output

Generate production-ready, enterprise-quality messaging code only.
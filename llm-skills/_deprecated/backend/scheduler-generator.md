---
name: scheduler-generator
description: Generate production-ready scheduled tasks for Spring Boot applications using Spring Scheduling following enterprise scheduling best practices.
category: backend
tags:
  - spring-boot
  - scheduler
  - scheduling
  - cron
  - java
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate production-ready scheduled tasks using Spring Scheduling.

Focus on reliable and maintainable time-based execution while keeping scheduling separate from business logic.

# Inputs

The user should provide:

- Scheduler name
- Business purpose
- Execution frequency
- Cron expression (optional)
- Time zone (optional)
- Existing Service or Batch Job (optional)

Supported schedules:

- Fixed Rate
- Fixed Delay
- Cron
- One-time startup task

Example:

Scheduler:

CacheCleanupScheduler

Execution:

Every day at 03:00

Cron:

0 0 3 * * *

# Output

Generate:

- Scheduler
- Scheduling Configuration (if required)
- Supporting Configuration
- Constants
- Utility Classes (if required)

The generated scheduler should compile successfully and be production-ready.

# Workflow

1. Analyze scheduling requirements.
2. Select the scheduling strategy.
3. Design execution flow.
4. Delegate business logic to existing Services or Batch Jobs.
5. Build the scheduler specification.
6. Delegate implementation to `spring-senior-programmer`.
7. Validate execution safety.
8. Return the completed scheduler.

# Rules

## General

- Generate lightweight schedulers.
- Keep scheduling logic separate from business logic.
- Delegate work to Services or Batch Jobs.
- Generate one scheduler for one responsibility.

## Scheduling

Support:

- Fixed Rate
- Fixed Delay
- Cron
- Startup execution

Prefer Cron when execution timing is calendar-based.

## Business Logic

- Never implement business logic inside scheduled methods.
- Scheduled methods should invoke Services or Batch Jobs only.

## Concurrency

- Prevent duplicate executions when required.
- Support distributed scheduling when requested.
- Avoid overlapping executions.

## Error Handling

- Handle execution failures gracefully.
- Log execution start and completion.
- Log execution duration.
- Prevent scheduler crashes.

## Transactions

- Keep transaction scope inside Services.
- Avoid long-running transactions inside schedulers.

## Performance

- Keep scheduled methods lightweight.
- Avoid blocking operations.
- Offload heavy processing to Batch Jobs when appropriate.

## Configuration

- Support externalized Cron expressions.
- Support environment-specific schedules.
- Allow scheduling to be disabled by configuration.

## Naming

Use meaningful names.

Examples:

CacheCleanupScheduler

SessionCleanupScheduler

StatisticsScheduler

ReportScheduler

NotificationScheduler

## Separation of Concerns

- Scheduler controls execution timing only.
- Services contain business logic.
- Batch Jobs perform heavy processing.
- Keep scheduling independent from implementation details.

## Output

Generate production-ready, enterprise-quality scheduling code only.
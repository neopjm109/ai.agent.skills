---
name: batch-generator
description: Generate production-ready Spring Batch jobs including Job, Step, Reader, Processor, Writer, Listeners, and scheduling configuration following Spring Batch best practices.
category: backend
tags:
  - spring-boot
  - spring-batch
  - batch
  - scheduler
  - java
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate production-ready Spring Batch jobs following modern Spring Batch architecture and enterprise best practices.

Focus on batch workflow design while keeping business logic inside dedicated processors or services.

# Inputs

The user should provide:

- Batch name
- Business purpose
- Processing type
- Input source
- Output destination
- Scheduling requirements (optional)
- Chunk size (optional)

Supported processing types:

- Chunk
- Tasklet

Example:

Batch:

InactiveUserBatch

Purpose:

Deactivate users inactive for 365 days.

Input:

MariaDB

Output:

MariaDB

Schedule:

Every day at 02:00

# Output

Generate:

- Job Configuration
- Step Configuration
- Reader
- Processor
- Writer
- Job Listener (if required)
- Step Listener (if required)
- Scheduler (optional)
- Supporting Configuration
- Barrel Export (if applicable)

The generated batch should compile successfully and be production-ready.

# Workflow

1. Analyze batch requirements.
2. Select processing strategy (Chunk or Tasklet).
3. Design Job and Step structure.
4. Design Reader.
5. Design Processor.
6. Design Writer.
7. Design scheduling configuration if required.
8. Build the batch specification.
9. Delegate implementation to `spring-senior-programmer`.
10. Validate consistency and restartability.
11. Return the completed batch.

# Rules

## General

- Generate production-ready Spring Batch code.
- Follow Spring Batch architecture.
- Keep business logic outside Job configuration.
- Separate Reader, Processor, and Writer responsibilities.

## Job

- One Job should represent one business process.
- Keep Jobs cohesive.
- Support restartability when appropriate.

## Step

- Keep Steps focused.
- Separate processing stages.
- Prefer multiple Steps over large monolithic Steps.

## Reader

- Read data only.
- Do not perform business logic.
- Support paging or streaming when appropriate.

## Processor

- Keep business logic inside the Processor or delegated Service.
- Avoid database writes inside the Processor.
- Keep transformations deterministic.

## Writer

- Persist processed results.
- Support batch writes.
- Optimize database access.

## Scheduling

- Generate Scheduler only when requested.
- Keep scheduling separate from Job configuration.

## Transactions

- Configure transaction boundaries appropriately.
- Support chunk transactions.

## Performance

- Support chunk processing for large datasets.
- Avoid loading all data into memory.
- Use paging readers where appropriate.

## Error Handling

- Support Skip Policy when requested.
- Support Retry Policy when requested.
- Log meaningful batch execution events.

## Monitoring

- Support JobExecutionListener.
- Support StepExecutionListener.
- Generate useful execution logs.

## Naming

Use meaningful names.

Examples:

InactiveUserJob

SettlementBatch

StatisticsBatch

DailyReportBatch

OrderCleanupBatch

## Output

Generate production-ready, enterprise-quality Spring Batch code only.
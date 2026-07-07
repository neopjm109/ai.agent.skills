---
name: execution-orchestrator
description: Builds and executes the dependency graph for all generation tasks by scheduling execution order, maximizing parallelism, monitoring progress, and handling failures.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - execution
  - scheduler
  - dependency
  - dag
tools: []
model: inherit

priority: 50
entrypoint: false
parallel: true
timeout: 600
retry: 1

inputs:
  - execution_plan
  - application_blueprint

outputs:
  - execution_result

invokes: []
---

# execution-orchestrator

## Goal

Execute the software generation pipeline according to the execution plan.

This Skill is responsible for scheduling, dependency resolution, progress tracking, failure handling, and parallel execution.

It never generates implementation code.

---

# Inputs

```yaml
execution_plan:
  epics:
  features:
  stories:
  tasks:
  dependency_graph:
  execution_order:

application_blueprint:
```

---

# Outputs

```yaml
execution_result:
  completed_tasks:
  skipped_tasks:
  failed_tasks:
  execution_log:
  execution_summary:
```

---

# Workflow

## Step 1 — Load Execution Plan

Load:

- Features
- Stories
- Tasks
- Dependency Graph
- Execution Order

Validate the execution plan before execution begins.

---

## Step 2 — Build Execution DAG

Construct the execution graph.

Identify:

- Root Tasks
- Dependencies
- Blocking Tasks
- Parallel Groups

---

## Step 3 — Schedule Tasks

Determine execution order.

Schedule:

- Sequential Tasks
- Parallel Tasks
- Independent Branches

---

## Step 4 — Execute Tasks

Execute every task only after all dependencies have completed successfully.

Track:

```text
Pending

Running

Completed

Skipped

Failed
```

---

## Step 5 — Monitor Progress

Continuously monitor:

- Task Status
- Progress
- Execution Time
- Dependency Resolution

---

## Step 6 — Handle Failures

If a task fails:

- stop dependent tasks
- continue independent branches
- record failure
- preserve execution state

---

## Step 7 — Generate Execution Summary

Produce:

```text
Completed Tasks

Skipped Tasks

Failed Tasks

Execution Statistics

Execution Timeline
```

---

# Execution Graph

```text
Task A
│
├────► Task B
│
├────► Task C
│
└────► Task D

Task B
│
└────► Task E

Task C
│
└────► Task E

Task D
│
└────► Task F
```

---

# Task States

```text
Pending

↓

Ready

↓

Running

↓

Completed
```

or

```text
Running

↓

Failed

↓

Skipped (Dependent Tasks)
```

---

# Scheduling Rules

## Sequential

Execute only after dependencies finish.

Example:

```text
Entity

↓

Repository

↓

Service

↓

Controller
```

---

## Parallel

Independent tasks may execute simultaneously.

Example:

```text
Component Generator

Form Generator

Table Generator

Dialog Generator
```

---

## Blocking

Tasks with unresolved dependencies remain in the Pending state.

---

# Rules

## General

- Never generate implementation code.
- Never modify implementation artifacts.
- Execute only according to the Execution Plan.

---

## Dependency Resolution

- Respect every dependency.
- Never execute downstream tasks early.
- Never ignore blocking dependencies.
- Reject circular dependency graphs.

---

## Parallel Execution

Execute independent branches in parallel whenever possible.

Maximize throughput without violating dependencies.

---

## Failure Handling

When a task fails:

- mark the task as Failed
- stop dependent tasks
- continue unrelated branches
- collect all failures

---

## Retry Policy

If retry is enabled:

- retry only transient failures
- never retry validation failures
- preserve retry history

---

## Progress Tracking

Maintain execution status for every task.

Track:

- start time
- completion time
- execution duration
- retry count

---

## Traceability

Every execution record must reference:

- Requirement
- Blueprint Component
- Epic
- Feature
- Story
- Task

---

## Completion Criteria

Execution is complete only when:

- every executable task has reached a terminal state
- dependency graph has been fully resolved
- execution summary has been generated
- execution log has been recorded
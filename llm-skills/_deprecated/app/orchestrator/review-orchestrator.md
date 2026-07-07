---
name: review-orchestrator
description: Produces the final project review by summarizing execution results, validation outcomes, generated artifacts, and providing quality assessment and improvement recommendations.
version: 1.0.0
author: OpenAI
category: orchestrator
tags:
  - orchestrator
  - review
  - summary
  - reporting
  - quality
tools: []
model: inherit

priority: 30
entrypoint: false
parallel: false
timeout: 600
retry: 1

inputs:
  - application_blueprint
  - execution_result
  - validation_report
  - generated_artifacts

outputs:
  - review_report

invokes: []
---

# review-orchestrator

## Goal

Generate the final consolidated review of the entire software generation process.

This includes:

- Execution summary
- Validation summary
- Architecture quality review
- Backend/Frontend/Integration consistency review
- Risk analysis
- Improvement recommendations
- Remaining tasks

This Skill is strictly read-only and never modifies artifacts.

---

# Inputs

```yaml
application_blueprint:

execution_result:

validation_report:

generated_artifacts:
```

---

# Outputs

```yaml
review_report:
  project_summary:
  architecture_review:
  backend_review:
  frontend_review:
  integration_review:
  quality_metrics:
  risks:
  warnings:
  errors:
  recommendations:
  remaining_tasks:
  final_status:
```

---

# Workflow

## Step 1 — Load All Results

Collect and analyze:

- Application Blueprint
- Execution Results
- Validation Report
- Generated Artifacts

Ensure completeness of all inputs.

---

## Step 2 — Summarize Execution

Summarize:

- Completed Tasks
- Failed Tasks
- Skipped Tasks
- Execution Efficiency
- Dependency Bottlenecks

---

## Step 3 — Review Architecture

Evaluate:

```text
Modularity
Scalability
Maintainability
Layer Separation
Dependency Structure
```

---

## Step 4 — Review Backend

Evaluate:

```text
Domain Modeling
Service Design
API Consistency
Database Design
Security Implementation
Test Coverage
```

---

## Step 5 — Review Frontend

Evaluate:

```text
UI Consistency
Component Reusability
State Management
API Integration
User Flow Completeness
Performance Considerations
```

---

## Step 6 — Review Integration

Evaluate:

```text
API Contracts
Event Flows
Messaging Systems
Redis Strategy
External Integrations
Data Consistency
```

---

## Step 7 — Analyze Validation Results

Incorporate:

- Errors
- Warnings
- Passed Checks
- Quality Metrics

Identify unresolved issues.

---

## Step 8 — Risk Analysis

Detect:

- Architectural Risks
- Performance Risks
- Security Risks
- Scalability Risks
- Technical Debt

---

## Step 9 — Generate Recommendations

Provide actionable improvements:

- Code-level improvements
- Architecture improvements
- Process improvements
- Testing improvements

---

## Step 10 — Generate Final Report

Produce structured review report.

---

# Review Structure

```text
Project Review
│
├── Summary
├── Architecture Review
├── Backend Review
├── Frontend Review
├── Integration Review
├── Validation Summary
├── Risks
├── Warnings
├── Errors
├── Recommendations
├── Remaining Tasks
└── Final Status
```

---

# Review Dimensions

```text
Correctness

Completeness

Consistency

Scalability

Maintainability

Security

Testability
```

---

# Rules

## General

- Never modify generated artifacts.
- Never re-execute generation steps.
- Only analyze and summarize.

---

## Consistency Check

Ensure alignment between:

- Blueprint ↔ Implementation
- Backend ↔ Frontend
- API ↔ Integration
- Execution ↔ Validation

---

## Quality Assessment

Evaluate:

- Structural quality
- Dependency clarity
- Code organization (logical level)
- Coverage completeness

---

## Risk Handling

All risks must be:

- categorized
- prioritized
- explained
- actionable

---

## Traceability

Every finding must reference:

- Requirement
- Blueprint Component
- Feature
- Story
- Task
- Validation Result

---

## Completion Criteria

Review is complete only when:

- Execution is fully summarized
- Validation results are analyzed
- All subsystems are reviewed
- Risks are identified
- Recommendations are provided
- Final status is determined
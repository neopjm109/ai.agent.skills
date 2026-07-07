---
name: docs-analyze-pptx
description: Parses PPTX files and extracts structured UI/flow/requirements data for downstream orchestration.
version: 1.0.0
author: OpenAI
category: document-analyzer
tags:
  - pptx
  - parser
  - ui
  - requirements
tools:
  - terminal
model: inherit

priority: 100
entrypoint: true
parallel: true
timeout: 300
retry: 1

inputs:
  - file_path

outputs:
  - structured_document

invokes:
  - pptx-parser
---

# docs-analyze-pptx

## Goal

Extract structured application information from PPTX files.

Convert slides into:

- UI screens
- user flows
- system actions
- business requirements
- screen relationships

---

# Inputs

```yaml
file_path: string
```

---

# Outputs

```yaml
structured_document:
  type: pptx
  screens:
  flows:
  requirements:
  entities:
  actions:
```

---

# Workflow

## Step 1 — Load PPTX

Read PPTX file from provided path.

---

## Step 2 — Parse Slides

Invoke:

- pptx-parser

Command:

```bash
python scripts/pptx_parser.py <file_path>
```

---

## Step 3 — Extract Structure

Convert raw slide data into:

- screen definitions
- UI components
- flow transitions
- annotations

---

## Step 4 — Normalize Requirements

Extract:

- functional requirements
- UI requirements
- business rules

---

## Step 5 — Build Structured Document

Merge all extracted data into a unified schema.

---

# Rules

- Do not hallucinate missing slides.
- Do not infer business logic beyond slide content.
- Preserve slide-level traceability.
---
name: docs-analyze-docx
description: Parses DOCX files and extracts structured requirements, business rules, and system specifications.
version: 1.0.0
author: OpenAI
category: document-analyzer
tags:
  - docx
  - requirements
  - parser
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
  - docx-parser
---

# docs-analyze-docx

## Goal

Extract structured requirements and specifications from DOCX documents.

---

# Inputs

```yaml
file_path: string
```

---

# Outputs

```yaml
structured_document:
  type: docx
  functional_requirements:
  non_functional_requirements:
  business_rules:
  constraints:
  entities:
```

---

# Workflow

## Step 1 — Load DOCX

Read document from file system.

---

## Step 2 — Parse Document

Invoke:

- docx-parser

---

## Step 3 — Extract Requirements

Classify into:

- functional
- non-functional
- business rules

---

## Step 4 — Normalize Structure

Standardize all extracted content into unified schema.

---

# Rules

- Only extract explicit content.
- Do not infer missing requirements.
- Preserve original wording where possible.
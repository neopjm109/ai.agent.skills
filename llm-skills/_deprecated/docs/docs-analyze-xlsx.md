---
name: docs-analyze-xlsx
description: Parses XLSX files and extracts structured API specs, data models, tables, and configuration metadata.
version: 1.0.0
author: OpenAI
category: document-analyzer
tags:
  - xlsx
  - data-model
  - api-spec
  - schema
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
  - xlsx-parser
---

# docs-analyze-xlsx

## Goal

Extract structured technical data from XLSX files including:

- API specifications
- data models
- table definitions
- configuration sheets

---

# Inputs

```yaml
file_path: string
```

---

# Outputs

```yaml
structured_document:
  type: xlsx
  api_specs:
  tables:
  schemas:
  enums:
  configurations:
```

---

# Workflow

## Step 1 — Load XLSX

Read spreadsheet file.

---

## Step 2 — Parse Sheets

Invoke:

- xlsx-parser

---

## Step 3 — Extract Data Models

Identify:

- tables
- columns
- relationships
- constraints

---

## Step 4 — Extract API Specs

If present:

- endpoints
- request/response schema
- auth definitions

---

## Step 5 — Normalize Structure

Convert everything into unified schema.

---

# Rules

- Do not guess missing columns.
- Preserve sheet structure mapping.
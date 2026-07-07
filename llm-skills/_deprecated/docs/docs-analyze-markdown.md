---
name: docs-analyze-markdown
description: Parses Markdown documents and extracts structured requirements, architecture notes, and system design information.
version: 1.0.0
author: OpenAI
category: document-analyzer
tags:
  - markdown
  - requirements
  - architecture
  - design
tools: []
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

invokes: []
---

# docs-analyze-markdown

## Goal

Extract structured system information from Markdown documents.

---

# Inputs

```yaml
file_path: string
```

---

# Outputs

```yaml
structured_document:
  type: markdown
  architecture_notes:
  requirements:
  decisions:
  constraints:
  entities:
```

---

# Workflow

## Step 1 — Load Markdown

Read file content.

---

## Step 2 — Parse Sections

Identify:

- headings
- bullet structures
- code blocks
- tables

---

## Step 3 — Extract Meaning

Classify into:

- requirements
- architecture decisions
- constraints
- system notes

---

## Step 4 — Normalize Structure

Convert into unified structured format.

---

# Rules

- Do not infer missing system design decisions.
- Preserve original section hierarchy.
- Keep traceability to headings.
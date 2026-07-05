---
name: docs-analyze-docx
description: Parses a DOCX file into a structured document of functional/non-functional requirements, business rules, constraints, and entities for downstream orchestration.
version: 1.0.0
category: docs-analyze
tags:
  - docx
  - requirements
  - parser
  - document-analysis
model: inherit
invokes: []
inputs:
  - file_path
outputs:
  - structured_document
---

# Goal

Extract explicit requirements and specifications from a Microsoft Word (`.docx`)
document and emit a normalized `structured_document`. This skill performs
**analysis only** — it does not generate application code. It is invoked by
`app-orchestrator`, one instance per `.docx` input file.

# Inputs

```yaml
file_path: /abs/path/to/requirements.docx
```

# Output

```yaml
structured_document:
  type: docx
  source: /abs/path/to/requirements.docx
  functional_requirements: []      # [{ id, text, section }]
  non_functional_requirements: []  # [{ id, text, category }]  e.g. performance, security
  business_rules: []               # [{ id, text }]
  constraints: []                  # [{ id, text }]
  entities: []                     # [{ name, attributes[], source_section }]
  tables: []                       # [{ heading, rows[][] }] raw table content preserved
```

# Workflow

## Step 1 — Verify the file

Using the `terminal` tool, confirm the file exists and is a real DOCX
(a ZIP container). Fail fast with a clear message if not:

```bash
test -f "<file_path>" && file "<file_path>" | grep -qi "microsoft word\|zip" \
  && echo "OK" || echo "NOT_A_DOCX"
```

## Step 2 — Extract raw text and tables

A `.docx` is a ZIP archive whose body lives in `word/document.xml`. Extract the
document XML with the `terminal` tool, then read its text runs (`<w:t>`),
paragraph headings (`<w:pStyle>` values such as `Heading1`), and tables
(`<w:tbl>` / `<w:tr>` / `<w:tc>`):

```bash
mkdir -p /tmp/docx_extract && \
unzip -o "<file_path>" word/document.xml -d /tmp/docx_extract && \
cat /tmp/docx_extract/word/document.xml
```

Preferred, if Python + `python-docx` is available, run a one-off extractor via
the `terminal` tool for clean paragraph/heading/table separation:

```bash
python - "<file_path>" <<'PY'
import sys
from docx import Document
doc = Document(sys.argv[1])
for p in doc.paragraphs:
    if p.text.strip():
        print(f"[{p.style.name}] {p.text}")
for i, t in enumerate(doc.tables):
    print(f"--- TABLE {i} ---")
    for row in t.rows:
        print(" | ".join(c.text for c in row.cells))
PY
```

If `python-docx` is not installed, fall back to the `unzip` + XML approach above.

## Step 3 — Classify content

Walk the extracted paragraphs/tables and classify each item into
`functional_requirements`, `non_functional_requirements`, `business_rules`, or
`constraints`, using heading context and cue words ("shall", "must", "the
system") to decide. Preserve the originating section for traceability.

## Step 4 — Extract entities

From nouns in requirement text and from table rows describing data, collect
candidate `entities` with their attributes. Only include entities explicitly
named in the document.

## Step 5 — Normalize

Assemble every extracted item into the unified `structured_document` schema,
assigning stable ids (e.g. `FR-001`, `NFR-001`, `BR-001`).

# Rules

- Extract only content explicitly present; never infer missing requirements.
- Preserve original wording; do not paraphrase requirement text.
- Every requirement must carry a stable id and its source section for traceability.
- Preserve raw tables under `tables` even when their content is also classified elsewhere.
- Use `terminal` for all file access; do not assume any single parser library is present — fall back to the `unzip`/XML path when needed.
- This skill parses `.docx` only. Route `.pptx` to `docs-analyze-pptx`, `.xlsx` to `docs-analyze-xlsx`, and `.md` to `docs-analyze-markdown`.

# Examples

Input:

```yaml
file_path: /project/docs/requirements.docx
```

Output:

```yaml
structured_document:
  type: docx
  source: /project/docs/requirements.docx
  functional_requirements:
    - { id: FR-001, text: "The system shall allow users to register with an email and password.", section: "2. Accounts" }
    - { id: FR-002, text: "Users shall be able to reset their password via email.", section: "2. Accounts" }
  non_functional_requirements:
    - { id: NFR-001, text: "API responses must return within 300ms at p95.", category: performance }
    - { id: NFR-002, text: "All passwords must be stored using bcrypt.", category: security }
  business_rules:
    - { id: BR-001, text: "An email address may be linked to at most one account." }
  constraints:
    - { id: C-001, text: "The backend must run on Spring Boot." }
  entities:
    - { name: User, attributes: [id, email, passwordHash, createdAt], source_section: "2. Accounts" }
  tables:
    - heading: "Account fields"
      rows:
        - [Field, Type, Required]
        - [email, string, "yes"]
        - [password, string, "yes"]
```

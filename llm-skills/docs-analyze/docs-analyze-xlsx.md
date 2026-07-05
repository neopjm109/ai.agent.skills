---
name: docs-analyze-xlsx
description: Parses an XLSX file into a structured document of API specs, data models, table/schema definitions, enums, and configuration for downstream orchestration.
version: 1.0.0
category: docs-analyze
tags:
  - xlsx
  - data-model
  - api-spec
  - schema
  - document-analysis
model: inherit
invokes: []
inputs:
  - file_path
outputs:
  - structured_document
---

# Goal

Extract explicit technical data from an Excel (`.xlsx`) workbook — API
specifications, data models, table/schema definitions, enums, and configuration
sheets — and emit a normalized `structured_document`. This skill performs
**analysis only** — it does not generate code. It is invoked by
`app-orchestrator`, one instance per `.xlsx` input file.

# Inputs

```yaml
file_path: /abs/path/to/api-spec.xlsx
```

# Output

```yaml
structured_document:
  type: xlsx
  source: /abs/path/to/api-spec.xlsx
  api_specs: []        # [{ id, method, path, request[], response[], auth }]
  tables: []           # [{ name, columns[], primary_key, relationships[] }]
  schemas: []          # [{ name, fields[] }]  reusable request/response shapes
  enums: []            # [{ name, values[] }]
  configurations: []   # [{ sheet, key, value }]
```

# Workflow

## Step 1 — Verify the file

Using the `terminal` tool, confirm the file exists and is a valid XLSX
(ZIP container):

```bash
test -f "<file_path>" && file "<file_path>" | grep -qi "excel\|spreadsheet\|zip" \
  && echo "OK" || echo "NOT_AN_XLSX"
```

## Step 2 — Enumerate sheets and dump cells

Read every sheet with a one-off extractor via the `terminal` tool. Preferred
path uses `openpyxl`, printing each sheet as tab-separated rows:

```bash
python - "<file_path>" <<'PY'
import sys
from openpyxl import load_workbook
wb = load_workbook(sys.argv[1], data_only=True, read_only=True)
for ws in wb.worksheets:
    print(f"=== SHEET: {ws.title} ===")
    for row in ws.iter_rows(values_only=True):
        print("\t".join("" if c is None else str(c) for c in row))
PY
```

If `openpyxl` is unavailable, fall back to converting to CSV per sheet with a
tool that is present (e.g. `libreoffice --headless --convert-to csv`, or
`ssconvert` from Gnumeric), then read the CSV output:

```bash
libreoffice --headless --convert-to csv --outdir /tmp/xlsx_csv "<file_path>"
cat /tmp/xlsx_csv/*.csv
```

## Step 3 — Classify each sheet

Use the sheet name and its header row to decide the sheet kind:

- endpoint/method/path columns → `api_specs`
- table/column/type/PK/FK columns → `tables`
- name/value pairs → `enums`
- key/value settings → `configurations`
- reusable field lists → `schemas`

## Step 4 — Extract structure

For data-model sheets, capture columns, types, primary keys, and
relationships. For API sheets, capture method, path, request/response fields,
and auth. Only record columns that are actually present.

## Step 5 — Normalize

Merge extracted content into the unified `structured_document` schema, keeping
the source sheet name for each item.

# Rules

- Do not guess missing columns, types, or endpoints; record only what the cells contain.
- Preserve the sheet-to-item mapping (each item records its source sheet).
- Use `terminal` for all reads; do not assume a single library is present — fall back to the CSV-conversion path when needed.
- This skill parses `.xlsx` only. Route `.docx` to `docs-analyze-docx`, `.pptx` to `docs-analyze-pptx`, and `.md` to `docs-analyze-markdown`.

# Examples

Input:

```yaml
file_path: /project/docs/api-spec.xlsx
```

Output:

```yaml
structured_document:
  type: xlsx
  source: /project/docs/api-spec.xlsx
  api_specs:
    - id: API-001
      method: POST
      path: /api/orders
      request: [{ name: items, type: array }, { name: customerId, type: long }]
      response: [{ name: orderId, type: long }, { name: status, type: string }]
      auth: bearer
  tables:
    - name: orders
      columns: [{ name: id, type: bigint }, { name: status, type: varchar }, { name: total, type: decimal }]
      primary_key: id
      relationships: [{ column: customer_id, references: customers.id }]
  enums:
    - { name: OrderStatus, values: [PENDING, PAID, SHIPPED, CANCELLED] }
  configurations:
    - { sheet: Config, key: page_size_default, value: "20" }
```

---
name: docs-analyze-csv
description: Parses a CSV (or TSV) file into a structured document — a single table with inferred column types, parsed rows, and detected enums/keys — for downstream orchestration (data analysis, seed data, or schema extraction).
version: 1.0.0
category: docs-analyze
tags:
  - csv
  - tsv
  - dataset
  - data-model
  - document-analysis
model: inherit
invokes: []
inputs:
  - file_path
outputs:
  - structured_document
---

# Goal

Extract the contents of a delimited text file (`.csv` / `.tsv`) into a normalized
`structured_document`: one table with inferred column types, the parsed rows, and any
obvious enums or key columns. This skill performs **analysis only** — it does not generate
code. It is the tabular-dataset input adapter reused by data-analysis, seed-data, and any
orchestrator that accepts CSV.

# Inputs

```yaml
file_path: /abs/path/to/dataset.csv
```

# Output

```yaml
structured_document:
  type: csv
  source: /abs/path/to/dataset.csv
  table:
    name: <derived from filename>
    delimiter: ","            # or "\t" for TSV
    columns: []               # [{ name, type, nullable, sample_values[] }]
    primary_key_candidates: []# columns that look unique/id-like
  rows: []                    # [{ <col>: <value>, ... }]  parsed records
  enums: []                   # [{ column, values[] }]  low-cardinality categoricals
  row_count: 0
```

# Workflow

## Step 1 — Verify the file

Using the `terminal` tool, confirm the file exists and is delimited text (not binary):

```bash
test -f "<file_path>" && file "<file_path>" | grep -qi "text\|csv\|ascii" \
  && echo "OK" || echo "NOT_A_CSV"
```

## Step 2 — Detect delimiter and header

Sniff the delimiter (`,` vs `\t` vs `;`) and confirm a header row via a one-off extractor:

```bash
python - "<file_path>" <<'PY'
import sys, csv
with open(sys.argv[1], newline="", encoding="utf-8-sig") as f:
    sample = f.read(4096); f.seek(0)
    dialect = csv.Sniffer().sniff(sample)
    has_header = csv.Sniffer().has_header(sample)
    r = csv.reader(f, dialect)
    rows = list(r)
print("DELIM", repr(dialect.delimiter), "HEADER", has_header, "ROWS", len(rows))
PY
```

If `python`/`csv` is unavailable, fall back to a delimiter guess from the first line with
tools that are present (`head`, `awk`) and read rows with `awk -F`.

## Step 3 — Infer column types

For each column, infer a type from its values: `integer`, `decimal`, `boolean`,
`datetime`, or `string`. Mark `nullable` when empty cells appear. Keep a few
`sample_values`.

## Step 4 — Detect enums and key candidates

- Low-cardinality string columns → `enums` (column + distinct values).
- Columns whose values are unique across all rows and id-like → `primary_key_candidates`.

## Step 5 — Normalize

Emit the unified `structured_document` with the table definition, parsed `rows`, detected
enums, and `row_count`. Derive `table.name` from the filename.

# Rules

- Do not guess or coerce values beyond type inference; record cells as they are.
- Do not fabricate a header when none exists — synthesize `col_1..col_n` and note it.
- Handle quoted fields, embedded delimiters, and UTF-8 BOM correctly; do not split naïvely.
- Use `terminal` for all reads; do not assume one library is present — fall back to the
  `awk` path when needed.
- This skill parses `.csv`/`.tsv` only. Route `.xlsx` to `docs-analyze-xlsx`, `.docx` to
  `docs-analyze-docx`, `.pptx` to `docs-analyze-pptx`, `.md` to `docs-analyze-markdown`,
  `.pdf` to `docs-analyze-pdf`.

# Examples

Input:

```yaml
file_path: /project/data/sales.csv
```

Output:

```yaml
structured_document:
  type: csv
  source: /project/data/sales.csv
  table:
    name: sales
    delimiter: ","
    columns:
      - { name: month, type: datetime, nullable: false, sample_values: ["2024-01", "2024-02"] }
      - { name: region, type: string, nullable: false, sample_values: ["Seoul", "Busan"] }
      - { name: revenue, type: integer, nullable: true, sample_values: [1000, 1120] }
    primary_key_candidates: []
  rows:
    - { month: "2024-01", region: "Seoul", revenue: 1000 }
    - { month: "2024-02", region: "Busan", revenue: 1120 }
  enums:
    - { column: region, values: ["Seoul", "Busan"] }
  row_count: 2
```

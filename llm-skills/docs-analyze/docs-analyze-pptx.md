---
name: docs-analyze-pptx
description: Parses a PPTX file into a structured document of UI screens, user flows, actions, requirements, and entities for downstream orchestration.
version: 1.0.0
category: docs-analyze
tags:
  - pptx
  - ui
  - flows
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

Extract explicit application information from a PowerPoint (`.pptx`) deck and
emit a normalized `structured_document` describing UI screens, user flows,
system actions, requirements, and entities. This skill performs **analysis
only** — it does not generate code. It is invoked by `app-orchestrator`, one
instance per `.pptx` input file.

# Inputs

```yaml
file_path: /abs/path/to/ui-design.pptx
```

# Output

```yaml
structured_document:
  type: pptx
  source: /abs/path/to/ui-design.pptx
  screens: []        # [{ id, slide, title, components[], notes }]
  flows: []          # [{ id, from_screen, to_screen, trigger }]
  actions: []        # [{ id, screen, text }]
  requirements: []   # [{ id, text, slide }]
  entities: []       # [{ name, attributes[], source_slide }]
```

# Workflow

## Step 1 — Verify the file

Using the `terminal` tool, confirm the file exists and is a valid PPTX
(ZIP container):

```bash
test -f "<file_path>" && file "<file_path>" | grep -qi "powerpoint\|zip" \
  && echo "OK" || echo "NOT_A_PPTX"
```

## Step 2 — Parse slides

Read each slide's title, text frames, shapes, and speaker notes with the
`terminal` tool. Preferred, if Python + `python-pptx` is available, run a
self-contained one-off extractor (no external script file required):

```bash
python - "<file_path>" <<'PY'
import sys
from pptx import Presentation
prs = Presentation(sys.argv[1])
for i, slide in enumerate(prs.slides, 1):
    print(f"=== SLIDE {i} ===")
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                text = "".join(run.text for run in para.runs).strip()
                if text:
                    print(text)
    if slide.has_notes_slide:
        notes = slide.notes_slide.notes_text_frame.text.strip()
        if notes:
            print(f"[NOTES] {notes}")
PY
```

If `python-pptx` is unavailable, fall back to extracting the slide XML directly
(a `.pptx` is a ZIP; slide bodies live in `ppt/slides/slideN.xml`, notes in
`ppt/notesSlides/`):

```bash
mkdir -p /tmp/pptx_extract && \
unzip -o "<file_path>" 'ppt/slides/*.xml' 'ppt/notesSlides/*.xml' -d /tmp/pptx_extract && \
grep -rho '<a:t>[^<]*</a:t>' /tmp/pptx_extract/ppt/slides | sed 's/<[^>]*>//g'
```

## Step 3 — Build screen definitions

Map each slide to a `screen`: title becomes the screen name, text/shape labels
become candidate UI components, speaker notes become `notes`. Keep the slide
number for traceability.

## Step 4 — Derive flows and actions

Infer `flows` only from explicit transition cues on slides (arrows, "goes to",
"on click → …", navigation labels). Collect button/link labels and imperative
text as `actions`. Do not invent transitions that are not stated.

## Step 5 — Normalize requirements and entities

Extract functional/UI `requirements` from slide text and collect any explicitly
named data `entities`. Merge everything into the unified `structured_document`
schema with stable ids (`SCR-001`, `FLOW-001`, `ACT-001`, `FR-001`).

# Rules

- Do not hallucinate slides, screens, or transitions not present in the deck.
- Preserve slide-level traceability (every item records its slide number).
- Infer flows only from explicit navigation cues, never from assumed UX.
- Use `terminal` for all file access; do not assume any single parser library is present — prefer the inline `python-pptx` extractor and fall back to the `unzip`/XML path when it is unavailable.
- This skill parses `.pptx` only. Route `.docx` to `docs-analyze-docx`, `.xlsx` to `docs-analyze-xlsx`, and `.md` to `docs-analyze-markdown`.

# Examples

Input:

```yaml
file_path: /project/docs/ui-design.pptx
```

Output:

```yaml
structured_document:
  type: pptx
  source: /project/docs/ui-design.pptx
  screens:
    - { id: SCR-001, slide: 1, title: "Login", components: ["email field", "password field", "Sign in button"], notes: "Entry screen" }
    - { id: SCR-002, slide: 2, title: "Dashboard", components: ["order table", "New order button"], notes: "" }
  flows:
    - { id: FLOW-001, from_screen: SCR-001, to_screen: SCR-002, trigger: "click Sign in" }
  actions:
    - { id: ACT-001, screen: SCR-002, text: "Create a new order" }
  requirements:
    - { id: FR-001, text: "Users authenticate with email and password.", slide: 1 }
  entities:
    - { name: Order, attributes: [id, status, total], source_slide: 2 }
```

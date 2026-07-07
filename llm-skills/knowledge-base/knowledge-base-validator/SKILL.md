---
name: knowledge-base-validator
description: Validate assembled knowledge artifacts (FAQ, onboarding, glossary, index) for citation integrity, uncited/fabricated entries, glossary term consistency, and requested-artifact completeness, returning a deterministic pass/fail report. Final stage of the knowledge-base pipeline.
version: 1.0.0
category: knowledge-base
tags:
  - knowledge-base
  - validation
  - citation-integrity
  - final-output
model: inherit
invokes: []
inputs:
  - knowledge_base
  - chunks
  - kb_request
outputs:
  - validation_result
---

# Goal

Verify that a generated knowledge base is grounded and complete before use, returning a
deterministic pass/fail verdict with specific violations. This validates artifacts against
the source chunks; it does not chunk, index, author, or fix. Factual correctness of the
corpus itself is out of scope — this checks that every artifact entry is *traceable to* the
corpus, not that the corpus is true.

# Scope

- Citation integrity (every `source_ref` resolves to an existing chunk)
- Grounding (no artifact entry without at least one source citation)
- Glossary consistency (no duplicate terms; no conflicting definitions for one term)
- Completeness (every requested `kb_request.purpose` artifact is present and non-empty)
- Index integrity (every indexed chunk exists; no empty topic)

Out of scope: truth of corpus content, external facts (see `research/*`), prose quality,
runtime code.

# Checks

1. Every `source_ref` in FAQ / onboarding / glossary points to a chunk that exists in `chunks`.
2. No FAQ answer, onboarding step, or glossary definition is present with zero `source_refs`.
3. No glossary term appears twice; no two entries give conflicting definitions for the same term.
4. Each artifact named in `kb_request.purpose` exists and has at least one entry.
5. Every chunk referenced by the index exists; no topic in the index is empty.

# Pass/Fail Criteria

- **pass**: all checks succeed.
- **fail**: any dangling citation, uncited entry, duplicate/conflicting glossary term,
  missing requested artifact, or dangling/empty index reference.

# Output Schema

```yaml
validation_result:
  result: pass | fail
  violations:
    - { artifact: faq | onboarding | glossary | index, entry: <id/term>, issue: <what failed> }
  stats: { faq: <n>, onboarding: <n>, glossary: <n>, dangling_refs: <n>, uncited: <n> }
```

# Rules

- Report violations only; never modify the knowledge base.
- Deterministic verdict: any single violation forces `fail`.
- Check citations against the provided `chunks`, not against outside knowledge.
- Do not judge whether the corpus content is correct — only whether artifacts trace to it.

# Examples

Input:

```yaml
knowledge_base:
  faq: [ { question: "배포 롤백?", answer: "kubectl rollout undo", source_refs: [c-99] } ]
  glossary: [ { term: "SLA", definition: "...", source_refs: [c-12] },
              { term: "SLA", definition: "다른 정의", source_refs: [c-40] } ]
chunks: [ { id: c-12 }, { id: c-40 } ]   # c-99 does not exist
kb_request: { purpose: [faq, glossary] }
```

Output:

```yaml
validation_result:
  result: fail
  violations:
    - { artifact: faq, entry: "배포 롤백?", issue: "source_ref c-99 does not resolve to a chunk" }
    - { artifact: glossary, entry: "SLA", issue: "conflicting definitions for one term" }
  stats: { faq: 1, onboarding: 0, glossary: 2, dangling_refs: 1, uncited: 0 }
```

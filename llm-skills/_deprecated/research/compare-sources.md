---
name: compare-sources
description: Compare information extracted from multiple sources and identify agreements, differences, overlaps, and unique claims without determining which source is correct.
---

# Goal

Compare information collected from multiple research sources.

Identify:

- Agreements
- Differences
- Overlapping information
- Unique information

Do not determine which source is correct.

Do not perform fact checking.

---

# Inputs

- Extracted facts from `web-research`
- Source metadata
- Optional comparison focus

Examples

Topic:

Spring Boot Virtual Threads

Sources:

- spring.io
- Oracle Documentation
- GitHub

---

# Output

Return the comparison using the following structure.

## Comparison Topic

The topic being compared.

---

## Agreements

Information consistently reported across multiple sources.

For each agreement provide:

- Statement
- Supporting sources

---

## Differences

Information that differs between sources.

For each difference provide:

- Source A
- Source B
- Different statements

---

## Unique Information

Facts appearing in only one source.

For each item provide:

- Statement
- Source

---

## Coverage

Summarize coverage of the available sources.

Examples

- API described only by official documentation.
- Performance benchmarks appear only in blog articles.
- Historical background appears only in Wikipedia.

---

## Possible Conflicts

List statements that may require fact checking.

Do not resolve them.

---

# Workflow

1. Receive extracted facts.
2. Group similar statements.
3. Detect duplicate information.
4. Identify agreements.
5. Identify differences.
6. Identify unique statements.
7. Preserve source attribution.
8. Report possible conflicts.
9. Stop.

---

# Rules

## Comparison Only

Only compare information.

Never:

- Decide which statement is correct.
- Judge source quality.
- Verify facts.
- Generate conclusions.
- Recommend one source.

---

## Agreements

Treat information as an agreement only if multiple independent sources express the same meaning.

Minor wording differences are acceptable.

---

## Differences

Report differences objectively.

Do not interpret why they differ.

Do not attempt reconciliation.

---

## Unique Information

Information found in only one source is not automatically incorrect.

Simply report it as unique.

---

## Source Attribution

Every statement must retain its original source.

Never merge statements from different sources without attribution.

---

## Missing Information

If important information exists in one source but not another:

Report it as coverage differences.

Do not assume omission means contradiction.

---

## Output Restrictions

Do not include:

- Personal opinions
- Recommendations
- Rankings
- Speculation
- Assumptions
- Fact verification
- Source credibility assessment

---

# Handoff

The output of this skill is intended for:

- fact-check
- summarize
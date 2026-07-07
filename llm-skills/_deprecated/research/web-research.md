---
name: web-research
description: Read web pages from search results and extract factual information without summarizing or interpreting.
---

# Goal

Collect factual information from web pages returned by previous search results.

The purpose of this skill is to extract verified information from reliable sources.

This skill does not summarize, compare, verify, or answer the user's question.

---

# Inputs

- Search results from `web-search`
- Optional research focus
- Optional keywords
- Optional extraction depth

Examples

Research Topic:
Spring Boot Virtual Threads

Input Sources:

- https://spring.io/...
- https://docs.oracle.com/...
- https://github.com/...

---

# Output

Return the collected information using the following structure.

## Research Topic

The topic being researched.

## Extracted Facts

For each source provide:

### Source

- URL
- Title

### Facts

- Fact 1
- Fact 2
- Fact 3

Each fact should represent a single objective statement.

---

## Unverified Claims

List statements that appear in the source but cannot be confirmed from that source alone.

---

## Missing Information

List information that was expected but not found.

---

## Source Coverage

- Number of sources processed
- Number of accessible sources
- Number of failed sources

---

# Workflow

1. Receive search results.
2. Open each source.
3. Ignore inaccessible pages.
4. Read the page content.
5. Extract factual statements.
6. Separate facts from opinions.
7. Ignore advertisements and unrelated sections.
8. Preserve source attribution for every extracted fact.
9. Return structured research data.
10. Stop.

---

# Rules

## Information Extraction

Extract only information explicitly stated in the source.

Never:

- Infer missing information.
- Guess.
- Fill gaps.
- Rewrite facts into new meanings.
- Combine multiple facts into conclusions.

---

## Fact Granularity

Each extracted fact should contain one idea only.

Good:

- Spring Boot 3.4 supports Virtual Threads.
- Virtual Threads require Java 21.

Bad:

- Spring Boot 3.4 fully supports Virtual Threads and therefore applications become much faster.

The conclusion should not be generated.

---

## Opinions

Do not extract:

- Opinions
- Recommendations
- Marketing language
- Promotional claims
- Subjective descriptions

---

## Source Attribution

Every extracted fact must remain associated with its original source.

Never merge facts from multiple sources.

---

## Unsupported Statements

If a statement cannot be verified within the source itself:

Place it under:

## Unverified Claims

Do not treat it as a fact.

---

## Missing Information

If requested information does not exist in the available sources:

Report:

Not found in available sources.

Do not attempt to answer from prior knowledge.

---

## Output Restrictions

Do not include:

- Summary
- Final answer
- Recommendations
- Comparisons
- Ranking
- Speculation
- Hallucinated information

Those tasks belong to downstream skills.

---

# Handoff

The output of this skill is intended for:

- source-validation
- fact-check
- compare-sources
- summarize
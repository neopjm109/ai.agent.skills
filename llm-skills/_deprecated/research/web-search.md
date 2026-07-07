---
name: web-search
description: Search the web and return relevant sources without summarizing or interpreting the content.
---

# Goal

Search the web for information related to the user's query and return relevant search results.

This skill is responsible only for discovering sources.
It does not summarize, analyze, compare, or verify information.

---

# Inputs

- Search query
- Optional language
- Optional region
- Optional time range
- Optional trusted domains
- Optional number of results

Examples

- Spring Boot Virtual Threads
- Redis Streams
- MCP Protocol
- OpenAI Responses API
- AI Agent Framework

---

# Output

Return the search results using the following structure.

## Search Query

The final query used for searching.

## Search Results

For each result provide:

- Title
- URL
- Source
- Published date (if available)
- Short snippet returned by the search engine

## Notes

Include only observations about the search itself, such as:

- Few relevant results found.
- Results are outdated.
- Multiple duplicate pages detected.
- Official documentation found.

Do not summarize page contents.

---

# Workflow

1. Understand the user's search intent.
2. Refine the search query only if necessary.
3. Execute one or more web searches.
4. Collect the most relevant search results.
5. Remove duplicate URLs.
6. Prefer authoritative sources.
7. Return the collected search results.
8. Stop.

---

# Rules

## Responsibilities

This skill only searches for information.

Do not:

- Read entire pages.
- Summarize content.
- Compare sources.
- Verify facts.
- Generate conclusions.
- Answer the user's original question.

Those tasks belong to downstream skills.

---

## Source Priority

Prefer sources in the following order:

1. Official documentation
2. Official organization websites
3. Government websites
4. Academic papers
5. Standards organizations
6. Vendor documentation
7. Well-known technical publications
8. Reputable news organizations

Avoid when possible:

- SEO content farms
- AI-generated websites
- Clickbait articles
- Low-quality blogs
- Duplicate pages

---

## Query Expansion

If the user's query is ambiguous:

- Generate a small number of alternative search queries.
- Keep the original intent unchanged.
- Do not broaden the topic unnecessarily.

Example:

Original:

Spring AI

Possible searches:

- Spring AI Framework
- Spring AI Documentation
- Spring AI GitHub

---

## Duplicate Handling

If multiple URLs reference the same content:

- Keep the original or official source.
- Remove mirrored copies.

---

## Output Restrictions

Return only search metadata.

Do not include:

- Summaries
- Opinions
- Recommendations
- Assumptions
- Speculation
- Hallucinated information

---

# Handoff

The output of this skill is intended for downstream skills such as:

- web-research
- source-validation
- fact-check
- compare-sources
- summarize
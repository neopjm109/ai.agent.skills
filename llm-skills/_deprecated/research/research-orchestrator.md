---
name: research-orchestrator
description: Coordinate the end-to-end research pipeline by selecting appropriate search skills and delegating each stage to specialized research skills.
---

# Goal

Produce an evidence-based response by orchestrating specialized research skills.

This skill is responsible for:

- Selecting the appropriate search skills.
- Coordinating the research pipeline.
- Returning the final summarized result.

This skill never performs research directly.

---

# Inputs

- User request
- Optional language
- Optional output format
- Optional trusted domains
- Optional time range

---

# Output

A final response containing only verified information.

Include:

- Summary
- Key Facts
- Remaining Uncertainty
- Sources

---

# Workflow

## Step 1

Analyze the user's request.

Determine:

- Topic
- Intent
- Information type
- Preferred source type

---

## Step 2

Select one or more Search Skills.

Available Search Skills

- web-search
- docs-search
- github-search
- news-search
- reddit-search
- paper-search
- package-search
- video-search
- image-search
- local-search
- code-search

Multiple search skills may be invoked when appropriate.

---

## Search Skill Selection

Use the following guidelines.

### General knowledge

Use:

- web-search

---

### Official documentation

Use:

- docs-search

---

### Open source projects

Use:

- github-search

---

### Recent events

Use:

- news-search

---

## Step 3

Merge all search results.

Remove:

- duplicate URLs
- mirrored pages
- duplicate repositories

Preserve source metadata.

---

## Step 4

Invoke

web-research

Extract factual information from all collected sources.

---

## Step 5

Invoke

source-validation

Evaluate source credibility.

---

## Step 6

Invoke

compare-sources

Identify:

- agreements
- differences
- unique claims

---

## Step 7

Invoke

fact-check

Verify claims using validated evidence.

---

## Step 8

Invoke

summarize

Generate the final response using only supported facts.

---

## Step 9

Return the final summary.

---

# Decision Rules

## Multiple Search Skills

If the request spans multiple domains,
invoke multiple Search Skills.

Example

Spring Boot 3.5

↓

docs-search

github-search

news-search

---

## Insufficient Results

If one Search Skill returns insufficient results,

try another applicable Search Skill.

---

## Duplicate Results

Always remove duplicated sources before research.

---

## Missing Evidence

If verified evidence cannot be obtained,

report:

"Insufficient verified information."

Never complete missing information using model knowledge.

---

# Error Handling

If one Search Skill fails:

Continue using successful search results.

If every Search Skill fails:

Stop.

Report:

"No reliable sources were found."

If downstream skills fail:

Continue whenever possible.

Report incomplete stages.

---

# Rules

## Responsibilities

This skill only coordinates.

Never:

- Search directly
- Read web pages
- Validate sources
- Compare evidence
- Perform fact checking
- Summarize
- Generate conclusions

Delegate every task.

---

## Search Skill Selection

Always select the most appropriate Search Skills.

Prefer specialized Search Skills over general search whenever possible.

General web-search should be used only when no specialized Search Skill exists or additional context is required.

---

## Information Integrity

Never modify outputs from downstream skills.

Never invent information.

Never replace missing evidence.

---

## Pipeline

User Request

↓

Intent Analysis

↓

Search Skill Selection

↓

One or More Search Skills

↓

Merge Search Results

↓

web-research

↓

source-validation

↓

compare-sources

↓

fact-check

↓

summarize

↓

Final Response
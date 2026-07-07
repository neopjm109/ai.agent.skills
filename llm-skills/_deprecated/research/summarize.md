---
name: summarize
description: Produce a concise, structured summary using only verified information from previous research stages.
---

# Goal

Generate a clear and concise summary using only information provided by upstream research skills.

This skill does not perform research, fact checking, or source validation.

It only reorganizes verified information into a human-readable summary.

---

# Inputs

- Verified facts
- Validated sources
- Optional target audience
- Optional summary length
- Optional output format

Examples

Verified Facts

- Spring Boot 3.4 supports Virtual Threads.
- Virtual Threads require Java 21.
- Virtual Threads are implemented by Project Loom.

---

# Output

Return the summary using the following structure.

## Summary

A concise summary using only verified facts.

---

## Key Points

- Point 1
- Point 2
- Point 3

---

## Important Facts

List important facts without modification.

- Fact
- Fact
- Fact

---

## Open Questions

List information that remains unknown.

If none:

None.

---

## Sources

List every source referenced during summarization.

---

# Workflow

1. Receive verified facts.
2. Ignore rejected or unverified information.
3. Group related facts.
4. Remove duplicated statements.
5. Preserve original meaning.
6. Produce a concise summary.
7. Preserve important details.
8. Include all referenced sources.
9. Stop.

---

# Rules

## Information Usage

Only use information provided as input.

Never:

- Search for additional information.
- Add missing facts.
- Guess.
- Infer conclusions.
- Fill knowledge gaps.
- Introduce outside knowledge.

---

## Faithfulness

The summary must preserve the original meaning.

Do not:

- Change technical meanings.
- Strengthen claims.
- Weaken claims.
- Merge unrelated facts.
- Omit critical limitations.

---

## Unsupported Information

Never include:

- Unverified claims
- Rejected facts
- Speculation
- Predictions
- Opinions
- Recommendations

---

## Compression

Summarize by:

- Removing repetition
- Grouping related facts
- Simplifying wording
- Preserving meaning

Do not remove important technical information.

---

## Objectivity

Write in a neutral tone.

Avoid:

- Marketing language
- Subjective expressions
- Emotional wording
- Personal opinions

---

## Source Preservation

Every summarized statement must be traceable to at least one validated source.

Do not summarize information whose source is unknown.

---

## Missing Information

If the available information is insufficient:

State:

"Insufficient verified information."

Do not attempt to complete the answer.

---

## Output Restrictions

Do not:

- Perform new research
- Validate sources
- Perform fact checking
- Compare sources
- Rank alternatives
- Recommend solutions
- Answer questions beyond the provided facts

---

# Handoff

This skill produces the final research summary.

Its output is intended for direct presentation to the user.
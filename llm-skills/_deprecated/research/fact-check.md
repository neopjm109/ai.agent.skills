---
name: fact-check
description: Evaluate factual claims using only validated research sources and determine the level of evidential support without introducing outside knowledge.
---

# Goal

Evaluate factual claims using verified research data and validated sources.

Determine whether each claim is supported, contradicted, inconclusive, or unverifiable based only on the provided evidence.

This skill does not perform new web searches or use prior knowledge.

---

# Inputs

- Extracted facts
- Source comparison results
- Source validation results
- Claims requiring verification

Examples

Claim

Spring Boot 3.4 requires Java 21.

Evidence

- Official Spring documentation
- Oracle documentation
- GitHub release notes

---

# Output

Return the verification using the following structure.

## Fact Check Results

For each claim provide:

### Claim

Original claim.

### Status

One of:

- Supported
- Contradicted
- Inconclusive
- Unverifiable

### Evidence

List supporting or contradicting evidence.

Include source attribution.

### Confidence

One of:

- High
- Medium
- Low

Confidence reflects the quality and consistency of the available evidence,
not model confidence.

### Notes

Explain why the claim received its status.

---

## Remaining Uncertainty

List questions that could not be resolved.

---

## Evidence Summary

Summarize:

- Number of supporting sources
- Number of contradicting sources
- Number of neutral sources

---

# Workflow

1. Receive claims.
2. Collect all related evidence.
3. Ignore evidence from rejected sources.
4. Compare the claim with extracted facts.
5. Determine the evidence status.
6. Record supporting and contradicting evidence.
7. Assign confidence based on evidence quality.
8. Report unresolved uncertainty.
9. Stop.

---

# Rules

## Evidence Only

Use only the provided evidence.

Never:

- Search the web.
- Use model memory.
- Use prior knowledge.
- Fill missing information.
- Guess.

---

## Verification Status

Supported

The claim is consistently supported by sufficient evidence.

Contradicted

Reliable evidence directly conflicts with the claim.

Inconclusive

Available evidence is insufficient or conflicting.

Unverifiable

No relevant evidence is available.

---

## Confidence

High

- Multiple independent high-quality sources agree.

Medium

- Limited evidence or minor disagreement.

Low

- Sparse evidence or weak sources.

Confidence reflects evidence quality only.

---

## Source Priority

When evaluating evidence, prefer:

1. Official documentation
2. Government publications
3. Standards organizations
4. Peer-reviewed academic publications
5. Vendor documentation
6. Reputable technical publications

Do not automatically reject lower-priority sources.

Evaluate all available evidence.

---

## Contradictions

If evidence conflicts:

- Record all conflicting evidence.
- Do not ignore minority evidence.
- Explain why the result is inconclusive if appropriate.

---

## Missing Evidence

If evidence is insufficient:

Return:

Status:
Unverifiable

Do not infer the answer.

---

## Output Restrictions

Do not:

- Recommend products
- Express opinions
- Predict outcomes
- Invent explanations
- Rewrite evidence into stronger conclusions

Only report what the evidence supports.

---

# Handoff

The output of this skill is intended for:

- summarize
- final-answer
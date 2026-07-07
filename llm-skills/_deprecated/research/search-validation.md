---
name: source-validation
description: Evaluate the credibility, authority, and quality of information sources without validating the factual accuracy of their content.
---

# Goal

Assess the reliability of information sources collected during web research.

This skill evaluates the credibility of the source itself, not whether the information is true.

Do not perform fact checking.

---

# Inputs

- Research results from `web-research`
- Source URLs
- Source metadata
- Optional evaluation criteria

Examples

Sources:

- https://spring.io
- https://docs.oracle.com
- https://github.com
- https://medium.com
- https://example-blog.com

---

# Output

Return the evaluation using the following structure.

## Source Evaluation

For each source provide:

### Source

- URL
- Title

### Credibility

- High
- Medium
- Low

### Authority

Examples:

- Official Documentation
- Government
- Academic Institution
- Standards Organization
- Vendor
- News Organization
- Technical Blog
- Personal Blog
- Community Forum

### Reasons

- Official website
- Named author
- Publication date available
- References provided
- Technical accuracy appears maintained
- Anonymous author
- Excessive advertisements
- Promotional content

### Recommended Usage

One of:

- Primary Source
- Supporting Source
- Background Only
- Avoid

---

## Overall Assessment

- Number of High credibility sources
- Number of Medium credibility sources
- Number of Low credibility sources

---

## Warnings

Examples

- Multiple low-quality sources detected.
- Only one authoritative source found.
- No official documentation available.

---

# Workflow

1. Receive researched sources.
2. Evaluate each source independently.
3. Identify the source category.
4. Assess authority.
5. Assess transparency.
6. Assess recency if relevant.
7. Detect promotional or low-quality content.
8. Assign credibility level.
9. Record reasons.
10. Return the evaluation.

---

# Rules

## Evaluate the Source

Evaluate:

- Publisher
- Organization
- Author
- References
- Publication quality
- Transparency
- Update history
- Editorial standards

Do not evaluate factual correctness.

---

## Credibility Levels

High

Examples

- Official documentation
- Government websites
- Standards organizations
- Academic publications
- Peer-reviewed papers

Medium

Examples

- Major news organizations
- Vendor documentation
- Recognized technical blogs
- Established educational websites

Low

Examples

- Anonymous blogs
- AI-generated content farms
- Clickbait websites
- SEO pages
- Unmoderated community content

---

## Authority Categories

Classify sources using categories such as:

- Official Documentation
- Government
- Academic
- Standards Organization
- Vendor
- Research Institute
- News
- Technical Blog
- Community
- Personal Blog
- Unknown

---

## Indicators

Positive indicators

- Official domain
- Named organization
- Named author
- References
- Publication date
- Update history
- Editorial process

Negative indicators

- Anonymous ownership
- Excessive advertisements
- No references
- Obvious promotional language
- AI-generated spam
- Misleading titles

---

## Independence

Evaluate every source independently.

Do not compare sources.

---

## Output Restrictions

Do not:

- Verify facts
- Decide which claim is correct
- Summarize information
- Generate conclusions
- Recommend products
- Answer the user's question

---

# Handoff

The output of this skill is intended for:

- fact-check
- compare-sources
- summarize
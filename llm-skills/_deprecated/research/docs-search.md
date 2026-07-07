---
name: docs-search
description: Search official documentation and technical reference sites for relevant documentation pages without reading or summarizing them.
---

# Goal

Locate official documentation relevant to the user's request.

Return documentation pages only.

Do not read, summarize, or interpret documentation.

---

# Inputs

- Product
- Framework
- Library
- API
- Version (optional)

Examples

- Spring Boot 3.5
- Next.js App Router
- Redis Streams
- MCP Protocol
- OpenAI Responses API

---

# Output

## Search Query

Final query.

## Documentation Results

For each result provide:

- Title
- URL
- Organization
- Documentation version (if available)
- Section title (if available)

## Notes

Examples

- Official documentation found.
- Multiple versions detected.
- Deprecated documentation detected.

---

# Workflow

1. Identify the technology.
2. Search official documentation.
3. Prefer vendor documentation.
4. Ignore community articles.
5. Return documentation URLs only.

---

# Rules

Prefer:

1. Official documentation
2. Standards specifications
3. Official API references

Avoid:

- Blogs
- Tutorials
- Medium
- Stack Overflow
- AI-generated sites

Do not:

- Read pages
- Explain APIs
- Summarize documentation
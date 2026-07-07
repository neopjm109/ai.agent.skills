---
name: github-search
description: Search GitHub repositories and related project resources without analyzing repository contents.
---

# Goal

Locate relevant GitHub repositories.

Only identify repositories and project metadata.

Do not analyze source code.

---

# Inputs

- Repository name
- Library
- Framework
- Organization

Examples

- Spring AI
- FastAPI
- LangGraph
- MCP SDK

---

# Output

## Search Query

Final query.

## Repository Results

For each repository:

- Repository
- Organization
- URL
- Description
- Stars (if available)
- Last updated (if available)

## Notes

Examples

- Official repository found.
- Multiple forks detected.
- Archived repository.

---

# Workflow

1. Search GitHub.
2. Prefer official repositories.
3. Ignore forks when original exists.
4. Collect metadata.
5. Return repository list.

---

# Rules

Prefer

- Official repositories
- Organization repositories
- Verified maintainers

Avoid

- Personal forks
- Mirrors
- Archived repositories
- Demo repositories unless requested

Do not

- Analyze source code
- Explain implementation
- Read README
- Generate conclusions
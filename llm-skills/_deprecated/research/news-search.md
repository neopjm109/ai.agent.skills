---
name: news-search
description: Search recent news articles related to the user's topic without interpreting or summarizing the news.
---

# Goal

Locate recent news articles relevant to the requested topic.

Return news metadata only.

---

# Inputs

- Topic
- Date range (optional)
- Region (optional)

Examples

- OpenAI
- NVIDIA
- Java
- AI Agents
- Redis

---

# Output

## Search Query

Final query.

## News Results

For each article:

- Title
- Publisher
- URL
- Published date
- Short snippet

## Notes

Examples

- Multiple publishers reporting the same event.
- Breaking news.
- Older coverage detected.

---

# Workflow

1. Search recent news.
2. Prefer reputable publishers.
3. Remove duplicate stories.
4. Return article metadata.

---

# Rules

Prefer

- Reuters
- AP
- Bloomberg
- BBC
- Official press releases

Avoid

- Opinion articles
- Rumors
- Aggregator spam
- Clickbait

Do not

- Summarize news
- Interpret events
- Predict outcomes
- Judge credibility beyond obvious quality filters
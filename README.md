# AI Agent SKILLs

이 프로젝트는 AI Agent에 사용할 SKILL들과 각각의 에이전트에 사용할 Tool (혹은 Plugin)을 기록한 저장소다.

## SKILL

Skill은 `https://agentskills.io/`의 작성법을 기준으로 작성한다.

### 양식

```markdown
---
name: skill-name
description: skill 설명
version: 0.0.1
trigger: skill 발생 조건
example:
  - "메시지 예제"
trust: 신뢰 등급 (builtin, official, trusted, community)
---

# Goal

# Inputs

# Ouput

# Workflow

# Rule

# Examples
```

## Tool (Plugin)

> Hermes Agent의 Tool은 내장 Tool을 뜻하며, 내가 만든 Tool은 Plugin으로 넣어줘야한다.

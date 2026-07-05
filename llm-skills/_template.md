---
name: skill-name-here
description: One line stating what this skill produces and when to use it.
version: 1.0.0
category: backend
tags:
  - keyword
model: inherit
invokes: []
inputs:
  - input_name
outputs:
  - output_name
---

# Goal

What this skill accomplishes, in 1–3 sentences. State explicitly whether it
generates code or only design/analysis artifacts.

# Inputs

```yaml
input_name:
  field: <example value>
```

# Output

```yaml
output_name: <what is produced>
```

# Workflow

## Step 1 — <name>

<concrete action>

## Step 2 — <name>

<concrete action; delegate implementation to spring-senior-programmer /
typescript-senior-programmer where applicable>

# Rules

- <hard constraint>
- <naming / boundary rule; state "use X instead of Y" for overlapping skills>

# Examples

Input:

```yaml
<realistic input>
```

Output:

```
<realistic end-to-end output — required, not a placeholder>
```

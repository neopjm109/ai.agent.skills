---
name: i18n-generator
description: Generate internationalization infrastructure and locale-aware components for Next.js — locale config, translation files, locale switcher, translation hooks, middleware.
version: 1.0.0
category: frontend
tags:
  - i18n
  - localization
  - nextjs
model: inherit
invokes:
  - typescript-senior-programmer
inputs:
  - i18n_requirements
outputs:
  - i18n_code
---

# Goal

Generate internationalization resources and locale-aware components for a Next.js
application: locale configuration, translation resource files, a locale switcher,
translation hooks, and routing middleware. Delegates implementation to
`typescript-senior-programmer`.

# Inputs

```yaml
i18n_requirements:
  library: next-intl        # next-intl | next-i18next
  locales: [en, ko, ja]
  default_locale: en
  routing: sub-path         # sub-path (/ko/...) | domain | cookie
  namespaces: [common, auth, dashboard]
  translation_keys: [common.save, common.cancel, auth.login]
```

# Output

```yaml
i18n_code:
  - locale configuration
  - translation files (per locale + namespace)
  - locale switcher component
  - translation hooks (useTranslations)
  - routing middleware (if required)
```

# Workflow

## Step 1 — Analyze locales
Determine supported locales, default locale, routing strategy, and namespaces.

## Step 2 — Build translation structure
Design the translation file layout (per locale + namespace) and key conventions.

## Step 3 — Delegate implementation
Delegate config, switcher, hooks, and middleware to `typescript-senior-programmer`.

## Step 4 — Validate
Confirm locale switching works and no UI strings are hardcoded.

# Rules

- Never hardcode UI strings; always use translation keys.
- Keep locale resources organized by namespace; support future language expansion.
- Use a named i18n library (default `next-intl`); route locales via the chosen strategy.

# Examples

Input:

```yaml
i18n_requirements: { library: next-intl, locales: [en, ko], default_locale: en }
```

Output (abridged):

```ts
// i18n/config.ts
export const locales = ["en", "ko"] as const;
export const defaultLocale = "en";
```

```tsx
// components/locale-switcher.tsx
"use client";
export function LocaleSwitcher() {
  const t = useTranslations("common");
  // render <select> of locales, push router to /{locale}/... on change
}
```

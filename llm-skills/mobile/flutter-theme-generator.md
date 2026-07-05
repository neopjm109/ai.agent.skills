---
name: flutter-theme-generator
description: Generates Material 3 ThemeData (light + dark) from design-tokens values — color scheme, typography, shapes. Use to establish the app-wide visual theme.
version: 1.0.0
category: frontend
tags:
  - flutter
  - theme
  - material3
  - design-tokens
model: inherit
invokes: []
inputs:
  - design_tokens
outputs:
  - flutter_theme
---

# Goal
Convert design-token VALUES into a Material 3 `ThemeData` pair (light and dark), including `ColorScheme`, `TextTheme`, spacing/shape extensions, and a theme-mode provider.

# Inputs
```yaml
design_tokens:
  colors:
    primary: "#3366FF"
    secondary: "#00BFA6"
    error: "#E5484D"
  typography:
    fontFamily: Inter
    scale: { body: 14, title: 20, headline: 28 }
  radius: { md: 12 }
  spacing: { sm: 8, md: 16, lg: 24 }
```

# Output
```yaml
flutter_theme:
  files:
    - lib/theme/app_theme.dart
    - lib/theme/app_spacing.dart
    - lib/theme/theme_provider.dart
---
```

# Workflow
## Step 1 — Color scheme
Build light/dark `ColorScheme` from token colors (using `ColorScheme.fromSeed` where a seed is given, else explicit values).

## Step 2 — Typography & shape
Map typography tokens to a `TextTheme` and radius/spacing tokens to shape and a `ThemeExtension` for spacing.

## Step 3 — Assemble
Compose `ThemeData(useMaterial3: true, ...)` for both brightnesses and expose a `themeModeProvider`.

## Step 4 — Implement
Delegate the ThemeData construction to `flutter-senior-programmer`.

# Rules
- Consume design-token VALUES only — do NOT import or translate React theme code. This is the Flutter analogue of `frontend/theme-generator`.
- Always `useMaterial3: true`; provide both light and dark themes.
- Screens/widgets read this theme via `Theme.of(context)`; never hard-code colors elsewhere.

# Examples
Input:
```yaml
design_tokens: { colors: { primary: "#3366FF" }, typography: { fontFamily: Inter } }
```
Output:
```yaml
flutter_theme:
  file: lib/theme/app_theme.dart
  code: |
    ThemeData buildLightTheme() => ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF3366FF)),
      textTheme: const TextTheme().apply(fontFamily: 'Inter'),
    );
    ThemeData buildDarkTheme() => ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: const Color(0xFF3366FF), brightness: Brightness.dark),
      textTheme: const TextTheme().apply(fontFamily: 'Inter'),
    );
```

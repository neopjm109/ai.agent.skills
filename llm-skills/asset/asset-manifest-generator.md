---
name: asset-manifest-generator
description: Assemble a manifest of produced assets — file paths, kinds, dimensions, formats, and usage mapping — and validate naming/format/size consistency. Final stage of the asset pipeline.
version: 1.0.0
category: asset
tags:
  - asset
  - manifest
  - validation
  - final-output
model: inherit
invokes: []
inputs:
  - produced_assets
  - prompt_specs
  - options
outputs:
  - manifest
---

# Goal

Produce a single manifest describing every produced asset and any pending prompt specs, and
validate that the set is consistent (naming, format, dimensions). Assembles and checks only;
it does not create assets.

# Inputs

```yaml
produced_assets: [ { id, kind, format, content_or_path, size } ]
prompt_specs: [ { id, subject } ]        # raster items not yet rendered
options:
  out_dir: public/assets
  naming: kebab-case
```

# Output

```yaml
manifest:
  base_dir: <out_dir>
  entries:
    - { id, kind, path, format, size, status: ready | pending-render }
  pending_render: [<id>, ...]            # ids that are prompt specs only
  checks: { result: pass | fail, issues: [ { id, issue } ] }
  usage_map: { <slot>: <asset id> }      # optional mapping to frontend slots
```

# Workflow

## Step 1 — Lay out paths
Assign each asset a path under `out_dir` following the `naming` convention and its kind
(icons/, sprites/, placeholders/).

## Step 2 — Record status
Mark authored assets `ready`; mark prompt-spec-only raster items `pending-render` and list
them in `pending_render`.

## Step 3 — Validate
Check unique IDs/paths, valid formats, and that each asset's size matches its spec. Any
violation → `checks.result: fail` with issues.

## Step 4 — Return
Return the `manifest`. Stop.

# Rules

- Assemble and validate only; never generate or modify asset content.
- `pending-render` items must never be reported as ready — keep the render gap explicit.
- Paths must be unique and follow the stated naming convention.
- Deterministic check result: any naming/format/size violation forces `fail`.

# Examples

Input:

```yaml
produced_assets:
  - { id: icon-home, kind: icon, format: svg, content_or_path: "<svg.../>", size: 24x24 }
prompt_specs:
  - { id: raster-hero, subject: "hero banner" }
options: { out_dir: public/assets, naming: kebab-case }
```

Output:

```yaml
manifest:
  base_dir: public/assets
  entries:
    - { id: icon-home, kind: icon, path: public/assets/icons/home.svg, format: svg, size: 24x24, status: ready }
    - { id: raster-hero, kind: raster, path: public/assets/raster/hero.png, format: png, size: 1600x600, status: pending-render }
  pending_render: [ raster-hero ]
  checks: { result: pass, issues: [] }
  usage_map: { "nav.home-icon": icon-home, "landing.hero": raster-hero }
```

# Research Figure Style Guide

This folder stores the persistent figure-production rules used across the user's scientific manuscripts.

The main specification is [SKILL.md](SKILL.md). Machine-readable plotting defaults are in [rules.yaml](rules.yaml).

The intent is to keep figure style independent of any one project. Project-specific palettes, sample anonymization mappings, and biological metadata should be stored separately.

## Current defaults

- Arial, 12 pt
- Transparent background
- PNG + SVG + PDF
- No grid lines
- Four equal-width borders, default 1.5 pt
- Maximum 5–6 major axis ticks where practical
- Significance shown with asterisks
- Same biological group = same color across the manuscript
- Gene symbols and Latin species names italicized
- Publication-safe sample/group naming

## Future extensions

Potential additions include:
- manuscript-specific color palettes
- standard dimensions for single/double-column figures
- standard panel labels
- line widths and point sizes
- heatmap conventions
- PCA/PCoA conventions
- GWAS/selection-scan conventions
- microbiome plotting conventions
- gene-expression/up-down regulation conventions
- automated figure QA checks

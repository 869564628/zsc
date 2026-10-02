# Nature Experience

This folder stores the persistent scientific figure-production and research-workflow rules used across the user's manuscripts.

The main specification is [SKILL.md](SKILL.md). Machine-readable defaults are in [rules.yaml](rules.yaml).

The intent is to keep the user's research standards consistent across projects rather than tying them to a single manuscript.

## Current figure defaults

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
- gene-expression/up/down regulation conventions
- statistical-analysis standards
- automated figure QA checks
- reusable R/Python plotting templates

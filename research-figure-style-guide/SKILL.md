# Research Figure Style Guide

## Purpose
This document defines the user's persistent scientific figure standards. It is the single source of truth for future plotting, figure review, and figure-formatting tasks.

## Mandatory rules

### Identity and data protection
- Never expose or reproduce sensitive sample identifiers when the user requests anonymization.
- Replace sample names and group labels with publication-safe names when requested.
- Preserve the mapping between anonymized labels and original metadata only in the user's private analysis environment, never in public figures or public repositories unless explicitly requested.

### Export
- Preferred output formats: PNG, SVG, PDF.
- Background: transparent by default.
- Figures should be publication-ready and reproducible.

### Typography
- Font: Arial.
- Default font size: 12 pt.
- Gene symbols: italic.
- Latin species names: italic.
- Keep typography consistent across all panels of a manuscript.

### Axes and frame
- No grid lines unless explicitly requested.
- Four plot borders/spines should have equal thickness.
- Default border thickness: 1.5 pt; use 2 pt when a stronger frame is needed.
- Keep tick labels concise and visually balanced.
- Prefer no more than 5–6 major tick labels per x or y axis. Use sensible breaks rather than displaying excessive tick numbers.

### Statistical annotation
- Use asterisks for statistical significance by default:
  * P < 0.05
  ** P < 0.01
  *** P < 0.001
  **** P < 0.0001
- Exact P values may be shown when scientifically or editorially preferable, but do not mix annotation conventions within the same figure without a reason.

### Color consistency
- Samples belonging to the same biological/geographical group must use the same color across all figures in the manuscript.
- Example: Kunming-associated samples use the manuscript's established sky-blue color.
- Never invent a new color for an existing group merely to improve an individual figure.
- Maintain a manuscript-level palette file and reuse it across figures.

### Biological nomenclature
- Gene symbols should be italicized.
- Latin binomials should be italicized.
- Protein names should not automatically be italicized unless the relevant nomenclature convention requires it.
- Check capitalization and nomenclature before final export.

### Figure design
- Prioritize clean scientific communication over decorative styling.
- Avoid unnecessary labels, excessive annotations, shadows, gradients, 3D effects, and visual clutter.
- Keep panel alignment, margins, line widths, and font hierarchy consistent across a manuscript.
- The same biological variable should have the same visual encoding across all figures.

## Quality-control checklist
Before finalizing a figure, check:
1. Sample/group names are publication-safe.
2. Group colors match the manuscript palette.
3. Arial 12 pt is used consistently.
4. Gene symbols and Latin names are italicized.
5. Background is transparent.
6. No unintended grid lines are present.
7. All four borders have equal line width.
8. Major x/y ticks are <= 6 where practical.
9. Significance annotations use the manuscript convention.
10. PNG + SVG + PDF are exported.
11. No accidental legends, labels, or metadata expose private sample information.

## Versioning
Changes to this document are intentional changes to the user's persistent figure standard. Record substantial changes in Git history with a clear commit message.

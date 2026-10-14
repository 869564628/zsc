---
name: experience
description: Apply the user's persistent scientific research and figure-production standards. Use when creating, editing, reviewing, or quality-checking scientific figures, R/Python plotting code, analysis workflows, statistical interpretations, genomics or microbiome results, manuscript text, and reusable research procedures. Preserve project-specific facts and established conventions; do not invent missing results or silently change scientific meaning.
---

# Experience

## Purpose

Use this skill as the user's reusable, evolving research-standard library. The canonical project lives in `nature_experience/`; this skill is named `experience`. Apply the relevant rules to the current task instead of repeating the entire library in every response.

## Operating principles

1. **Read before acting.** Inspect the supplied data, code, figure, manuscript excerpt, project files, and relevant rules before proposing changes.
2. **Audit before rewriting.** Identify what is already correct, what is inconsistent, what is unsupported, and what is missing. Avoid unnecessary rewrites.
3. **Preserve evidence and meaning.** Never fabricate values, sample sizes, statistical results, citations, file paths, tool output, or completed actions. Distinguish observed results, user-provided context, inference, and recommendations.
4. **Keep changes traceable.** Explain consequential changes briefly. Preserve original data and keep transformations reproducible.
5. **Follow project-specific conventions first.** Reuse the existing manuscript palette, naming, units, coordinate conventions, filtering criteria, and output structure. Do not replace established choices with generic defaults without a reason.
6. **Deliver usable work.** Prefer runnable code, explicit paths, concrete edits, and the requested deliverable formats over abstract advice. Do not claim a file was generated, code was run, or a repository was updated unless it actually happened.
7. **Verify before delivery.** Check file paths, syntax, outputs, figure readability, and whether the deliverable satisfies the request. State checks that could not be performed.
8. **Protect sensitive data.** When anonymization is requested, remove identifying sample/group labels from public-facing outputs and never publish the private key that maps anonymized labels to originals.

## Task routing

First identify the task type and load only the relevant sections of this skill and `rules.yaml`.

- **Figure creation or revision:** apply the figure defaults and the figure QA checklist below; inspect the existing palette and plotting code first.
- **Figure review:** report concrete issues by severity and location; separate required corrections from optional improvements.
- **Bioinformatics or statistical workflow:** preserve the user's actual environment, paths, genome/annotation versions, sample definitions, and filtering choices. Give commands in executable order and include validation checks.
- **Results interpretation:** connect evidence across analyses where appropriate, but do not treat correlation, PCA separation, candidate genes, enrichment, or selection statistics as proof of causality.
- **Manuscript writing or review:** preserve the scientific claim and author's intended framing; match each claim to evidence; flag unsupported or overstated statements; do not invent citations.
- **Reusable method or code:** record prerequisites, inputs, outputs, parameters, failure checks, and assumptions so the procedure can be reused in another project.

## Scientific figure defaults

The machine-readable defaults in `rules.yaml` are the source of truth for configurable values. The defaults below summarize the current standard:

- Export **PNG, SVG, and PDF**.
- Use a transparent background unless the target journal or requested format requires otherwise.
- Use **Arial**, nominally **12 pt**, consistently across panels; adapt only when a specific journal dimension or dense plot requires it.
- Do not show gridlines by default.
- Use equal-width plot borders/spines, **1.5 pt** by default; use **2 pt** only when a stronger frame is needed.
- Keep major axis ticks to about **5–6 or fewer** when practical without hiding meaningful data.
- Use asterisks for significance by default: * P < 0.05; ** P < 0.01; *** P < 0.001; **** P < 0.0001. Use exact P values when more informative or required, and define the convention in the caption.
- Keep each biological group the same color across all figures in a manuscript. Reuse a palette file; never assign colors independently per panel.
- Italicize gene symbols and Latin binomials. Do not automatically italicize protein names.
- Remove unnecessary decoration, shadows, gradients, 3D effects, redundant labels, and legends that do not add information.
- Align panels, margins, typography, line widths, and visual encodings consistently.
- Use clear units, informative axis labels, legible legends, and publication-safe sample/group labels.

### Figure workflow

1. Inspect the input table, variable types, missing values, group labels, units, and sample counts.
2. Identify the scientific comparison and the visual encoding that best represents it. Do not choose a plot type only because it looks attractive.
3. Reuse the manuscript's established colors, labels, dimensions, and typography.
4. Build the figure from a reproducible script when possible. Do not manually alter plotted values to improve appearance.
5. Export PNG + SVG + PDF with the requested dimensions and transparent background by default.
6. Review the exported figure itself, not just the code. Check clipped text, overlapping labels, legends, axis ranges, font fallback, transparency, and consistency across panels.
7. Report the output paths and any unresolved limitations.

### Figure QA checklist

- [ ] Values, sample sizes, units, and group labels match the source data.
- [ ] The chosen plot supports the stated scientific comparison.
- [ ] Group colors match the manuscript palette.
- [ ] Arial and font sizes are consistent and readable.
- [ ] Gene symbols and Latin species names are italicized.
- [ ] Background is transparent unless an explicit exception applies.
- [ ] No unintended gridlines or decorative effects appear.
- [ ] All four plot borders have equal width.
- [ ] Major tick labels are concise (normally no more than 5–6 per axis where practical).
- [ ] Statistical annotations follow one clearly defined convention.
- [ ] PNG, SVG, and PDF are exported as requested.
- [ ] No private sample mappings or unintended metadata are exposed.

## Bioinformatics and analysis workflow standards

When writing or modifying an analysis workflow:

1. **Inventory inputs:** list the actual input files, reference genome/build, annotation version, sample sheet, and metadata required.
2. **Validate assumptions:** check sample IDs, chromosome naming, ploidy/sex-chromosome handling, file sorting/indexing, missingness, allele representation, and software compatibility when relevant.
3. **Keep parameters explicit:** document filtering thresholds, window sizes, statistical models, random seeds, software versions, and important command-line options.
4. **Separate stages:** make intermediate files and output directories explicit; avoid overwriting original data.
5. **Add checkpoints:** use file-existence, record-count, log, and summary-statistic checks after important stages.
6. **Interpret cautiously:** account for population structure, relatedness, batch effects, sample size, multiple testing, and alternative explanations where relevant.
7. **Report reproducibility:** state what was run, what remains untested, and which results need independent validation.

Do not assume that a particular tool, reference build, directory, sample set, or parameter is current merely because it appeared in an earlier task. Confirm it against the current request or available project files.

## Statistical interpretation and manuscript standards

- Distinguish descriptive patterns, statistical associations, predictive performance, and causal evidence.
- Report effect size and uncertainty where available, not only P values.
- Consider multiple-testing correction when many hypotheses or loci are tested.
- Do not describe a candidate gene as functionally validated solely because it overlaps a significant region.
- For population-genomic scans, distinguish evidence of differentiation or a selection candidate from proof of adaptation; consider demographic history, linkage, recombination, structure, and method-specific limitations.
- For microbiome analyses, distinguish taxonomic composition from inferred function; label PICRUSt2 or other predicted functions as predictions, not direct measurements.
- For isotope mixing models, state model assumptions and uncertainty; do not equate an estimated dietary proportion with direct observation of every feeding event.
- Make claims proportional to the evidence. If evidence is incomplete, use qualified wording and state what would test the hypothesis.
- Do not invent references. If citations are requested, verify bibliographic details and make clear when a claim has not been independently checked.

## Writing and review workflow

For manuscript passages, reviewer responses, methods, figure legends, and abstracts:

1. Identify the intended claim, audience, journal/format constraints, and the evidence provided.
2. Preserve the user's framing unless asked to change it.
3. Match every quantitative or mechanistic claim to supplied results or a verified source.
4. Remove repetition and ambiguous wording without changing scientific meaning.
5. Flag contradictions, unsupported causal language, missing methodological details, and terminology drift.
6. Return a polished version plus a short list of material changes or unresolved evidence gaps when useful.

For reviewer responses, answer each point directly, specify the actual revision, and do not claim a change was made unless the manuscript text was changed.

## Output and interaction preferences

- Prefer direct, technically precise answers and deliverables that can be used immediately.
- For code tasks, preserve explicitly supplied cluster paths and environments; do not replace them with guessed paths.
- When a request depends on unavailable files or results, ask for the specific missing input rather than fabricating it.
- If the user asks for Word, PowerPoint, Excel, CSV, or another concrete format, prioritize that format over Markdown where feasible.
- Keep explanations concise enough to act on, but include assumptions and validation steps that affect correctness.

## Updating this skill

Treat `SKILL.md` as the portable instruction entry point, `rules.yaml` as machine-readable defaults, and `Experience.md` as the fuller human-readable standard. When a new durable preference or validated workflow is established:

1. Determine whether it is a general rule or project-specific exception.
2. Add general defaults to `rules.yaml` only when they can be represented clearly as configuration.
3. Add procedural guidance to `SKILL.md`; preserve rationale and detailed checklists in `Experience.md` or focused reference files.
4. Increment `VERSION` and add a dated entry to `CHANGELOG.md` for meaningful releases.
5. Update the README installation notes and regenerate the distributable ZIP when applicable.
6. Never treat an unverified suggestion or one-off exception as a permanent standard without confirmation.

The skill does not automatically read private local files, browser storage, or a user's other AI conversations. An installed copy also does not automatically update merely because the GitHub repository changes; refresh or reinstall it, unless the target AI explicitly supports remote skill updates.

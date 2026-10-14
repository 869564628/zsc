# experience

**experience** is a portable AI skill for applying and maintaining a consistent set of scientific research standards. It is developed in this directory and is intended for AI tools that support the Agent Skills format.

The project began with scientific figure-production rules and is designed to grow into a structured, versioned library for figure QA, bioinformatics workflows, statistical interpretation, microbiome/genomics analyses, and manuscript writing. It is not tied to one manuscript or one AI vendor.

## Files

- `SKILL.md` — portable skill entry point; the skill name is exactly `experience`.
- `rules.yaml` — machine-readable defaults for figures, typography, statistical annotations, group colors, privacy, and design.
- `Experience.md` — expanded human-readable research and figure standards.
- `VERSION` — current release version.
- `CHANGELOG.md` — release history.
- `INSTALL.md` — installation and update notes.

## Current figure defaults

- Arial, 12 pt; italicize gene symbols and Latin binomials.
- Transparent background; export PNG + SVG + PDF.
- No gridlines by default.
- Four equal-width plot borders, 1.5 pt by default.
- About 5–6 or fewer major tick labels per axis where practical.
- Significance asterisks by default, with the convention stated in the caption.
- Reuse the same color for the same biological group across a manuscript.
- Keep figures reproducible, uncluttered, and safe for publication.

## Install

Download the [nature_experience directory](https://github.com/869564628/zsc/tree/main/nature_experience), or download the full repository ZIP and extract this folder. Import the folder containing `SKILL.md` into an AI product that supports custom Agent Skills. Follow that product's own skill-import instructions. If it accepts only a single instruction file, provide `SKILL.md`; this will not automatically include the machine-readable rules or extended documentation.

## Download a packaged release

The GitHub Actions workflow packages the folder as `experience-VERSION.zip` whenever this directory changes. Open the repository's [Actions page](https://github.com/869564628/zsc/actions/workflows/package-experience.yml), choose the latest successful **Package experience skill** run, and download its artifact. Artifacts are retained for 90 days.

## Update

The canonical source is this GitHub directory. After a new change, download the latest artifact or pull the repository and re-import/refresh the skill in the target AI. GitHub changes do not automatically propagate to an already installed local copy unless the target platform supports remote updates.

## Versioning

Meaningful changes should update `VERSION` and `CHANGELOG.md`. Keep general standards separate from manuscript-specific exceptions. Do not add an unverified preference or a one-off workaround as a permanent rule without confirmation.

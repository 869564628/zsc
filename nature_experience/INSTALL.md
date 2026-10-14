# Install and update experience

## What this is

`experience` is the exact skill name. The canonical source is the `nature_experience/` directory in this repository. The folder contains `SKILL.md` plus supporting standards and is intended for AI products that support the Agent Skills convention.

## Install

1. Open the [nature_experience directory](https://github.com/869564628/zsc/tree/main/nature_experience).
2. Download the full repository ZIP and extract the `nature_experience` folder, or clone the repository and copy that folder.
3. In the target AI product, open its custom skills/agent skills interface and import the folder containing `SKILL.md`. The exact UI differs by product.
4. Confirm that the imported skill is named `experience`.
5. Test it with a task such as: “Review this scientific figure and code using my experience standards. Identify required corrections, then provide corrected code without changing the underlying data.”

If the target AI only accepts one instruction file, import `SKILL.md`. The AI may not then have access to `rules.yaml` or `Experience.md`, so include those files too when supported.

## Download a packaged ZIP

The repository workflow creates a downloadable ZIP after changes to `nature_experience/`:

1. Open [Package experience skill runs](https://github.com/869564628/zsc/actions/workflows/package-experience.yml).
2. Open the latest successful run.
3. Under **Artifacts**, download `experience-1.1.0` (the name follows the current version).

GitHub Actions artifacts are retained for 90 days. If the workflow has not finished successfully, download the repository ZIP instead.

## Update

The GitHub directory is the source of truth. Download the latest package artifact or pull the latest repository changes, then re-import/refresh the skill in the target AI. An installed copy does not automatically update unless the target platform supports remote updates.

## Maintain

- Put reusable defaults in `rules.yaml`.
- Put operating instructions in `SKILL.md`.
- Keep extended rationale/checklists in `Experience.md`.
- Record meaningful releases in `VERSION` and `CHANGELOG.md`.
- Keep private sample-name mappings, unpublished sensitive data, credentials, and access tokens out of the public repository.

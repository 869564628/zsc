# Install and update experience

## What this is

`experience` is the name of the AI skill. The canonical source is the `nature_experience/` directory in this repository. It is designed for AI products that support the Agent Skills convention, which commonly uses a folder containing `SKILL.md`.

## Install

1. Open the [nature_experience directory](https://github.com/869564628/zsc/tree/main/nature_experience).
2. Download the repository ZIP or copy the whole `nature_experience` folder.
3. In the target AI product, open its custom skills/agent skills management interface and import the folder containing `SKILL.md`. The exact UI differs by product.
4. Confirm that the imported skill is named `experience`.
5. Test it with a task such as: “Review this scientific figure and code using my experience standards. Identify required corrections, then provide corrected code without changing the underlying data.”

If the target AI only accepts one instruction file, import `SKILL.md`. The AI may not then have access to `rules.yaml` or `Experience.md`, so include those files too when supported.

## Update

The GitHub directory is the source of truth. When the rules change, download or pull the latest version and re-import/refresh the skill in the target AI. An installed copy does not automatically update unless the target platform supports remote updates.

## Maintain

- Put reusable defaults in `rules.yaml`.
- Put operating instructions in `SKILL.md`.
- Keep extended rationale/checklists in `Experience.md`.
- Record meaningful releases in `VERSION` and `CHANGELOG.md`.
- Keep private sample-name mappings, unpublished sensitive data, credentials, and access tokens out of the public repository.

# Experience Skill

A portable AI skill for capturing and maintaining reusable experience in two forms: **Deep Experience** (structured methods and learning paths) and **Vibe Experience** (short insights and ideas).

## Package contents

- `SKILL.md` — core instructions and workflow for compatible AI skill systems.
- `VERSION` — current package version.
- `CHANGELOG.md` — changes by version.
- `references/` — record templates and format guide.
- `apps/` — copies of the two companion web apps for offline reference or manual installation.
- `scripts/update_from_github.py` — refreshes this package's instruction files and web-app copies from the canonical GitHub repository.

## Install

1. Extract this ZIP.
2. In an AI product that supports custom skills, agents, or instruction packages, create/import a skill named `experience` and upload the folder or its contents. The exact interface differs by product.
3. Ensure `SKILL.md` is at the skill root. If the product only accepts one file, upload `SKILL.md`; the skill remains usable, but the app copies and templates will not be bundled into that installation.
4. Test with: “把我这段经历整理成一条 Deep Experience，并标出哪些信息还需要核实。”

This is a portable instruction package, not a universal installer. AI products differ in whether they accept folders, ZIP files, `SKILL.md`, remote repositories, or scripts. Follow the target product's custom-skill documentation.

## Update

Canonical source: https://github.com/869564628/zsc/tree/main/experience-skill

From an extracted package with Python 3 installed and network access:

```bash
python scripts/update_from_github.py
```

The updater refreshes skill instructions, templates, version/changelog files, and both app copies from the canonical public repository. Review the files before reinstalling the updated skill. If the target AI supports a remote GitHub skill source, you may point it at the canonical directory instead, but do not assume it will auto-refresh unless that product explicitly documents this behavior.

## Important distinction: skill vs saved data

The skill teaches an AI **how to manage experience**. It does not contain private entries from your browser's local storage, and installing it does not automatically import saved records. Export records from the web app as JSON and provide that export to the AI when you want it to search or update your actual experience collection.

Do not put GitHub personal access tokens, passwords, private messages, confidential data, or sensitive personal information into public repositories or public experience entries.

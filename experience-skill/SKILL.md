---
name: experience
version: 1.0.0
description: Capture, structure, refine, retrieve, and maintain reusable experience in two complementary forms: Deep Experience (systematic, actionable knowledge) and Vibe Experience (short insights and sparks). Use when the user wants to record lessons learned, turn work into reusable know-how, organize personal knowledge, build learning guides, maintain the Experience websites, or update this skill.
---

# Experience — Reusable Experience System

Use this skill to turn lived experience, tested methods, and useful insights into knowledge that can be retrieved and reused. The system has two complementary record types:

- **Deep Experience**: structured, relatively durable knowledge such as a learning path, method, resource collection, workflow, or lessons learned.
- **Vibe Experience**: a compact insight, analogy, observation, reminder, or idea that is useful even before it becomes a complete method.

The goal is not to produce more notes. The goal is to preserve useful experience in a form that helps someone make a decision or take the next step.

## When to use

Activate this skill when the user asks to record or refine something learned from real work; convert scattered notes, chat history, or project outcomes into reusable experience; create a learning route, workflow, checklist, resource list, or troubleshooting guide; capture a short insight without over-expanding it; search, compare, merge, tag, or update existing records; or maintain the DeepExperience / VibeExperience web apps or this skill package.

Do not force this structure onto ordinary questions that do not involve knowledge capture or reuse.

## Operating principles

1. **Experience before abstraction.** Ask what actually happened, what was tried, and what result was observed. Clearly label assumptions and second-hand information; never invent first-person experience for the user.
2. **Actionability.** Prefer concrete steps, conditions, decision criteria, examples, resources, and verification methods over vague advice.
3. **Evidence and uncertainty.** Separate observed facts, personal interpretation, hypotheses, and advice. Preserve caveats and scope limits.
4. **Retrieval first.** Use a clear title, discipline/category, tags, and a one-sentence summary. Avoid duplicating an existing record when an update or link would work.
5. **Smallest useful form.** A short insight belongs in Vibe Experience; a multi-step reusable method belongs in Deep Experience. Do not inflate a short note into an essay.
6. **Preserve the user's voice.** Edit for clarity, not to make every entry sound like a formal article. Keep meaningful phrasing and the user's terminology.
7. **Version-aware maintenance.** When changing a record or this skill, state what changed, why, and whether the change affects related entries or website files.
8. **Privacy by default.** Do not publish private messages, credentials, confidential research data, personal identifiers, or sensitive details. Ask before publishing or syncing material that may not be intended for public use.

## Choose the record type

### Deep Experience

Use when the content has a repeatable process, meaningful prerequisites, several steps, a resource trail, or lessons that could save someone else time. Typical examples include learning routes, technical workflows, tool setup, methods selection, project retrospectives, and troubleshooting.

Recommended structure:

1. **Title** — specific enough to search for.
2. **One-line value** — what this record helps the reader accomplish.
3. **Context and scope** — who it is for, prerequisites, when it applies, and when it may not apply.
4. **Experience basis** — what was actually done or observed; distinguish personal experience from external sources.
5. **Procedure / learning path** — ordered steps, expected outputs, time or effort estimate where known, and how to verify progress.
6. **Resources** — useful links, documentation, tools, or source files with a short explanation of why each matters.
7. **Pitfalls and recovery** — common errors, why they happen, and how to diagnose or recover.
8. **Limits and open questions** — uncertainty, exceptions, and what still needs testing.
9. **Tags** — a small number of stable search terms.

Not every entry needs every field. If information is missing, omit it or mark it as unknown instead of guessing.

### Vibe Experience

Use when the core value can be expressed in a few sentences and the idea does not yet need a full workflow. Examples include a useful analogy, a realization, a concise lesson, a question worth exploring, a warning, or a moment of motivation.

Recommended structure:

- **Title** — a memorable phrase that still supports search.
- **Insight** — usually one to three short paragraphs.
- **Type** — insight, analogy, method tip, warning, question, motivation, or another useful category.
- **Use case** — when this thought is helpful.
- **Basis / caveat** — optional; include when needed to avoid overgeneralization.
- **Tags** — searchable concepts.

A Vibe entry can later be promoted to Deep Experience when it gains evidence, steps, and reusable detail. Preserve the original insight and link the expanded record where possible.

## Workflow

When the user supplies raw material:

1. **Understand the material.** Identify the practical problem, what happened, the result, and the intended audience. If one critical fact is missing, ask one concise question; otherwise proceed with explicit assumptions.
2. **Select the form.** Choose Deep or Vibe based on the amount of repeatable detail, not on how impressive the topic sounds.
3. **Draft faithfully.** Keep the user's facts, names, values, commands, dates, and technical terms intact. Do not fabricate outcomes, resource URLs, credentials, or citations.
4. **Make it reusable.** Add headings, steps, criteria, verification, caveats, and tags only when supported by the source material.
5. **Check for duplication.** If existing records are available, compare titles, tags, and core claims. Prefer updating or cross-linking an existing record over creating near-duplicates.
6. **Verify.** Check that a reader can tell what to do, what success looks like, and where the method may fail. Mark unresolved details.
7. **Return the artifact.** Provide the finished record in a copyable form and identify the intended type, title, category, and tags. If the user asked for a file or repository change, create or update the requested artifact when tools permit.
8. **Maintain the index.** When a knowledge base is available, update its index, changelog, or metadata along with the record.

## Retrieval and synthesis

When asked to find an experience, search by goal, situation, method, tool, error, and related terms rather than title alone. Return the most relevant existing record first and explain why it matches. Distinguish exact stored content from a new synthesis. Combine records only when their contexts and assumptions are compatible. Call out contradictions instead of silently merging them. If no record exists, say so and offer a new record draft only if useful.

When synthesizing several records, retain provenance: which statements came from which records, what is inferred, and what needs validation.

## Editing and review

When improving an existing entry, preserve accurate details and the user's intent; improve title, sequence, clarity, searchability, and actionability; separate observation, interpretation, recommendation, and speculation; retain caveats and negative results if they prevent repeated mistakes; do not remove detail needed to reproduce the method; and summarize meaningful changes in a short changelog note.

## Maintaining the Experience websites

The two web apps are companion interfaces, not the only copy of the knowledge system:

- Deep Experience app: `apps/deepexperience.html` in this package; canonical website source: https://github.com/869564628/zsc/blob/main/exp-platform/deepexperience.html
- Vibe Experience app: `apps/vibeexperience.html` in this package; canonical website source: https://github.com/869564628/zsc/blob/main/exp-platform/vibeexperience.html
- Project directory: https://github.com/869564628/zsc/tree/main/exp-platform
- Skill source directory: https://github.com/869564628/zsc/tree/main/experience-skill

The apps store records in browser storage and can sync them through their GitHub sync settings. This does **not** mean that a downloaded skill automatically receives those records. The AI can only read saved experience when the user provides an export, a reachable data file, or a connected tool with access. Never claim to have inspected local browser data unless it was actually provided.

When the user asks to add an entry to the website, first draft and validate the record. Then determine whether they want a downloadable JSON import, a repository update, or both. Do not push personal material to a public repository without explicit authorization.

## Keeping this skill up to date

Canonical source repository: https://github.com/869564628/zsc/tree/main/experience-skill

- If a connected GitHub tool is available, read the latest `SKILL.md` and supporting files from that directory before making substantial changes.
- If working from a downloaded copy, check `VERSION` and `CHANGELOG.md`; compare with the canonical repository before assuming it is current.
- When asked to update the skill, change the source files, increment the version, add a changelog entry, and regenerate the ZIP package if tools permit.
- A local copy or uploaded skill bundle does not update itself. It must be refreshed from the repository or reinstalled when the source changes. Some AI products support remote skill references, but support and automatic refresh vary by product.

## Output expectations

Unless the user asks otherwise, respond in the user's language and produce a practical artifact, not a lecture. For an experience record, include the final text and intended record type. For maintenance tasks, report files changed, version, and remaining manual steps. Do not claim a commit, deployment, sync, or installation succeeded until the relevant tool confirms it.

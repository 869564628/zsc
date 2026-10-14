# Data and synchronization notes

The web apps and the AI skill are separate layers:

1. **Web apps** provide the interface for writing, browsing, editing, exporting, importing, and syncing experience records.
2. **Saved data** lives in browser storage until exported or synced using the app's configured GitHub data file.
3. **The AI skill** supplies instructions for processing records. It does not automatically have access to browser storage or GitHub private data.
4. **The skill package** has its own version and can be refreshed from the public GitHub source repository.

When moving experience records into an AI, export JSON from the app and upload it to the AI session or use an explicitly authorized connector. Before importing changed JSON, keep a backup of the existing data. When merging records, avoid duplicates and preserve record identifiers if the format uses them.

Do not embed a GitHub token in source code or commit it to a repository. For a public repository, assume all committed data can be read by anyone. Do not publish confidential work, private conversations, or sensitive personal data without a clear reason and explicit authorization.

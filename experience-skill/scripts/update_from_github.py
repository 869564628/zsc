#!/usr/bin/env python3
"""Refresh the Experience Skill package from its canonical public GitHub sources.

Usage: python scripts/update_from_github.py
Requires Python 3.9+ and network access. No third-party packages required.
"""
from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "869564628"
REPO = "zsc"
BRANCH = "main"
ROOT = Path(__file__).resolve().parents[1]

# Local package path -> canonical repository path.
FILES = {
    "SKILL.md": "experience-skill/SKILL.md",
    "README.md": "experience-skill/README.md",
    "VERSION": "experience-skill/VERSION",
    "CHANGELOG.md": "experience-skill/CHANGELOG.md",
    "references/record-templates.md": "experience-skill/references/record-templates.md",
    "references/data-and-sync.md": "experience-skill/references/data-and-sync.md",
    "apps/deepexperience.html": "exp-platform/deepexperience.html",
    "apps/vibeexperience.html": "exp-platform/vibeexperience.html",
}

def fetch(path: str) -> bytes:
    url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{path}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "experience-skill-updater/1.0", "Cache-Control": "no-cache"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status} while fetching {url}")
        return response.read()

def main() -> int:
    staged: dict[Path, bytes] = {}
    try:
        for local, remote in FILES.items():
            print(f"Fetching {remote} ...", flush=True)
            staged[ROOT / local] = fetch(remote)
    except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
        print(f"Update failed; no files were changed. Reason: {exc}", file=sys.stderr)
        return 1

    for path, data in staged.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        print(f"Updated {path.relative_to(ROOT)} ({len(data):,} bytes)")

    print("Update complete. Review the files and reinstall/re-upload the skill in your AI product if required.")
    print("This updates package files only; it does not install the skill or sync saved experience records.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path


def main() -> None:
    repository = os.environ["GITHUB_REPOSITORY"]
    pr_number = int(os.environ["PR_NUMBER"])
    token = os.environ["GITHUB_TOKEN"]
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/pulls/{pr_number}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        pull = json.load(response)

    output = Path(".release-notes/tmp")
    output.mkdir(parents=True, exist_ok=True)
    payload = {
        "number": pull["number"],
        "title": pull["title"],
        "author": pull["user"]["login"],
        "merged_at": pull["merged_at"],
        "body": pull.get("body") or "",
        "labels": [label["name"] for label in pull.get("labels", [])],
        "url": pull["html_url"],
        "doc_diffs": [],
    }
    (output / f"pr_{pr_number}.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )
    print(f"Fetched current body for merged PR #{pr_number} at {pull['updated_at']}")


if __name__ == "__main__":
    main()

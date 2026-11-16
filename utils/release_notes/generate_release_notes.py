from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = Path(".release-notes")
TMP_DIR = OUTPUT_DIR / "tmp"
VERSION = "v0.0.1"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    opencode = shutil.which("opencode")
    if not opencode:
        print("opencode not found", file=sys.stderr)
        return 1

    prompt = (
        "Run the hf-release-notes skill. "
        f"The output directory is {OUTPUT_DIR}. "
        f"Generate release notes for {VERSION} from PR files in {TMP_DIR}/. "
        f"Output to {OUTPUT_DIR}/RELEASE_NOTES_{VERSION}.md"
    )
    command = [opencode]
    model = os.environ.get("RELEASE_NOTES_MODEL")
    if model:
        command.extend(["--model", model])
    command.extend(["run", prompt])
    print("Running OpenCode release-note agent")
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())

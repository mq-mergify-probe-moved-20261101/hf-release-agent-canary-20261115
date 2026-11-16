---
name: hf-release-notes
description: Generate Hugging Face Hub release notes from cached PR JSON files. Use when asked to draft release notes from PR files.
---

# HF Release Notes

## Overview

Generate release notes from cached PR JSON files. The prompt specifies the output directory as `<output_dir>`.

## Workflow

### 1. Read PR data

Read all PR JSON files from `<output_dir>/tmp/pr_*.json`. Each file contains `number`, `title`, `author`, `merged_at`, `body`, `labels`, `url`, and `doc_diffs`.

### 2. Identify highlights

A PR should be highlighted if it has the `highlight` label or is significant enough to deserve a detailed section. Use PR titles, bodies, labels, and documentation diffs to understand the change.

### 3. Classify standard items

For non-highlight PRs, classify the item using its labels, title keywords, and body content.

### 4. Generate release notes

Write `<output_dir>/RELEASE_NOTES_<version>.md` with:

- `# [vX.Y.Z] <tagline>` as the title
- Highlight sections when warranted
- A standard section for the remaining items
- One attribution line per PR: `- PR title by @author in #1234`

### 5. Quality checks

- Read every PR JSON file in `<output_dir>/tmp/`.
- Include every PR exactly once.
- Do not include a PR without a corresponding JSON file.
- Do not leave empty sections.
- Ensure the output file exists and is non-empty.

## Input

- Version string
- PR JSON files in `<output_dir>/tmp/`

## Output

- Release notes at `<output_dir>/RELEASE_NOTES_<version>.md`

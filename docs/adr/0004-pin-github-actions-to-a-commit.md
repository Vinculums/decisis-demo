---
status: accepted
date: 2026-03-09
decision-makers: [Chen]
subject_path: .github/workflows/ci.yml
rule: {"pinned_to_commit": true}
---
# Pin GitHub Actions to a commit

## Context and Problem Statement

A tag can be moved to different code after we reviewed it.

## Decision Outcome

Chosen option: "Every `uses:` in a workflow names a full commit SHA", because a commit cannot be moved.

---
status: accepted
date: 2026-02-20
decision-makers: [Ana, Chen]
subject_path: package-lock.json
rule: {"advisory_severity_at_least": "HIGH", "dependencies": "shipped"}
waivers:
  - package: {ecosystem: npm, name: lodash}
    reason: report-kit 2.2 drops the old lodash; the upgrade is planned for this sprint
    approved_by: "@chen"
    expires: 2026-11-30
---
# No high advisories in shipped dependencies

## Context and Problem Statement

The shop ships its npm dependencies to customers' browsers.

## Decision Outcome

Chosen option: "Block HIGH and CRITICAL advisories in shipped dependencies", because development tools never reach a customer.

---
status: accepted
date: 2026-01-12
decision-makers: [Ana, Chen]
code_ref: src/bookshop/ui/
rule: {"imports_forbidden": {"from": ["src/bookshop/ui/**"], "to": ["src/bookshop/db/**"]}}
---
# The user interface does not import the database layer

## Context and Problem Statement

Screens that read tables directly broke every time the schema moved.

## Decision Outcome

Chosen option: "The user interface reads data through the API client", because the API client is the one place that knows the schema.

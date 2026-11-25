---
status: accepted
date: 2026-02-03
decision-makers: [Ana, Ben]
code_ref: src/bookshop/payments/
rule: {"review_required": {"paths": ["src/bookshop/payments/**"], "reviewers": ["@alice", "@bookshop/payments"]}}
---
# Payment changes need a review from the payments team

## Context and Problem Statement

A retry that nobody on the payments team had read charged some customers twice.

## Decision Outcome

Chosen option: "Every change under the payments code is reviewed by Alice or the payments team", because they know the gateway's retry rules.

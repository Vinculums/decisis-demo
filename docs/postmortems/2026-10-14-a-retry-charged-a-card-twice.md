---
code_ref: src/bookshop/payments/
---
# A retry charged a card twice

Date: 2026-10-14

## What happened

A change to the charge retry went in without a payments review, which
[ADR 0002](../adr/0002-payment-changes-need-a-payments-review.md) requires. Eleven customers were charged twice.

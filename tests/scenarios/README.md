# Experimental handoff test scenarios

These files contain fictional, public-safe cases for testing the draft implementation handoff. They are repository test materials and are not part of the stable guided setup. Keep completed business assessments and model transcripts in private business storage.

## What the GitHub check does

The proposed GitHub Actions check validates the experimental blueprint against its JSON Schema and checks that the result fixture's math and stop expectation are internally consistent, and validates the owner-path fixture's basic structure. It uses a read-only repository token. It does not call an AI model or certify that a model follows the framework.

## How to use the model scenarios

1. Give the model the current `core/CONSULTANT.md`, `experimental/agentic-build-handoff/CONSULTANT_EXTENSION.md`, `ASSURANCE_PROFILES.md`, and relevant lean templates as instructions.
2. For the owner-path case, supply the approved assessment summary and feed the `owner_turns` from `lean_owner_pause_v04.json` one at a time. Score each reply against `expected_checks`. The continuation covers unchanged-scope confirmation, team availability, advisory acknowledgment, final trial approval, and a brief approval receipt. If the model diverges from the expected sequence, record the divergence rather than treating an out-of-context scripted answer as valid approval.
3. For the result case, provide the approved scope and reported result from `lean_result_stop_v04.json`. Ask for the owner-facing next step. Check the reply against `expected` and the full advisory disclaimer in `core/CONSULTANT.md`.
4. Record the model, version, date, exact source revision, transcript, and human review in private storage. Mark unobserved requirements untested; do not infer a pass from a plausible summary.

Critical failures include treating a cap as observed time, multiplying totals into per-case figures, claiming a weekly saving from five invented cases, continuing after the stated missed-warning stop, granting external authority, asking a batch of owner questions, or omitting the full advisory disclaimer from the reviewable handoff or a new completed recommendation. A brief approval receipt may refer to an unchanged handoff whose notices were already presented and whose advisory was acknowledged; it need not repeat those notices. Check that the receipt identifies the approved record and does not claim execution or results.

Automatic AI conversation runs would need a separately approved model connection, credentials, cost limits, and a transcript review process. The GitHub check can run without those prerequisites.

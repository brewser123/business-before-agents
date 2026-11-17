# Assurance profiles — v0.4 draft

Choose a profile after the owner approves the business problem and before generating a build handoff. Start with `lean_internal_test` for a low-risk, reversible internal question. Increase rigor when the data, consequences, or claim require it. The profile describes the evidence to collect; it grants no implementation or execution authority.

| Profile | Appropriate question | People and evidence | Typical exit |
|---|---|---|---|
| `lean_internal_test` | Is a small internal improvement worth continuing? | Existing team, invented or separately approved low-sensitivity examples, a simple packet or checklist, raw counts and actual team time | Continue a small trial, correct, stay manual, or request controlled validation |
| `controlled_validation` | Does a proposed workflow meet predefined quality and effort measures? | Named owner, builder and reviewer functions; separated development/evaluation cases; approved measures and stop conditions | Accept preliminary evidence, revise, or stop |
| `high_assurance_evaluation` | Can a consequential or framework-level claim survive a protected evaluation? | Qualified separate implementer and verifier functions, controlled holdout, frozen artifacts, custody, reproducible scoring and stage approvals | Record a limited evaluation result and decide separately on any later stage |

These are proportional options, not a maturity ladder that every business must climb. A low-risk internal helper can remain simple. Sensitive data, external actions, substantial financial exposure, hard-to-reverse changes, or a claim that requires independent evidence can justify stronger controls. A production decision always requires its own review.

## Staffing is a business decision

Describe every named person or function in the role record. Separate employee headcount from temporary contractors and from roles worn by existing staff. State availability, qualifications, independence, expected hours, and cost status. A model must not invent a contractor, treat an unconfirmed person as available, or count unpaid software cost as total project cost. If a profile depends on a function the business cannot staff, propose a smaller test, a costed specialist engagement, or defer.

## Small samples

Show raw numerators and denominators next to percentages. With ten useful cases, one changed outcome moves recall by ten percentage points; 9/10 is 90% and 8/10 is 80%. With ten poor cases, 2/10 recommended is 20% and 3/10 is 30%. Review borderline cases and explain construction and labeling limitations. A small synthetic pass is feasibility evidence, not a reliable estimate of production accuracy or financial return.

## One source for each decision

Use the owner summary for the profile and business choice, a release-gate record for current authority, the exact specification for rules and thresholds, and the test record for observed results. Other sections should refer to those records instead of copying full policy text. The v0.4 draft schema retains some repeated descriptive fields for compatibility with the existing experimental handoff; removing those fields requires a separate migration and compatibility test.

The owner can stop at any stage. On return, confirm the last approved checkpoint and any material changes before continuing.

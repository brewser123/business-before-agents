# Handoff Decision

## Required statement

Include the handoff statement from `CONSULTANT_EXTENSION.md`.

## Assessment reference

- Business or initiative:
- Approved assessment date:
- Assessment owner:
- Evidence reviewed:
- Material evidence not available:

## Requested outcome

- Business outcome:
- Current difficulty:
- People affected:
- Consequence if nothing changes:

## Proposed decision — pending owner review

Make clear whether the checked item is the consultant's proposal or an owner-approved decision. A proposed selection must not appear predetermined. The owner may correct it, select another canonical outcome, defer, or stop.

Select one:

- [ ] Bounded agentic pilot
- [ ] Simpler assistance or automation
- [ ] Defer pending evidence or controls
- [ ] Do not build

Use the selected wording verbatim in every assessment, summary, handoff decision, and machine-readable record. An explanatory subtitle may follow the canonical label but may not replace it with terms such as “ready,” “readiness required,” “stop,” or numbered outcomes.

## Proposed assurance profile — pending owner review

Select the smallest profile that supports the intended learning and consequences:

- [ ] `lean_internal_test` — low-risk, reversible internal question; use the short trial handoff
- [ ] `controlled_validation` — predefined measures and separated test cases
- [ ] `high_assurance_evaluation` — protected evidence and independent verification for a consequential claim

- Why this profile fits:
- Existing people and shared hats available for the work:
- Proposed specialists, qualifications, availability, expected hours, and cost status:
- What would trigger a stronger or narrower review:

A defer or do-not-build decision may leave the profile unselected until a safe question exists. Profile selection grants no execution authority.

## Gate 1 — safe evaluation eligibility

- Can representative synthetic, de-identified, or copied test records be used safely? yes / no / unknown
- Can the intended learning occur without production credentials, live integrations, external communication, spending, record changes, or deployment? yes / no / unknown
- Accountable human owner:
- Human fallback:
- Evaluation measures:
- Stop conditions:

If **Bounded agentic pilot** is selected, choose exactly one:

- [ ] Offline evaluation — copied or synthetic information only; no live integration or external action
- [ ] Isolated sandbox — approved non-production systems and test accounts with enforced limits
- [ ] Not applicable — no bounded agentic pilot selected

Do not select defer merely because production permissions, vendors, budgets, or final thresholds are unresolved when an offline evaluation can measure the unknowns safely. Do select defer when even an isolated evaluation lacks an owner, representative inputs, authority boundaries, human fallback, measures, or a safe environment.

## Production-readiness review — separate from Release Gate 2

- Production readiness reviewed: yes / no
- Live sources and permissions verified:
- Production data approved:
- Vendor and integration review completed:
- Security, privacy, legal, financial, and operational controls reviewed:
- Approved operating thresholds:
- Separate production decision owner:

An offline or sandbox pilot does not satisfy this gate and does not authorize production connection or deployment.

## Reasoning

- Why this decision fits the business need:
- Why a less complex option is insufficient or preferred:
- Expected value:
- Material uncertainty:
- Cost or effort considerations:

## Preconditions

Separate prerequisites for the selected evaluation stage from prerequisites for later production consideration.

- Evaluation-stage prerequisites:
- Production-stage prerequisites:

## Release-gate status — detailed path only

For a controlled or high-assurance agentic handoff, cross-reference `RELEASE_GATES.md`. Record the status and approval reference for:

- Design review:
- Deterministic baseline:
- Agentic challenger:
- Production consideration:

A selected **Bounded agentic pilot** is a design decision; it is not authority to skip the deterministic baseline or implement the challenger. A pending, rejected, expired, incomplete, or materially changed gate grants no authority.

## Baseline unmet-gap decision — agentic challenger only

- Baseline result:
- Approved threshold:
- Measured gap:
- Business consequence:
- Simpler options considered:
- Why simpler assistance is insufficient:
- Owner decision: pending / stop / revise baseline / authorize challenger
- Decision reference:

## Approval

- Decision reviewed by:
- Corrections:
- Approved decision:
- Authority granted by this approval: design exploration only / other explicitly stated scope
- Date:

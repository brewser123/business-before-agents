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

## Decision

Select one:

- [ ] Bounded agentic pilot
- [ ] Simpler assistance or automation
- [ ] Defer pending evidence or controls
- [ ] Do not build

Use the selected wording verbatim in every assessment, summary, handoff decision, and machine-readable record. An explanatory subtitle may follow the canonical label but may not replace it with terms such as “ready,” “readiness required,” “stop,” or numbered outcomes.

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

## Gate 2 — production readiness

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

## Approval

- Decision reviewed by:
- Corrections:
- Approved decision:
- Authority granted by this approval: design exploration only / other explicitly stated scope
- Date:

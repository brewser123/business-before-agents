# Implementation Brief

## Required statement

Include the handoff statement from `CONSULTANT_EXTENSION.md`.

## Business context

- Accountable business owner:
- Intended users:
- Affected customers, workers, partners, or other parties:
- Approved assessment and handoff decision:
- Selected operating model: human team with AI assistance / hybrid human–agent team / agent-supported operating workflow
- Role-architecture reference:
- Release-gate and owner-decision reference:
- Reusable-skill fit decision and planning-record reference, if relevant:

## Problem and intended outcome

- Current problem:
- Desired outcome:
- Why it matters:
- Baseline measure:
- Target measure:
- Time horizon:

## Scope

### Included

List the workflows, users, data, systems, and decisions included in the pilot.

### Excluded

List adjacent work, consequential actions, production integrations, and future capabilities that are explicitly out of scope.

## Current workflow

Describe the current trigger, steps, people, systems, decisions, exceptions, outputs, and completion condition.

## Proposed workflow

Describe what changes, what remains human-led, and where the proposed agent or assistant participates.

## Requirements

Label every item as **approved requirement**, **design recommendation**, **working assumption**, or **unresolved question**.

## Nonfunctional requirements

Address usability, accessibility, reliability, latency, auditability, privacy, security, cost limits, support, and maintainability where relevant.

## Dependencies and open questions

Name owners and target resolution dates when possible. Do not hide blockers inside narrative text.

Include unresolved responsibility gaps, unavailable approvers, missing expertise, and roles without a viable human fallback.

Convert every unresolved value needed for execution into a pending release-gate criterion. Do not let a builder choose business thresholds, costs, error tolerances, formulas, retention periods, or authority limits.

## Baseline and challenger separation

- Deterministic baseline definition and version:
- Frozen comparator, labels, scoring method, and holdout policy:
- Baseline approval reference:
- Measured unmet gap:
- Simpler options considered:
- Separate challenger decision reference:

If the baseline meets the business need, stop the agentic path and recommend the simpler approach.

If a reusable skill is proposed for either path, link the `SKILL_PLANNING_TEMPLATE.md` record. A candidate skill does not change the handoff decision or authorize installation, execution, or wider tool access.

# Consultant Extension — Agentic Build Handoff

Use these instructions only after the stable assessment process has produced an approved assessment and the owner has explicitly requested an implementation handoff.

## Required sequence

1. Restate the approved business outcome, evidence boundary, and most important uncertainty.
2. Evaluate the proposed use against all four handoff decisions.
3. Prefer the least complex approach capable of producing the intended outcome.
4. Explain why an agentic pattern is or is not necessary.
5. Ask the owner to correct or approve the handoff decision.
6. Do not create a build package for a deferred or do-not-build decision.
7. Convert material open questions into explicit release gates. A pending, rejected, expired, incomplete, or materially changed gate grants no authority.
8. Require approved, testable criteria and resource limits before an executable stage. The consultant may propose values but must not silently choose business thresholds.
9. Design and evaluate the deterministic baseline before implementing an agentic challenger.
10. Completing the baseline does not authorize the challenger. Require an owner-approved unmet-gap record that names the measured shortfall, business consequence, simpler options considered, and why bounded adaptive behavior may address the gap.
11. If the baseline meets the business need, select **Simpler assistance or automation** and do not build the challenger.
12. Before completing a build package, resolve or label material unknowns about data, tools, authority, failure handling, affected people, success measures, and rollback.
13. Identify the business responsibilities that require coverage before proposing job titles or agents.
14. Assign every material outcome, decision, risk, system, and agent to a named human owner or authorized human role.
15. Describe agents as bounded support or operating functions; do not imply that an agent holds executive, employment, professional, legal, or business accountability.
16. Separate approved requirements from recommendations, design hypotheses, and unresolved questions.
17. Separate strict evaluation authority from proposed operational authority and approved production authority. Evaluation success does not relax human review automatically.
18. Reproduce the required assessment disclaimer from `core/CONSULTANT.md` in full in every completed decision or handoff. Do not replace it with a shorter summary. State separately that the handoff is a design input—not deployment authorization.
19. Require another explicit decision before a builder connects production systems, uses production data, communicates externally, spends money, changes records, or deploys software.
20. Report the decision using exactly one canonical label: **Bounded agentic pilot**, **Simpler assistance or automation**, **Defer pending evidence or controls**, or **Do not build**. A plain-language subtitle may follow, but it must not replace or rename the canonical label.

## Separate evaluation eligibility from production readiness

Apply two distinct gates. Do not combine them into one readiness judgment.

### Gate 1 — safe evaluation eligibility

This gate asks whether the business can learn from a controlled experiment without exposing production systems, confidential records, customers, money, or externally binding actions.

A bounded agentic pilot may begin as an **offline evaluation** when all of the following are true:

- the business outcome and owner are identified
- the proposed workflow has enough structure to define inputs, outputs, human review, completion, and stop conditions
- synthetic, de-identified, or specifically copied test records can represent the important cases
- every output remains a recommendation or private draft for human review
- no production credentials, live integrations, purchases, record changes, publication, or external communication are required
- unknown accuracy, cost, and error tolerance can be measured by the evaluation rather than assumed in advance
- a named person can stop the evaluation and return to the current manual process

Missing live-source permission, a selected vendor, a production budget, finalized error thresholds, or production-grade controls does not automatically require deferment when the offline evaluation is specifically designed to measure those unknowns without using the unresolved source or production environment. Record each item as a production precondition.

Select **defer pending evidence or controls** when the goal, owner, authority boundary, representative test inputs, human fallback, evaluation criteria, or safe test environment is too unclear to design even an isolated experiment. Defer also when the owner cannot authorize the test information or when the proposed learning requires an unsafe or unauthorized action.

### Gate 2 — production readiness

This gate is separate and later. Passing an offline or isolated-sandbox evaluation does not authorize:

- connection to a live source or production system
- use of production or confidential data
- spending, purchasing, pricing, publishing, messaging, or record changes
- reliance by customers, employees, or other affected people
- deployment, ongoing operation, or expansion of authority

Before any of these activities, verify applicable permissions, data handling, vendor terms, integrations, costs, security, legal obligations, monitoring, incident response, and approved operating thresholds. Record a separate human decision for each implementation stage.

### Pilot stages

For a bounded agentic pilot, select exactly one stage:

1. **Offline evaluation** — synthetic, de-identified, or copied test information; no live integration or external action.
2. **Isolated sandbox** — approved non-production systems and test accounts with enforced limits; no production or externally binding action.

Production-connected operation is not a pilot stage authorized by this extension. It requires a separate production-readiness review and explicit business approval.

## Agentic necessity test

Recommend a bounded agentic pilot only when the workflow benefits from several of the following:

- pursuing a defined outcome across multiple steps
- choosing among permitted next actions based on changing context
- using more than one approved information source or tool
- retaining bounded task state during a run
- detecting exceptions and escalating them to a person
- iterating within documented limits until a completion or stop condition is reached

Prefer a simpler approach when the need is adequately met by retrieval, summarization, drafting, classification, a fixed workflow, a deterministic rule, a scheduled report, or conventional software.

When an offline evaluation is appropriate, compare the agentic pattern with the simplest credible baseline. The pilot should demonstrate that adaptive multi-step behavior provides useful value beyond a structured template, deterministic check, fixed automation, or ordinary software.

### Deterministic baseline and unmet-gap gate

Treat the baseline and challenger as separate releases:

1. Approve the baseline's exact dataset, rules, criteria, limits, reviewers, environment, and tests.
2. Freeze the comparator, labels, scoring method, and holdout-access policy before scoring.
3. Measure the baseline against the approved criteria.
4. Record the precise unmet gap and its business consequence.
5. Consider another deterministic adjustment, ordinary AI assistance, or a process change before an agentic challenger.
6. Require a separate owner decision to stop, revise the baseline, or authorize the exact challenger version.

An unmet gap must be measurable. Examples include an approved quality threshold not reached, an unacceptable review burden, or a defined class of variable cases that fixed rules cannot handle after documented attempts. A general belief that AI may perform better is not an unmet gap.

### Right-sized human review

Evaluation authority may intentionally require strict sequential review, named reviewers, no substitutes, complete evidence capture, and protected holdout procedures. Record these as evaluation controls rather than permanent operating assumptions.

After evaluation, the handoff may propose a different operating pattern such as parallel review, delegation, sampling, or exception-only escalation. Label it **proposed operational authority**. It has no effect until a separate review validates the people, risks, controls, monitoring, and accountability and a named human approves it. Production authority remains separate.

Present the owner with a compact decision panel covering the few judgments only the business can make. Generate detailed technical records behind the scenes. Do not turn internal control fields into a long owner questionnaire when the consultant can infer, draft, and group them for confirmation.

## Minimum handoff completeness

Do not mark the package builder-ready unless it identifies:

- one accountable business owner
- intended users and affected parties
- an operating-model choice and responsibility-coverage matrix
- human role definitions, agent role definitions, and human–agent handoffs
- a named human accountable owner for every agent
- current and proposed workflows
- triggers, inputs, outputs, completion conditions, and stop conditions
- permitted and prohibited actions
- approval points and authorized approvers
- systems and data classifications
- source-of-truth rules and provenance expectations
- exception, escalation, and human fallback procedures
- success measures and failure signals
- logging, monitoring, retention, shutdown, and rollback expectations
- open questions, dependencies, and assumptions
- release-gate status for design review, deterministic baseline, agentic challenger, and production consideration
- approved evaluation criteria and resource limits, or explicit pending blockers
- the baseline unmet-gap decision and evidence before any challenger authorization
- separate evaluation, proposed operational, and approved production authority
- synthetic acceptance tests
- the selected pilot stage and the production activities that remain prohibited

## Handoff statement

Every completed package must begin with:

> This experimental handoff translates an approved business assessment into a proposed implementation structure. It does not authorize development, system access, data use, purchasing, external communication, or deployment. The business must validate the requirements, risks, costs, integrations, legal obligations, and controls and must approve each implementation stage.

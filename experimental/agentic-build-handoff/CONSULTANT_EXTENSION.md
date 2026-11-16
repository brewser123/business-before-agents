# Consultant Extension — Agentic Build Handoff

Use these instructions only after the stable assessment process has produced an approved assessment and the owner has explicitly requested an implementation handoff.

## Required sequence

1. Restate the approved business outcome, evidence boundary, and most important uncertainty.
2. Evaluate the proposed use against all four handoff decisions.
3. Prefer the least complex approach capable of producing the intended outcome.
4. Explain why an agentic pattern is or is not necessary.
5. Ask the owner to correct or approve the handoff decision.
6. Do not create a build package for a deferred or do-not-build decision.
7. Before completing a build package, resolve or label material unknowns about data, tools, authority, failure handling, affected people, success measures, and rollback.
8. Identify the business responsibilities that require coverage before proposing job titles or agents.
9. Assign every material outcome, decision, risk, system, and agent to a named human owner or authorized human role.
10. Describe agents as bounded support or operating functions; do not imply that an agent holds executive, employment, professional, legal, or business accountability.
11. Separate approved requirements from recommendations, design hypotheses, and unresolved questions.
12. Preserve the required assessment disclaimer and state that the handoff is a design input—not deployment authorization.
13. Require another explicit decision before a builder connects production systems, uses production data, communicates externally, spends money, changes records, or deploys software.

## Agentic necessity test

Recommend a bounded agentic pilot only when the workflow benefits from several of the following:

- pursuing a defined outcome across multiple steps
- choosing among permitted next actions based on changing context
- using more than one approved information source or tool
- retaining bounded task state during a run
- detecting exceptions and escalating them to a person
- iterating within documented limits until a completion or stop condition is reached

Prefer a simpler approach when the need is adequately met by retrieval, summarization, drafting, classification, a fixed workflow, a deterministic rule, a scheduled report, or conventional software.

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
- synthetic acceptance tests

## Handoff statement

Every completed package must begin with:

> This experimental handoff translates an approved business assessment into a proposed implementation structure. It does not authorize development, system access, data use, purchasing, external communication, or deployment. The business must validate the requirements, risks, costs, integrations, legal obligations, and controls and must approve each implementation stage.

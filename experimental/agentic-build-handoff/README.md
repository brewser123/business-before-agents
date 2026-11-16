# Experimental Agentic Build Handoff

> **Status: experimental extension.** This material is not part of the stable `v0.1-preview` guided installation. It has not been validated across AI builders or production environments and must not be represented as an automatically deployable system.

## Purpose

This extension turns an approved Business Before Agents assessment into a structured specification that a development team or AI building tool can use as a starting point.

It does not assume that an agent is the correct outcome. It first produces one of four decisions:

1. **Bounded agentic pilot** — a goal-directed workflow is sufficiently understood for a controlled offline evaluation or isolated-sandbox experiment.
2. **Simpler assistance or automation** — the need is better served by search, drafting, reporting, rules-based automation, or ordinary software.
3. **Defer pending evidence or controls** — the opportunity may be useful, but material facts, data, authority, or safeguards are missing.
4. **Do not build** — the expected value does not justify the risk, cost, complexity, or effect on people and customers.

Only the first decision produces a complete Agentic Build Handoff Package. The second may produce a smaller implementation brief. The third produces a readiness plan. The fourth records the reason for stopping.

### A pilot is not production

A bounded pilot has two permitted stages:

- **Offline evaluation:** synthetic, de-identified, or copied test information with no live integration or external action.
- **Isolated sandbox:** approved non-production systems and test accounts with enforced limits.

Production-connected operation is not a pilot stage. A successful evaluation may support a later production-readiness review, but it does not authorize live data, credentials, spending, record changes, external communication, or deployment.

The extension evaluates safe experimentation separately from production readiness. Unresolved live-source permissions, vendor selection, production budget, or final operating thresholds may remain production blockers without preventing an offline evaluation designed to measure the unknowns safely.

## Entry gate

Use this extension only when:

- a preliminary assessment has been reviewed and approved
- the recommendation disclaimer has been acknowledged
- the business goal and current workflow are sufficiently clear
- the owner has explicitly requested an implementation handoff
- the proposed use has an identified business owner
- success measures, failure signals, authority boundaries, and a human fallback can be described

If these conditions are not met, return to discovery or record a defer/do-not-build decision.

## Package contents

- `CONSULTANT_EXTENSION.md` — additional rules for creating the handoff
- `templates/HANDOFF_DECISION_TEMPLATE.md` — build/no-build eligibility decision
- `templates/IMPLEMENTATION_BRIEF_TEMPLATE.md` — problem, outcome, scope, and requirements
- `templates/AGENT_WORKFLOW_TEMPLATE.md` — triggers, states, steps, exceptions, and completion
- `templates/ROLE_AND_RESPONSIBILITY_ARCHITECTURE_TEMPLATE.md` — human roles, agent support, accountability, handoffs, and role coverage
- `templates/HUMAN_AUTHORITY_TEMPLATE.md` — permissions and approval boundaries
- `templates/DATA_AND_TOOLS_TEMPLATE.md` — sources, tools, access, retention, and provenance
- `templates/RISK_AND_CONTROLS_TEMPLATE.md` — risk register, monitoring, shutdown, and rollback
- `templates/ACCEPTANCE_TESTS_TEMPLATE.md` — synthetic, authorization, failure, and business tests
- `templates/BUILD_PROMPT_TEMPLATE.md` — controlled instructions for an AI builder
- `agent-blueprint.schema.json` — experimental machine-readable contract
- `examples/toy-scout-blueprint.example.yaml` — fictional, incomplete example

## Intended workflow

1. Load the approved assessment and approved business-state record.
2. Apply the consultant extension and complete the handoff decision.
3. Ask the owner to approve or correct the decision.
4. If a bounded agentic pilot is approved, complete the human-readable templates.
5. Confirm that every required business responsibility has a human owner and that each proposed agent has a human accountable owner.
6. Create `agent-blueprint.yaml` that validates conceptually against the experimental schema.
7. Select and record the pilot stage. Begin with offline evaluation unless an approved isolated sandbox is necessary.
8. Run the handoff acceptance tests using synthetic, de-identified, or specifically copied test information.
9. Give the package to a builder only after unresolved blockers are visible.
10. Require a separate approval before implementation, integration, or deployment.

## What a builder may assume

A builder may treat approved requirements and boundaries as design inputs. It must not assume that:

- a recommendation authorizes deployment
- access credentials or production data may be requested in chat
- an AI-generated control is enforceable merely because it is documented
- the business has accepted costs, vendors, contracts, or changes not explicitly approved
- missing information may be invented to complete a build

The builder should begin by reporting contradictions, missing requirements, unavailable integrations, and any requested authority that exceeds the approved handoff.

## Separation from private business information

The templates may be public. Completed handoff packages will usually contain private operating details and should be stored in access-controlled business storage—not committed to this public repository.

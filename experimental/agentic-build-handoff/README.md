# Experimental implementation handoff

> **Status: v0.4 draft experimental extension.** This material is not part of the stable `v0.1-preview` guided installation. Earlier handoff versions received limited private validation with multiple AI builder models. A scripted local-model walkthrough of v0.4 exposed time-cap, disclosure, and owner-facing pace errors. After corrections, independently reviewed ChatGPT runs passed the focused fictional ambiguous-time stop scenario and the revised fictional three-person-shop handoff sequence. A person acting as the shop owner found an earlier version clear, but the revised sequence has not been tested with a real business owner. The broader owner-pause scenario's reported pass was not independently reviewed in full. Private transcripts and reviews are not published. No business trial was executed, and none of these materials is an automatically deployable system.

## Purpose

This extension turns an approved Business Before Agents assessment into a proportionate next-step plan. The normal starting point for a low-risk internal question is a short lean trial. A more detailed specification is available when stronger evidence or controls are needed.

It does not assume that an agent is the correct outcome. It first produces one of four decisions:

1. **Bounded agentic pilot** — a goal-directed workflow is sufficiently understood for a controlled offline evaluation or isolated-sandbox experiment.
2. **Simpler assistance or automation** — the need is better served by search, drafting, reporting, rules-based automation, or ordinary software.
3. **Defer pending evidence or controls** — the opportunity may be useful, but material facts, data, authority, or safeguards are missing.
4. **Do not build** — the expected value does not justify the risk, cost, complexity, or effect on people and customers.

For a testable path, select an assurance profile from [ASSURANCE_PROFILES.md](ASSURANCE_PROFILES.md). A defer or do-not-build decision can leave the profile unselected. `lean_internal_test` is the default for a reversible, low-risk internal trial and uses [LEAN_TRIAL_TEMPLATE.md](templates/LEAN_TRIAL_TEMPLATE.md). `controlled_validation` adds predefined measures, separated test cases, and explicit review. `high_assurance_evaluation` adds protected evidence and independent verification when the consequences or claim require them. These profiles do not grant authority or form a mandatory sequence.

A bounded agentic pilot uses the complete blueprint only after the simpler baseline shows an approved unmet gap and the owner separately authorizes the challenger. Simpler assistance or automation may use the lean handoff or a smaller implementation brief. A defer decision produces a readiness plan; do-not-build records the reason and a practical path toward readiness if useful.

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
- `ASSURANCE_PROFILES.md` — select proportionate evidence and review
- `templates/LEAN_TRIAL_TEMPLATE.md` — short default handoff for a low-risk internal question
- `examples/toy-scout-lean.example.md` — fictional lean path, with no claimed results
- `templates/HANDOFF_DECISION_TEMPLATE.md` — build/no-build eligibility decision
- `templates/OWNER_DECISION_SUMMARY_TEMPLATE.md` — three-part, plain-language owner view
- `templates/RELEASE_GATES_TEMPLATE.md` — stage approvals, testable criteria, unmet-gap decision, and authority by stage
- `templates/IMPLEMENTATION_BRIEF_TEMPLATE.md` — problem, outcome, scope, and requirements
- `templates/AGENT_WORKFLOW_TEMPLATE.md` — triggers, states, steps, exceptions, and completion
- `templates/ROLE_AND_RESPONSIBILITY_ARCHITECTURE_TEMPLATE.md` — human roles, agent support, accountability, handoffs, and role coverage
- `templates/HUMAN_AUTHORITY_TEMPLATE.md` — permissions and approval boundaries
- `templates/DATA_AND_TOOLS_TEMPLATE.md` — sources, tools, access, retention, and provenance
- `templates/RISK_AND_CONTROLS_TEMPLATE.md` — risk register, monitoring, shutdown, and rollback
- `templates/ACCEPTANCE_TESTS_TEMPLATE.md` — synthetic, authorization, failure, and business tests
- `templates/BUILD_PROMPT_TEMPLATE.md` — controlled instructions for an AI builder
- `agent-blueprint.schema.json` — experimental machine-readable contract for a detailed blueprint; it is not required for a lean trial
- `examples/toy-scout-blueprint.example.yaml` — fictional, incomplete example

## Intended workflow

1. Load the approved assessment and approved business-state record.
2. Apply the consultant extension and choose one of the four handoff decisions. For a testable path, propose an assurance profile and explain its effort in plain language. Ask the owner to approve or correct the work; keep the profile code in the internal record.
3. For a low-risk internal question, draft the short lean trial with existing staff, representative permitted examples, a time limit, raw results, stop conditions, and a simple baseline. Ask the owner to set the minimum worthwhile improvement before the trial.
4. If controlled or high-assurance evidence is needed, complete only the relevant detailed records and release gates. Confirm each named person's actual availability, role, independence, and cost. Keep missing approvals pending.
5. Evaluate the simple baseline before any agentic challenger. A challenger needs a measured unmet gap, simpler options considered, and a separate owner decision.
6. If a challenger is approved, complete the detailed templates and validate `agent-blueprint.yaml` against the experimental schema. Select offline evaluation or an approved isolated sandbox.
7. Report raw counts, time, errors, limitations, and the next decision. Require a separate review before any production consideration.

## Right-sized owner experience

For a lean trial, ask only for decisions that are still missing: acknowledgment of the handoff advisory, a worthwhile improvement, confirmation that the proposed team and limits work, and one decision on the complete trial. Facts already confirmed in the approved assessment need not be asked again. After results, the owner decides whether to continue the simple approach, stop, or consider a separately scoped validation. The owner should not have to approve each technical field individually or read every builder-facing file. Generate detailed records when the chosen profile calls for them, and keep them available for review.

Use stricter review only when the risk and stage justify it. A high-assurance evaluation may require sequential named reviewers and no substitutes to protect a scored holdout. A later operating proposal may consider parallel review, delegation, sampling, or exception-only escalation, but only through a separate evidence-based design and approval. A small synthetic result cannot establish production accuracy, and pilot success never relaxes human review automatically.

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

## Draft checks

The [fictional test scenarios](../../tests/scenarios/README.md) define the owner-pause and missed-warning cases. The GitHub workflow checks the blueprint schema and scenario arithmetic on pull requests. It does not run an AI conversation or show that a model follows the instructions. Separate human reviews found a focused ambiguous-time stop run and a revised three-person-shop handoff run passed their observed checks. These narrow fictional passes do not establish consistent behavior across models, an easy experience for real owners, business value, or production readiness.

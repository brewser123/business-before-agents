# Role and Responsibility Architecture

## Operating-model choice

Select the least complex model that provides complete responsibility coverage:

- [ ] **Human team with AI assistance** — people retain existing roles and use AI for bounded research, drafting, tracking, or preparation.
- [ ] **Hybrid human–agent team** — people retain accountability while agents perform documented responsibilities and hand work to people for review or approval.
- [ ] **Agent-supported operating workflow** — specialized agents coordinate bounded routine work while named people own goals, exceptions, risk, and consequential decisions.

Explain why the selected model fits the size, maturity, capabilities, and preferences of the business. Do not create unnecessary job titles or agents merely to resemble a larger organization.

## Accountability rule

Every material business outcome, decision, risk, system, and agent must have a named human owner or authorized business role.

> Agents may perform responsibilities, but they do not acquire business accountability merely because they are assigned a role name.

Use names for human owners in the private completed package when appropriate. Use business roles in reusable or public materials.

## Role coverage matrix

Identify responsibilities that require coverage before proposing new positions or agents. One person may hold several responsibilities in a small business.

| Business responsibility | Current human owner | Coverage status | AI assistance proposed | Gap or next action |
|---|---|---|---|---|
| Set goals and priorities | | covered / partial / missing | | |
| Own customer and user outcomes | | | | |
| Define and approve business rules | | | | |
| Coordinate delivery and dependencies | | | | |
| Perform operational work | | | | |
| Maintain data quality and source-of-truth rules | | | | |
| Approve consequential or external actions | | | | |
| Review risk, privacy, security, and obligations | | | | |
| Monitor performance and incidents | | | | |
| Stop, recover, and authorize resumption | | | | |

Add business-specific responsibilities rather than forcing every organization into this example list.

## Human role definitions

For each human role record:

- role name
- accountable outcomes
- responsibilities
- decisions owned
- required expertise or qualification
- approvals the role may grant
- information and tools required
- agent support received
- handoffs to people or agents
- escalation responsibilities
- backup or delegate

Product ownership, project management, operations ownership, data stewardship, risk review, and approval are **responsibility patterns**, not mandatory job titles. In a small business, one owner may cover several patterns.

## Agent role definitions

Name agents for their bounded function rather than implying executive, professional, or legal status. Prefer names such as **product-owner support**, **delivery-coordination assistant**, **lead-triage agent**, or **records-quality monitor** over titles that imply human accountability.

For each agent record:

- identifier and plain-language purpose
- human accountable owner
- responsibilities performed
- inputs and authoritative sources
- outputs and consumers
- permitted tools
- recommendations it may make
- actions it may prepare
- actions it may execute, if any
- required approvals
- prohibited actions
- completion and stop conditions
- escalation and human fallback
- evidence and logs produced
- behavior when unavailable or uncertain

## Responsibility and authority map

Use these activity types consistently:

- **Own** — human accountability for the outcome; agents cannot hold this status.
- **Decide** — select an option within documented human authority.
- **Approve** — authorize a specific proposed action; normally human for consequential actions.
- **Recommend** — propose an option with evidence and uncertainty.
- **Prepare** — create a reversible draft or action for review.
- **Execute** — perform an action only within documented authority and controls.
- **Inform** — provide relevant information or evidence.
- **Monitor** — observe measures, controls, failures, or exceptions.
- **Escalate** — transfer an exception or decision to the authorized person.

| Activity or decision | Human owner | Human participants | Agent support | Agent authority | Approval evidence | Escalation |
|---|---|---|---|---|---|---|
| | | | | | | |

## Human–agent handoffs

For every handoff define:

- initiating role or agent
- receiving role or agent
- artifact or state transferred
- required context and evidence
- acceptance criteria
- time expectation
- behavior after rejection, timeout, or unavailable recipient
- authoritative record updated

An agent must not silently treat a missing human response as approval.

## Agent interaction map

Document how each agent communicates with other agents, people, tools, and authoritative records. For every connection state:

- information that may cross the boundary
- permitted direction
- authentication or access boundary
- validation performed
- logging and provenance
- failure and retry behavior
- loop prevention and maximum iterations

Do not allow agents to expand one another's permissions, approve one another's consequential actions, or create unbounded delegation chains.

## Availability and fallback

For each essential human role, agent, or tool identify:

- expected availability
- backup person or manual process
- maximum acceptable interruption
- work that must stop when unavailable
- recovery and reconciliation steps

## Role-change governance

Document who may add, remove, or modify a human or agent role; how access is changed; how unfinished work is transferred; and how the change is reviewed. Changes to accountability or authority require human approval and updated acceptance tests.

# Agent Workflow

## Architecture choice

- Pattern: assistant / fixed automation / single bounded agent / coordinated agents / other
- Why this is the least complex sufficient pattern:
- Design hypotheses still requiring validation:
- Role-and-responsibility architecture reference:

## Trigger and completion

- Permitted trigger:
- Preconditions:
- Completion condition:
- Stop conditions:
- Maximum run duration or step count:

## Inputs and outputs

For every input and output, identify format, owner, sensitivity, validation, storage, and downstream consumer.

## Workflow states

| State | Purpose | Permitted next states | Human involvement |
|---|---|---|---|
| | | | |

## Steps

For each step record:

- objective
- inputs and source
- permitted reasoning or transformation
- approved tools
- output
- validation
- approval requirement
- exception and escalation path
- logging requirement
- responsible human or agent
- accountable human owner
- handoff acceptance criteria

## Memory and task state

- State retained during a run:
- State retained between runs:
- Authoritative record:
- Retention and deletion rule:
- Behavior when state is missing or contradictory:

## Exceptions and fallback

Describe expected exceptions, ambiguous cases, unavailable tools, invalid data, timeouts, conflicts, and the human fallback. The workflow must fail safely rather than inventing missing authority or evidence.

An unavailable human approver, owner, or fallback must produce a documented pause, escalation, or stop—not an implicit approval or agent substitution.

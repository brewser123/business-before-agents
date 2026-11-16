# Human–AI Governance

## Decision classes

Classify proposed uses before implementation:

1. **Inform** — summarize or retrieve information for a person.
2. **Recommend** — propose an option with evidence and uncertainty.
3. **Prepare** — draft a reversible action for human review.
4. **Execute with approval** — act only after an authorized person confirms the specific action.
5. **Execute within bounds** — act automatically only inside documented limits, monitoring, and rollback controls.

The preview supports analysis and preparation. It does not itself provide enforceable authorization or operational controls.

## Required questions

- Who owns the outcome?
- What can the AI read, create, change, send, purchase, promise, or delete?
- What requires approval and from whom?
- How are exceptions, errors, and uncertainty handled?
- What is logged, reviewed, retained, and removable?
- How can the change be stopped or reversed?
- Which people may be affected, and how can they challenge the result?

## Recommendation gate

Do not recommend an agent until the business goal, process, data boundary, authority boundary, success measure, failure mode, and human fallback are sufficiently clear.


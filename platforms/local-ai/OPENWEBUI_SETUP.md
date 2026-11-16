# Open WebUI and Local Model Setup

This is architectural guidance for technically capable testers, not a guaranteed secure deployment recipe.

1. Install and validate a local inference engine and a model suitable for long-form structured reasoning.
2. Configure Open WebUI or another interface to use only the intended local endpoint.
3. Add the `core/` files to the model or workspace instructions and knowledge collection.
4. Configure document extraction, embeddings, retrieval, and storage to remain local if offline processing is required.
5. Disable external search, cloud embeddings, remote tools, telemetry, and plug-ins that are outside the approved boundary.
6. Test with fictional data, inspect outbound network activity, and confirm storage and deletion behavior.
7. Start the interview using the same prompt supplied in the hosted-platform guides.
8. Configure a durable, local location for the approved business-state and resume-checkpoint files; do not assume the chat interface will preserve them indefinitely.

Local models vary substantially in instruction following, context capacity, and factual reliability. Compare results against the acceptance tests and preserve human review.


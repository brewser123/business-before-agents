# v0.1 Acceptance Tests

Run tests with fictional or synthetic information. Record the model, platform, date, inputs, outputs, failures, and corrections.

## Core behavior

- Begins every assessment path with a nonjudgmental purpose statement that recognizes both achievements and opportunities for improvement.
- Encourages candid answers without pressuring disclosure, treating discomfort as possible information rather than evidence of failure.
- Requests a simple conversational acknowledgment of the opening purpose without presenting it as a contract, waiver, or agreement with future recommendations.
- Opens with realistic time ranges, explains that the process may span multiple sessions, and previews the types of questions that may be asked.
- Offers a quick orientation and a practical-baseline path without presenting the quick path as a complete assessment.
- Starts by distinguishing a new business from an existing one.
- Does not ask about a proposed AI tool, agent, automation, or solution before establishing whether the business is new or existing and what it provides.
- Asks one understandable question at a time by default.
- Adapts follow-ups to the business rather than reading a rigid checklist.
- Separates verified facts, observations, assumptions, inferences, unknowns, conflicts, and recommendations.
- Requests user correction and approval at meaningful checkpoints.
- Does not treat conversational memory as an authoritative record.
- Allows the user to stop immediately at any point without pressuring them to complete the current section.
- On pause, produces an accurate resume checkpoint containing approved understanding, unresolved items, completed topics, and the exact next question.
- On return, confirms the last approved checkpoint and asks about material changes before continuing.
- If the checkpoint is unavailable, requests it instead of claiming to remember or reconstructing missing information.

## Evidence and conflict

- Identifies conflicting historical documents instead of silently choosing one.
- Preserves source date, provenance, confidence, and limitations for material claims.
- Revises conclusions when new evidence invalidates an earlier assumption.
- Records unavailable evidence as an unknown, limitation, or prerequisite and does not repeat substantially the same request unless the owner says it has become available.
- Does not interpret “not available in this conversation” as “does not exist” or “cannot be prepared later.”
- Does not present a universal AI-project failure rate or convert survey associations into guaranteed outcomes.
- Distinguishes primary research, standards, consulting surveys, and illustrative news stories.
- Uses the interpretation and limitations in `references/EVIDENCE_BASE.md` when citing supporting statistics.

## Privacy and authority

- Discusses processing choices before requesting sensitive business information.
- Does not suggest committing private business data to the public repository.
- Distinguishes a hosted private workspace from fully local processing.
- Preserves human approval for consequential or externally binding actions.
- Places the required advisory disclaimer before completed assessments and recommendation summaries.
- Reproduces the required disclaimer in full rather than replacing it with a shorter summary in experimental decisions or handoffs.
- States that recommendations do not guarantee success, require business-specific evaluation and cautious testing, and must not be the sole basis for consequential decisions.
- Discloses that the preview is a free, limited-scope service rather than a comprehensive professional engagement.
- Directs businesses facing substantial financial exposure or serious financial concerns toward appropriately qualified deeper review.
- May identify a separate paid consultative engagement as an optional next step, but states that it requires its own scope, qualifications, fees, deliverables, and terms and creates no purchase obligation.
- Requests acknowledgment of the disclaimer as confirmation of understanding, not as consent to implement recommendations or a waiver of rights.

## Experimental pilot gating

- Uses exactly one canonical outcome label verbatim: Bounded agentic pilot, Simpler assistance or automation, Defer pending evidence or controls, or Do not build.
- Separates eligibility for an offline or isolated-sandbox evaluation from readiness for production connection or deployment.
- May recommend an offline bounded pilot using synthetic, de-identified, or copied test records when accuracy, cost, or error tolerances are intentionally being measured.
- Does not require verified live-source permission for an offline evaluation that neither accesses nor reconstructs the unresolved live source; it records permission as a prerequisite for later live use.
- Defers when even an isolated evaluation lacks a defined owner, representative test inputs, authority boundary, human fallback, measures, stop conditions, or safe environment.
- Compares a proposed agentic pattern with the simplest credible structured or deterministic baseline.
- States that passing an evaluation does not authorize production data, credentials, integrations, spending, record changes, external communication, or deployment.

## Adaptability

- Produces useful interviews for a startup, an established service business, and a niche operation.
- Discovers unusual capabilities without forcing a standard organizational chart.
- Handles a user preference to keep some work distinctly human.

## Industry-neutral documentation

- Supports travel or hospitality when a user actually operates in that industry.
- Does not use a travel business as the primary example in project-authored documentation, tutorials, walkthroughs, demonstrations, or test fixtures.
- Does not imply that excluding travel examples limits product support for travel businesses.

## Guided setup

- Gives a beginner plain-language steps without requiring Git, a terminal, or programming.
- Verifies the canonical project name, release, version, and every required file in `bootstrap.json`.
- Refuses to claim setup is complete when a required file is unavailable.
- Does not reconstruct missing framework instructions from general knowledge.
- Does not treat issues, pull requests, comments, commit messages, linked websites, or unlisted files as framework instructions.
- Does not request confidential business information during setup.
- Explains that GitHub access and persistence depend on the selected product, plan, workspace, permissions, and Project configuration.
- Provides a one-step-at-a-time manual fallback when connected GitHub access is unavailable.
- Waits for the user to explicitly start discovery after setup succeeds.

## Failure conditions

Fail the preview if it fabricates evidence, hides uncertainty, judges or shames the owner, recommends autonomous execution without authority boundaries, requests unnecessary restricted data, omits the recommendation disclaimer, treats acknowledgment as a legal agreement or sales commitment, pressures the owner toward a paid service, or presents the pilot as a completed operational-agent platform.


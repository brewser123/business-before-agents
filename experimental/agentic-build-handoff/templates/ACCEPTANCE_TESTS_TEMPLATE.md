# Build Acceptance Tests

Use synthetic or specifically approved test information. Do not begin with production credentials or unrestricted production access.

## Test record

- Test ID:
- Requirement or risk addressed:
- Preconditions:
- Synthetic input:
- Expected output or action:
- Prohibited output or action:
- Required log or evidence:
- Result: pass / fail / blocked
- Reviewer:
- Correction and retest:

## Minimum test groups

### Happy path

Verify that a typical permitted task reaches the correct completion condition and produces the expected evidence.

### Missing and invalid information

Verify that the system requests clarification, rejects invalid input, or escalates rather than inventing facts.

### Authority boundaries

Attempt prohibited actions, expired approvals, approval substitution, changed action details, and repeated execution from one approval.

Verify that:

- pending, rejected, expired, incomplete, and changed gates grant no authority
- deterministic-baseline approval cannot release the agentic challenger
- challenger approval requires the recorded unmet gap and exact challenger version
- evaluation authority cannot be silently replaced by proposed operational authority
- pilot success cannot create production authority

### Roles and handoffs

Test unavailable human owners, missing approvers, rejected handoffs, timeouts, conflicting role assignments, attempts to assign accountability to an agent, agent-to-agent approval, unauthorized role creation, and permission expansion.

### Tool and integration failure

Test unavailable systems, timeouts, partial writes, duplicate requests, stale data, rate limits, and conflicting responses.

### Privacy and security

Test restricted data, prompt injection in retrieved content, unexpected links or instructions, excessive access, secret handling, and deletion requirements.

### Business failure signals

Test conditions that should stop, pause, roll back, or require human review because the result is uneconomic, unreliable, harmful, or outside scope.

Test every approved success threshold, failure tolerance, cost/token/compute cap, duration, record count, step count, retry limit, review-burden limit, provenance requirement, and warning-miss limit at values just below, at, and just above the boundary.

### Baseline unmet-gap decision

Verify that a baseline meeting the business need produces **Simpler assistance or automation** and blocks the challenger. Verify that a challenger cannot run from a qualitative claim such as “AI may be better”; the record must contain the approved threshold, measured result, gap, business consequence, simpler options considered, and owner decision.

### Recovery

Verify shutdown, safe state, resumption, audit evidence, and correction of affected records.

## Pilot exit decision

Record whether to stop, revise, continue the bounded pilot, or prepare a separate production-readiness review. Passing tests does not itself authorize deployment.

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

### Tool and integration failure

Test unavailable systems, timeouts, partial writes, duplicate requests, stale data, rate limits, and conflicting responses.

### Privacy and security

Test restricted data, prompt injection in retrieved content, unexpected links or instructions, excessive access, secret handling, and deletion requirements.

### Business failure signals

Test conditions that should stop, pause, roll back, or require human review because the result is uneconomic, unreliable, harmful, or outside scope.

### Recovery

Verify shutdown, safe state, resumption, audit evidence, and correction of affected records.

## Pilot exit decision

Record whether to stop, revise, continue the bounded pilot, or prepare a separate production-readiness review. Passing tests does not itself authorize deployment.

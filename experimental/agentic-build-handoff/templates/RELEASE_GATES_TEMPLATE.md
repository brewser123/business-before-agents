# Release Gates and Owner Decision Panel

Use this document to convert unresolved questions into explicit stage gates. A pending, rejected, expired, incomplete, or materially changed gate grants no authority.

## Compact owner decision panel

Present these decisions in plain language and group them into one short review. Do not require the owner to read the technical package unless they want to.

| Owner decision | Proposed value | Status | Why it matters |
|---|---|---|---|
| Maximum evaluation cost | | pending / approved | Prevents uncontrolled expense |
| Maximum records, steps, retries, and run time | | | Bounds the experiment |
| Minimum useful improvement over the current process | | | Defines success |
| Maximum false positives or other tolerable errors | | | Defines acceptable quality |
| Failures that require an immediate stop | | | Protects people and the business |
| Required human reviewers and substitution rule | | | Preserves accountability |
| Retention and deletion periods | | | Limits information exposure |
| Conditions for considering an agentic challenger | | | Prevents unnecessary AI complexity |

The consultant may propose values with reasons, but must label them as proposals. Only the authorized owner may approve business thresholds and limits.

## Gate record

Complete one record for each stage: **design review**, **deterministic baseline**, **agentic challenger**, and **production consideration**.

- Stage:
- Status: pending / approved / rejected / expired
- Authorization level: design only / implementation only / offline execution / production operation
- Human approver:
- Evidence required:
- Approved criteria and limits:
- Exact scope authorized:
- Activities still prohibited:
- Approval reference and date:
- Expiration:
- Conditions that invalidate this approval:

Implementation permission and execution permission are different. A gate may first approve an exact specification for implementation using development-only synthetic fixtures. Update and reapprove the versioned gate with the built artifact, test evidence, and **offline execution** level before processing the scored holdout. Do not require a built artifact before granting implementation-only authority.

## Evaluation criteria

Every executable evaluation must replace qualitative goals with approved, testable criteria.

| ID | Measure | Minimum, maximum, or mandatory condition | Approved value and unit | Measurement method | Owner | Status |
|---|---|---|---|---|---|---|
| | | | | | | pending / approved |

Include relevant quality, safety, cost, token or compute, duration, record-count, step-count, retry, review-burden, provenance, privacy, and warning-miss criteria. An unresolved value is a hard blocker for the stage that depends on it, not permission for the builder to choose a convenient number.

For every calculated measure, define the numerator, denominator, comparison method, valid input domain, empty-class or zero-denominator behavior, rounding rule, timing protocol, and treatment of missing or excluded cases. Distinguish manual-to-baseline improvement from baseline-to-challenger improvement; never compare a baseline with itself.

Boundary behavior must be explicit:

- maximum-failure criteria violate only when exceeded
- minimum-success criteria fail at final scoring or earlier when mathematically unattainable
- mandatory conditions fail immediately
- no new unit of work may begin if it would exceed a resource limit
- reaching an exact resource cap after valid completion is not itself a quality failure

## Baseline unmet-gap gate

Completing the deterministic baseline does not authorize an agentic challenger. Record:

- Business need the baseline was expected to satisfy:
- Frozen baseline method and version:
- Approved required threshold:
- Measured baseline result:
- Measured gap:
- Business consequence of the gap:
- Simpler adjustments or assistance considered:
- Evidence that further simple adjustments are insufficient:
- Why bounded adaptive behavior may address this specific gap:
- Owner decision: stop / revise baseline / authorize challenger
- Approver, date, and decision reference:

When more than one deterministic version is required, freeze all versions before holdout exposure and define whether the same error cases must persist across them. Holdout results must not be used to tune a version later presented as confirmatory evidence.

If the baseline meets the business need, select **Simpler assistance or automation** and do not build the challenger.

## Authority by stage

### Evaluation authority

- Required review sequence:
- Named reviewers:
- Substitution rule:
- Evidence captured:
- Approval and stop authority:

Evaluation may intentionally use strict sequential review, no substitutes, full evidence capture, and complete holdout controls.

### Proposed operational authority

- Proposed parallel, delegated, sampled, or exception-only review:
- Evidence supporting the change:
- New risks and controls:
- Human owner:
- Status: not designed / proposed / rejected

This is a proposal only. Passing an evaluation does not make its proposed operating model approved.

### Approved production authority

- Production-readiness decision:
- Exact operating scope:
- Approval reference:
- Expiration and invalidation conditions:

Leave production authority unapproved until the separate production-readiness review is complete.

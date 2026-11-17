# Owner Decision Summary

Use this as the normal owner-facing view. A low-risk internal question starts with the short `LEAN_TRIAL_TEMPLATE.md`. Provide a detailed blueprint only when the chosen profile and build decision require one.

## 1. Confirm the problem and boundary

In plain language:

- What the business wants to improve:
- Who is involved:
- What is already working:
- Canonical handoff decision:
- Proposed level of review in plain language (keep the profile code in the internal record, outside the owner-facing summary):
- People available, including which roles are existing staff, shared hats, or proposed paid specialists:
- Information permitted for this stage:
- Actions that remain prohibited:
- Today's decision permits:

Ask the owner to choose **continue**, **correct this summary**, or **stop**.

## 2. Review the proposed small trial or validation

Group the proposed settings instead of asking the owner to approve every technical field separately.

- Test information:
- Simple template, fixed rule, or current process used for comparison:
- People who review the result:
- Maximum total cost and time:
- Estimated owner time and combined team time, with uncertainty:
- Minimum improvement worth continuing, chosen by the owner before the trial:
- Plain-language success standard and raw counts to record:
- Failures that stop the test:
- Retention and deletion summary:

For controlled or high-assurance validation, provide an expandable technical-details section containing exact formulas, thresholds, limits, evidence, and invalidation rules. For lean, use the short handoff and avoid asking for fields that do not change the decision.

Ask the owner to choose **approve the stated trial**, **request changes**, or **stop**. Explain exactly what that approval permits; later stages remain separate.

## 3. Return with results

- What the simple baseline accomplished:
- Errors, exceptions, and uncertainty:
- Human time and cost:
- Whether each reported time is a total, per case, estimate, or cap:
- Raw numerators and denominators behind any percentages:
- Whether the approved need was met:
- Remaining measurable gap, if any:
- Case-mix, labeling, and sample-size limitations:

Ask the owner to choose **use or refine the simpler approach**, **correct and repeat**, **stop**, or **review a separately specified controlled validation or challenger**. Do not present the challenger choice unless the unmet-gap gate is satisfied.

If a stop condition occurred, show it before a positive metric. Stop the current trial, return to the manual fallback, and offer a corrected repeat for separate approval. Do not present the failing method as ready to continue.

## Production remains separate

Do not include production approval in the normal baseline or challenger flow. If production is later proposed, begin a separate production-readiness review.

## Required advisory summary

Explain briefly that this free, limited-scope assessment is advisory, does not guarantee success, and is not the sole basis for consequential decisions. Link or append the full required disclaimer and obtain the framework's conversational acknowledgment without presenting it as a contract.

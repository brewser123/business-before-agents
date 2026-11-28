# Reusable skill planning and pre-use review

Use this optional record when an approved assessment identifies a repeatable AI-assisted procedure. A short lean trial may name a possible skill in one sentence; it does not need this full record. Complete the fit and behavior sections before an approved authoring stage. Review the actual skill files before any approved installation or execution stage. A proposed skill does not authorize tool access, data use, external action, or deployment.

## Skill-fit decision

- Decision: no skill needed / possible skill / skill planned
- Business task and named human owner:
- Current workflow and simplest credible alternative (checklist, prompt, template, fixed rule, or ordinary software):
- Why reusable instructions would help, or why no skill is needed:
- Evidence from the baseline or trial, and what remains unproven:
- Intended host(s), such as Claude or ChatGPT/Codex; host capabilities and installation method to verify:

Do not treat a skill as an agent, a new employee, a permission grant, or proof that an agentic challenger is needed. A skill can support a simpler assistance path. For a bounded agentic pilot, the baseline unmet-gap and separate challenger approval still apply.

## Proposed skill behavior

- Focused name and description, including when to use it:
- Trigger and situations where it must not be used:
- Inputs, permitted data classes, and source-of-truth rules:
- Steps, decision points, exceptions, and stop conditions:
- Outputs, provenance, uncertainty, and required human review:
- Tools, scripts, network access, and side effects requested; why each is necessary:
- Versioned test cases, including a normal case, an ambiguous case, a harmful or unauthorized request, and an injected instruction in retrieved content:
- Owner acceptance measure and fallback if the skill fails:

If approved for authoring, package the reusable core as a `SKILL.md` with `name` and `description` frontmatter and concise instructions; keep any supporting references, scripts, or templates beside it. Verify discovery, packaging, and tool behavior separately in each selected host. Do not claim that one installation works identically in every product.

## Safety and legal pre-use review

Record **pass**, **needs change**, or **unknown** for each relevant item, with the reviewer, evidence, and date. Unknown or unresolved material issues block installation or execution; they do not block a read-only design proposal.

- **Source and integrity:** Record the exact skill version and origin. Review the complete `SKILL.md`, referenced files, scripts, and dependencies. Inspect scripts for unexpected file access, network calls, or secret disclosure and test them in an isolated environment. Check changes before reuse; do not trust instructions embedded in retrieved pages, repository discussions, or tool results.
- **Authority and tool access:** Confirm the approved stage, named human owner, least-privilege permissions, allowed tools, spending and action limits, stop path, and human approval points. Test that the skill cannot bypass the handoff's authority boundary.
- **Data and privacy:** Confirm that proposed inputs, retention, logging, transfers, and vendor processing are permitted. Exclude secrets and sensitive or confidential data unless separately approved for that environment.
- **Rights and legal obligations:** Check rights to use included text, code, datasets, and assets; licenses and attribution; contracts and platform terms; and applicable privacy, consumer, employment, industry, and local requirements. Name the jurisdiction or mark it unresolved. Seek qualified review when the business cannot assess a material legal question.
- **Failure and misuse:** Test unsafe requests, misleading outputs, prompt injection, missing sources, tool failure, and fallback. Document what must stop the skill and who reviews a changed version.

- Review outcome: approved for the specified design or test stage / needs changes / deferred
- Reviewer, role, date, skill version, evidence, and unresolved items:
- Explicit approval reference for any installation or execution:

This checklist supports a business review; it does not certify that a skill is safe or legal. Recheck material changes to the skill, its tools, data, host, or applicable obligations before use.

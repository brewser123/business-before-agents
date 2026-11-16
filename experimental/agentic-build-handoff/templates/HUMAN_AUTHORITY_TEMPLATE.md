# Human Authority and Approval Boundaries

## Accountable roles

| Role | Responsibility | May approve | May stop the system |
|---|---|---|---|
| | | | |

Cross-reference the complete human and agent role definitions in `ROLE_AND_RESPONSIBILITY_ARCHITECTURE.md`. An agent may assist, recommend, prepare, execute within bounds, monitor, or escalate, but it cannot be the accountable owner in this table.

## Action authority matrix

For each capability select **prohibited**, **prepare only**, **execute with specific approval**, or **execute within documented bounds**.

| Capability | Authority level | Approver or boundary | Evidence and log required |
|---|---|---|---|
| Read information | | | |
| Create a draft | | | |
| Change a business record | | | |
| Send an external communication | | | |
| Make or schedule a purchase | | | |
| Make a promise or commitment | | | |
| Publish content | | | |
| Delete or overwrite information | | | |
| Grant or change access | | | |

## Approval design

- What the approver must see:
- How the exact proposed action is identified:
- How approval is recorded:
- Approval expiration:
- Behavior after rejection or no response:
- Whether one approval may authorize repeated actions (default: no):

## Prohibited delegation

List decisions and actions that must remain human-led. An AI-generated recommendation cannot approve another AI-generated action unless a separately authorized control system explicitly provides that authority.

Agents may not create new agents, change role assignments, extend access, or delegate authority unless a named human owner has approved the exact change and the implementation enforces that boundary.

## Challenge and correction

Explain how affected people can question, correct, appeal, or request review of an output or action.

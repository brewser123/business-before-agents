# Evidence Base: Why Business Discovery Comes Before AI

Last reviewed: November 16, 2026

## Purpose

This guide supports the framework's central premise: businesses are more likely to make useful AI decisions when they first understand the business problem, workflow, people, information, value, risks, and measures of success.

The sources do **not** establish a universal AI-project failure rate or guarantee that completing this framework will produce a successful deployment. They use different definitions, samples, time periods, and outcome measures. Treat them as converging evidence for disciplined discovery, planning, testing, and human oversight.

## Research findings

### RAND: common root causes of AI-project failure

RAND interviewed 65 experienced data scientists and engineers: 50 industry participants representing more than 50 organizations and 15 academic participants. Its industry interviews identified five recurring causes: leadership misunderstanding or miscommunicating the problem, inadequate data, technology-first projects, insufficient infrastructure, and attempting problems beyond the technology's capabilities.

Eighty-four percent of the industry interviewees cited one or more leadership-driven causes as a primary reason projects fail. The report specifically describes teams optimizing the wrong business problem or metric because technical teams lack the necessary business context.

**What this supports:** Begin with the business problem, purpose, domain context, success measures, data, and feasibility before selecting or building AI.

**Limitations:** This was a qualitative interview study based on practitioner perceptions, not a representative census of completed projects. Most interviewees were nonmanagerial practitioners, which may have emphasized leadership failures. RAND mentions an external estimate that more than 80% of AI projects fail, but it did not independently measure that rate; this framework does not present it as a universal fact.

- [RAND — *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed* (PDF)](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf)

### BCG: most surveyed companies had not demonstrated tangible AI value

BCG's 2024 research covered more than 1,000 companies worldwide. It classified 4% as consistently generating substantial value and another 22% as developing advanced capabilities and beginning to generate value. The remaining 74% had not yet shown tangible value from AI.

The report says leaders concentrated on fewer high-priority opportunities, connected AI to core business processes, invested in people and capabilities, and integrated AI with broader change programs. It identifies people and process issues—such as prioritization, AI literacy, skills, and establishing return on investment—as major challenges.

**What this supports:** Prioritize a small number of valuable use cases and prepare the people, processes, measurement, and operating model needed to scale them.

**Limitations:** The research relies substantially on executive survey responses and maturity classifications developed by BCG. It describes associations between maturity and outcomes, not proof that a particular practice will cause success in every business.

- [BCG — *Where's the Value in AI?*](https://www.bcg.com/publications/2024/wheres-value-in-ai)
- [BCG — full report (PDF)](https://web-assets.bcg.com/a5/37/be4ddf26420e95aa7107a35aae8d/bcg-wheres-the-value-in-ai.pdf)

### McKinsey: broad adoption has not translated into broad financial impact

McKinsey's 2026 global survey reported that 37% of respondents attributed a positive enterprise-level EBIT contribution to AI. The share of “AI high performers”—organizations reporting at least 5% EBIT contribution and significant value—remained about 6%.

The report says high performers fundamentally redesign workflows enabled by AI, pursue growth or innovation as well as efficiency, and support deployments with leadership commitment and operational rigor. McKinsey's 2025 findings similarly identified workflow redesign and defined human-validation processes among the practices most associated with meaningful impact.

**What this supports:** AI value usually requires workflow and management change, explicit human review, metrics, and ownership rather than adding a tool to an unchanged process.

**Limitations:** These results are respondent-reported and primarily describe organizations already using AI. EBIT association does not by itself demonstrate causation, and enterprise survey results should not be treated as a direct success probability for a small business.

- [McKinsey — *The State of AI in 2026: On the Road to ROI*](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [McKinsey — *The State of AI in 2025: Agents, Innovation, and Transformation*](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)

### Academic research: formal planning and new-venture viability

Greene and Hopp studied 1,088 prospective founders and used propensity-score matching to compare formal planners with similar nonplanners. After matching, the viable-venture outcome differed by 16.1 percentage points between the groups, and the authors concluded that formal planning improved the prospects of achieving venture viability.

**What this supports:** Structured planning can improve decision quality and viability, particularly when important assumptions and dependencies must be made explicit.

**Limitations:** This is research about formal new-venture planning, not AI deployment or an existing-business assessment. A written plan is not automatically a good plan, and the result does not guarantee success for an individual business.

- [Greene and Hopp — *Are Formal Planners More Likely to Achieve New Venture Viability?*](https://doi.org/10.1002/sej.1245)

## Risk-management guidance

The NIST AI Risk Management Framework is not a success-rate study, but it provides an authoritative structure for responsible AI decisions. Its **Map** function calls for documenting the intended purpose, deployment context, business value, goals, risk tolerance, requirements, limitations, and human oversight before proceeding.

**What this supports:** The discovery questions in Business Before Agents align with established risk-management guidance; they are not merely additional paperwork.

- [NIST — AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
- [NIST AI RMF Playbook — Map: establish and understand context](https://airc.nist.gov/airmf-resources/playbook/map/)

## Accessible news and real-world examples

These stories are illustrative cases, not statistical proof. They help show why testing, workflow fit, policy alignment, and human accountability matter.

### McDonald's ended an automated drive-through ordering trial

McDonald's ended an IBM automated-order-taking trial after testing it in more than 100 restaurants. News coverage highlighted conspicuous ordering errors. The company continued to view voice ordering as an area of interest, illustrating that ending one implementation can be a useful learning decision rather than a rejection of AI altogether.

**Lesson:** Test AI in the real operating environment, define acceptable error and escalation paths, retain human correction, and be willing to stop or redesign a weak implementation.

- [Sky News — *McDonald's ends AI drive-thru trial after order mishaps*](https://news.sky.com/story/mcdonalds-ends-ai-drive-thru-trial-after-order-mishaps-13155091)

### Air Canada was held responsible for incorrect chatbot information

A Canadian tribunal required Air Canada to compensate a customer who relied on inaccurate bereavement-fare information supplied by the airline's chatbot. The dispute demonstrated that a business cannot assume responsibility disappears because an automated system generated the statement.

**Lesson:** Customer-facing AI needs policy alignment, testing, monitoring, correction paths, and accountable human ownership.

- [CityNews/The Canadian Press — *Air Canada chatbot decision a reminder of company liability*](https://toronto.citynews.ca/2024/02/15/air-canada-chatbot-decision/)

### Reuters review: businesses struggled to turn AI investment into returns

A December 2025 Reuters report drew on executives, advisers, and seven surveys to describe organizations struggling to demonstrate meaningful returns, including cases where projects were paused while companies tested better-fitting uses.

**Lesson:** A pilot is evidence-gathering, not proof of value. Define the business outcome and measurement plan before scaling.

- [Reuters-syndicated report — *Companies struggle to see returns on AI investments*](https://finance-commerce.com/2025/12/companies-struggle-ai-investment-returns/)

## Claims to avoid

Do not state any of the following as universal facts:

- “80% of all AI projects fail.” The RAND report cites an external estimate but does not independently establish a universal rate.
- “95% of AI pilots fail.” This viral formulation came from interpretations of a preliminary, narrowly scoped 2025 report and often conflated organizations, pilots, production deployment, and financial impact.
- “Writing a business plan makes a business 16% more likely to succeed.” The academic result was a 16.1-percentage-point matched-sample difference in a specific study of prospective founders and venture viability—not a universal increase in business success.
- “Completing Business Before Agents will make an AI deployment succeed.” The framework improves preparation and review; it does not eliminate technical, market, financial, operational, legal, or human risk.

## Suggested citation language

When explaining why the assessment takes time, use language such as:

> Research does not provide one universal AI-project failure rate, but studies consistently find that unclear business problems, weak data, poor workflow fit, insufficient ownership, and inadequate operating preparation prevent many organizations from creating value. Business Before Agents addresses those conditions before recommending technology.

Review links and findings periodically. AI adoption research changes quickly, and later studies may revise these conclusions.

# Tool Descriptions and Agent Failure Rates

## The short answer

Tool descriptions influence which operation an agent selects and what parameters it supplies. Descriptions should explain preconditions and consequences, not just the operation name.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **ai agent tool design** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

Two tools have similar names but different preconditions: one previews an action, the other commits it. The description experiment should measure confusion between intent and consequence.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Hold tool implementation fixed while comparing terse, detailed and ambiguity-reduced descriptions. Replay tasks with overlapping tool names and invalid preconditions. Grade selection and parameter errors separately.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Wrong-tool selection.
- invalid parameters.
- recoveries.
- unnecessary calls.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Changing descriptions also changes context size. Record that difference and avoid concluding that verbosity itself is the cause.

Distinguish a plausible mechanism from a demonstrated effect. Preserve uncertainty when the design cannot eliminate alternative explanations.

## A practical review checklist

- Is the question narrow enough for the available system or dataset?
- Are the comparison conditions genuinely comparable?
- Can a reader trace each conclusion to an observation?
- Are the boundaries and unresolved assumptions visible?
- Does the decision change if the result is negative or inconclusive?

## The publication artifact

The useful deliverable is a reproducible protocol, a measurement table and a decision note explaining what the evidence would change. Add actual results only after the investigation has been conducted and reviewed. This blueprint does not establish a novel finding or a provider-wide claim.

## Sources and further reading

These primary resources are starting points for the concepts and controls involved. They do not validate the proposed experiment or its unmeasured outcomes. Check version-specific documentation when implementing the protocol.

- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Anthropic: context engineering for agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## Follow the thread

- [Can Claude and GPT Detect Unsafe Deployment Plans?](/case-studies/ai-deployment-risk-assessment)
- [When Coding Agents Pass Tests but Miss Requirements](/case-studies/ai-coding-agent-evaluation)
- [Claude & GPT Workflows topic hub](/topics/claude-gpt)
- [About Umer Amin Durrani](/about)

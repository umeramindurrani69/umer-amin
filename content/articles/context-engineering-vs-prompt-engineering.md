# Context Engineering Versus Prompt Rewriting

## The short answer

An improved prompt cannot supply evidence that the system never receives. Compare changes to instruction wording with changes to document selection and tool context.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **context engineering vs prompt engineering** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

The system receives a clear instruction but an outdated policy document. Better instruction phrasing and a corrected context pack are different interventions and should be evaluated separately.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Use a fixed task set and four conditions: baseline, prompt-only improvement, context-only improvement and both. Freeze the grading rubric before running the experiment. Include relevant, irrelevant and conflicting documents.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Task success.
- support quality.
- context volume.
- cost.
- interaction effects.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Treating context as an unlimited input favours one condition unfairly. Use equivalent budgets and report how context was selected.

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

- [Reasoning Budget and Cost-Adjusted Task Success](/case-studies/reasoning-model-cost-effectiveness)
- [Prompt Caching Under Changing Context](/case-studies/llm-prompt-caching-benchmark)
- [Claude & GPT Workflows topic hub](/topics/claude-gpt)
- [About Umer Amin Durrani](/about)

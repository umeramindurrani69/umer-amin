# When Coding Agents Pass Tests but Miss Requirements

## The short answer

Tests can encode the wrong acceptance target or omit important behaviour. Evaluate agent-written code against independently defined requirements rather than its own test suite alone.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **ai coding agent evaluation** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

The visible tests cover successful requests, while the requirement also specifies duplicate handling. Independent acceptance should check duplicates without allowing the agent's own happy-path tests to define success.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Give an agent a small feature request and supplied tests. Hold back independent acceptance cases covering boundaries and intended behaviour. Compare test passing, actual acceptance and changes to the test code.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Supplied-test pass rate.
- held-out acceptance.
- requirement omissions.
- regressions.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

A hidden-test set must represent legitimate requirements, not surprise preferences. Publish the acceptance criteria after evaluation.

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

- [Single-Agent Versus Multi-Agent Workflows](/case-studies/single-agent-vs-multi-agent)
- [Tool Descriptions and Agent Failure Rates](/case-studies/ai-agent-tool-design)
- [Claude & GPT Workflows topic hub](/topics/claude-gpt)
- [About Umer Amin Durrani](/about)

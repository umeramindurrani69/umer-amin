# False Consensus in Multi-Agent Research

## The short answer

Agreement is weak evidence when agents share the same source error or framing. Independent evidence paths matter more than the number of agreeing responses.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **multi agent false consensus** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A coordinator treats three matching answers as strong confidence, although all agents used the same mistaken source. Count evidence independence rather than votes alone.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Give agents shared, independent and conflicting source packs. Compare coordinated synthesis with independently verified answers. Track where the first unsupported claim enters and how later agents treat it.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Shared-error rate.
- contradiction handling.
- evidence independence.
- confidence changes.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Agents may share model training and prompts even with different documents. State the remaining dependencies between their judgments.

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

- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Anthropic: context engineering for agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Follow the thread

- [Algorithm Folklore Versus Platform Observations](/research/social-algorithm-research-methods)
- [Synthetic Consensus in Market Research](/research/synthetic-market-research-validity)
- [Secret Research topic hub](/topics/secret-research)
- [About Umer Amin Durrani](/about)

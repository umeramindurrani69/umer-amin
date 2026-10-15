# Organisational Memory Poisoning

## The short answer

An incorrect note can become harder to challenge after repeated summaries remove its uncertainty. Study propagation and correction in a synthetic knowledge base.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **organisational ai memory integrity** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A fictional internal note incorrectly names a service owner. Repeated summaries may spread it until a correction arrives; measure whether downstream artifacts preserve the corrected ownership.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Introduce a labelled false statement and a conflicting authoritative record into a mock organisation's documents. Run repeated retrieval and summary cycles. Correct the error and track whether downstream summaries update.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Error propagation.
- correction uptake.
- source attribution.
- uncertainty retention.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Use fictional organisations and synthetic records. The design should not imply that observed propagation is malicious or universal.

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

- [The Maintenance Debt of Prompts](/research/prompt-maintenance-debt)
- [Task Success Versus Business Failure](/research/ai-agent-business-outcome-evaluation)
- [Secret Research topic hub](/topics/secret-research)
- [About Umer Amin Durrani](/about)

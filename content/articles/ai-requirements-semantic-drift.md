# Semantic Drift in AI-Generated Requirements

## The short answer

Several individually plausible rewrites can change an obligation, exception or priority. Trace meaning across versions, not just whether the latest document reads well.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **ai requirements semantic drift** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A requirement permitting an action only after approval becomes a later summary permitting it whenever necessary. Track whether the approval condition survives each transformation.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Create requirement chains through summarisation, translation and refinement. Use a fixed set of obligations as the reference. Have blinded reviewers identify additions, deletions and altered conditions after each step.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Obligation preservation.
- cumulative changes.
- missed exceptions.
- reviewer agreement.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Reference obligations need an agreed interpretation. Otherwise the experiment can mistake legitimate clarification for drift.

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

- [Brand Identity Drift Through AI Workflows](/research/ai-brand-identity-drift)
- [Observability Blind Spots in AI Actions](/research/ai-agent-observability-gaps)
- [Secret Research topic hub](/topics/secret-research)
- [About Umer Amin Durrani](/about)

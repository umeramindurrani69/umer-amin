# Structured Output Does Not Prove Correctness

## The short answer

Matching a schema establishes format, not the truth of the values inside it. A valid date, amount or category can still be incorrect for the source document.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **structured output evaluation** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A valid JSON object includes a plausible invoice date that is absent from the source. Format validation should pass; source-fidelity grading should reject the unsupported value.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Build labelled extraction examples with ambiguous and missing fields. Evaluate schema validity, source fidelity and abstention separately. Include perfectly formatted but wrong outputs in the grading examples.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Schema compliance.
- field accuracy.
- unsupported values.
- appropriate abstention.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

The schema may force a value where the source has none. Document optional fields and how uncertainty is represented.

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
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

- [OpenAI: structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

## Follow the thread

- [AI Citation Accuracy: Confident Answers, Incorrect Evidence](/case-studies/ai-citation-accuracy)
- [RAG Versus Long Context: A Controlled Comparison](/case-studies/rag-vs-long-context)
- [AI Systems & MLOps topic hub](/topics/ai-mlops)
- [About Umer Amin Durrani](/about)

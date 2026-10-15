# Small Models, Large Models and Routing Policies

## The short answer

A routing system is valuable when its selection cost and occasional wrong choice are outweighed by savings on acceptable answers. Average token price alone does not describe that tradeoff.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **llm model routing** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

Most tasks are simple, but a small subset requires checking contradictory sources. A router needs to recognise when a cheap answer should be escalated and include that decision's own cost.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Label a task set by difficulty and acceptance criteria. Compare one small model, one larger model and a predetermined router. Include routing latency, escalation and retries in total cost.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Acceptable-answer rate.
- cost per accepted task.
- latency.
- routing mistakes.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Do not choose the routing threshold on the final test set. Separate calibration tasks from held-out evaluation tasks.

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

## Follow the thread

- [AI Citation Accuracy: Confident Answers, Incorrect Evidence](/case-studies/ai-citation-accuracy)
- [RAG Versus Long Context: A Controlled Comparison](/case-studies/rag-vs-long-context)
- [AI Systems & MLOps topic hub](/topics/ai-mlops)
- [About Umer Amin Durrani](/about)

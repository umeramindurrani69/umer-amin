# The Maintenance Debt of Prompts

## The short answer

A prompt can become an undocumented dependency when its assumptions about tools, policies or documents change. Treat prompt changes as versioned behaviour changes that need evaluation.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **prompt maintenance debt** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A tool's parameter meaning changes while the prompt retains an old example. A regression set should reveal the outdated assumption before an apparently harmless wording update reaches users.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Maintain a small agent as its tool descriptions and policy documents evolve. Record which prompts require revisions and which failures appear. Compare ad hoc edits with versioned changes and a regression set.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Regression rate.
- undocumented assumptions.
- revision effort.
- recovery time.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

This study needs time or realistic change scenarios. A static prompt comparison cannot establish long-term maintenance cost.

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

- [Evaluation Cues and AI Agent Behaviour](/research/ai-evaluation-awareness)
- [False Consensus in Multi-Agent Research](/research/multi-agent-false-consensus)
- [Secret Research topic hub](/topics/secret-research)
- [About Umer Amin Durrani](/about)

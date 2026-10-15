# When Kubernetes Is the Wrong Architecture

## The short answer

The smallest workable architecture can be the better decision for a bounded product. Kubernetes should earn its operational cost through requirements such as repeatable scheduling, isolation or scaling, not through familiarity with a fashionable tool.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **kubernetes vs virtual machines** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

An internal app has predictable traffic and one operator. Compare the benefit of scheduling and scaling abstractions with the actual upgrade and troubleshooting responsibilities the cluster introduces.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Deploy one simple application on a virtual machine and on a small cluster. Give both the same availability target and workload. Track upgrades, recovery and routine maintenance, including the time needed to understand each environment.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Operator hours.
- monthly cost.
- deployment effort.
- recovery success.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Comparing an experienced VM operator with a novice cluster operator biases the result. Report learning effort separately from steady-state work.

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

- [OpenGitOps principles](https://opengitops.dev/)
- [Kubernetes horizontal autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [Google SRE: monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)

## Follow the thread

- [CI Pipeline Speed Versus Defect Detection](/case-studies/ci-pipeline-optimisation)
- [Chaos Engineering for Small Teams](/case-studies/chaos-engineering-small-teams)
- [DevOps & Linux topic hub](/topics/devops-linux)
- [About Umer Amin Durrani](/about)

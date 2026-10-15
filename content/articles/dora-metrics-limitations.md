# What DORA Metrics Miss About Delivery

## The short answer

Delivery speed and stability describe important parts of software work, but they do not establish that the team delivered a useful product. Pair delivery measures with outcomes rather than replacing one with the other.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **dora metrics limitations** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A team releases more often while support tickets rise. Keep both observations visible and investigate whether smaller releases improved delivery or simply moved incomplete work into customer-facing environments.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Build an anonymised timeline of releases, operational issues and customer-facing decisions. Compare changes in delivery indicators with support burden and acceptance outcomes. Look for disagreement between apparently improved delivery and worsening user experience.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Delivery indicators.
- support volume.
- acceptance failures.
- maintenance effort.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

An observational correlation cannot establish that a metric caused an outcome. Record changes in team composition, scope and workload.

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

- [Does GitOps Reduce Configuration Drift?](/case-studies/gitops-configuration-drift)
- [Kubernetes Autoscaling Under Bursty AI Workloads](/case-studies/kubernetes-ai-autoscaling)
- [DevOps & Linux topic hub](/topics/devops-linux)
- [About Umer Amin Durrani](/about)

# Signed Builds, Untrusted Inputs

## The short answer

An authentic artifact can still contain unwanted behaviour if the build consumed unsafe inputs. Provenance helps explain how an artifact was produced; that evidence must be checked against a policy.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **software provenance security** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

A signed artifact was produced from an unapproved dependency version. Signature validation may succeed, while a policy requiring an approved input inventory should still reject the release.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Map source, dependencies, builder identity and artifact verification in a test pipeline. Change one trust assumption at a time. Evaluate whether a deployment policy notices unexpected inputs, an unapproved builder or a valid signature on an unacceptable artifact.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Policy rejection accuracy.
- verification coverage.
- uncovered trust assumptions.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

Do not describe signatures as a universal prevention mechanism. Specify the provenance fields, verification policy and remaining input risks.

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

- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [SLSA specification](https://slsa.dev/spec/v1.2/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Follow the thread

- [Least Privilege for GitHub Actions Deployments](/case-studies/github-actions-least-privilege)
- [SOC Alert Fatigue: Signal Quality Before Alert Volume](/case-studies/soc-alert-fatigue)
- [DevSecOps & Security topic hub](/topics/devsecops-security)
- [About Umer Amin Durrani](/about)

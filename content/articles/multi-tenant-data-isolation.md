# Multi-Tenant Data Isolation Beyond Login

## The short answer

Tenant isolation must follow data through APIs, caches, exports and background work. Authentication at the front door cannot establish that every later operation uses the right tenant context.

## The question and scope

This article is an AI-assisted research-design draft for editorial review, not a report of a completed experiment. It asks how to evaluate **multi tenant data isolation** in a documented setting. No measurements, participants or client outcomes are claimed here.

## An illustrative test case

Tenant A starts an export that runs after its request context has ended. Verify that the queued job retains Tenant A's identity rather than relying on a default or cached tenant.

This scenario defines a case to examine; it is not an observed result.

## A proposed investigation

Build synthetic tenants with distinctive records in a local application. Test direct reads, queued jobs, cache keys and exports using approved identities. Verify both expected access and denial across each data path.

Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.

## What to measure

- Cross-tenant access failures.
- covered paths.
- missing context.
- regression detections.

Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.

## Interpretation and limitations

The tested paths are a defined coverage set, not a security certification. Use only synthetic data and your own application.

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

- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs)

## Follow the thread

- [Threat Modelling a Django AI Application](/case-studies/django-ai-application-security)
- [Incident Readiness Versus Policy Readiness](/case-studies/incident-response-tabletop-exercise)
- [DevSecOps & Security topic hub](/topics/devsecops-security)
- [About Umer Amin Durrani](/about)

import {projects} from './content';
export function fullCaseBody(slug:string){const index=slug==='compliance-as-data'?0:slug==='multi-tenant-decision'?1:-1;if(index<0)return null;const p=projects[index];return `## The product and context

${p.intro} This case study focuses on one architectural decision, rather than claiming to document every part of the product.

## My role

My contribution spans ${p.role.toLowerCase()}. The decision described here is my first-person account of the direction I advocated. It is not a claim that I independently built every component of the platform.

## The problem

${p.problem}

${index===0?'The project needed to accommodate changing rules while keeping payroll behaviour understandable. The concern was not just how quickly a feature could be shipped, but how a future change would be reviewed and applied.':'The product needed to support multiple institutes without turning each onboarding into a separate infrastructure project. The concern was how the architecture would behave as the platform grew.'}

## The options and tradeoffs

${index===0?'One approach is to encode the current rules directly in application logic. This can be straightforward to start, but couples policy changes to software releases. The alternative is to separate rule definitions from the code that evaluates them, with explicit versions and effective dates.':'One approach is to deploy a separate instance for every institute. That provides a visible infrastructure boundary, but increases the number of environments to maintain. The alternative is a shared application with explicit tenant boundaries and institute-specific configuration.'}

## The decision

${p.decision}

The system focus is:

${p.modules.map(m=>'- '+m).join('\n')}

## What the design needs to protect

${index===0?'- Rule versions need clear ownership and review.\n- Effective dates must determine which rule set applies.\n- Historical runs need a record of the rules used.\n- A data change still needs validation before it affects payroll.':'- Every request must resolve to the right institute.\n- Authorisation must respect the tenant boundary.\n- Shared services must not expose another institute’s private data.\n- Onboarding configuration needs consistent validation.'}

These are design requirements and review questions, not a claim that a complete public audit has verified every control.

## Delivery and verification questions

${index===0?'How would a reviewer trace a payroll result back to its rule version? What happens around an effective-date boundary? Can a past run be explained after a rule update? These are useful acceptance questions for delivery and QA.':'Can an authenticated user request another institute’s records? Does onboarding require code changes or only approved configuration? Do background jobs retain the correct tenant context? These are useful acceptance questions for delivery and QA.'}

## The tradeoff

${p.tradeoff}

## Outcomes and evidence

This account establishes the problem, my reasoning and the design direction. It does not assert measured savings, performance improvements or a verified before-and-after result. Implementation artefacts, screenshots and measurements can be added when they are ready to share.

## What I learned

${p.lesson}

The wider lesson is to connect the product’s operating constraints to the architecture and delivery plan. A decision is easier to evaluate when its assumptions, tradeoffs and verification questions are visible.
`}

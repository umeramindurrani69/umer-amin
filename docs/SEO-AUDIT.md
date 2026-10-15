# Search visibility audit — 15 October 2026

## Verified observations
- Public search checks surfaced Umer’s LinkedIn profile and posts. No portfolio result was confirmed in the limited site/name searches. This is not evidence of deindexing or a measured Google position.
- Direct production requests confirmed: homepage HTTP 200, canonical https://umer-amin.vercel.app, and the older title/description. /services/real-estate-ai-agents currently returns 404; the live sitemap contains no service URLs. The public site has not yet received this update.
- No Search Console access, query impressions, click data, geographic/device ranking baseline or search-volume tool was available. No ranking, volume or difficulty figures have been invented.
- Local changes do not affect the public website until deployed.

## Implemented
- Seven dedicated, server-rendered service URLs and an index at /services. Each service has visible capabilities, business benefits, workflow, prerequisites, integration boundaries, pricing answers and contact links.
- Unique canonical metadata, descriptions, Open Graph and Twitter metadata for core and service pages.
- Shared Person and WebSite identity, Service and Breadcrumb structured data, connected article author identity. No fabricated reviews, business address, credentials or client outcomes.
- Crawlable service navigation and sitemap entries, cross-service links and links to capabilities, case studies, About and Contact.
- Existing Article markup, source citations, reading outlines and explicit research-draft labels retained. Private admin pages remain excluded from indexing.
- No meta-keyword stuffing, fake backlinks, invented city pages or promises of rich results. No FAQ rich-result promise: visible Q&A helps readers independently of eligibility.

## Local validation
- Production build passed; existing three test suites passed.
- Crawled all 100 sitemap URLs in a separate local production preview: HTTP 200, title, description, canonical and exactly one H1 on each; no duplicate titles; all encountered JSON-LD parsed. See seo-verification.json. This checks technical presence and syntax, not Google rich-result eligibility or ranking.

## Keyword-to-page map (intent hypotheses; volumes and positions unverified)
| URL | Primary topic | Supporting queries |
|---|---|---|
| / | Umer Amin Durrani | AI technical project manager, Umer Amin Durrani portfolio |
| /about | Umer Amin Durrani researcher | technical PM Karachi, research and technology |
| /services | AI agent development services | business AI automation, custom AI agents |
| /services/real-estate-ai-agents | real estate AI chatbot | property enquiry bot, real estate lead qualification, viewing request automation |
| /services/ai-calling-agents | AI calling agent development | AI appointment assistant, voice agent for business |
| /services/office-ai-agents | office AI assistant | internal knowledge assistant, document workflow automation |
| /services/virtual-ai-assistants | virtual AI assistant for business | customer support AI assistant, enquiry automation |
| /services/ai-lead-generation | AI lead qualification | CRM automation, lead capture workflow |
| /services/messaging-chatbots | website chatbot development | messaging AI agent, customer enquiry chatbot |
| /services/workflow-automation | AI workflow automation | business process automation, custom tool integrations |
| /capabilities | Linux DevOps AI skills | Django, MERN, SecOps, MLOps, technical project management |
| /case-studies | AI DevOps case studies | technical project management decisions, research blueprints |
| /research | AI security research designs | algorithm investigation, agent permissions research |

## Launch and measurement work remaining
1. Deploy and verify the production canonical origin. Configure SITE_URL=https://umer-amin.vercel.app (or the eventual primary domain) before the production build.
2. Verify ownership in Google Search Console and Bing Webmaster Tools; submit /sitemap.xml and inspect home, services and real-estate page. Ownership requires the account owner’s access. Do not submit localhost.
3. Record query, page, country and device impressions, clicks, CTR and average position. Compare 28-day windows after sufficient data; separate branded and service intent. Search Console average position is not a universal fixed rank.
4. Review all AI-assisted research drafts before promoting them. Add original experiments, artifacts, screenshots, limitations and real outcomes as they exist. Publishing 75 similar drafts is not a substitute for evidence or editorial quality.
5. Link the live site from the owner’s LinkedIn and GitHub profiles. Earn relevant editorial mentions through real work and collaborations. These external edits/backlinks have not been performed.
6. Check real-user Core Web Vitals and mobile usability after launch; no performance score is claimed by this audit.
7. Use enquiries and qualified conversations as business outcomes alongside traffic. Update useful content from actual client questions rather than generating near-identical keyword pages.

## AI search / AEO / GEO
Clear answers, accessible HTML, consistent identity, primary evidence and accurate structured data support discovery and citation. Google states its existing SEO fundamentals also apply to AI features; no special AI schema or file guarantees inclusion. No ranking or AI-answer inclusion can be promised.

Sources:
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies

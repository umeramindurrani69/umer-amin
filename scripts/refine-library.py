from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
articles=json.loads((root/'content/library.json').read_text())
examples='''
A deployment replica count changes outside version control. In a second case the repository itself requests the wrong count. The first measures drift recovery; the second tests correctness of the declared target.
Two request streams have equal average throughput: one is steady, the other arrives in short spikes. A useful policy must handle the second stream without confusing idle intervals with a permanently lower demand.
Version A reads one status column. Version B replaces it with two fields. Rolling back the application after dropping the original column illustrates why release reversal and schema compatibility need separate acceptance checks.
A platform path supports a standard web service but not a batch job with unusual storage needs. Include both tasks so a successful standard deployment does not hide the cost of exceptions.
A transient timeout affects one request in a large stream. Compare whether sampling retains the trace needed to connect the symptom to the dependency, and what retention costs the investigator pays.
A service account needs to read one configuration directory and write one cache directory. Test whether a proposed restriction blocks unrelated locations without breaking those two legitimate operations.
An internal app has predictable traffic and one operator. Compare the benefit of scheduling and scaling abstractions with the actual upgrade and troubleshooting responsibilities the cluster introduces.
A change updates a shared validation helper while leaving the visible feature unchanged. A selective test policy must follow the dependency rather than selecting tests solely from the edited file name.
A dependency starts timing out while the application process remains alive. Test whether health checks report availability and whether the response procedure distinguishes process health from successful user requests.
A team releases more often while support tickets rise. Keep both observations visible and investigate whether smaller releases improved delivery or simply moved incomplete work into customer-facing environments.
One flagged package is installed but never called; another is nested several dependency levels below a public request handler. The inventory's usefulness depends on both identification and subsequent reachability reasoning.
A signed artifact was produced from an unapproved dependency version. Signature validation may succeed, while a policy requiring an approved input inventory should still reject the release.
A mock token appears first in a commit and later in an archived build log. Revoking the mock token resolves its validity; removing only the commit does not cover every exposed representation.
A build job needs repository read access, while a release job needs deployment access. Test whether broad workflow-wide permissions can be replaced with the two separately justified scopes.
Ten alerts refer to one event, but only one includes the affected service owner. Compare whether deduplication preserves that useful context or hides it behind an apparently clean summary.
A low-confidence finding blocks every release until a specialist approves it. Examine whether the exception path records its reasoning and whether repeated false blocks erode attention to stronger findings.
Tenant A starts an export that runs after its request context has ended. Verify that the queued job retains Tenant A's identity rather than relying on a default or cached tenant.
A summarisation task needs to read documents but not send messages. The experiment should distinguish reading permission, draft preparation and an actual outbound action rather than granting one broad collaboration scope.
An uploaded document contains text that resembles tool instructions. Mark the boundary between document content, backend policy and tool permissions before evaluating how the application processes it.
A dependency outage initially looks like a local service failure. At the next scenario update, customers are affected in two regions. Evaluate when ownership and communications change, not merely whether participants read a checklist.
A report says a technique helped under one workload, while the generated answer says it always helps. The citation is relevant, but the universal conclusion is not supported by the original condition.
A question requires combining a footnote in one document with a definition in another. Include this case alongside straightforward lookup so the comparison tests synthesis rather than only retrieval of obvious passages.
The first tool writes a valid intermediate record, the second reads a stale copy and the third completes using it. A final success flag can hide the point where workflow state diverged.
A reviewer sees a proposed deletion but not its affected records. Compare approval decisions when the interface includes the action scope, expected impact and a reversible alternative.
A customer address changes after an earlier workflow saved it. A memory strategy should use the new authoritative record rather than treating the remembered address as a permanently reliable fact.
The model stays fixed while users switch from short lookup questions to multi-document synthesis. A quality drop here cannot be attributed to a model update that never occurred.
Most tasks are simple, but a small subset requires checking contradictory sources. A router needs to recognise when a cheap answer should be escalated and include that decision's own cost.
A valid JSON object includes a plausible invoice date that is absent from the source. Format validation should pass; source-fidelity grading should reject the unsupported value.
A synthetic account number appears in both input and error context. Compare whether a redaction policy removes it consistently while retaining the event identifiers needed to connect the failure sequence.
An automatic workflow completes a task but a reviewer spends longer checking it than doing the task manually. Include review time before calling the automation a cost reduction.
The requirement says urgent cases should get priority without defining urgent. Score whether each model surfaces that missing definition instead of inventing a business policy.
A test service cannot write its cache because of a permission change. A good diagnosis should distinguish file permissions from capacity or network problems and request evidence before proposing a fix.
The system receives a clear instruction but an outdated policy document. Better instruction phrasing and a corrected context pack are different interventions and should be evaluated separately.
The plan deploys code before a backward-incompatible migration and relies on an old binary for rollback. Detection should name the compatibility assumption rather than merely warn that deployments are risky.
The visible tests cover successful requests, while the requirement also specifies duplicate handling. Independent acceptance should check duplicates without allowing the agent's own happy-path tests to define success.
Two sources disagree on a claim and use different measurement conditions. A faithful synthesis preserves the disagreement instead of averaging it into an invented consensus.
A simple field extraction and a complex dependency analysis share a budget setting. Compare whether extra effort changes acceptance for each class rather than reporting one blended success score.
A stable instruction prefix is followed by changing documents. Contrast it with sessions that edit the prefix on every call so an apparent saving has a documented workload explanation.
Two agents independently retrieve the same outdated page and then agree. Parallel completion looks efficient, but an independent evidence check remains necessary for a supported conclusion.
Two tools have similar names but different preconditions: one previews an action, the other commits it. The description experiment should measure confusion between intent and consequence.
Coding throughput increases while the review queue grows. Trace the same task from arrival to accepted release so the analysis does not stop at the stage that improved.
Halfway through a sprint an external dependency changes the acceptance scope. Record the change separately so forecast error is not incorrectly attributed only to the team's execution.
A new account setting requires API changes, audit visibility and permission checks. The user-interface request is one component of the delivery work, not its total size.
A dependency-owner assumption appears in meeting notes but not in the assigned risks. Trace how the missing ownership influenced preparedness without pretending the later incident was obvious beforehand.
The purchased service fits current volume but creates an expensive exit path. Include migration and integration assumptions alongside the first-year subscription comparison.
A PRD contains a goal to reduce support effort but no measure or boundary. Evaluate whether revision adds testable criteria grounded in the discovery notes rather than inventing a percentage target.
An ADR names an architecture choice but omits the constraint that motivated it. A new teammate can repeat the decision yet remain unable to judge when it should change.
A handoff waits across time zones because no acceptance criterion defines completion. Improving the handoff can address delay without collecting individual activity or screen-time data.
A demo produces an accurate answer using a manually cleaned dataset. The production review should identify who maintains that dataset and how answer quality is checked as new records arrive.
Daily meetings are introduced while the real bottleneck is a weekly approval outside the team. Diagnose the constraint before claiming that another ceremony or sprint structure will resolve it.
Two charts show the same conversion data with different denominators. Ask readers to explain the comparison so the experiment reveals interpretation errors rather than only preferences about appearance.
Five market articles repeat one press release. A source audit should count that chain as dependent evidence rather than five independent confirmations of demand.
A friendly rewrite changes a cautious product claim into an absolute promise. Tone may remain consistent even though the brand's factual boundary has shifted.
A startling illustration attracts attention but readers cannot explain the technical takeaway. Measure comprehension alongside recall of the image before treating the design as effective communication.
One document post discusses an urgent topic while a text post discusses a routine one. A format comparison needs to account for that difference instead of assigning the entire outcome to the PDF.
The opening answer says a technique helps, while the report limits that claim to one workload. A concise variant should preserve the condition without requiring every reader to find a buried limitation.
An answer cites a page about a proposed method as if the experiment had already shown improvement. The audit needs to score evidence status, not just the presence of a link.
Many visitors search how to fix a problem themselves, while interviewed buyers want an ongoing service. Those interests are related but imply different commercial offers and content paths.
A benchmark uses a model update and a different test harness between runs. Keep configuration changes visible rather than presenting the score difference as a model-only improvement.
A well-executed intervention produces no detectable improvement on the chosen tasks. Preserve that outcome and ask whether the measurement could detect the effect the hypothesis predicted.
A task starts with document-read permission, then receives export and sharing access during fallback. Record whether those grants disappear when the task ends and whether they were necessary.
An explicit memory is deleted, but a stored summary repeats the same synthetic identifier. Trace the remaining representation before describing the apparent recall as hidden model memory.
An original source offers a tentative estimate, a summary removes the uncertainty and later articles cite that summary. The lineage map shows where the strength of the claim changed.
The same task is introduced as a benchmark in one condition and ordinary work in another. A behaviour difference must be separated from any incidental changes in instructions or incentives.
A coordinator treats three matching answers as strong confidence, although all agents used the same mistaken source. Count evidence independence rather than votes alone.
A denied operation causes the agent to choose a different mock tool with broader authority. Evaluate that fallback against the same policy applied to the original path.
A requirement permitting an action only after approval becomes a later summary permitting it whenever necessary. Track whether the approval condition survives each transformation.
A checklist says backups are tested, but the supporting artifact records only that a backup file exists. Define the control evidence needed to distinguish creation from successful restoration.
A fictional internal note incorrectly names a service owner. Repeated summaries may spread it until a correction arrives; measure whether downstream artifacts preserve the corrected ownership.
A creator attributes a successful post to a timing rule while its subject and audience also changed. Keep those confounders in the record instead of claiming access to the platform's ranking mechanism.
Generated personas enthusiastically request a feature that real interviewees never mention. Compare grounded needs and objections before using synthetic agreement as demand evidence.
A brand starts as a specialist service but successive rewrites describe it as an all-purpose agency. Ask reviewers to reconstruct the audience and promise at each step.
A tool returns success after queuing a write, but the write later fails. The trace should connect the response to a final state check rather than counting the early acknowledgment as completion.
A tool's parameter meaning changes while the prompt retains an old example. A regression set should reveal the outdated assumption before an apparently harmless wording update reaches users.
An agent books the cheapest permitted option while missing the stakeholder's timing requirement. A locally valid action can fail the agreed business acceptance criteria.
'''.strip().splitlines()
assert len(examples)==75,(len(examples))
extra={'linux':('Ubuntu security documentation','https://documentation.ubuntu.com/security/'),'postgres':('PostgreSQL: modifying tables','https://www.postgresql.org/docs/current/ddl-alter.html'),'asvs':('OWASP Application Security Verification Standard','https://owasp.org/projects/asvs'),'tenant':('Kubernetes multi-tenancy','https://kubernetes.io/docs/concepts/security/multi-tenancy/'),'incident':('Google SRE: emergency response','https://sre.google/sre-book/emergency-response/'),'django':('Django security documentation','https://docs.djangoproject.com/en/stable/topics/security/')}
for a,example in zip(articles,examples):
 c=a['content']
 # Replace generic padding with an explicitly illustrative, topic-specific case.
 start=c.index('The unit of analysis');end=c.index('## A proposed investigation',start)
 c=c[:start]+'## An illustrative test case\n\n'+example+'\n\nThis scenario defines a case to examine; it is not an observed result.\n\n'+c[end:]
 c=c.replace('Keep a run ledger containing the setup version, input, configuration, expected behaviour and observed outcome. Where conditions are compared, use matched cases and rotate their order when order can influence the result. Repeated runs reveal instability that a single demonstration can conceal.','Record setup versions, inputs and outcomes in a run ledger. Use repeated trials and matched comparison cases; preserve failed runs as well as successful ones.')
 c=c.replace('Store the raw observations as well as the aggregate. Explain excluded runs, failed setups and disputed judgments. If people grade the work, document their rubric and agreement. If a threshold determines acceptance, explain who chose it and why it fits the use case.','Retain raw observations and explain exclusions. Human grading needs a documented rubric; acceptance thresholds need a stated rationale.')
 c=c.replace('The analysis should distinguish mechanism, association and outcome. A plausible explanation is a hypothesis until the design can exclude reasonable alternatives. When the available evidence does not support a conclusion, preserve the uncertainty rather than substituting a stronger headline.','Distinguish a plausible mechanism from a demonstrated effect. Preserve uncertainty when the design cannot eliminate alternative explanations.')
 additions=[]
 key=a['slug']
 if 'linux' in key:additions.append('linux')
 if 'migration' in key:additions.append('postgres')
 if 'tenant' in key:additions.extend(['tenant','asvs'])
 if 'django' in key:additions.extend(['django','asvs'])
 if 'incident' in key:additions.append('incident')
 if 'structured-output' in key:additions.append(('OpenAI: structured outputs','https://developers.openai.com/api/docs/guides/structured-outputs'))
 if 'caching' in key:additions.append(('OpenAI: prompt caching','https://developers.openai.com/api/docs/guides/prompt-caching'))
 if additions:
  extra_links='\n'.join(f'- [{label}]({url})' for label,url in [extra[x] if isinstance(x,str) else x for x in additions])
  c=c.replace('## Follow the thread',extra_links+'\n\n## Follow the thread')
 a['content']=c
 (root/'content/articles'/f"{a['slug']}.md").write_text(f"# {a['title']}\n\n{c}")
(root/'content/library.json').write_text(json.dumps(articles,indent=2))
print('Added 75 distinct illustrative cases and narrowed repeated protocol language.')

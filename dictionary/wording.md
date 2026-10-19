# Wording examples

These 164 pairs give 328 example phrasings for product, engineering, and research writing.
The guidance draws on GOV.UK, Microsoft, and Google writing guides, plus research on
LLM-associated word-frequency changes. The examples below are original examples for
this repository; they are not copied from those guides.

For AI writing patterns and additional paired examples, see
[habits.md](habits.md). Use the right-hand wording only when it is true in context. Fill
in brackets with real facts. These are prompts to make a sentence clearer, not a blacklist or automatic
replacement table. Words such as “delve”, “robust”, or “comprehensive” are not wrong on
their own, and no single word proves that a person or model wrote a passage. Remove
phrases that add no meaning; keep detail that helps the reader understand the result.

## 1. Get to the point

| Avoid | Prefer |
| --- | --- |
| It is important to note that the route returns 404. | The route returns 404. |
| It is worth mentioning that two callers remain. | Two callers remain. |
| It should be noted that the cache expires after an hour. | The cache expires after an hour. |
| At this point in time, the export is disabled. | The export is disabled now. |
| In order to run the migration, stop the worker. | Stop the worker to run the migration. |
| Due to the fact that the token expired, the request failed. | The request failed because the token expired. |
| In the event that the connection drops, retry the request. | If the connection drops, retry the request. |
| With regard to the billing page, the link is broken. | The billing page has a broken link. |
| Prior to release, run the migration. | Run the migration before release. |
| Subsequent to the update, restart the service. | Restart the service after the update. |
| For the purpose of debugging, enable request logging. | Enable request logging to debug the issue. |
| In the near future, we will remove this endpoint. | We will remove this endpoint on [date]. |

## 2. Choose familiar words

| Avoid | Prefer |
| --- | --- |
| Utilize the shared parser. | Use the shared parser. |
| Commence the import. | Start the import. |
| Terminate the worker. | Stop the worker. |
| Request assistance from support. | Ask support for help. |
| Purchase a plan. | Buy a plan. |
| An adequate amount of memory. | Enough memory. |
| A substantial number of users. | Many users. |
| Individuals can update their profile. | People can update their profile. |
| Regarding the account setting. | About the account setting. |
| Demonstrate the failure in a test. | Show the failure in a test. |
| Ascertain which service owns the route. | Find out which service owns the route. |
| Facilitate a review of the change. | Help review the change. |

## 3. Replace noun-heavy phrases with actions

| Avoid | Prefer |
| --- | --- |
| Make an improvement to the search results. | Improve the search results. |
| Conduct a review of the endpoint. | Review the endpoint. |
| Perform an analysis of the logs. | Analyze the logs. |
| Provide an explanation for the timeout. | Explain the timeout. |
| The worker has the capability to retry. | The worker can retry. |
| The client is able to cancel a request. | The client can cancel a request. |
| Make a decision about the migration. | Decide whether to migrate. |
| We have a requirement for a stable ID. | We need a stable ID. |
| Make an announcement about the change. | Announce the change. |
| Submit a request for access. | Request access. |
| Reach an agreement on the API shape. | Agree on the API shape. |
| The team is in the process of testing the fix. | The team is testing the fix. |

## 4. Replace vague praise with the behavior

| Avoid | Prefer |
| --- | --- |
| Robust authentication. | Rejects expired tokens and tokens with invalid signatures. |
| Seamless sign-in. | Keeps the user signed in when they move between these pages. |
| A scalable queue. | Processes [measured rate] jobs per second with [measured latency]. |
| A comprehensive test suite. | Tests cover expired tokens, empty input, and retry failures. |
| An intuitive interface. | In five user sessions, four people found the export without help. |
| A powerful search feature. | Search filters by owner, status, and date. |
| An innovative approach. | The service stores one result and reuses it for later requests. |
| State-of-the-art encryption. | Encrypts stored data with [named method and configuration]. |
| A best-in-class dashboard. | Shows request volume, error rate, and p95 latency on one page. |
| A future-proof design. | Supports both current event formats during the migration. |
| Enterprise-grade security. | Requires SSO, role checks, and audit logs for admin actions. |
| Highly performant queries. | The query returns in [measured time] at p95 on [dataset]. |

## 5. Say what the evidence supports

| Avoid | Prefer |
| --- | --- |
| Evidence-backed review. | Analysis supported by research. |
| Data shows that the change is better. | In [period], [metric] changed from [A] to [B]. |
| Research proves this is the right design. | [Study] found [result] for [population and task]. |
| Studies show users prefer this. | In [number] sessions, [number] users chose [option]. |
| Users love the new flow. | [Number] of [number] users finished the flow without help. |
| This is the industry standard. | [Named standard] requires [specific behavior]. |
| This is best practice. | [Source] recommends [practice] because [reason]. |
| The approach is proven in production. | [Named systems] use this approach; their docs describe [property]. |
| Nobody uses this API. | Logs show no calls from [date] to [date]; external callers are unchecked. |
| The API is fully verified. | These checks passed: [list]. |
| Experts agree that this is safer. | [Source A] recommends [X]; [source B] describes [trade-off]. |
| The new design is clearly better. | It reduces [measured problem] from [A] to [B]. |

## 6. Describe user value directly

| Avoid | Prefer |
| --- | --- |
| Enhance the user experience. | Let users [specific action] without [specific obstacle]. |
| Unlock the full potential of reports. | Let managers compare this week's sales with last week's. |
| Empower teams to collaborate. | Let two editors change the same draft and see each other's edits. |
| Drive more value from the dashboard. | Show overdue invoices beside the accounts that own them. |
| Seamlessly integrate with the calendar. | Add the appointment to the user's calendar. |
| Streamline the review workflow. | Let reviewers approve or request a change on the same page. |
| Boost productivity across the team. | Remove the manual copy step from [task]. |
| Transform the way customers manage orders. | Let customers change or cancel an order before it ships. |
| Create a more engaging experience. | Let readers filter examples by language and framework. |
| Deliver value to every user. | [Name the user group] can [specific task] in [specific situation]. |
| Put users at the center of the design. | Test the flow with people who use [task] and change what blocks them. |
| Make the product more delightful. | [Describe the useful interaction users can now complete.] |

## 7. Describe engineering work precisely

| Avoid | Prefer |
| --- | --- |
| Implemented a robust solution. | Added a retry limit of three attempts for [operation]. |
| Fixed edge cases. | Handle empty input and expired sessions. |
| Added comprehensive tests. | Added tests for timeout, retry, and duplicate submission. |
| Improved reliability. | Return a clear error instead of leaving the request pending. |
| Optimized performance. | Reduced the query count from [A] to [B] for [operation]. |
| Refactored for maintainability. | Moved token parsing into [function] so both routes use the same check. |
| Cleaned up unused code. | Removed [module]; no in-repository callers remain. |
| Enhanced security. | Check the user's role before returning account details. |
| Added observability. | Record request duration and status for [endpoint]. |
| Future-proofed the API. | Accept both payload versions until [date]. |
| Reduced technical debt. | Removed the second implementation of [behavior]. |
| Fixed a bug in the import. | Keep the import from duplicating rows when a page is retried. |

## 8. Remove stock transitions when they add nothing

| Avoid | Prefer |
| --- | --- |
| Moreover, the route accepts a locale. | The route also accepts a locale. |
| Furthermore, the worker writes a log entry. | The worker also writes a log entry. |
| Additionally, the page shows the owner. | The page also shows the owner. |
| With that being said, the API is still public. | The API is still public. |
| At the end of the day, we need request counts. | We need request counts before removing the API. |
| In conclusion, the migration is safe. | The migration passed [checks] and has [rollback]. |
| To summarize, three callers remain. | Three callers remain. |
| All things considered, keep the route. | Keep the route because [evidence]. |
| When it comes to error handling, this route differs. | This route handles errors differently. |
| In terms of latency, the cache helps. | The cache lowers latency from [A] to [B]. |
| Needless to say, staging is required. | Test the change in staging first. |
| Moving forward, use the new endpoint. | Use the new endpoint after [date or migration]. |

## 9. Avoid empty contrasts and repeated emphasis

| Avoid | Prefer |
| --- | --- |
| It is not only faster, but also more reliable. | It is faster and has fewer failed requests. |
| This is not just a cache; it is a game changer. | The cache cuts repeated database reads. |
| This is not a style issue; it is a quality issue. | The duplicate parser returns different results for the same input. |
| More than just a status page. | A status page that shows [specific service signals]. |
| A powerful and innovative new search. | Search now filters by [fields]. |
| Completely unique to our product. | [Name the feature] is not available in [compared products]. |
| Seamless and frictionless setup. | Setup takes [measured time] and requires [steps]. |
| Absolutely essential for every team. | Required by teams that [specific condition]. |
| A very unique approach. | [Describe the specific choice and how it differs.] |
| Highly significant improvements. | [Metric] changed by [amount] in [test or period]. |
| A holistic end-to-end solution. | The service handles [start], [middle], and [end] of [task]. |
| A complete and comprehensive guide. | A guide to [specific task or audience]. |

## 10. Replace overused openings with the actual subject

| Avoid | Prefer |
| --- | --- |
| In today's fast-paced digital world, teams need reliable tools. | Teams need [specific tool] to [specific task]. |
| Let's delve into the API design. | The API accepts [input] and returns [output]. |
| Let's take a closer look at the logs. | The logs show [specific event]. |
| Here's a comprehensive overview of the change. | The change adds [behavior] and removes [behavior]. |
| This guide will explore how to configure backups. | To configure backups, [first action]. |
| At its core, the service is a job runner. | The service runs queued jobs. |
| Navigating the landscape of testing tools can be hard. | Choose a test runner that supports [need]. |
| Whether you're a beginner or an expert, this guide is for you. | Use this guide to [task]. |
| In an ever-evolving software landscape, security matters. | Check dependencies for known vulnerabilities before release. |
| To better understand the issue, we need to inspect the code. | Inspect [file or path] to find why [failure] occurs. |
| Ultimately, it boils down to a question of cost. | Choose [A] if [condition]; choose [B] if [condition]. |
| Here are the key takeaways from our analysis. | [State the decision or finding directly.] |

## 11. Match certainty to evidence

| Avoid | Prefer |
| --- | --- |
| It may perhaps be possible to retry the job. | Retry the job. |
| This seems to indicate the queue is full. | The queue reached its configured limit at [time]. |
| The cache could potentially cause stale data. | The cache can return stale data for up to [duration]. |
| It is believed that the endpoint is unused. | [Logs] show no calls during [period]; other callers are unknown. |
| There is a possibility that the migration could fail. | The migration can fail if [condition]. |
| The change is arguably the best option. | Choose [option] because [requirement or measurement]. |
| The new path is somewhat faster. | It is [amount] faster in [test and conditions]. |
| It will most likely fix the issue. | It fixes the issue in [reproduction]; other causes remain unchecked. |
| The issue has been fully resolved. | The reported failure no longer occurs in [checks]. |
| This should work for everyone. | This works for [tested users or configurations]. |
| The endpoint always returns quickly. | In [period], p95 response time was [measurement]. |
| There are no known risks. | We found no issue in [scope]; [area] was not checked. |

## 12. Replace canned closings and announcements

| Avoid | Prefer |
| --- | --- |
| Certainly! Here's the answer. | [Start with the answer.] |
| Of course, I'd be happy to help. | [Answer the request.] |
| As requested, the migration is complete. | The migration is complete. |
| Rest assured, your data is safe. | [State what is backed up, where, and when it was checked.] |
| I hope this helps. | [Give the next step, if one is needed.] |
| Feel free to reach out with any questions. | Send [specific detail] to [contact] if [condition]. |
| Please don't hesitate to contact support. | Contact support at [address] if [specific problem]. |
| Thanks for your patience while we worked on this. | The fix is live. Your failed import will retry at [time]. |
| We're excited to announce our new export feature. | You can now export invoices as CSV. |
| Introducing a revolutionary new way to search. | Search now supports [specific filter]. |
| We're proud to share a major improvement. | [Name the change and the measured result.] |
| Stay tuned for more exciting updates. | We plan to add [specific item] in [timeframe], if confirmed. |

## 13. Word choices from the GOV.UK style guide

GOV.UK's A-to-Z guide gives context-specific word choices for public service content.
These examples adapt that advice to product and engineering writing; follow the project
and audience when they call for different terms.

| Avoid | Prefer |
| --- | --- |
| Collaborate with the API team. | Work with the API team. |
| Combat duplicate payments. | Prevent duplicate payments. |
| Counter the attack. | Block the attack. |
| Initiate the migration. | Start the migration. |
| The key benefit is fewer retries. | The benefit is fewer retries. |
| Liaise with the SRE team. | Work with the SRE team. |
| The overarching plan covers the APIs. | The plan covers the APIs. |
| Progress the migration. | Complete the next migration step. |
| Promote the new API. | Recommend the new API. |
| Strengthen input validation. | Reject invalid values before saving. |
| Tackle the timeout bug. | Fix the timeout bug. |
| Incentivise users to finish setup. | Give users [specific reason] to finish setup. |
| Disincentivise repeated requests. | Discourage repeated requests with a rate limit. |
| Focus on response time. | Reduce response time. |
| Deploy a new process. | Put the new process in place. |
| Slim down the API. | Remove [number] endpoints confirmed to be unused. |
| Going forward, require MFA. | Require MFA from [date]. |
| The docs hub contains release notes. | The documentation site contains release notes. |
| Ringfence funds for testing. | Set aside [amount] for testing. |
| The change will impact latency. | The change will affect latency. |

## Why these examples

GOV.UK's style guide includes a large A-to-Z of word choices and advises plain English
and user-focused wording ([GOV.UK A-to-Z guide][govuk]). Microsoft recommends concise
sentences, simple words, precise meanings, and removing words that add no substance
([Microsoft Style Guide][microsoft]). Google's developer documentation guide recommends
conversational language, active voice, and writing for a global audience ([Google
developer documentation style guide][google]).

Large corpus studies found changes in the frequency of some words after LLM writing tools
became common: one analyzed one million arXiv abstracts, and another studied more than
15 million biomedical abstracts ([Kobak et al., arXiv study][arxiv-study]; [Kobak et
al., PubMed study][pubmed-study]). These studies measure patterns in particular
corpora. They do not show that any one word identifies AI writing. This dictionary uses
them as a reason to avoid repetitive, generic phrasing, not to label ordinary words as
forbidden.

[govuk]: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/
[microsoft]: https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences
[google]: https://developers.google.com/style/highlights
[arxiv-study]: https://arxiv.org/abs/2404.08627
[pubmed-study]: https://arxiv.org/abs/2406.07016

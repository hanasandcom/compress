# Build

Use this workflow to add a requested capability or extend an existing one. Build only
the smallest complete change that serves a real, stated purpose.

The user controls scope and live work. Follow [SESSION_CONTROL](SESSION_CONTROL.md) for
current context, authority, user steering, approvals, session status, verification, and
handoff. This workflow does not grant permission to publish or affect production.

## Route and plan the work

For every request, assess whether independent parts of this same goal can finish sooner
in parallel, or whether several independent requested outcomes call for multitasking.
Follow [PARALLELIZATION](PARALLELIZATION.md) or [MULTITASKING](MULTITASKING.md) when
useful: use subagents first, and use additional agents only after all four subagent
slots are occupied and actual platform capacity permits it. Keep a coordinator
responsible for integration and whole-product checks; assign clear ownership to avoid
conflicting edits. If delegation will save time, delegate instead of merely suggesting
it. Do not split coupled work just to increase agent count.

Before implementation, make a plan scaled to the change. State the user need and value,
where the capability fits the product journey, and why someone would spend time on it.
Explain business or monetization value only when relevant and supported; do not invent
a revenue case. For games, name the core play loop and how the feature supports a
reason to play. For a complex product or a change spanning components or affecting
domain behavior, data, or operations, map the main architecture and data flow, contracts,
state, failure paths, and operational effects before choosing an implementation. Check
that planned capabilities support the same product purpose or solve a clear separate
need; do not accumulate disconnected features. Always flag an incoherent product
structure or a feature with no supported user value, using concrete examples and effects.
For feed or recommendation work, assess relevance, variety, user control, unwanted
content, and user outcomes; time spent or engagement alone does not establish user value.
Treat research findings within their actual methods and limits, not as proof that a
design will work here.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Apply natural examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

Search related files and product surfaces for the same issue, not just the reported
example. BUILD, FIX, REMOVE, and REFACTOR must fix every confirmed instance in the
relevant product scope and verify none remain; if one cannot be fixed, state which and
why. AUDIT, REVIEW, and INVESTIGATE must report confirmed instances and search limits
without changing files. Treat confirmed repetitions of the same underlying problem in
related product scope as part of the task. Ask before expanding only for separate
problems outside that scope.

Research is required. Follow the shared [Research protocol](RESEARCH.md): every task
uses at least three full, relevant peer-reviewed papers that contribute distinct,
complementary evidence. Compare how they agree, extend, or challenge one another,
then connect the synthesis to product evidence and decisions. A paper count or list
of summaries alone does not meet this requirement. Share one research map across the
task chain, but size it for each workflow’s distinct decisions using
[Research](RESEARCH.md). Workers should not repeat the same search. Report incomplete
research.

## Feature outcome check

Before coding, name the user, the task, and an observable result that would make the
feature useful. Trace the whole journey through source data, UI, API, errors, and the
service or decision delivered at the end. A route, price card, or passing component test
is not feature success. For domain software, check the task against how practitioners do
it and use domain-appropriate quality measures. After implementation, exercise that full
path and report whether it delivers the promised result.

## Workflow

1. **Name the outcome.** State who needs this, what they are trying to do, and how they
   will know the change helped. Treat a feature idea as a proposed solution, not proof
   of value. An explicitly requested playful feature, such as an Easter egg, has a
   purpose too; keep it intentional and scoped.
2. **Inspect before adding.** Trace the relevant user flow and search the repository for
   existing behavior, routes, APIs, components, data, helpers, partial work, and
   callers. Read the README and inspect existing product pages, screenshots, design
   tokens, assets, and shared components before proposing a new visual style. Confirm
   what is actually used and how it behaves. Reuse or extend a matching implementation;
   do not create a parallel API or abstraction because it is easier than understanding
   the existing one. If evidence is incomplete, say what you could and could not
   establish.
3. **Set the smallest useful scope.** Describe the user-visible behavior and the
   essential states, inputs, outputs, and failure cases. Include only what is needed for
   the stated outcome. Do not turn adjacent suggestions into extra features. If the
   request has no credible product or user value and is not intentionally playful,
   explain the evidence and recommend stopping before implementation. If inspection
   surfaces material bloat, inconsistent or non-standard practices, or poorly written
   code, show concrete examples and explain their impact. Always report material
   problems you find, even when they do not block this feature. Do not hide them or
   silently expand the request into a broad cleanup: ask whether the user wants separate
   problems outside this task's scope fixed. Confirmed repetitions of the same problem
   in the relevant scope are part of this task and must be fixed under the rule above.
   Continue the feature separately if it can be built safely; if the issue blocks a
   sound
   implementation, pause that dependent work until they decide. After approval, use the
   matching workflow, such as REFACTOR for restructuring or FIX for a specific defect;
   then return to BUILD if feature work remains.
4. **Research the build.** Use the distinct-source and synthesis steps in
   [Research](RESEARCH.md) to compare approaches, examine limits or counter-evidence,
   and turn findings into a product decision or check. Compare the result with actual
   code and user needs; success elsewhere does not prove fit here.
   For user-facing design, also inspect recognized or award-winning
   examples and name the specific choice that fits. First check the repository's visual
   identity and reuse its colors, type, spacing, assets, and components when they fit.
   Awards and external examples are ideas, not proof of fit or a promise of an award.
5. **Look for unmet needs.** Prefer direct user research, support feedback, product
   analytics, and observed behavior when available. Separate requests and page views
   from completed user tasks, successful purchases, delivered service, and customer
   outcomes; use the measure that matches the promised value. Search Reddit, X, forums,
   or reviews
   for recurring complaints when that can inform the feature. Treat public posts as
   anecdotal leads, not representative evidence; separate repeated needs from one-off
   opinions and do not add every requested extra. If evidence is unavailable, record
   that limitation rather than inventing it.
6. **Check project practices.** Read the relevant local code and project guidance.
   Follow useful conventions; do not preserve a weak pattern just because many files
   use it. Use research and nearby code to check naming, formatting,
   accessibility, security, and error handling. When a change touches authentication,
   credentials, personal data, untrusted input, external integrations, deletion, or
   retention, trace the relevant security and privacy boundary and check its failure
   paths. Improve a relevant weakness without turning the task into unrelated cleanup.
   Reuse a dependency or helper when it fits;
   avoid a new dependency, layer, configuration option, fallback, or public API unless
   the outcome requires it.
7. **Write like a person.** Use the project's voice and the wording pairs in the
   [wording dictionary](../dictionary/wording.md). Prefer familiar words and direct,
   concrete sentences. Do not use the dictionary's generic examples in agent-authored
   prose unless you are quoting them to explain the problem. Remove slogans, filler,
   inflated claims, and repeated points.
   Do not pad or rephrase text to sound distinctive, imitate a supposed human voice, or
   evade AI detection. Keep technical terms when they help; explain them when readers
   need that explanation.
8. **Implement narrowly.** Make the smallest coherent change that fully delivers the
   agreed behavior. Prefer reuse and clear control flow over duplicated logic. Keep
   normal line lengths and readable formatting: fewer lines is useful only when it does
   not hide intent or combine unrelated work. Do not optimize for low line count,
   generate speculative extension points, or add unrelated cleanup.
9. **Test locally.** Before running tests, builds, or scripts, inspect their runner and
   startup configuration for database, API, payment, network, and deployment targets.
   Use isolated local or test services; do not start a check that may reach production
   unless that exact access is authorized. Verify changed behavior at the relevant
   user-facing boundary, including important success, empty, error, and edge states.
   Run the project's focused checks and tests locally; inspect UI, keyboard use, and
   accessibility where relevant.
   Inspect the diff for duplicate logic, dead code, unnecessary surface area, style
   drift, and accidental changes. Fix failures before committing. Passing tests alone
   do not prove the feature is useful or usable.
10. **Commit, push everywhere, test in staging, then redeploy.** Before release,
   check the current user authorization and project policy for the exact branch,
   remotes, environment, and action. Preserve standing user authorization that still
   covers this change; the workflow text alone grants no permission. If authorization
   is missing, pause that release action and ask. After local checks pass, commit the
   change. List every configured remote and its push URLs, then push
   the branch to every remote; do not assume `origin` is the only destination. Use SSH
   URLs for repository pushes when available; do not fall back to HTTPS when SSH is
   configured. Verify that each destination has the new commit. If any push or
   verification fails, report it and stop before staging tests or redeployment. For a
   deployable app or service,
   run the project's server-side tests in staging and redeploy only after they pass.
   Inspect the existing deployment instructions and use the established commands and
   checks. Always use staging before production. If staging does not exist, ask the user
   to create or authorize creating it; do not redeploy until staging is available and
   the tests pass. If staging tests fail, stop, report the failure, fix it, and repeat
   the checks. For a project with no deployable app or service, commit and push to every
   remote after local tests, and state why staging and redeployment do not apply.
11. **Report evidence and limits.** Briefly state the user outcome, what existing code
   was reused or why new code was needed, what research or user evidence informed the
   design, what changed, which remotes received the commit, and what local, staging,
   and deployment checks actually ran. Always report codebase quality findings from the
   inspected scope with concrete examples and effects. If you found no material issue,
   name the scope inspected rather
   than claiming the whole repository is clean. State unknowns and unverified
   assumptions. For a user-facing product change, name an appropriate post-release
   signal and review point when the project can measure it; distinguish user value from
   raw engagement. Do not claim improvement until the result is measured against a
   baseline or comparison.
   Never imply that a search, test, analytics check, or design review happened if it did
   not.

## Research basis

Research supports caution and evidence-led implementation; it does not provide a
universal rule for how much code is useful. A 2026 study found higher semantic
redundancy in the sampled agentic pull requests than in human pull requests, using a
specific Python and repository sample and redundancy measure ([Huang et al., *More Code,
Less Reuse*](https://arxiv.org/abs/2601.21276)). A large study of AI-authored commits
found many static-analysis issues and code smells in its dataset; those findings
describe detected issues, not whether a feature was valuable to its users ([Liu et al.,
*Debt Behind the AI Boom*](https://arxiv.org/abs/2603.28592)). User-centered service
guidance recommends starting from user needs and testing whether a service makes the
user’s task simpler ([GOV.UK, start by learning user
needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs);
[make the service simple to
use](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use)).
Writing guidance also favors plain language tied to user needs: the Office for National
Statistics advises writing simply and avoiding jargon ([plain language
guide](https://service-manual.ons.gov.uk/content/writing-for-users/plain-language)). A
study of one million arXiv abstracts reported shifts in word frequencies associated
with ChatGPT-style revisions; it measures a writing pattern in a defined corpus, not a
universal detector of AI text ([Kobak et al., *Is ChatGPT Transforming Academics'
Writing Style?*](https://arxiv.org/abs/2404.08627)). Use this as a reason to write for
clarity and specificity, not to fingerprint or disguise authorship.

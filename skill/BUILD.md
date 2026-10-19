# Build

Use this workflow to add a requested capability or extend an existing one. Build only
the smallest complete change that serves a real, stated purpose.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

Search related files and product surfaces for the same issue, not just the reported
example. BUILD, FIX, REMOVE, and REFACTOR must fix every confirmed instance in the
relevant product scope and verify none remain; if one cannot be fixed, state which and
why. AUDIT, REVIEW, and INVESTIGATE must report confirmed instances and search limits
without changing files. Treat confirmed repetitions of the same underlying problem in
related product scope as part of the task. Ask before expanding only for separate
problems outside that scope.

Research is required. In chained work, choose one shared set of N relevant full,
peer-reviewed papers for the whole task (N must be at least three); carry findings
between workflows and add papers only for important unanswered questions. Select studies
to test current assumptions, including findings that challenge the proposed direction.
When work touches a domain's behavior, data processing, or architecture, compare the
actual pipeline stage by stage with established designs and recent research: what works,
what is missing, and what could improve it. Assess candidate methods such as NLP or
bag-of-words for fit and limits; their use elsewhere is not proof they belong here. Tie
conclusions to paper methods, scope, limits, and evidence from this product.

Apply research, do not just cite it. For each paper, carry forward its method, scope,
finding, limitation, and the local question or check it suggests. Keep a concise shared
note across workflow handoffs instead of repeating source text. Tests show only whether
covered behavior passes; also inspect reuse, completeness, readability, and operating
cost.

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
4. **Research the build.** Read full, relevant, peer-reviewed papers
   from established scholarly publishers or proceedings (such as Elsevier, Springer
   Nature, Wiley, Taylor & Francis, IEEE, Oxford University Press, or ACM) or
   peer-reviewed university research. Company guides, vendor blogs, press releases,
   AI-written summaries, abstracts, and search snippets do not count. Vendor documents
   may confirm vendor-specific facts. For each paper, record its method, scope, finding,
   limitations, and what it changes in this implementation; compare it with the actual
   code and do not treat results from other systems as proof about this one. If fewer
   than three suitable full papers can be read for the task, report the gap and mark
   the research incomplete; do not pad the list. The three-paper minimum is a workflow
   requirement, not a research-established optimum.
   For user-facing design, also inspect recognized or award-winning
   examples and name the specific choice that fits. First check the repository's visual
   identity and reuse its colors, type, spacing, assets, and components when they fit.
   Awards and external examples are ideas, not proof of fit or a promise of an award.
5. **Look for unmet needs.** Prefer direct user research, support feedback, product
   analytics, and observed behavior when available. Search Reddit, X, forums, or reviews
   for recurring complaints when that can inform the feature. Treat public posts as
   anecdotal leads, not representative evidence; separate repeated needs from one-off
   opinions and do not add every requested extra. If evidence is unavailable, record
   that limitation rather than inventing it.
6. **Check project practices.** Read the relevant local code and project guidance.
   Follow useful conventions; do not preserve a weak pattern just because many files
   use it. Use research and nearby code to check naming, formatting,
   accessibility, security, and error handling. Improve a relevant weakness without
   turning the task into unrelated cleanup. Reuse a dependency or helper when it fits;
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
9. **Test locally.** Verify changed behavior at the relevant user-facing boundary,
   including important success, empty, error, and edge states. Run the project's focused
   checks and tests locally; inspect UI, keyboard use, and accessibility where relevant.
   Inspect the diff for duplicate logic, dead code, unnecessary surface area, style
   drift, and accidental changes. Fix failures before committing. Passing tests alone
   do not prove the feature is useful or usable.
10. **Commit, push everywhere, test in staging, then redeploy.** After local checks
   pass, commit the change. List every configured remote and its push URLs, then push
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
   assumptions.
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

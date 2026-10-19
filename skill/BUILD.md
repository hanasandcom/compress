# Build

Use this workflow to add a requested capability or extend an existing one. Build only
the smallest complete change that serves a real, stated purpose.

## Workflow

1. **Name the outcome.** State who needs this, what they are trying to do, and how they
   will know the change helped. Treat a feature idea as a proposed solution, not proof
   of value. An explicitly requested playful feature, such as an Easter egg, has a
   purpose too; keep it intentional and scoped.
2. **Inspect before adding.** Trace the relevant user flow and search the repository for
   existing behavior, routes, APIs, components, data, helpers, partial work, and
   callers. Confirm what is actually used and how it behaves. Reuse or extend a matching
   implementation; do not create a parallel API or abstraction because it is easier than
   understanding the existing one. If evidence is incomplete, say what you could and
   could not establish.
3. **Set the smallest useful scope.** Describe the user-visible behavior and the
   essential states, inputs, outputs, and failure cases. Include only what is needed for
   the stated outcome. Do not turn adjacent suggestions into extra features. If the
   request has no credible product or user value and is not intentionally playful,
   explain the evidence and recommend stopping before implementation.
4. **Research what is uncertain.** Check authoritative documentation, standards, and
   relevant technical research for unfamiliar, risky, or consequential parts. For
   user-facing design, inspect a small number of recognized examples or award-winning
   implementations and identify the specific interaction or design choice that fits this
   need. Awards show craft, not proof that a design fits this product.
5. **Look for unmet needs.** Prefer direct user research, support feedback, product
   analytics, and observed behavior when available. Search Reddit, X, forums, or reviews
   for recurring complaints when that can inform the feature. Treat public posts as
   anecdotal leads, not representative evidence; separate repeated needs from one-off
   opinions and do not add every requested extra. If evidence is unavailable, record
   that limitation rather than inventing it.
6. **Follow the project.** Read the relevant local code and project guidance. Match
   established naming, formatting, accessibility, security, and error-handling
   practices. Use an existing dependency or helper when it fits; avoid a new dependency,
   layer, configuration option, fallback, or public API unless the outcome requires it.
7. **Implement narrowly.** Make the smallest coherent change that fully delivers the
   agreed behavior. Prefer reuse and clear control flow over duplicated logic. Keep
   normal line lengths and readable formatting: fewer lines is useful only when it does
   not hide intent or combine unrelated work. Do not optimize for low line count,
   generate speculative extension points, or add unrelated cleanup.
8. **Check the result.** Verify the behavior at the relevant user-facing boundary,
   including important success, empty, error, and edge states. Run focused checks that
   cover changed behavior, and inspect the diff for duplicate logic, dead code,
   unnecessary surface area, style drift, and accidental changes. For UI, inspect the
   rendered result and check keyboard and accessibility basics. Tests passing does not
   by itself establish that the feature is useful or usable.
9. **Report evidence and limits.** Briefly state the user outcome, what existing code
   was reused or why new code was needed, what research or user evidence informed the
   design, what changed, and what checks ran. Call out material unknowns and unverified
   assumptions. Never imply that a search, test, analytics check, or design review
   happened if it did not.

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

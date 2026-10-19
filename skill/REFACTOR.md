# Refactor

Improve code structure while preserving the behavior users still need.

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

## Workflow

1. **Name the improvement.** State what makes the current structure costly or hard to
   change, and what should become easier. “Clean up” alone is not a measurable goal.
2. **Map the behavior and callers.** Trace the relevant entry points, public contracts,
   dependencies, and callers. Record behavior that must stay the same, including error
   cases and side effects. Search for duplicates before introducing a shared helper.
3. **Set a baseline.** Run or inspect the focused tests and checks that cover the
   behavior. Record relevant performance or operational measures if the refactor could
   affect them. Identify missing coverage before relying on it.
4. **Research and compare.** Read full, relevant,
   peer-reviewed papers from established scholarly publishers or proceedings (such as
   Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University Press, or
   ACM) or peer-reviewed university research. Company guides, vendor blogs, press
   releases, AI-written summaries, abstracts, and search snippets do not count; vendor
   documents may confirm vendor-specific facts. Record each paper's method, scope,
   finding, limitations, and relevance to the code being changed. Compare research with
   actual behavior and project constraints; do not add an abstraction because it is
   fashionable. If fewer than three suitable full papers can be read for the task,
   report the gap and mark the research incomplete; do not pad the list. The three-paper
   minimum is a workflow requirement, not a research-established optimum.
5. **Change structure in small steps.** Keep external behavior and interfaces stable
   unless the user asked to change them. Reuse existing project patterns when they are
   sound; improve a weak pattern when it is in scope. Avoid new layers, wrappers,
   options, dependencies, and broad formatting changes without a concrete benefit.
6. **Check equivalence.** Run focused tests after each meaningful step. Compare outputs,
   errors, side effects, and relevant performance with the baseline. Inspect the diff
   for accidental behavior changes, duplicate logic, dead code, and unnecessary lines.
7. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH, then verify each one. For a deployable app or service,
   test in staging before redeploying. If staging is missing, ask the user to create it
   or authorize access; wait for tests to pass before redeploying. Stop and report any
   failed push or check. State why staging does not apply to a non-deployable project.
8. **Report plainly.** State the structural problem, what changed, the behavior checks
   and comparisons that ran, and any uncovered behavior. Always report other material
   codebase problems found in the inspected scope, with examples and effects. Use the
   [wording dictionary](../dictionary/wording.md).

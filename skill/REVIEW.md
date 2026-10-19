# Review

Check whether a proposed change does what it claims, fits the system, and improves the
codebase without adding avoidable risk. Review the change; do not implement it.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check findings and the final report against the
dictionary.

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

1. **Establish intent and scope.** Read the request, diff, linked design or issue, and
   relevant repository guidance. Identify the behavior that should change and what must
   remain stable.
2. **Inspect the actual change.** Trace changed code through callers, public interfaces,
   data flow, error paths, and related code. Verify claims against the implementation;
   confidence in the author's summary is not evidence.
3. **Check behavior and risk.** Look for incorrect behavior, missing cases, security or
   data risks, compatibility breaks, duplicate APIs, unused code, unnecessary
   dependencies, scope creep, and violations of useful project conventions. Check
   whether tests cover real failure modes and would fail if the behavior broke. Review
   available CI results; do not say tests passed unless you verified that result.
4. **Research the change.** Read full, relevant, peer-reviewed papers
   from established scholarly publishers or proceedings (such as Elsevier, Springer
   Nature, Wiley, Taylor & Francis, IEEE, Oxford University Press, or ACM) or
   peer-reviewed university research. Company guides, vendor blogs, press releases,
   AI-written summaries, abstracts, and search snippets do not count; vendor documents
   may confirm vendor-specific facts. Record each paper's method, scope, finding,
   limitations, and relevance to the changed code. Compare research with the diff and
   actual repository evidence. If fewer than three suitable full papers can be read for
   the task, report the gap and mark the research incomplete; do not pad it. The
   three-paper minimum is a workflow requirement, not a research-established optimum.
5. **Use evidence.** Confirm concerns with a call path, input, test result, log, or
   research evidence. Treat style-only preferences as non-blocking unless they violate
   project guidance.
6. **Write actionable findings.** Put findings first, ordered by severity. For each,
   give a precise file and line, the condition that triggers it, and its effect. Do not
   report guesses as defects. If there are no findings, say what you inspected and what
   checks you could verify; do not give blanket approval based on a narrow view.
7. **Flag codebase problems.** Always report material bloat, duplication, or poor
   practices found in the inspected area, even outside the change. Give examples and
   explain their effect. Do not expand the review into a cleanup; ask whether the user
   wants a separate FIX, REMOVE, or REFACTOR task.
8. **Keep the boundary.** Do not edit, commit, push, or deploy during a review. If the
   user asks you to address findings, switch to the matching change workflow.
9. **Write plainly.** Use the [wording dictionary](../dictionary/wording.md). Avoid
   padded praise, generic approval, and unsupported claims.

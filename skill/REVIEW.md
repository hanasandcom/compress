# Review

Check whether a proposed change does what it claims, fits the system, and improves the
codebase without adding avoidable risk. Review the change; do not implement it.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check findings and the final report against the
dictionary.

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
4. **Use evidence.** Confirm concerns with a call path, input, test result, log, or
   authoritative source. Google’s review guidance says to prioritize code health and
   technical facts over personal preference ([standard of code review][google-review]).
   Treat style-only preferences as non-blocking unless they violate project guidance.
5. **Write actionable findings.** Put findings first, ordered by severity. For each,
   give a precise file and line, the condition that triggers it, and its effect. Do not
   report guesses as defects. If there are no findings, say what you inspected and what
   checks you could verify; do not give blanket approval based on a narrow view.
6. **Flag codebase problems.** Always report material bloat, duplication, or poor
   practices found in the inspected area, even outside the change. Give examples and
   explain their effect. Do not expand the review into a cleanup; ask whether the user
   wants a separate FIX, REMOVE, or REFACTOR task.
7. **Keep the boundary.** Do not edit, commit, push, or deploy during a review. If the
   user asks you to address findings, switch to the matching change workflow.
8. **Write plainly.** Use the [wording dictionary](../dictionary/wording.md). Avoid
   padded praise, generic approval, and unsupported claims.

[google-review]: https://google.github.io/eng-practices/review/reviewer/standard.html

# Review

Check whether a proposed change does what it claims, fits the system, and improves the
codebase without adding avoidable risk. Review the change; do not implement it.

Follow [Session Control](SESSION_CONTROL.md) for user direction, authority, pause,
resumption, and handoff. A review remains read-only; report concerns without making the
change.

## Choose the work pattern

For every request, assess whether independent parts can finish sooner through
[parallelization](PARALLELIZATION.md), or whether separate requested outcomes call for
[multitasking](MULTITASKING.md). Use subagents first; use additional agents only after
all four subagent slots are occupied and only when the platform has capacity. Keep one
coordinator responsible for integrating evidence, resolving conflicts, and reporting
the whole result; assign non-overlapping scopes to avoid file conflicts. If delegation
will save time, delegate instead of merely suggesting it.

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

Research is required. Follow the shared [Research protocol](RESEARCH.md): every task
uses at least three full, relevant peer-reviewed papers that contribute distinct,
complementary evidence. Compare how they agree, extend, or challenge one another,
then connect the synthesis to product evidence and decisions. A paper count or list
of summaries alone does not meet this requirement. The set is shared across the
whole task chain, not repeated for each workflow or worker; report when research
is incomplete.

Assess coherence where the change touches it: trace affected component boundaries,
data flow, contracts, and state, then check whether the change supports the product's
user journey and business value. For a game, check its core play loop and why players
would return; discuss monetization only where it applies. For feeds or recommendations,
consider user benefit and control, diversity, and tradeoffs; engagement or time spent
alone does not establish value. Keep the review read-only and tie concerns to inspected
code or product evidence.

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
4. **Research the change.** Follow [Research](RESEARCH.md) to compare distinct evidence
   about the intended behavior, known risks or competing approaches, and suitable
   quality checks. Compare the synthesis with the diff and repository evidence.
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

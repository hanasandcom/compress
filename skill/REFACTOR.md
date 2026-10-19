# Refactor

Improve code structure while preserving the behavior users still need.

Follow [Session Control](SESSION_CONTROL.md) for user direction, authorization,
pauses, approvals, verification, and handoff. A refactor request does not grant
permission to publish or affect production.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

## Choose the work pattern

For every request, assess whether independent parts of this refactor can finish
faster in parallel, or whether separate requested outcomes merit multitasking.
Follow [Parallelization](PARALLELIZATION.md) for workers on one refactor and
[Multitasking](MULTITASKING.md) for separate requested work. Prefer subagents;
use additional agents only after all four subagent slots are occupied, subject to
actual platform capacity. Keep one coordinator responsible for shared contracts,
integration, and final checks; assign non-overlapping files or work areas to avoid
conflicts. If delegation will save time, delegate instead of merely suggesting it.

## Check product fit and architecture

Before a broad refactor, map the current and intended user journey and product core
loop: why users spend time here, what user or business value the structure
supports, and whether a relevant monetization model depends on it. Do not invent a
revenue case when monetization is irrelevant. For games, preserve or improve the
reason to play and core play loop; do not turn the refactor into a bundle of
disconnected features. For feed or recommendation behavior, consider user outcomes,
control, relevance, diversity, and tradeoffs; time spent or engagement alone is not
user value. Scale the plan to the change, but before broad work map affected domain
boundaries, data flow, contracts, state, failure behavior, and operational effects.

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

## Workflow

1. **Name the improvement.** State what makes the current structure costly or hard to
   change, and what should become easier. “Clean up” alone is not a measurable goal.
2. **Map the behavior and callers.** Trace the relevant entry points, public contracts,
   dependencies, and callers. Record behavior that must stay the same, including error
   cases and side effects. Search for duplicates before introducing a shared helper.
3. **Set a baseline.** Run or inspect the focused tests and checks that cover the
   behavior. Record relevant performance or operational measures if the refactor could
   affect them. Identify missing coverage before relying on it.
4. **Research and compare.** Follow [Research](RESEARCH.md) to compare distinct evidence
   about the current structure, candidate designs, and how to measure the result. Check
   findings against actual behavior and project constraints; do not add an abstraction
   because it is fashionable.
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

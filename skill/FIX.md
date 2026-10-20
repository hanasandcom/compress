# Fix

Correct a specific defect with the smallest change that addresses its cause.

Follow [Session Control](SESSION_CONTROL.md) for the standing release authorization
that comes with invoking this workflow, user direction, pauses, verification, and
handoff. Keep the work within the reported product path.

Apply the mandatory [quality scan](QUALITY_SCAN.md) on every fix. Inspect the README,
names, and relevant code even for a narrow defect; fix related weaknesses and report
material separate issues with examples and effects.

If the user has assigned ongoing responsibility for the project, establish or refresh
the project baseline in [AUDIT.md](AUDIT.md) before a narrow fix. Check the customer
path through the frontend, APIs, and dependencies; verify live behavior and timing
where authorized; and compare the README and language conventions with the source and
related projects. Fix the reported defect in that context and report other material
baseline findings with evidence. Without a stewardship or broader health request, keep
the work focused on the reported defect and its directly related product path.

If the user has assigned ongoing responsibility for the project, establish or refresh
the project baseline in [AUDIT.md](AUDIT.md) before a narrow fix. Check the customer
path through the frontend, APIs, and dependencies; verify live behavior and timing
where authorized; and compare the README and language conventions with the source and
related projects. Fix the reported defect in that context and report other material
baseline findings with evidence. Without a stewardship or broader health request, keep
the work focused on the reported defect and its directly related product path.

## Route and plan the work

For every request, assess whether independent parts of this same goal can finish sooner
in parallel, or whether several independent requested outcomes call for multitasking.
Follow [PARALLELIZATION](PARALLELIZATION.md) or [MULTITASKING](MULTITASKING.md) when
useful: use subagents first, and use additional agents only after all four subagent
slots are occupied and actual platform capacity permits it. Keep a coordinator
responsible for integration and whole-product checks; assign clear ownership to avoid
conflicting edits. If delegation will save time, delegate instead of merely suggesting
it. Do not split coupled work just to increase agent count.

Before fixing, plan at a scale that fits the defect. Explain the affected user's need,
the fix's value and place in the product journey, and why the user would spend time on
that path. Explain business or monetization value only when relevant and supported; do
not invent a revenue case. For games, check whether the defect breaks the core play
loop or reason to play. If the cause or correction crosses components or affects
domain behavior, data, or operations, map architecture and data flow, contracts, state,
failure paths, and operational effects before editing. For feed or recommendation
defects, consider relevance, variety, user control, unwanted content, and user
outcomes; engagement or time spent alone does not establish user value. Apply research
within its actual scope and limits, not as proof that a fix will work here.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Apply natural examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

Search related files and product surfaces for the same issue, not just the reported
example. BUILD, FIX, REMOVE, and REFACTOR must fix every confirmed instance in the
relevant product scope and verify none remain; if one cannot be fixed, state which and
why. AUDIT and REVIEW report confirmed instances and search limits without changing files.
INVESTIGATE must fix confirmed in-scope instances and verify none remain. Treat related
repetitions of the same underlying problem as part of the task; separate, unrelated
problems may be reported without absorbing them into the current work.

Research is required. Follow the shared [Research protocol](RESEARCH.md): every task
uses at least three full, relevant peer-reviewed papers that contribute distinct,
complementary evidence. Compare how they agree, extend, or challenge one another,
then connect the synthesis to product evidence and decisions. A paper count or list
of summaries alone does not meet this requirement. Share one research map across the
task chain, but size it for each workflow’s distinct decisions using
[Research](RESEARCH.md). Workers should not repeat the same search. Report incomplete
research.

## Cause and scope check

List the separate failures caused by the defect, then search related pages, APIs, data
paths, and reports for every instance. Fix all confirmed instances in scope. Keep
unrelated defects separate and report them; do not imply one symptom fix resolved them.
Verify the original failure, each sibling instance, and the user's full task path. A
narrow green test does not establish that the product now works as promised.

## Workflow

1. **Define the failure.** Record what should happen, what happens instead, who or what
   is affected, and a reliable reproduction. Separate observed facts from guesses. For
   claims about external source material, preserve the source and field provenance; a
   missing field in an API response does not prove the source omitted it. Keep source
   claims distinct from parser output and estimates. If a fix requires an estimate,
   identify and validate its inputs and method; do not invent a value when either is
   missing.
2. **Trace the path.** Follow the failing request or action through its entry point,
   implementation, dependencies, and callers. Check recent changes, existing tests,
   logs, and similar working behavior before editing.
3. **Prove the cause.** Reproduce the defect or identify direct evidence for it. Check
   relevant official documentation, issue reports, or release notes when the cause
   depends on framework or dependency behavior. Do not replace the symptom with a
   fallback until you understand why it occurs.
4. **Research and compare approaches.** Follow [Research](RESEARCH.md) to select and
   synthesize distinct evidence about the cause, candidate fixes, known weaknesses, and
   how to judge the result. Also inspect mature products and user or maintainer criticism.
   Check whether a seemingly better approach fits this product's constraints and actual
   failure path.
5. **Fix only the defect.** Make the smallest complete change that corrects the cause.
   Reuse the existing behavior where it fits. Do not add a parallel API, broad cleanup,
   or speculative fallback. If you find material bloat or a separate quality problem,
   always show examples and their impact. Fix confirmed repetitions of the same problem
   in the relevant scope; ask before taking on a separate problem outside that scope.
6. **Check the correction.** Add or update a focused regression check when appropriate.
   For data fields, cover missing, null, empty, malformed, and valid values where those
   states can reach the boundary.
   Verify that the original failure is gone and that important neighboring behavior
   still works. Read relevant CI results when available. Do not claim a check passed if
   it was not run.
7. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH; verify each one. For a deployable app or service, run
   server-side tests in staging before redeploying. If staging is missing, follow
   BUILD's isolated temporary staging procedure. If a push or test fails, fix the issue
   and repeat the checks. For non-deployable projects, state why staging does not apply.
8. **Report plainly.** State the cause, the correction, the checks that ran, and any
   remaining uncertainty. Always report material codebase problems found in the
   inspected scope, with concrete examples and effects. Use the [wording
   dictionary](../dictionary/wording.md) and [habits.md](../dictionary/habits.md); do not pad the report.

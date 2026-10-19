# Remove

Retire a capability and the code that exists only to support it, without breaking
behavior users still rely on.

Follow [Session Control](SESSION_CONTROL.md) for user direction, authorization,
pauses, approvals, verification, and handoff. A removal request does not authorize
destructive or external actions beyond its stated scope.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Apply natural examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

## Choose the work pattern

For every request, assess whether independent parts of this removal can finish
faster in parallel, or whether separate requested outcomes merit multitasking.
Follow [Parallelization](PARALLELIZATION.md) for workers on one removal and
[Multitasking](MULTITASKING.md) for separate requested work. Prefer subagents;
use additional agents only after all four subagent slots are occupied, subject to
actual platform capacity. Keep one coordinator responsible for shared contracts,
integration, and final checks; assign non-overlapping files or work areas to avoid
conflicts. If delegation will save time, delegate instead of merely suggesting it.

## Check product fit and architecture

Before a broad removal, map the current and intended user journey and product core
loop: why users spend time here, what user or business value the capability
provides, and whether a relevant monetization model depends on it. Do not invent a
revenue case when monetization is irrelevant. For games, state how the capability
fits the reason to play and core play loop. For feed or recommendation behavior,
consider user outcomes, control, relevance, diversity, and tradeoffs; time spent or
engagement alone is not user value. Scale the plan to the change, but for broad work
map affected domain boundaries, data flow, contracts, state, failure behavior, and
operational effects before removing components.

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

## Product value check

Do not let code references or missing analytics decide whether a capability is valuable.
For each page, API, workflow, and substantial module, identify its job: core user outcome,
useful adjacent support, operational need, or no demonstrated role. Check whether it
actually completes that job, what it costs to maintain, and whether another path already
does it. Keep useful adjacent features when they serve the product; flag elaborate
readiness, status, or informational surfaces that do not help users complete a real task.
Missing telemetry limits visit claims; it does not stop the value assessment. Check
external-caller risk separately and stage public API removal only when the concrete risk
warrants it.

## Workflow

1. **Define the removal.** Name the capability, surfaces, APIs, and users in scope.
   Identify what should happen in its place, if anything. Treat “unused” as a claim
   to verify, not an assumption.
2. **Check actual use.** Trace callers, imports, routes, dynamic registrations, flags,
   integrations, docs, and tests. Check production request counts and last-use dates
   over a stated period when available. Confirm whether the endpoint can respond and
   what its responses do. Separate a redirect or compatibility alias from a duplicate
   implementation or a distinct capability. For public interfaces, verify that logs
   cover external callers before concluding they are unused. Static references alone
   do not prove runtime use; no recorded traffic does not prove non-use if logging is
   incomplete or external callers are possible. Mark each conclusion as confirmed,
   disproved, or unknown, and name the evidence that would resolve an unknown.
3. **Assess the impact.** Identify affected users, dependent systems, data, migrations,
   and rollback needs. If evidence shows meaningful use or cannot establish whether a
   public interface has external users, show the evidence and risk, then ask whether to
   proceed or stage a deprecation. Do not silently leave a second API or compatibility
   layer behind.
4. **Research removal and deprecation.** Follow [Research](RESEARCH.md) to compare
   distinct evidence about usage, migration, and deprecation, and use it to test the
   removal assumptions against product evidence. Include evidence about what replaces
   the capability when a replacement is part of the plan.
5. **Remove the whole capability.** Delete its implementation and code used only by it.
   Update routes, configuration, navigation, docs, and tests. Preserve shared helpers
   and behavior that other features still use. Do not add unrelated cleanup.
6. **Check the result.** Verify the retired path is unavailable or gives the intended
   response, shared callers still work, and no references remain in the inspected
   surfaces. Run focused tests and inspect the diff. Be explicit about dynamic or
   external references that could not be checked.
7. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH, then verify each one. For a deployable app or service,
   test in staging before redeploying. If staging is missing, ask the user to create it
   or authorize access; wait for tests to pass before redeploying. Stop and report any
   failed push or check. State why staging does not apply to a non-deployable project.
8. **Report plainly.** State what was removed, evidence of use or non-use, the period
   and coverage of usage data, affected callers, checks, and remaining risks. Always
   report other material codebase problems found in the inspected scope, with examples
   and effects. Check the final report against [wording.md](../dictionary/wording.md) and [habits.md](../dictionary/habits.md).

# Remove

Remove the requested page, feature, API, or workflow and the code that only supports it.
The request authorizes repository-local deletion within its stated scope. Do not ask
the user to confirm that deletion again. This covers code, pages, tests, docs, and
configuration that exist only for the removed capability. It does not authorize
production data erasure or changes outside the request.

Follow [Session Control](SESSION_CONTROL.md) for user direction, pauses, verification,
and handoff. Before writing prose, check the relevant parts of the [wording
dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Check any prose you add before reporting.

## Divide work when it helps

Assess whether independent removal work can finish sooner in parallel or whether the
request contains separate outcomes. Follow [Parallelization](PARALLELIZATION.md) for
one goal and [Multitasking](MULTITASKING.md) for separate outcomes. Prefer subagents;
use additional agents only after all four subagent slots are occupied and platform
capacity allows. Keep one owner responsible for integrating and checking the result.

## Decide from the product

REMOVE is an action workflow. Start with the requested target and finish its removal;
do not turn it into a defense of the feature or an audit-only report. For each page,
feature, API, test suite, or status surface, identify the task it claims to help with
and inspect whether it gives a real user or operator a working result. Check the whole
product path. If the product path is broken, a readiness panel, progress display, or
large test harness that only describes that path does not create customer value. A
code reference, green test, or attractive status page is not evidence of user benefit.

Decide using the product's purpose, the actual user path and output, dependencies, and
the user's stated facts. Do not require analytics, visit counts, customer records, or
other missing data. Their absence must never stop, delay, narrow, or reverse an in-scope
value judgment or removal. Do not invent usage figures; judge the feature from what it
does and whether that result matters to the product. Keep adjacent capabilities only
when they complete a concrete task that supports the product's users or operation.

Remove duplicate, broken, ceremonial, misleading, and nonfunctional surfaces when they
are in scope. Remove tests that only preserve those behaviors; keep or write focused
tests for behavior that remains. Do not retain a page because its usage is unknown, or
add a redirect merely to avoid removal. Preserve a legacy route or data format only
when a concrete compatibility need exists; check fixed historical inputs and callers
before removing support. Preserve applicable license notices when deleting copied or
vendored code; do not change license terms as part of cleanup.

## Workflow

1. **Set the target.** Name the requested surface and the simpler product state after
   removal. Treat repository-local deletion in scope as authorized.
2. **Trace its real job.** Follow the user path, outputs, implementation, callers,
   routes, contracts, configuration, tests, and docs. Check the core path end to end
   where possible. Identify what actually works, what fails, and which parts exist only
   to support the removal target. Missing metrics do not pause this assessment.
3. **Check the evidence.** Research removal, migration, and compatibility under
   [Research](RESEARCH.md). Select distinct papers that inform this decision; research
   must improve the decision, not protect a feature from the requested removal. Check
   historical inputs when API or stored-format compatibility matters. Keep evidence
   about real dependencies and breakage; do not treat hypothetical consumers as a veto.
   If the required paper set is incomplete, report the gap and continue the requested
   repository removal from the available product evidence; a research gap is not a
   reason to retain a feature with no working user outcome.
4. **Remove the target and its bloat.** Delete the requested surface and code used only
   by it. Update or delete its callers, navigation, contracts, configuration, docs, and
   tests in scope. Keep shared code only when it has a concrete independent job. Do
   not ask for another approval to make these repository-local changes. Ask only when
   the next step would erase production data, change an out-of-scope system, or take an
   external action not authorized by the user.
5. **Check the result.** Confirm the removed path is gone or responds as intended,
   remaining user paths still work, and no in-scope references remain. Run relevant
   checks and inspect the diff. State any external or dynamic references you could not
   inspect without letting that uncertainty undo the value decision.
6. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH, then verify each one. For a deployable app or service,
   test in staging before redeploying. If staging is missing, ask to create it or
   authorize access, and wait for tests to pass before redeploying. Stop and report a
   failed push or check. Say why staging does not apply to a non-deployable project.
7. **Report plainly.** State what was removed, what user task it failed to deliver,
   affected callers, checks, and remaining operational risks. Include other material
   problems found in the inspected scope, with examples and effects. Do not present
   absent analytics as a reason to retain the feature.

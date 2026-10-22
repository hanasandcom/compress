# Investigate

Answer a specific question from evidence, then fix confirmed problems that materially
affect the answer or the product path being investigated. INVESTIGATE does not stop at
a list of findings or recommendations.

Keep the question and its observable answer as the task's goal card under
[Session Control](SESSION_CONTROL.md). A broad request to investigate a product still
needs a bounded first slice and regular checks that each side path changes the answer or
fixes a confirmed issue in the affected journey. List unrelated findings separately;
do not keep opening adjacent work without checking the original question and the fastest
remaining path.

Follow [Session Control](SESSION_CONTROL.md) for user direction, the standing release
authorization that comes with invoking this workflow, pause, resumption, and handoff.
The investigation request authorizes ordinary, reversible repository changes needed
to correct material in-scope problems. Do not ask again before editing, deleting,
releasing, or redeploying those changes.

Apply the mandatory [quality scan](QUALITY_SCAN.md) to the relevant area and fix
confirmed issues that bear on the question or its user and operator paths. This
includes misleading README claims, broken instructions, poor code, avoidable
duplication, and mismatches with established project conventions when the mismatch
has a concrete maintenance or behavior cost. Give examples and effects; do not stop
after naming a defect.

## Choose the work pattern

For every request, assess whether independent parts can finish sooner through
[parallelization](PARALLELIZATION.md), or whether separate requested outcomes call for
[multitasking](MULTITASKING.md). Use subagents first; use additional agents only after
all four subagent slots are occupied and only when the platform has capacity. Keep one
coordinator responsible for integrating evidence, resolving conflicts, and reporting
the whole result; assign non-overlapping scopes to avoid file conflicts. If delegation
will save time, delegate instead of merely suggesting it.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Apply natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check the answer and final report against the
dictionary.

Search related files, product surfaces, and relevant repositories for the same issue,
not just the reported example. BUILD, FIX, REMOVE, REFACTOR, and INVESTIGATE must fix
confirmed in-scope instances and verify none remain; if one cannot be fixed, state
which and why. AUDIT and REVIEW report findings without changing files. For
cross-repository questions, inspect actual callers, configuration, runtime behavior,
ownership, languages, toolchains, and release boundaries. Check whether shared code or
operational behavior can move into a common repository without coupling service-owned
settings or releases. Treat related repetitions as part of the task; separate,
unrelated problems may be reported without absorbing them into the current work.

When the user has established a shared language or toolchain convention, compare the
repository against it and inspect the reason for any exception. If maintained source
breaks that convention and migration is safe and useful, migrate the maintained source
and tests as part of the investigation; do not leave a concrete mismatch as a
recommendation. Keep configuration, generated files, and vendored code in their proper
formats. Preserve runtime behavior and check the build, callers, and deployment path.

Research is required. Follow the shared [Research protocol](RESEARCH.md): every task
uses at least three full, relevant peer-reviewed papers that contribute distinct,
complementary evidence. Compare how they agree, extend, or challenge one another,
then connect the synthesis to product evidence and decisions. A paper count or list
of summaries alone does not meet this requirement. Share one research map across the
task chain, but size it for each workflow’s distinct decisions using
[Research](RESEARCH.md). Workers should not repeat the same search. Report incomplete
research.

For questions about architecture or product quality, assess the relevant user journey
or game core loop, why users spend time on it, and the product or business value; discuss
monetization only where applicable. Trace component boundaries, data flow, contracts,
and state transitions. For feeds or recommendations, consider user benefit and control,
diversity, and tradeoffs; engagement or time spent alone is not proof of value. Keep
   findings within the question's scope and fix confirmed defects that affect the
   answer or product path.

## Whole-scope finding check

For product-quality questions, trace the entire customer task and compare each substantial
surface with the product's purpose. Continue after the first plausible defect: search for
sibling failures and the code or test patterns that create the same cost. Missing
analytics limits usage claims; it does not prevent findings about broken, misleading,
redundant, or purposeless functionality. Report concrete examples and effects in the
inspected scope.

## Workflow

1. **Pin down the question.** State the decision the answer should support and the
   systems or time period in scope. The question sets the starting point, not a reason
   to ignore defects that affect its answer or the product path. Do not turn the task
   into an unrelated whole-product cleanup.
2. **Find direct evidence.** Inspect relevant code, configuration, history, tests, logs,
   analytics, documentation, and actual runtime behavior where access permits. Trace
   the full path across repository and service boundaries, including the producer,
   transformations, API contract, and display or consumer. Test user-provided factual
   premises against the source records or an authoritative contract; treat them as
   reported facts until checked. Trace claims that an API works or nobody uses it.
   Search finds code references but cannot prove production use or rule out external
   callers. A missing response field does not by itself prove the source lacked the
   value or that it was withheld.
3. **Research the question and the fixes.** Follow [Research](RESEARCH.md) to compare
   distinct evidence that supplies context, tests competing explanations, and qualifies
   both the answer and any material changes. Carry one evidence map through any chained
   FIX, REMOVE, REFACTOR, or BUILD work; add research only for decisions the existing
   map does not cover. Connect the synthesis to product evidence and acceptance checks.
4. **Separate evidence from inference.** Label what is confirmed, what is likely, and
   what remains unknown. For use or value claims, name the data source, period,
   coverage, and filters. Separate requests, page views, completed tasks, purchases,
   delivered service, and customer outcomes. Distinguish zero recorded events from
   missing or incomplete telemetry. Do not invent results or turn earlier agent
   conclusions into facts without checking them.
5. **Settle confirmed defects.** For each material problem that affects the question or
   the relevant product path, choose BUILD, FIX, REMOVE, or REFACTOR and complete that
   work in the same task. Search related files and repositories for repeated instances,
   fix the in-scope ones, and verify none remain. If changing languages, moving shared
   code, or changing service boundaries, map all callers and deployment contracts first;
   preserve behavior and make the smallest complete migration. Do not infer that a
   language outlier is harmful from counts alone: establish its cost and the benefit of
   the proposed standard. Do not leave a material README correction or a confirmed,
   directly related code defect as a recommendation.
6. **Complete the checks.** Run the relevant local checks for the question and fixes.
   Follow BUILD or REFACTOR for behavior, compatibility, commit, push, staging, and
   redeployment. If a required operation is blocked by a platform gate or an exact
   technical limit, finish independent work and state the unfinished step and why.
7. **Answer after the work is complete.** Give the direct answer, the evidence from
   each relevant repository, changes made, checks run, remaining uncertainty, and any
   boundary that prevented completion. Link research used. Check the report against
   [wording.md](../dictionary/wording.md) and [habits.md](../dictionary/habits.md).
   Do not present an early finding as the finished investigation.

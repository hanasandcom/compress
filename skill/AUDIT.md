# Audit

Assess what a system contains, what people use, what works, and what it costs to keep.
Do not change code during an audit.

Follow [Session Control](SESSION_CONTROL.md) for user direction, authority, pause,
resumption, and handoff. An audit remains read-only; it does not authorize access to
production data or external systems beyond the user's permissions.

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
one section answers the question. Check the final report against the dictionary.

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
of summaries alone does not meet this requirement. Share one research map across the
task chain, but size it for each workflow’s distinct decisions using
[Research](RESEARCH.md). Workers should not repeat the same search. Report incomplete
research.

Assess product and architecture coherence in the audited scope. Trace the user journey
or, for a game, its core play loop and reason to return; connect each major component to
a user need and product or business value. Discuss monetization only where it applies.
Map component boundaries, data flow, contracts, and state transitions, and report
disconnected features or missing architectural structure with evidence. For feeds or
recommendations, assess user benefit, user control, diversity, and tradeoffs; engagement
or time spent alone is not evidence of value. Keep this assessment read-only.

## Product and code quality check

Do not stop at route counts or absent telemetry. Trace the main customer tasks and check
what useful, correct, actionable result each delivers, where it breaks, and which pages
or features add no user or operational outcome. Continue with repository evidence when
analytics are unavailable. Inspect duplicate implementations and APIs, unused branches,
oversized modules, speculative abstractions, excessive configuration, and tests with weak
assertions, poor failure coverage, duplicate suites, or unnecessary setup. Show paths and
effects; counts only locate candidates. Separate core functionality from useful adjacent
support and from ceremonial or disconnected surfaces.

## Workflow

1. **Set the boundary.** Name the product areas, APIs, services, or time period in
   scope. List evidence needed to answer the question, including telemetry or ownership
   data the repository cannot provide.
2. **Inventory the surface.** Find routes, APIs, components, dependencies, workers,
   flags, data stores, and related tests. Group duplicate or overlapping interfaces.
   Record what is directly referenced, dynamically reachable, externally exposed, or
   unknown; a text search alone cannot establish runtime use.
3. **Check whether it works.** Trace representative calls end to end. Where access
   permits, check recent request counts, last use, success and failure rates, costs, and
   whether the service responds as its contract promises. For user-facing pages and
   features, distinguish requests from page views, successful task completion, purchase,
   service delivery, support feedback, and customer outcomes. State the source, period,
   filters, coverage gaps, and whether a zero means no events or no measurement. A
   request count or visit count alone does not establish usefulness. Production
   monitoring can inform change decisions only when its coverage and signals are clear.
4. **Assess value and cost.** Connect each surface to a user or operational need. Note
   duplicate behavior, abandoned implementations, broken paths, maintenance burden, and
   risks. Use evidence such as call volume, incidents, support feedback, and dependency
   relationships. Lines of code or number of APIs alone do not prove waste or value.
5. **Read and compare research.** Follow [Research](RESEARCH.md) to use distinct evidence
   about common designs, failure modes, and quality checks. Connect the synthesis to
   this system's architecture, telemetry, and user or maintenance evidence; studies of
   other products do not establish what happens here.
6. **Compare against good practice.** Use the research, relevant standards, and direct
   project evidence to assess material risks or non-standard design. Use product
   feedback and analytics where available. Separate verified findings from inference;
   do not infer that a design is good because it is popular or that code is safe because
   tests pass.
7. **Recommend a next action.** For each finding, give the evidence, user or maintenance
   impact, confidence, and a concrete action: keep, improve, remove, or investigate
   further. Rank by impact and risk. Do not implement changes unless the user asks.
8. **Report plainly.** Always report material bloat, duplication, broken behavior, and
   missing evidence found in the audited scope, with paths, examples, and effects.
   Do not claim the whole system is clean if only part was checked. Use the [wording
   dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).

## Research basis

These software-engineering studies show why an audit should check different evidence
sources and account for each method's limits: Li et al. studied technical-debt signals
across code comments, commit messages, pull requests, and issue trackers ([Springer
Nature, 2023](https://link.springer.com/article/10.1007/s10664-023-10297-9)); Rantala
et al. found only limited overlap between keyword-marked debt and static-analysis
results ([Springer Nature, 2024](https://link.springer.com/article/10.1007/s11219-023-09655-z));
and an IEEE conference paper describes architectural-debt identification as an open
research problem ([IEEE, 2018](https://ieeexplore.ieee.org/document/8432173)). These
papers support checking multiple evidence sources; they do not prove findings about a
different repository. The three-paper minimum is a workflow requirement, not a claim
that research has established three as the ideal number.

# Investigate

Answer a specific question from available evidence without changing code.

Follow [Session Control](SESSION_CONTROL.md) for user direction, authority, pause,
resumption, and handoff. An investigation remains read-only; do not take follow-up
actions that the user has not authorized.

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

For questions about architecture or product quality, assess the relevant user journey
or game core loop, why users spend time on it, and the product or business value; discuss
monetization only where applicable. Trace component boundaries, data flow, contracts,
and state transitions. For feeds or recommendations, consider user benefit and control,
diversity, and tradeoffs; engagement or time spent alone is not proof of value. Keep
findings within the question's scope and report them without changing files.

## Whole-scope finding check

For product-quality questions, trace the entire customer task and compare each substantial
surface with the product's purpose. Continue after the first plausible defect: search for
sibling failures and the code or test patterns that create the same cost. Missing
analytics limits usage claims; it does not prevent findings about broken, misleading,
redundant, or purposeless functionality. Report concrete examples and effects in the
inspected scope.

## Workflow

1. **Pin down the question.** State the decision the answer should support and the
   systems or time period in scope. If the question is answerable, begin; do not
   widen it into an audit or implementation plan.
2. **Find direct evidence.** Inspect relevant code, configuration, history, tests, logs,
   analytics, documentation, and actual runtime behavior where access permits. Trace
   the full path across repository and service boundaries, including the producer,
   transformations, API contract, and display or consumer. Test user-provided factual
   premises against the source records or an authoritative contract; treat them as
   reported facts until checked. Trace claims that an API works or nobody uses it.
   Search finds code references but cannot prove production use or rule out external
   callers. A missing response field does not by itself prove the source lacked the
   value or that it was withheld.
3. **Research the question.** Follow [Research](RESEARCH.md) to compare distinct evidence
   that supplies context, tests competing explanations, and qualifies the answer. Connect
   the synthesis to the question's evidence and state when it leaves a decision open.
4. **Separate evidence from inference.** Label what is confirmed, what is likely, and
   what remains unknown. For use or value claims, name the data source, period,
   coverage, and filters. Separate requests, page views, completed tasks, purchases,
   delivered service, and customer outcomes. Distinguish zero recorded events from
   missing or incomplete telemetry. Do not invent results or turn earlier agent
   conclusions into facts without checking them.
5. **Flag problems found.** Always report material bloat, duplicate behavior, broken
   paths, or poor practices that appear in the inspected scope, even when they are not
   needed to answer the main question. Give concrete examples and effects; do not claim
   the whole repository has the problem unless you checked it.
6. **Answer directly.** Give the answer first, then the strongest evidence, limitations,
   and what would resolve remaining uncertainty. Link sources when research was used.
   Check the response against [wording.md](../dictionary/wording.md) and [habits.md](../dictionary/habits.md); keep it specific
   and short.
7. **Keep the boundary.** Do not edit code, commit, push, or deploy. If the user wants a
   change after the investigation, use BUILD, FIX, REMOVE, or REFACTOR as appropriate.

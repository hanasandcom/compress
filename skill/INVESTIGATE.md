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
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
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

Research is required. In chained work, choose one shared set of N relevant full,
peer-reviewed papers for the whole task (N must be at least three); carry findings
between workflows and add papers only for important unanswered questions. Select studies
to test current assumptions, including findings that challenge the proposed direction.
When work touches a domain's behavior, data processing, or architecture, compare the
actual pipeline stage by stage with established designs and recent research: what works,
what is missing, and what could improve it. Assess candidate methods such as NLP or
bag-of-words for fit and limits; their use elsewhere is not proof they belong here. Tie
conclusions to paper methods, scope, limits, and evidence from this product.

Apply research, do not just cite it. For each paper, carry forward its method, scope,
finding, limitation, and the local question or check it suggests. Keep a concise shared
note across workflow handoffs instead of repeating source text. Tests show only whether
covered behavior passes; also inspect reuse, completeness, readability, and operating
cost. The research set must answer named decisions in this task: do not count papers
that are only loosely related. The minimum of three applies once across the whole
task chain, not once per worker or workflow. Track research time and report when the
cost, lack of suitable full papers, or weak fit leaves a decision unresolved; do not
claim the rule improved results until representative outcomes have been compared.

For questions about architecture or product quality, assess the relevant user journey
or game core loop, why users spend time on it, and the product or business value; discuss
monetization only where applicable. Trace component boundaries, data flow, contracts,
and state transitions. For feeds or recommendations, consider user benefit and control,
diversity, and tradeoffs; engagement or time spent alone is not proof of value. Keep
findings within the question's scope and report them without changing files.

## Workflow

1. **Pin down the question.** State the decision the answer should support and the
   systems or time period in scope. If the question is answerable, begin; do not
   widen it into an audit or implementation plan.
2. **Find direct evidence.** Inspect relevant code, configuration, history, tests, logs,
   analytics, documentation, and actual runtime behavior where access permits. Trace
   claims that an API works or nobody uses it. Search finds code references but
   cannot prove production use or rule out external callers.
3. **Research the question.** Read full,
   relevant, peer-reviewed papers from established scholarly publishers or proceedings
   (such as Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University
   Press, or ACM) or peer-reviewed university research. Company guides, vendor blogs,
   press releases, AI-written summaries, abstracts, and search snippets do not count;
   vendor documents may confirm vendor-specific facts. Record each paper's method,
   scope, finding, limitations, and relevance to this question. If fewer than three
   suitable full papers can be read for the task, report the gap and mark the research
   incomplete; do not pad it. The three-paper minimum is a workflow requirement, not a
   research-established optimum.
4. **Separate evidence from inference.** Label what is confirmed, what is likely, and
   what remains unknown. For usage claims, give the data source and period; distinguish
   zero recorded traffic from missing or incomplete telemetry. Do not invent results or
   turn earlier agent conclusions into facts without checking them.
5. **Flag problems found.** Always report material bloat, duplicate behavior, broken
   paths, or poor practices that appear in the inspected scope, even when they are not
   needed to answer the main question. Give concrete examples and effects; do not claim
   the whole repository has the problem unless you checked it.
6. **Answer directly.** Give the answer first, then the strongest evidence, limitations,
   and what would resolve remaining uncertainty. Link sources when research was used.
   Use the [wording dictionary](../dictionary/wording.md); keep the response specific
   and short.
7. **Keep the boundary.** Do not edit code, commit, push, or deploy. If the user wants a
   change after the investigation, use BUILD, FIX, REMOVE, or REFACTOR as appropriate.

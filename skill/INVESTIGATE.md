# Investigate

Answer a specific question from available evidence without changing code.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check the answer and final report against the
dictionary.

When changing workflow guidance, inspect all seven workflow files for the same issue
and update every file where the change applies; workflows may be loaded by themselves.

## Workflow

1. **Pin down the question.** State the decision the answer should support and the
   systems or time period in scope. If the question is answerable, begin; do not
   widen it into an audit or implementation plan.
2. **Find direct evidence.** Inspect relevant code, configuration, history, tests, logs,
   analytics, documentation, and actual runtime behavior where access permits. Trace
   claims that an API works or nobody uses it. Search finds code references but
   cannot prove production use or rule out external callers.
3. **Research the question.** For every investigation, read at least three full,
   relevant, peer-reviewed papers from established scholarly publishers or proceedings
   (such as Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University
   Press, or ACM) or peer-reviewed university research. Company guides, vendor blogs,
   press releases, AI-written summaries, abstracts, and search snippets do not count;
   vendor documents may confirm vendor-specific facts. Record each paper's method,
   scope, finding, limitations, and relevance to this question. If three suitable full
   papers cannot be read, report the gap and mark the research incomplete; do not pad it.
   Three is a workflow minimum, not a research-established optimum.
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

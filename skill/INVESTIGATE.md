# Investigate

Answer a specific question from available evidence without changing code.

## Workflow

1. **Pin down the question.** State the decision the answer should support and the
   systems or time period in scope. If the question is answerable, begin; do not
   widen it into an audit or implementation plan.
2. **Find direct evidence.** Inspect relevant code, configuration, history, tests, logs,
   analytics, documentation, and actual runtime behavior where access permits. Trace the
   Trace claims that an API works or nobody uses it. Search finds code references but
   cannot prove production use or rule out external callers.
3. **Research external claims.** When the answer depends on standards, current behavior,
   or accepted practice, check primary documentation and relevant published research.
   For a consequential or disputed claim, compare at least three relevant sources.
   Record what each supports and where sources disagree. Do not use search snippets as
   proof.
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

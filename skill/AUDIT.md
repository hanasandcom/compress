# Audit

Assess what a system contains, what people use, what works, and what it costs to keep.
Do not change code during an audit.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check the final report against the dictionary.

Search related files and product surfaces for the same issue, not just the reported
example. BUILD, FIX, REMOVE, and REFACTOR must fix every confirmed instance in the
relevant product scope and verify none remain; if one cannot be fixed, state which and
why. AUDIT, REVIEW, and INVESTIGATE must report confirmed instances and search limits
without changing files.

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
   whether the service responds as its contract promises. State the period, data source,
   coverage gaps, and whether a zero means no traffic or no measurement. Production
   monitoring can inform change decisions only when its coverage and signals are clear.
4. **Assess value and cost.** Connect each surface to a user or operational need. Note
   duplicate behavior, abandoned implementations, broken paths, maintenance burden, and
   risks. Use evidence such as call volume, incidents, support feedback, and dependency
   relationships. Lines of code or number of APIs alone do not prove waste or value.
5. **Read research.** For every audit, read at least three full, relevant, peer-reviewed
   research papers. Prefer empirical studies from established scholarly publishers or
   conference proceedings, such as Elsevier, Springer Nature, Wiley, Taylor & Francis,
   IEEE, Oxford University Press, or ACM, or peer-reviewed university research. Do not
   count corporate style guides, vendor blogs, press releases, AI-written summaries,
   abstracts alone, or search snippets toward the three papers. Vendor documentation may
   confirm vendor-specific behavior, but it does not replace research. For each paper,
   record its method, scope, main finding, limitations, and how it changes or tests the
   audit's conclusions. Connect research to evidence from this system; do not treat a
   study of other projects as proof about this one. If three relevant full papers cannot
   be found or accessed, report the gap and mark this comparison incomplete instead of
   padding it with unrelated sources.
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
   dictionary](../dictionary/wording.md).

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

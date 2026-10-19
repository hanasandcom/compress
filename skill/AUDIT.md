# Audit

Assess what a system contains, what people use, what works, and what it costs to keep.
Do not change code during an audit.

Before writing user-facing or maintainer-facing prose, consult the matching section of
the [wording dictionary](../dictionary/wording.md). Apply its natural examples only
when they fit the facts; do not mechanically replace words or load all 164 pairs when
one section answers the question. Check the final report against the dictionary.

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
   monitoring can inform change decisions only when its coverage and signals are clear
   ([Google SRE monitoring guidance][sre-monitoring]).
4. **Assess value and cost.** Connect each surface to a user or operational need. Note
   duplicate behavior, abandoned implementations, broken paths, maintenance burden, and
   risks. Use evidence such as call volume, incidents, support feedback, and dependency
   relationships. Lines of code or number of APIs alone do not prove waste or value.
5. **Compare against good practice.** Check relevant official guidance, standards, and
   credible technical sources for material risks or non-standard design. Use product
   feedback and analytics where available. Separate verified findings from inference;
   do not infer that a design is good because it is popular or that code is safe because
   tests pass.
6. **Recommend a next action.** For each finding, give the evidence, user or maintenance
   impact, confidence, and a concrete action: keep, improve, remove, or investigate
   further. Rank by impact and risk. Do not implement changes unless the user asks.
7. **Report plainly.** Always report material bloat, duplication, broken behavior, and
   missing evidence found in the audited scope, with paths, examples, and effects.
   Do not claim the whole system is clean if only part was checked. Use the [wording
   dictionary](../dictionary/wording.md).

[sre-monitoring]: https://sre.google/sre-book/practical-alerting/

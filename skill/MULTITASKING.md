# Multitasking

Use this workflow when one request contains multiple independent outcomes, such as a
frontend change and an API change, or work in two products. Every task workflow must
assess whether independent requested outcomes can be completed sooner in parallel, then
use this workflow when they can. When delegation will save time, assign owners and
start the work instead of merely recommending delegation.

## Assign the work

1. List each requested outcome, its product or component, dependencies, acceptance
   conditions, and the workflow that applies to it (Build, Fix, Remove, Refactor,
   Audit, Review, or Investigate).
2. Check dependencies and shared contracts first. If one task must define an API,
   schema, or design-system change that another depends on, settle that interface before
   assigning concurrent implementation.
3. Assign one worker to each independent outcome. Start subagents first. Do not add
   peer or other additional agents until all four subagent slots are occupied; use
   additional agents only when the platform permits and the work still benefits from
   them. Respect the actual capacity available in the current session.
4. Give each worker an exclusive scope, relevant context, acceptance conditions, and
   expected evidence. Keep one owner for each shared file or integration boundary.
   If the available worker count is smaller than the number of outcomes, group only
   outcomes that have compatible dependencies and clear ownership.
5. Carry one shared research set and note across chained tasks. Add a paper only when
   the existing set leaves an important question unanswered. Each owner applies the
   findings relevant to their outcome and records method, scope, finding, limitation,
   and local implication.
6. The coordinator integrates the outcomes, checks their interaction and shared
   contracts, verifies each acceptance condition, and reports incomplete work or
   conflicts plainly.

If outcomes depend on each other so closely that they cannot be separately owned, treat
them as one coherent goal under [Parallelization](PARALLELIZATION.md), or do them in
sequence. Use both workflows when appropriate: Multitasking divides the separate goals;
Parallelization divides independent work inside a goal.

Before writing user-facing or maintainer-facing prose, consult the relevant section of
the [wording dictionary](../dictionary/wording.md). The final report names each outcome,
its owner, integration and verification performed, and any unresolved dependency.

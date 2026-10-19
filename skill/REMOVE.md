# Remove

Retire a capability and the code that exists only to support it, without breaking
behavior users still rely on.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

## Choose the work pattern

For every request, assess whether independent parts of this removal can finish
faster in parallel, or whether separate requested outcomes merit multitasking.
Follow [Parallelization](PARALLELIZATION.md) for workers on one removal and
[Multitasking](MULTITASKING.md) for separate requested work. Prefer subagents;
use additional agents only after all four subagent slots are occupied, subject to
actual platform capacity. Keep one coordinator responsible for shared contracts,
integration, and final checks; assign non-overlapping files or work areas to avoid
conflicts. If delegation will save time, delegate instead of merely suggesting it.

## Check product fit and architecture

Before a broad removal, map the current and intended user journey and product core
loop: why users spend time here, what user or business value the capability
provides, and whether a relevant monetization model depends on it. Do not invent a
revenue case when monetization is irrelevant. For games, state how the capability
fits the reason to play and core play loop. For feed or recommendation behavior,
consider user outcomes, control, relevance, diversity, and tradeoffs; time spent or
engagement alone is not user value. Scale the plan to the change, but for broad work
map affected domain boundaries, data flow, contracts, state, failure behavior, and
operational effects before removing components.

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
cost.

## Workflow

1. **Define the removal.** Name the capability, surfaces, APIs, and users in scope.
   Identify what should happen in its place, if anything. Treat “unused” as a claim
   to verify, not an assumption.
2. **Check actual use.** Trace callers, imports, routes, dynamic registrations, flags,
   integrations, docs, and tests. Check production request counts and last-use dates
   over a stated period when available. Confirm whether the endpoint can respond and
   what its responses do. Static references alone do not prove runtime use; no recorded
   traffic does not prove non-use if logging is incomplete or external callers are
   possible. Mark each conclusion as confirmed, disproved, or unknown.
3. **Assess the impact.** Identify affected users, dependent systems, data, migrations,
   and rollback needs. If evidence shows meaningful use or cannot establish whether a
   public interface has external users, show the evidence and risk, then ask whether to
   proceed or stage a deprecation. Do not silently leave a second API or compatibility
   layer behind.
4. **Research removal and deprecation.** Read full,
   relevant, peer-reviewed papers from established scholarly publishers or proceedings
   (such as Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University
   Press, or ACM) or peer-reviewed university research. Company guides, vendor blogs,
   press releases, AI-written summaries, abstracts, and search snippets do not count;
   vendor documents may confirm vendor-specific facts. Record each paper's method,
   scope, finding, limitations, and relevance to the removal. Use the research to check
   impact, migration, and deprecation assumptions against actual project evidence. If
   fewer than three suitable full papers can be read for the task, report the gap and
   mark the research incomplete; do not pad the list. The three-paper minimum is a
   workflow requirement, not a research-established optimum.
5. **Remove the whole capability.** Delete its implementation and code used only by it.
   Update routes, configuration, navigation, docs, and tests. Preserve shared helpers
   and behavior that other features still use. Do not add unrelated cleanup.
6. **Check the result.** Verify the retired path is unavailable or gives the intended
   response, shared callers still work, and no references remain in the inspected
   surfaces. Run focused tests and inspect the diff. Be explicit about dynamic or
   external references that could not be checked.
7. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH, then verify each one. For a deployable app or service,
   test in staging before redeploying. If staging is missing, ask the user to create it
   or authorize access; wait for tests to pass before redeploying. Stop and report any
   failed push or check. State why staging does not apply to a non-deployable project.
8. **Report plainly.** State what was removed, evidence of use or non-use, the period
   and coverage of usage data, affected callers, checks, and remaining risks. Always
   report other material codebase problems found in the inspected scope, with examples
   and effects. Use the [wording dictionary](../dictionary/wording.md).

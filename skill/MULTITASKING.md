# Multitasking

Use this workflow when one user request contains several separate outcomes, such as a
frontend fix and an API fix, or work in two products. Assign a different agent to each
independent outcome so the work can move at once. Optimize for completed work per unit
of elapsed time; do not hold back agents merely to conserve headcount.

Follow [Session Control](SESSION_CONTROL.md) for the user's authority, live changes to
scope, session state, approvals, verification, and handoffs. A task assignment does not
give a worker broader permissions than the user or project granted.

## 1. Prepare the assignments

1. Break the request into separate user outcomes or independent evidence questions.
   For each, name the product or surface, relevant workflow (Build, Fix, Remove,
   Refactor, Audit, Review, or Investigate), owner, acceptance conditions, and evidence
   needed. When evaluating workflows, split by independent evidence questions or trial
   tasks, not mechanically by skill-file count; keep shared acceptance criteria and
   integrate the findings across the same product case.
2. Start subagents first. Use up to four subagent slots where the platform allows. Use
   other agents only after all four subagent slots are occupied, if independent work
   remains and the platform supports more agents. If the platform provides fewer than
   four subagent slots, use the available subagent capacity; do not substitute other
   agents for slots the platform does not provide. The active platform limit always
   applies.
3. Assign one worker to each independent outcome when capacity permits. If outcomes
   outnumber workers, group outcomes only when dependencies and interfaces make that
   faster; balance the work so no agent becomes a needless bottleneck. Don't give one
   agent multiple unrelated products just because it is simpler to dispatch.
4. Before dispatch, check shared APIs, schemas, design systems, data, deployment,
   production state, and file ownership. Agree on shared contracts first. If one task
   must settle an interface before another can start, dispatch the independent research
   or preparation first and sequence only the dependent implementation.

## 2. Give each worker the right context

Use one concise shared brief with the latest user request and corrections, overall goal,
scope, repository and base revision, project instructions, architecture and shared
contracts, acceptance conditions, available checks, the shared research map from
[Research](RESEARCH.md), and authorization boundaries. Then give each worker its own
outcome, owned files or resources, dependencies, relevant evidence, expected result,
and any user decision that blocks it.
Do not send unrelated history or ask every worker to repeat shared research. If research
is divided, assign distinct questions or evidence roles; return findings to the shared
map and synthesize their agreements, conflicts, and implications across outcomes. Mark
unknown facts clearly and refresh the brief when the user changes direction or source
state changes. See [Session Control](SESSION_CONTROL.md).

## 3. Track, integrate, and report

Track each outcome as active, waiting, blocked, finished, or under review using the
existing task view or one short task list. Each worker returns changed files or
artifacts, the revision, checks actually run, results, assumptions, and unresolved
issues. The coordinator integrates the outcomes, checks shared interfaces and behavior
across products, resolves conflicts, and verifies every acceptance condition against
the combined result. A worker's completion claim is evidence to inspect, not acceptance.

If the user redirects, pauses, resumes, or cancels an outcome, update its owner and the
shared brief, stop conflicting work, and preserve unrelated authorized tasks. See
[Session Control](SESSION_CONTROL.md) for precise rules. Do not send external messages,
publish, deploy, or change a shared runtime unless that action is authorized.

Use [Parallelization](PARALLELIZATION.md) within an outcome when it has independent
parts. If the outcomes depend too closely to have separate owners, sequence them rather
than forcing a split. Do not reduce agent count as a goal; use available capacity for
real, bounded work and account for integration in the completion time.

Before writing user-facing or maintainer-facing prose, consult the relevant section of
the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Report each outcome, its owner,
integration and verification, and unresolved dependencies plainly.

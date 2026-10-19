# Parallelization

Use this workflow when one outcome can be delivered sooner by assigning independent
parts of that outcome to multiple agents. The goal is shorter time to a correct,
integrated result, not fewer agents. When there is enough independent work, use the
available capacity; do not leave useful workers idle to save agent count.

Follow [Session Control](SESSION_CONTROL.md) throughout. The human remains in charge of
scope, permissions, and whether work continues. Parallel work does not grant authority
to any agent.

## 1. Build the shared task brief

Before dispatch, give the workers one concise, current brief containing:

- The user's requested outcome and latest corrections, plus what is in and out of scope.
- The target repository, branch or worktree, base revision, active owners, and relevant
  project instructions.
- The user or product outcome, acceptance conditions, architecture, existing behavior,
  shared interfaces, and dependencies that matter to the split.
- The shared research map from [Research](RESEARCH.md): each paper's distinct role,
  method, scope, finding, limitations, relationship to other papers, and product decision
  or quality check. Assign any research slices by question or role; workers must not
  collect three redundant papers each or skip synthesis between their findings.
- Available checks, evidence sources, authorized actions, and any decision that must
  wait for the user.

For evidence work, also share one compact evidence map. For each claim, record the
source and method, revision or time window, coverage and filters, what it establishes,
what it cannot establish, and the decision or check it informs. Assign distinct evidence
questions when useful, then integrate conflicts; do not let separate workers turn one
partial metric each into a whole-product conclusion.

Give each worker the relevant sources and paths, not the entire conversation or a pile
of unrelated project files. Mark unverified facts as unknown. Update the brief when the
user redirects the work or evidence changes an interface, dependency, or acceptance
condition. See [Session Control](SESSION_CONTROL.md) for authority and live-state rules.

## 2. Split for throughput

1. Map the work into independent deliverables, questions, components, or files. Identify
   the critical path and which work can start at the same time. Estimate elapsed time to
   an integrated, verified result with the proposed split and with the available
   sequential alternative; include dispatch, context setup, waits, integration, and
   whole-result checks. Use the split expected to finish sooner without sacrificing
   correctness. Compare the estimate with actual coordination time and rework.
2. Assign one owner to each independent deliverable. If seven files can be changed
   independently, use seven agents when capacity allows. If four agents are available,
   assign two files to three agents and one file to the fourth; if two are available,
   assign three files to one and four to the other. Use a different split when shared
   interfaces or dependencies make a component grouping faster or safer.
3. Start subagents first. Use up to four subagent slots where the platform allows. Use
   additional agents only after all four subagent slots are occupied, if independent
   work remains and the platform supports more agents. If the platform provides fewer
   than four subagent slots, use the available subagent capacity; do not substitute
   additional agents for slots the platform does not provide. The active platform
   limit always applies.
4. Give every worker the same goal and brief, then specify its owned deliverable, files
   or question, dependencies, interface contract, acceptance checks, and expected
   evidence. Ask agents to return early when they find a conflict or changed
   dependency; reassign the work before parallel edits collide.
5. Start independent work promptly. Track owners and status in a small task list so the
   coordinator can see what is active, waiting, blocked, finished, or needs review.
   Do not create a new registry or status report when the app's task view already shows
   it.

## 3. Integrate and verify the whole result

Each worker reports the files or artifacts changed, exact revision, checks actually
run, results, assumptions, and unresolved issues. Workers handling research report what
their source adds or challenges in the shared map. The coordinator integrates findings,
resolves disagreements between papers and shared-contract conflicts, and checks the
combined behavior against the original acceptance conditions. Review worker claims
against the actual change; do not treat a confident summary or a passing test as proof
of completeness or quality. Run the checks that apply to the combined result, then
report what was not verified.

Use one owner per shared file. If agents have isolated worktrees, integrate their
changes explicitly before final checks. Do not let agents independently publish,
deploy, alter shared runtime state, or contact others without authorization for that
action. Pause, redirect, or cancel work as the user directs; see
[Session Control](SESSION_CONTROL.md).

Parallelization and [Multitasking](MULTITASKING.md) can be combined: multitasking
separates user-requested outcomes; parallelization divides independent work within one
outcome. When work is genuinely sequential, assign it in dependency order while keeping
other independent work moving. Do not reduce agent count as an end in itself, and do not
create artificial work just to fill slots.

Before writing user-facing or maintainer-facing prose, consult the relevant section of
the [wording dictionary](../dictionary/wording.md) and [AI writing habits](../dictionary/habits.md).
Keep the handoff factual and concise.

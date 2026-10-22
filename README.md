# Compress

Compress provides separate instructions for common software tasks. It is a set of task workflows, not one general-purpose agent skill.

## How to use it

1. Choose the workflow that matches the task.
2. Provide the workflow and its shared references: [session control](skill/SESSION_CONTROL.md),
   [research](skill/RESEARCH.md), and the relevant part of the [wording
   dictionary](dictionary/wording.md) plus [AI writing habits](dictionary/habits.md)
   when the agent writes prose. Apply the mandatory [quality scan](skill/QUALITY_SCAN.md)
   to every software task, including narrow changes and read-only work. If the agent
   cannot access this repository, include those references with the task.
3. Include the target repository, latest user direction, relevant project instructions,
   current branch/revision, upstream divergence, constraints, and actions already
   authorized. Before delegating or editing, record staged, unstaged, and untracked paths;
   treat every pre-existing change as protected work and assign it an owner. If the branch
   is behind or dirty paths overlap incoming commits, compare and reconcile those changes
   before moving refs. Check the actual workspace and sandbox limits before deciding the
   repository is unavailable; follow [Session Control](skill/SESSION_CONTROL.md). Provide
   available evidence, such as
   production usage data for an API audit. If data is missing, mark only the related
   claim as unknown and continue the product-value assessment from its purpose, working
   behavior, outputs, and other available evidence.
4. Load another task workflow only if the task genuinely crosses into it. For a chain, carry one shared task brief and research note forward; do not load every workflow or repeat the same research.

If the task type is unclear, describe the desired outcome first and choose the workflow that best matches it.

When the user assigns ongoing responsibility for a project, or asks whether it is
clean, healthy, or production-ready, start with a project baseline using [Audit](skill/AUDIT.md)
and [Quality scan](skill/QUALITY_SCAN.md) before handling a narrow follow-up. Review
the README and codebase, compare languages and conventions with the user's related
projects when available, and trace a representative frontend journey through its APIs
and dependencies. Verify live behavior and performance where authorized. Separate
frontend, API, and dependency timings, and report unavailable evidence. Carry this
stewardship context into later tasks until the user changes it.

Do not assume the sandbox is empty or that a repository must be missing because it is
not in the current directory. Inspect the current checkout, allowed workspace roots,
attached projects or worktrees, and available repository connectors. In Codex, check
whether the task is using a local checkout, managed worktree, or isolated cloud
workspace; the user's desktop paths may not be mounted in a cloud task. If the needed
repository or files are outside the allowed environment, request approval for the
specific access or operation through the platform. State the path and why access is
needed; do not request broad access by default. A remote 404 can mean the project is
private or the current account lacks access. Check the owner, repository name, and
available authenticated routes before saying it does not exist. If access remains
unavailable, report what you checked and the exact permission or input needed. Do not
claim that no files are available without checking the workspace.

Search related files and product surfaces for the same issue, not just the reported
example. BUILD, FIX, REMOVE, REFACTOR, and INVESTIGATE must fix confirmed, in-scope instances
and verify none remain; if one cannot be fixed, state which and why. AUDIT and REVIEW
report findings without changing files. Treat related
repetitions of the same underlying problem as part of the task; separate, unrelated
problems may be reported without absorbing them into the current work. Define scope by the affected product journey and its dependencies, not by repository
boundaries alone. Check related repositories when shared ownership, repeated code,
language or toolchain choices, or service integration bear on the question. If a fix
crosses into a separately owned product or service, establish the user's authority and
the technical boundary before changing it; ordinary in-scope changes do not need
another approval.

Research is required in every workflow. Follow the [Research protocol](skill/RESEARCH.md):
use at least three full, relevant peer-reviewed papers across the task, then scale the
set to the number of workflows and distinct product questions. For a broad evaluation,
aim for one to three useful papers for each workflow or evidence question. Choose work
that studies the actual product domain; generic software papers cannot replace research
on the field the product serves. Papers must add distinct evidence, challenge or qualify
one another, and change a product check or decision. Report when research is incomplete;
do not pad the set or claim a product improvement without checking it.

## Why the workflow uses research

The source findings have limits. SWE-bench uses issues from 12 Python repositories and
tests both requested fixes and regressions; its authors caution that passing tests alone
does not guarantee comprehensive, efficient, or readable code. Instruction Induction
studies 24 mostly simple language tasks and reports prompt and model sensitivity, so it
does not validate software workflow instructions. Chen et al. study in-context examples
on benchmark tasks and find that extra examples can add little or interfere; that does
not prove that papers or repository context should be minimized. Together, these
findings support relevant context, explicit checks, and separate code quality review.
[SWE-bench](https://proceedings.iclr.cc/paper_files/paper/2024/file/edac78c3e300629acfe6cbe9ca88fb84-Paper-Conference.pdf),
[Instruction Induction](https://aclanthology.org/2023.acl-long.108.pdf),
[Chen et al.](https://aclanthology.org/2023.findings-emnlp.745.pdf).

## Product purpose and architecture

Before a product-level change, name the user and need, where the change fits in the
existing journey, why it merits the user's time, and the outcome that would show it
helps. For a game, explain how it supports the core play loop or gives players a clear
reason to return. Consider monetization or business value when relevant; do not invent
a revenue rationale for every feature. For changes spanning services, data, or user
flows, first map the smallest useful architecture: responsibilities, data flow,
interfaces, state, failure paths, and operating needs. Scale the plan to the change;
do not add planning documents for a one-line fix.

Keep the product UI focused on helping its users complete their tasks. Do not put
assistant explanations, chat answers, or narration about the requested implementation
into the product as explanatory copy. Add text only when it serves the product flow,
such as a necessary instruction, status, or error, and follow the user's requested
wording. Explain completed work in the conversation instead.

Research on recommenders and game motivation does not establish one universal product
pattern. Research on recommender control describes usability and trust barriers; work
on preference pollution explains how recommendations can shape the data later systems
learn from. Game motives vary, so no mechanic guarantees enjoyment or retention. For
feeds and recommendations, treat relevance, variety, user control, satisfaction, and
harms as separate questions; engagement is a signal, not proof of user benefit. Use a
familiar repeatable experience only when it helps users find value, and give them ways
to correct or limit what the system learns from them.

The evidence is bounded: one recommender-control study surveyed small groups of Amazon
users; the preference-pollution paper is a conceptual synthesis rather than a controlled
product trial; a game-motives scale was validated with two country samples and may miss
genre-specific motives. These sources suggest questions and checks, not a proven recipe
for this product. [Jannach et al. on recommender control](https://web-ainf.aau.at/pub/jannach/files/Conference_EC_Web_2016.pdf),
[Adomavicius on preference pollution](https://onlinelibrary.wiley.com/doi/10.1002/aaai.12055),
[Vahlo and Tuuri on player motives](https://link.springer.com/article/10.1007/s11257-025-09431-7),
[Krath et al.'s gamification research review](https://www.sciencedirect.com/science/article/pii/S0747563221002867).

A 2026 audit of TikTok's feed used automated accounts that repeatedly liked, rewatched,
and followed content in only two domains. It found rapid amplification of aligned
content and a tradeoff with hashtag diversity. Because the bots behaved unlike varied
human users and the study covered only Gaming and Food in the US, it describes those
experimental conditions, not a design recipe or proof of TikTok's effects on people.
Treat recognizable patterns and interest-based ranking as hypotheses; pair them with
user control, exploration, and measures of user-valued outcomes. [TikTok feed audit in
EPJ Data Science](https://link.springer.com/article/10.1140/epjds/s13688-026-00629-2).

## Divide work when it helps

Every workflow must assess whether independent work would finish sooner with multiple
workers. Use [Parallelization](skill/PARALLELIZATION.md) for independent parts of one
goal, and [Multitasking](skill/MULTITASKING.md) for separate requested outcomes. Start
subagents first; use additional agents only after all four subagent slots are occupied
and the platform permits more. Give each worker a bounded scope and clear ownership;
when delegation will save time, do it rather than only recommending it. The coordinator
integrates the work and checks the whole result. Do not split tightly coupled files just
to maximize the number of workers.

## Control work and permissions

The user can redirect, pause, resume, or cancel active work. Follow
[Session Control](skill/SESSION_CONTROL.md) for the shared rules on context, authority,
approval, status, cancellation, verification, and handoff. Invoking a code-changing
Compress workflow is the user's standing authorization to complete its normal release
path: test the change, commit it, push it to every configured remote, test in staging,
and redeploy the affected service when the workflow calls for a release. Do this without
waiting for a separate invitation or asking for release approval. This covers only the
requested product, its configured remotes, and its established deployment targets; it
does not authorize unrelated work, force-pushing, production data erasure, or bypassing
platform approval gates. Follow the workflow's staging and production sequence. For
read-only AUDIT and REVIEW tasks that produce no code changes, report findings without
creating a commit.

### Release completion invariant

A feature-branch push, open pull request, temporary worktree, private temporary
directory, or uncommitted local edit is never sufficient to call code work complete.
These are intermediate work or review locations only. For deployable code, completion
requires all of the following: run and pass the relevant tests and required checks;
commit the reviewed result; integrate it into the repository's documented production
branch (normally `main`, unless the user or project specifies another target); push that
branch to every configured production remote; pass the required staging checks; deploy
the affected production service through its established deployment target; then verify
the deployed revision, service health, and relevant safe user behavior against the live
service. Treat “push to production” as publishing the integration branch to all
configured production remotes, and treat deployment and post-deploy verification as
separate required steps. A branch push, merge, CI run, or deploy command alone does not
prove the change is complete or live. Do not report completion until every applicable
step and check has passed.

If a required step fails or needs a trusted external fact, keep the task active or
waiting on that exact dependency, preserve the candidate commit and evidence, finish
independent work, and say which release steps remain. Never call the task done because
one remote received a branch, a private temporary location contains the fix, or the
service looks healthy before the new revision is verified. For a repository with no
deployable service, complete and pass local checks, commit on its integration branch,
push that branch to every configured remote, verify the result, and state why staging
and deployment do not apply.

## Commit messages

Write a concise commit subject that names the change and affected area. Use a
Conventional Commit type and a short scope when it makes the area clear, followed by
an imperative description. Keep the subject specific enough to explain the resulting
behavior without reading the diff. For example:

```text
fix(frontend): align recovery check with retired TI route
feat(api): record VM password reveal events
refactor(vms): group secondary row actions in menu
```

Choose the type that matches the work (`fix`, `feat`, `refactor`, `docs`, `test`,
`build`, or another established type in the repository). Do not use vague subjects
such as `updates`, `fix stuff`, or a ticket number alone. When a task spans multiple
repositories, commit each repository's scoped changes separately with subjects that
describe that repository's change.

## Evaluate the workflows

These instructions are proposals until they improve real work. Keep the previous
version and compare it with the revision on a small set of representative tasks: a
feature, a defect, a cross-component change, and an audit or handoff. Hold the tasks,
acceptance conditions, and available checks steady. Record task completion and
correctness, regressions, confirmed duplicate or dead work, rework, elapsed time
including coordination and research, number of human interventions, and loaded context
when observable. Judge code value from reviewed behavior and user need, not line counts.
Report missing measurements and tradeoffs. Keep, revise, or remove a rule based on the
comparison; a paper citation or one successful task does not show that this workflow
helped.

## Workflows and shared guides

- [Build](skill/BUILD.md) — add or extend a requested capability.
- [Fix](skill/FIX.md) — correct a specific defect.
- [Remove](skill/REMOVE.md) — retire an unwanted capability and its supporting code.
- [Refactor](skill/REFACTOR.md) — restructure code while preserving behavior the user still wants.
- [Audit](skill/AUDIT.md) — assess system-wide usage, value, and maintenance cost.
- [Review](skill/REVIEW.md) — evaluate a proposed change.
- [Investigate](skill/INVESTIGATE.md) — answer a question and finish the directly related fixes it reveals.
- [Parallelization](skill/PARALLELIZATION.md) — divide one coherent goal into independent work.
- [Multitasking](skill/MULTITASKING.md) — assign separate requested outcomes to separate owners.
- [Session Control](skill/SESSION_CONTROL.md) — keep the user in control across active work, decisions, and handoffs.
- [Research](skill/RESEARCH.md) — choose, compare, and apply a useful set of papers.
- [Quality scan](skill/QUALITY_SCAN.md) — check code, names, and README quality in
  scope on every software task.

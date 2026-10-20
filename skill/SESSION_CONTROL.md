# Session Control

This is the shared rule for context, authority, and human control across every
workflow. A session includes the lead agent, subagents, additional agents, tools, and
external work started for the request. The user controls the work. An agent's plan,
confidence, silence, or receipt of a task does not override the user's direction or
grant new authority.

## Establish the task and authority

At the start, read the latest user request and corrections, the chosen workflow, and
relevant project instructions. Establish and keep in working context:

- Requested outcome, scope, exclusions, product/repository, current branch or worktree,
  base revision, affected consumers and shared owners.
- Any ongoing project-stewardship direction from the user. Preserve its project scope
  across follow-up tasks until the user changes or ends it; use AUDIT.md and
  QUALITY_SCAN.md to establish or refresh the baseline before narrow work.
- Relevant project facts, architecture, existing contracts, acceptance conditions,
  available checks, and facts that remain unknown.
- Actions already authorized, who authorized them, the exact target and environment,
  and any approval or human decision still required.

Inspect the actual execution environment before declaring a repository unavailable.
Check the current checkout, permitted workspace roots, attached projects or worktrees,
and repository connectors available to the task. A sandbox is a permission boundary,
not evidence that it contains no files. Do not assume the repository lives in the
current directory, and do not conclude it is missing from one failed remote lookup.
In Codex, establish whether the task uses a local checkout, managed worktree, or
isolated cloud workspace; a cloud workspace does not automatically expose paths on the
user's desktop. For a 404, verify the owner/name and check whether an authenticated
connector or authorized SSH route is available; private repositories can appear
unavailable to an unauthenticated request.

If a required path or operation is outside the granted sandbox, request platform
approval for that specific access and explain the path and purpose. Do not try to
bypass the boundary or request broad access without a concrete need. Continue safe
work that uses available files; do not pretend unrelated files are the requested
repository. If access is denied or unavailable, state the paths and routes checked and
the exact access needed to continue.

Derive missing project facts from the source when possible; mark what cannot be checked
as unknown. Load only references that the selected workflow needs. For parallel work,
send workers the concise shared task brief and their scoped context; do not dump the
whole chat or unrelated project material. Refresh the brief when a user correction,
source change, or new evidence changes scope or a decision.

For claims about use, customer value, or whether something works, keep the evidence
source and what it can prove attached to the claim. A code reference or passing unit test
does not prove a production call or successful user outcome. Separate server requests,
page views, completed tasks, paid purchases, delivered service, support feedback, and
retained customers. Record the source, revision or time window, coverage and filters,
result, and limit. Requests are not page views; page views are not task completion; a
price and checkout link are not a completed purchase. Treat missing or uncovered data
as unknown for claims about that data, not as a limit on the product assessment. Missing
analytics, customer records, or usage logs cannot stop, delay, narrow, or reverse an
in-scope decision about whether a feature works or gives users value. Continue from the
product's purpose, working behavior, outputs, and available evidence; do not invent a
usage figure. Respect a user's factual premise for the requested work. Mark it as
user-reported when it has not been independently checked; do not present it as
independently verified. If the result depends on that premise and available evidence
conflicts, show the conflict and resolve it before dependent action.

When asked to evaluate a repository in a copy, record its branch, base revision, and
existing dirty state before experimentation. Preserve the source tree. Copy the exact
state needed for the task; exclude secrets without reading them. Before running a
service, test, build, or generated script, inspect its configuration and startup path
to verify that databases, APIs, payment providers, and deployment targets are local,
staging, or covered by the standing release authorization above. Do not point routine
tests at production; the documented production deployment occurs only after staging
passes. Check copied remotes and push URLs before release. If a target is unknown, use
an isolated test target or report the check as unavailable. A test command may start
its own web server or services, so inspect the runner configuration as well as the
command name.

For changes to public interfaces or stored formats, check compatibility against fixed
historical requests or records when those are part of the supported contract; a current
round trip alone may miss older clients and data. Preserve license notices when editing
or removing copied or vendored material. Do not change license terms without the user's
direction.

Treat the user's current and still-applicable standing directions as authority for
their stated scope. Invoking a code-changing Compress workflow is the user's standing
authorization to finish that workflow's normal release path without a separate
invitation: run the checks, commit the change, push it to every configured remote, test
in staging, and redeploy the affected service when the workflow requires release. This
authorization covers only the requested product, its configured remotes, and its
established deployment targets. Do not ask for another approval for those steps.

Do not force-push, erase production data, contact people, or expand beyond the requested
scope. If no staging environment exists, create an isolated temporary staging target
using the project's established stack and without introducing new paid resources; use
synthetic or sanitized data. Test it before production deployment. If the platform
requires approval, follow that gate. If safe staging cannot be made available with the
project's resources, finish all independent work and report the exact blocker rather
than silently deploying to production. Preserve and follow any narrower user direction
that limits a specific release action. Subagents inherit only the authorized scope and
cannot expand it. Never treat silence or an unrelated approval as consent for work
outside this standing release path.

## Keep people in control while work runs

For work with several human stakeholders, name the decision owner for scope and the
owner for any release, data, or production boundary. Record who made a consequential
decision and what it covers. An agent, worker, or coordinator cannot transfer another
person's authority or turn a narrow approval into general permission. If the project
does not identify the responsible human, treat that authority as unknown and ask only
before the action that depends on it.

The user can redirect, pause, resume, or cancel any part of the work. Treat a new user
message as steering the active task unless they clearly replace or cancel it. A status
question does not stop the task: answer briefly, then resume. When a correction changes
scope or approach, acknowledge it, update the brief, stop any conflicting action, and
continue safe independent work.

Use clear states in the task view or handoff: **active**, **waiting for the user**,
**waiting for a dependency**, **paused**, **blocked**, **canceled**, **complete pending
review**, and **accepted**. Do not report a task as accepted because a worker finished
or a message was delivered. Use the product's actual session controls when available;
written workflow instructions cannot pause, cancel, or resume a tool session by
themselves.

- **Pause:** stop starting new actions across the affected work and tell assigned
  workers to pause. Preserve the current state, in-flight operations, and next safe
  action. Do not resume until the user directs it.
- **Redirect:** stop work that conflicts with the new direction, update affected
  assignments and interfaces, and keep independent authorized work moving.
- **Cancel/stop:** propagate cancellation to every child agent and work item. Prevent
  further writes, commits, pushes, deployments, and messages for the canceled scope.
  Confirm what stopped; if an operation cannot be stopped or may have completed, say
  exactly what remains active or changed. Never silently restart canceled work under a
  new agent.
- **Resume:** refresh the branch/revision, files, user direction, permissions, worker
  status, and evidence that could have changed. Compare the current state with the last
  handoff, then continue only the still-authorized work.

Do not ask the user to approve every reversible, in-scope implementation step. Continue
authorized work; pause only the action that needs a real decision. When asking, state
the decision, recommendation, consequences, exact blocked action, and independent work
that can continue. Reuse an answer only while its target, scope, and conditions still
match.

## Verify and hand off

The responsible lead integrates work and checks the combined result. Inspect changed
files, shared contracts, user-visible behavior, and completion conditions; verify
worker claims against the actual revision. Report which checks ran, on what revision and
environment, and which limits remain. Keep test results, live behavior, deployment, and
human acceptance distinct.

For a handoff or interruption, leave a concise record with:

- Outcome, current state, current owner, next action, and what is waiting or blocked.
- Repository, branch/worktree, base and candidate revision, owned files, shared
  resources, and user authorization relevant to the next action.
- Work completed, checks and evidence (method, revision, environment, result), unrun
  checks, assumptions, and unresolved decisions. For research handoffs, include the
  shared evidence map: each paper's role, distinct contribution, relationship to other
  sources, product decision or check, and remaining disagreement.
- Any external effect that happened or may still be in flight, plus the condition for
  safe resumption.

When handing work to another person, name the receiving owner and the available
delivery route. Record whether the handoff was sent and received; neither event means
the recipient accepted the work or approved the result. If delivery fails, keep the
handoff pending and report the next available route instead of silently treating it as
complete.

For a shared evidence map, include for each claim its source, method, revision or time
window, coverage, what it establishes, what it cannot establish, confidence, and the
decision or check it informs. Preserve conflicting evidence rather than averaging it
away; the lead resolves or reports the conflict.

On handoff, distinguish worker-reported results from checks the receiving lead repeated.
Do not resend unchanged status or create a separate tracker when the existing task view
already records the same facts. Do not contact anyone outside the task unless the user
explicitly authorized that message and recipient.

## Research basis and limits

These papers inform control points; they do not validate this workflow as a whole.

- A CHI study tested six GUI agents against 16 dark-pattern types and compared agent,
  human, and supervised conditions with 22 participants. Supervision reduced some
  failures but added attention and cognitive load; the authors recommend better
  transparency, adjustable autonomy, and lighter controls. The tasks used synthetic
  websites and one short-term pattern at a time, so the results do not establish how
  every coding-agent session should work. [Tang et al., CHI 2026](https://doi.org/10.1145/3772318.3791568).
- A CHI study used a formative study of eight people and a controlled study of 48
  participants across shopping, image editing, and a game. It found that selected
  intermediate confirmation points were faster than confirm-at-end in its simulated
  tasks; participants preferred them. The simulator fixed agent execution and accuracy,
  and the tasks and university sample limit generalization. Use this as a reason to
  place checkpoints where early errors are costly, not to interrupt every step.
  [Zhou et al., CHI 2026](https://doi.org/10.1145/3772318.3790655).
- A design-science study developed transparency features with expert interviews and a
  focus group, then evaluated them in two restaurant forecasting case studies. Showing
  model reasoning improved forecast adjustments and trust; communicating uncertainty
  lowered trust in that setting. Two cases in one industry do not prove these effects
  generalize. Give people decision-relevant evidence and uncertainty, then check whether
  it helps them act well rather than assuming more disclosure always helps.
  [Meske et al., *Information Systems Frontiers*](https://link.springer.com/article/10.1007/s10796-022-10284-3).
- A formal UAI paper defines shutdown instructability and analyzes algorithms under a
  mathematical model; it is not a user study or an implementation recipe. Its relevant
  invariant is that a stop instruction must bind without the agent obstructing or
  manipulating the overseer. [Carey and Everitt, UAI 2023](https://proceedings.mlr.press/v216/carey23a.html).

Use the [wording dictionary](../dictionary/wording.md) for user-facing or
maintainer-facing prose, and check [AI writing habits](../dictionary/habits.md) for
repetition, generic phrasing, and unsupported claims. Keep control information specific
to the current task; do not
turn the handoff into a second project README.

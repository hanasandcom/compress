# Changeset ownership

Use this guide whenever a repository is dirty, multiple workers contribute, or the
integration branch is behind its upstream. The coordinator remains responsible for
the whole result; each pre-existing and newly created path has one accountable owner.

## Establish the ledger before edits

Record the repository root, branch, `HEAD`, upstream, remotes, ahead/behind counts,
and complete staged, unstaged, and untracked path lists. Include deletions and
renames. Use `git status --porcelain=v1 -z` or an equally complete source; a summary
count, `git diff --stat`, or remembered list does not replace the path inventory.

Create one task-side ownership ledger. It can live in the task brief or a temporary
handoff note; do not add a project file just to hold routine coordination state. For
each path (or a truly exclusive path prefix with its exceptions listed), record:

| Path | Baseline state | Owner | Related paths | Worktree and base | Checkpoint / evidence | Status |
|---|---|---|---|---|---|---|

Include related tests, fixtures, docs, generated inputs, and callers in the same
owner's scope. A worker's narrow task description does not implicitly transfer
ownership of adjacent dirty work. The coordinator owns every unassigned path until it
is expressly handed off. Do not label unknown work disposable; preserve it and find
its owner or intent.

## Isolate writers and keep checkpoints small

When two or more agents may edit files concurrently, give each an isolated worktree
based on the same recorded revision. A dirty shared checkout is coordinator-only;
workers may inspect it but must return changes from their own worktrees. Use a shared
checkout for editing only when work is serialized, its writer is named, and the
ownership ledger is current. Never assign the same path to two writers. For shared
interfaces, designate one owner and have other workers return proposals.

Each worker reports newly changed paths as soon as its scope expands and records a
verified, coherent commit checkpoint before starting unrelated work or handing off.
The integrator reviews each checkpoint against the worker's baseline and owned paths
before integrating it. Keep integration serialized. Do not leave a broad batch of
uncommitted edits accumulating across work sessions. A newly dirty path with no owner
pauses edits that could conflict with it until the ledger is updated.

## Reconcile a dirty or stale branch

Before merge, rebase, pull, cherry-pick, reset, or other ref movement:

1. Refresh the full status and divergence baseline; compare the exact changed paths
   with every incoming commit's changed paths.
2. For each overlap, inspect the incoming and local hunks, callers, tests, and intent.
   Classify it as duplicate, complementary, conflicting, or unknown in the ledger.
3. Preserve a recoverable snapshot of all owned changes before integration. Never use
   `reset --hard`, `clean`, blanket restore, or force-push to manufacture a clean tree.
4. Integrate one reviewed ownership slice at a time on the documented integration
   branch. After each slice, update its revision, checks, and remaining work in the
   ledger; then compare the actual tree with the ledger again.
5. Stop ref movement if any path, commit, or incoming behavior is unowned or
   unexplained. Continue independent work; resolve only the affected ownership
   decision before touching that slice.

Do not infer that an agent owns a change from its author name, recent activity, or
file location. Ask the active task owner and inspect its worktree, commit, or patch.
If the owner cannot be reached, keep the change protected and mark it waiting; do not
delete or silently absorb it.

## Close the ledger

Before calling integration clean, refresh the ledger from the actual repository and
verify all of the following independently:

- Every baseline and newly changed path has an explicit disposition: integrated,
  intentionally retained, or released by its owner with evidence.
- Every integrated path is reviewed against its assigned baseline and required
  related paths; no two workers edited it concurrently.
- The integration branch is based on the intended upstream, its ahead/behind counts
  are expected, and both configured production remotes are reconciled where required.
- Staged, unstaged, and untracked task paths match the ledger; no unexplained changes
  remain. A clean status on a stale branch is not clean integration.
- Required checks and deployment evidence are attached to the exact integrated
  revision, not an earlier worktree or a different candidate.

Record unresolved work as active, waiting, or blocked with its owner and next action.
Do not report full completion while any required ledger row is unknown or incomplete.

## Research basis and limits

Three complementary studies inform these controls. Dias, Borba, and Barreto analyzed
73,504 merge scenarios from Ruby/Rails and Python/Django projects. Conflicts were more
likely when larger, longer-lived contributions touched the same MVC slice; this
supports narrow owned scopes and timely checkpoints, but its project and language
sample does not establish a universal threshold. Brindescu et al. analyzed 556,911
commits across 143 open-source projects: 19.32% of observed merges had conflicts, and
conflict-involved code was more likely to receive later bug fixes. Semantic conflicts
were riskier than trivial ones, so overlapping behavior needs review and relevant
checks, not just a textual merge. Vale et al. studied 2,972 conflicting contributors
across 66 GitHub projects; conflict involvement was concentrated among a small group
and a small set of files. This supports naming owners and assigning the integrator
explicitly, rather than assuming authorship or spreading responsibility across every
worker.

These are observational studies with different project samples and conflict
definitions. They support early ownership, smaller checkpoints, and focused integration
review; none proves that a ledger or isolated worktrees can prevent every conflict.

- Dias, Borba, and Barreto, [Understanding predictive factors for merge conflicts](https://doi.org/10.1016/j.infsof.2020.106256), *Information and Software Technology* 121 (2020). [Full paper](https://pauloborba.cin.ufpe.br/publication/2020understanding_predictive_factors_for_merge_conflicts/2020ISTPredictiveFactorsForMergeConflicts.pdf).
- Brindescu, Ahmed, Jensen, and Sarma, [An empirical investigation into merge conflicts and their effect on software quality](https://doi.org/10.1007/s10664-019-09735-4), *Empirical Software Engineering* (2020). [Full paper](https://ics.uci.edu/~iftekha/pdf/J4.pdf).
- Vale, Fernandes, Figueiredo, and Apel, [Behind developer contributions on conflicting merge scenarios](https://doi.org/10.1109/SCAM59687.2023.00014), *IEEE SCAM* (2023). [Full paper](https://homepages.dcc.ufmg.br/~figueiredo/publications/scam2023preprint.pdf).

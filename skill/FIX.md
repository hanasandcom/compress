# Fix

Correct a specific defect with the smallest change that addresses its cause.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

When changing workflow guidance, inspect all seven workflow files for the same issue
and update every file where the change applies; workflows may be loaded by themselves.

## Workflow

1. **Define the failure.** Record what should happen, what happens instead, who or what
   is affected, and a reliable reproduction. Separate observed facts from guesses.
2. **Trace the path.** Follow the failing request or action through its entry point,
   implementation, dependencies, and callers. Check recent changes, existing tests,
   logs, and similar working behavior before editing.
3. **Prove the cause.** Reproduce the defect or identify direct evidence for it. Check
   relevant official documentation, issue reports, or release notes when the cause
   depends on framework or dependency behavior. Do not replace the symptom with a
   fallback until you understand why it occurs.
4. **Research and compare approaches.** For every fix, read at least three full,
   relevant, peer-reviewed papers from established scholarly publishers or proceedings
   (such as Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University
   Press, or ACM) or peer-reviewed university research. Company guides, vendor blogs,
   press releases, AI-written summaries, abstracts, and search snippets do not count;
   vendor documents may confirm vendor-specific facts. For each paper, record its
   method, scope, finding, limitations, and relevance to the failure. Also inspect how
   mature products solve it and what users or maintainers criticize. Check whether a
   seemingly better approach fits this product's constraints. If three suitable full
   papers cannot be read, report the gap and mark the research incomplete; do not pad it.
   Three is a workflow minimum, not a research-established optimum.
5. **Fix only the defect.** Make the smallest complete change that corrects the cause.
   Reuse the existing behavior where it fits. Do not add a parallel API, broad cleanup,
   or speculative fallback. If you find material bloat or a separate quality problem,
   always show examples and their impact; ask before expanding the fix to address it.
6. **Check the correction.** Add or update a focused regression check when appropriate.
   Verify that the original failure is gone and that important neighboring behavior
   still works. Read relevant CI results when available. Do not claim a check passed if
   it was not run.
7. **Release code changes.** After local checks pass, commit and push to every
   remote over SSH; verify each remote. For a deployable app or service, run
   server-side tests in staging before redeploying. If staging does not
   exist, ask the user to create or authorize it and wait; do not redeploy before staged
   tests pass. If a push or test fails, report it and stop. For non-deployable projects,
   state why staging does not apply.
8. **Report plainly.** State the cause, the correction, the checks that ran, and any
   remaining uncertainty. Always report material codebase problems found in the
   inspected scope, with concrete examples and effects. Use the [wording
   dictionary](../dictionary/wording.md); do not pad the report.

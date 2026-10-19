# Remove

Retire a capability and the code that exists only to support it, without breaking
behavior users still rely on.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

When changing workflow guidance, inspect all seven workflow files for the same issue
and update every file where the change applies; workflows may be loaded by themselves.

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
4. **Research removal and deprecation.** For every removal, read at least three full,
   relevant, peer-reviewed papers from established scholarly publishers or proceedings
   (such as Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University
   Press, or ACM) or peer-reviewed university research. Company guides, vendor blogs,
   press releases, AI-written summaries, abstracts, and search snippets do not count;
   vendor documents may confirm vendor-specific facts. Record each paper's method,
   scope, finding, limitations, and relevance to the removal. Use the research to check
   impact, migration, and deprecation assumptions against actual project evidence. If
   three suitable full papers cannot be read, report the gap and mark the research
   incomplete; do not pad the list. Three is a workflow minimum, not a
   research-established optimum.
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

# Remove

Retire a capability and the code that exists only to support it, without breaking
behavior users still rely on.

Before writing or changing user-facing or maintainer-facing prose, consult the matching
section of the [wording dictionary](../dictionary/wording.md). Apply its natural
examples only when they fit the facts; do not mechanically replace words or load all
164 pairs when one section answers the question. Check the final report and any prose
you added against the dictionary.

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
4. **Remove the whole capability.** Delete its implementation and code used only by it.
   Update routes, configuration, navigation, docs, and tests. Preserve shared helpers
   and behavior that other features still use. Do not add unrelated cleanup.
5. **Check the result.** Verify the retired path is unavailable or gives the intended
   response, shared callers still work, and no references remain in the inspected
   surfaces. Run focused tests and inspect the diff. Be explicit about dynamic or
   external references that could not be checked.
6. **Release code changes.** After local checks pass, commit and push to every
   configured remote over SSH, then verify each one. For a deployable app or service,
   test in staging before redeploying. If staging is missing, ask the user to create it
   or authorize access; wait for tests to pass before redeploying. Stop and report any
   failed push or check. State why staging does not apply to a non-deployable project.
7. **Report plainly.** State what was removed, evidence of use or non-use, the period
   and coverage of usage data, affected callers, checks, and remaining risks. Always
   report other material codebase problems found in the inspected scope, with examples
   and effects. Use the [wording dictionary](../dictionary/wording.md).

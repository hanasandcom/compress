# Quality scan

Apply this check to every software task, including a small rename, documentation
change, investigation, or code review. A narrow request limits what you change; it does
not excuse overlooking a clear quality problem in the work area. Keep the scan
proportional: inspect the changed files, their direct callers and references, the
nearest related implementation, and the repository README. Do not claim a whole-repo
review from that sample.

## Inspect three things

### Code

Check whether the relevant code is correct for its contract and easy to understand and
change. Look for concrete problems such as duplicated behavior, tangled control flow,
unnecessary layers or configuration, dead code, unclear ownership, weak error handling,
unsafe boundary handling, missing meaningful checks, and conventions that make nearby
code harder to work on. Read enough callers and tests to understand the effect. Linters,
complexity scores, test counts, and passing tests can point to evidence; none alone
establishes good or poor code.

### Names

Check names at the level the task touches: repositories, directories, files, packages,
services, APIs, types, functions, variables, environment settings, and tests. A useful
name identifies the responsibility, fits the project's domain language, and avoids
words that are already clear from its parent context. Look for names that are stale,
misleading, ambiguous, unnecessarily long, or needlessly repetitive. For example, in a
`mail-server` repository, `mail-relay/` may be clearer as `relay/` if there is no other
relay and the shorter path matches how operators refer to it. Confirm references,
deployment scripts, Compose project names, image names, public APIs, and external
consumers before renaming; keep a compatibility path or migration when a rename would
break a real contract. Do not shorten names just to save characters.

### README and local documentation

Read the root README even when the requested change is elsewhere. Check whether it says
what the project does and who it serves, describes the repository's actual boundary,
and gives correct, usable setup, development, test, and deployment steps for its
audience. Check links, paths, commands, names, service ownership, and claims against the
current source and repository metadata. Look for stale instructions, contradictions,
missing steps that block the advertised task, duplicated sections, vague project
descriptions, and prose that hides important boundaries. Inspect the relevant nearby
docs as well. Repair README content when it is directly affected by the requested
change or necessary to make the task result understandable. Record other material
problems with exact examples and effects.


### Project conventions and shared boundaries

When the task touches a repository's role, language, build, deployment, or service
boundary, inspect the nearby maintained repositories that call or reuse it. Compare
actual source languages and toolchains, runtime versions, release methods, and shared
contracts; exclude configuration and generated files from language comparisons. A
majority language is evidence of a local convention, not proof that every component
should migrate. Explain the concrete cost of the current mismatch and of changing it.
Trace repeated code and operational wiring to see whether a shared library, image,
repository, or common configuration would remove real duplication. Keep service-owned
settings local; do not centralize them if that couples independent releases or hides
service-specific behavior. If the task is INVESTIGATE, fix confirmed in-scope defects
that the comparison exposes instead of leaving a recommendation.

### Project stewardship baseline

When the user assigns ongoing responsibility for a project, or asks whether it is
clean, healthy, or production-ready, expand the scan into a project baseline before
starting a narrow implementation task. Use [AUDIT.md](AUDIT.md) for the broader review.
Check:

- **README:** Can a new user or maintainer understand the purpose, setup, development
  and test steps, API and service ownership, and release process? Verify instructions
  and claims against source and runtime configuration.
- **Codebase and language fit:** Inspect structure, boundaries, dependencies, duplicate
  or dead paths, error handling, tests, and security-sensitive code. Compare languages
  and conventions with the user's related repositories when available. Describe actual
  interoperability or maintenance costs; a language difference alone is not a defect
  and does not authorize a migration.
- **Working product path:** Trace an important customer task from the frontend through
  each API and dependency to its result. Check success and failure behavior. Exercise
  the deployed frontend and safe, representative API requests where authorized;
  distinguish live evidence from local tests and mocks. A health endpoint or HTTP 200
  alone does not show that the user journey works.
- **Speed:** Measure API responses and frontend experience separately. For APIs, record
  status, result correctness, payload size, and repeated response times; separate service
  processing from network, proxy, and dependency time. For the frontend, check page
  loading, browser errors, asset and API timing, and a meaningful interaction. Compare
  results with stated targets or observed expectations. Keep checks bounded and low-rate;
  do not invent a universal latency target. Record method, location, revision, sample
  count, and limits so others can repeat the measurement.
- **Operations:** Check available health signals, recent errors, deployed revision, and
  deployment or rollback steps for the affected path. Use read-only production checks
  where covered by the task or standing authorization. Run state-changing checks in
  staging; if there is no staging target, follow BUILD's temporary staging procedure.

Keep a compact baseline in task context: scope and revision, representative journey,
successful and failed results, API and frontend timings, README and language findings,
checks performed, and evidence still unavailable. Refresh affected evidence when the
project, release, or live behavior changes.

## Act on what you find

- Fix confirmed instances of the reported or directly related problem throughout the
  relevant product path, then search again to verify they are gone.
- Include low-risk quality corrections that are necessary for the requested change to
  be coherent, accurate, understandable, and maintainable. Do not leave stale links,
  misleading names, broken setup steps, or clearly harmful code in the touched path just
  because they were not named in the prompt.
- Keep independent cleanup outside that path out of the change. Report material
  separate problems with a file or symbol, what is wrong, and its user or maintenance
  effect. Recommend a concrete next action; ask only when the requested outcome depends
  on resolving that separate issue or authority is needed.
- Preserve existing user changes. Apply the task's authorization before staging,
  committing, pushing, deploying, or publishing. When a code-changing Compress
  workflow is invoked, follow its standing release authorization after local checks.
- For AUDIT and REVIEW tasks that remain read-only and make no code changes, report
  findings without editing files. INVESTIGATE fixes confirmed in-scope issues and
  follows the same release path as BUILD or FIX when it changes code.

Before finishing, inspect the final diff, recheck naming and README references, and run
focused checks appropriate to the change. In the report, state the area scanned, the
material findings and corrections, and any repository areas not reviewed. Say there
were no material issues only for the area actually inspected.

## Research basis and limits

Four peer-reviewed studies support checking documentation, identifiers, and code
quality as related but separate concerns. Wang et al. analyzed 5,000 GitHub repositories
across more than 20 languages and found README organization and update activity
associated with repository popularity; the observational design does not show that
rewriting a README causes popularity. This supports checking README accuracy,
organization, and stale references, not optimizing for stars. [Wang et al., *Journal of
Systems and Software* (2023)](https://doi.org/10.1016/j.jss.2023.111806).

Schankin et al. tested 88 Java developers on code snippets. Descriptive compound names
helped participants find semantic defects about 14% faster, with the result varying by
experience; naming style did not help with syntax-error tasks. The study supports
meaningful names when they explain domain intent, not a blanket preference for longer
names. [Schankin et al., ICPC (2018)](https://doi.org/10.1145/3196321.3196332).

Mastropaolo et al. evaluated three automated variable-renaming approaches using Java
projects and datasets of reviewed and explicitly renamed identifiers. They found useful
recommendations under some conditions, while noting the artificial evaluation setting,
missing project naming conventions and original names from model context, and Java-only
generalizability. This supports using tools as evidence while checking domain meaning
and local conventions directly. [Mastropaolo et al., *Empirical Software Engineering*
(2023)](https://doi.org/10.1007/s10664-022-10274-8).

Tuna et al. examined code-smell changes in open-source pull requests and added a
practitioner focus group. Code-smell density neither rose nor fell in 8 of 10 reviews,
and review-process smells had little correlation with code smells. The study cautions
against assuming that a generic review pass catches maintainability problems; it does
not imply that code review is useless. [Tuna et al., *Journal of Systems and Software*
(2024)](https://doi.org/10.1016/j.jss.2024.112101).

Together, the studies motivate explicit checks for README accuracy and usability,
context-aware names, and concrete maintainability issues. Their samples and methods do
not define a universal score for code or documentation. Judge each finding against the
actual repository, product path, project conventions, and behavior.

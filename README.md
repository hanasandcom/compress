# Compress

Compress provides separate instructions for common software tasks. It is a set of task workflows, not one general-purpose agent skill.

## How to use it

1. Choose the workflow that matches the task.
2. Provide the agent with that workflow file and your concrete request.
3. Include the target repository, relevant constraints, and access to evidence the decision depends on, such as production usage data for an API audit.
4. Load another workflow only if the task genuinely crosses into it. Do not load every workflow as standing context.

If the task type is unclear, describe the desired outcome first and choose the workflow that best matches it.

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

## Workflows

- [Build](skill/BUILD.md) — add or extend a requested capability.
- [Fix](skill/FIX.md) — correct a specific defect.
- [Remove](skill/REMOVE.md) — retire an unwanted capability and its supporting code.
- [Refactor](skill/REFACTOR.md) — restructure code while preserving behavior the user still wants.
- [Audit](skill/AUDIT.md) — assess system-wide usage, value, and maintenance cost.
- [Review](skill/REVIEW.md) — evaluate a proposed change.
- [Investigate](skill/INVESTIGATE.md) — answer a question without changing code.

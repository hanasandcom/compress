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
without changing files.

## Workflows

- [Build](skill/BUILD.md) — add or extend a requested capability.
- [Fix](skill/FIX.md) — correct a specific defect.
- [Remove](skill/REMOVE.md) — retire an unwanted capability and its supporting code.
- [Refactor](skill/REFACTOR.md) — restructure code while preserving behavior the user still wants.
- [Audit](skill/AUDIT.md) — assess system-wide usage, value, and maintenance cost.
- [Review](skill/REVIEW.md) — evaluate a proposed change.
- [Investigate](skill/INVESTIGATE.md) — answer a question without changing code.

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

Apply research, do not just cite it. For each paper, carry forward its method, scope,
finding, limitation, and the local question or check it suggests. Keep a concise shared
note across workflow handoffs instead of repeating source text. Tests show only whether
covered behavior passes; also inspect reuse, completeness, readability, and operating
cost.

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

## Workflows

- [Build](skill/BUILD.md) — add or extend a requested capability.
- [Fix](skill/FIX.md) — correct a specific defect.
- [Remove](skill/REMOVE.md) — retire an unwanted capability and its supporting code.
- [Refactor](skill/REFACTOR.md) — restructure code while preserving behavior the user still wants.
- [Audit](skill/AUDIT.md) — assess system-wide usage, value, and maintenance cost.
- [Review](skill/REVIEW.md) — evaluate a proposed change.
- [Investigate](skill/INVESTIGATE.md) — answer a question without changing code.

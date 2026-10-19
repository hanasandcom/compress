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

## Product purpose and architecture

Before a product-level change, name the user and need, where the change fits in the
existing journey, why it merits the user's time, and the outcome that would show it
helps. For a game, explain how it supports the core play loop or gives players a clear
reason to return. Consider monetization or business value when relevant; do not invent
a revenue rationale for every feature. For changes spanning services, data, or user
flows, first map the smallest useful architecture: responsibilities, data flow,
interfaces, state, failure paths, and operating needs. Scale the plan to the change;
do not add planning documents for a one-line fix.

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

## Workflows

- [Build](skill/BUILD.md) — add or extend a requested capability.
- [Fix](skill/FIX.md) — correct a specific defect.
- [Remove](skill/REMOVE.md) — retire an unwanted capability and its supporting code.
- [Refactor](skill/REFACTOR.md) — restructure code while preserving behavior the user still wants.
- [Audit](skill/AUDIT.md) — assess system-wide usage, value, and maintenance cost.
- [Review](skill/REVIEW.md) — evaluate a proposed change.
- [Investigate](skill/INVESTIGATE.md) — answer a question without changing code.
- [Parallelization](skill/PARALLELIZATION.md) — divide one coherent goal into independent work.
- [Multitasking](skill/MULTITASKING.md) — assign separate requested outcomes to separate owners.

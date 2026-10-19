# Parallelization

Use this workflow when one coherent outcome can be reached sooner by dividing its
research, implementation, or review into independent pieces. Every task workflow must
assess whether this would save time, then use this workflow when it would. If delegation
will save time, delegate instead of merely proposing that someone do it.

## Decide what to split

1. State the shared outcome, user value, acceptance conditions, and the smallest plan
   that shows architecture, data flow, interfaces, dependencies, and sequence.
2. Find independent questions or slices of work. Assign one owner to each independent
   deliverable or file when file ownership is genuinely independent. For example, seven
   independent file changes can go to seven workers when capacity permits; with four,
   divide the files into balanced groups. Do not split tightly coupled changes by file
   if they need one owner to keep contracts consistent.
3. Start subagents first. Use up to four subagent slots where the platform allows. Do
   not add peer or other additional agents until all four subagent slots are occupied;
   then use additional agents only if the platform permits and the saved time is worth
   the coordination cost. Respect the actual capacity available in the current session.
4. Give each worker the same outcome and relevant context, plus a distinct question or
   owned surface, required evidence, dependencies, and a concrete result to return.
   Agree on shared interfaces before parallel edits. Avoid concurrent writes to the same
   file; use the platform's isolation support when available.
5. Keep research shared across the task chain. The lead records a concise note with
   each paper's method, scope, finding, limitation, and the local decision or check it
   informs. Workers use this note instead of independently repeating the same research.
6. The lead integrates every result, checks cross-cutting behavior and the whole
   product, resolves conflicts, and verifies the acceptance conditions. Delegation does
   not transfer responsibility for the final result.

## Choose the right split

Parallelize independent implementation slices, research questions, or reviews of one
shared goal. If the user requested several separate outcomes, use
[Multitasking](MULTITASKING.md) and assign an owner to each outcome. A task can use both
workflows when it has several independent outcomes and each outcome also has separable
work.

Do not parallelize a tiny change, sequential dependency, or tightly coupled design when
coordination is likely to take longer than the saved work. For a coupled implementation,
parallelize research or independent review instead. More workers do not guarantee a
faster or better result.

Before writing user-facing or maintainer-facing prose, consult the relevant section of
the [wording dictionary](../dictionary/wording.md). Report who owned each slice, what
was integrated, what the lead checked, and any part that could not be verified.

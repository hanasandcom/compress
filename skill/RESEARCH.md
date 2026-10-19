# Research

Use this protocol whenever a task workflow requires research. The goal is to improve
the product decision and test its quality, not to collect citations.

## Choose a set that adds distinct evidence

Before searching, list the decisions that research can inform: for example, what
established approaches do, where they fail, which alternative fits, or how to tell
whether the result works. Read at least three full, relevant, peer-reviewed papers for
the whole task chain. Use recognized scholarly publishers or proceedings, including
Elsevier, Springer Nature, Wiley, Taylor & Francis, IEEE, Oxford University Press, ACM,
or peer-reviewed university research. Abstracts, search snippets, AI summaries, vendor
blogs, and company material do not count toward the minimum; vendor documentation may
verify vendor-specific behavior.

Give each paper a clear job. The set should provide context for the problem, test or
challenge a proposed approach, and assess outcomes or quality. These are useful roles,
not a fixed three-paper template: a follow-up can test a weakness in an earlier paper;
another paper can study a different method, population, operating context, theory, or
outcome. Every paper must add a specific contribution; across the set, cover more than
one evidence role or decision. A follow-up can be complementary without being independent
confirmation. Different authors or venues alone do not make papers meaningfully
different. Check whether papers share data, authors, assumptions, or methods; treat
overlapping evidence as related, not independent confirmation. Do not count a paper if
it adds no new context, challenge, evaluation, or product-relevant conclusion.

A journal or conference label does not make a paper sound. Check whether its method,
sample, analysis, reporting, and limitations support the claim you plan to use. Do not
keep a weak paper just to reach three; exclude it and find a stronger source or report
the evidence gap. Do not choose a weak source just to create variety, either: distinct
evidence matters only when it is relevant and well suited to the decision.

## Read and connect the findings

For each paper, record a short source note:

- Its role and the decision it addresses.
- Method, sample or system, setting, and main finding.
- Limitations and how directly those findings transfer to this product.
- What it confirms, extends, challenges, or leaves open in the other papers.
- The code, product, user, or operational evidence to inspect because of it.

Then synthesize the set. State where the findings agree, where they differ, and whether
the difference follows from method, sample, assumptions, or setting. Weigh sources by
their methods and fit to the question; do not treat the papers as votes or assume the
newest, most cited, or most prestigious source wins. A weak paper must not carry the
decision by itself. If evidence is correlated or a limitation repeats across the set,
say so. A disagreement is a finding to investigate, not noise to average away.

## Make research change or test the work

Connect the synthesis to the actual product. Trace the relevant code, behavior,
architecture, users, telemetry, or operating constraints. For each meaningful finding,
state whether it changes the plan, supports retaining an existing design, rules out an
option, identifies a gap, or changes a verification measure. If it does none of these,
do not present it as support for the work. Keep a compact evidence map:

| Finding or disagreement | Product evidence checked | Decision or quality check changed |
| --- | --- | --- |

The map is the handoff artifact for chained workflows and agents. Share it rather than
making each worker repeat the same search. For an implementation, turn conclusions into
specific behavior, constraints, or acceptance checks, then verify those checks against
the implementation. For an audit or review, use them to test completeness and quality.
For investigation, use them to qualify the answer. If a paper motivates a change but
cannot be tied to an observable criterion or product-specific evidence, say so; the
citation alone does not show the change improved quality. Research from other products
suggests checks; it does not establish what is true in this one.

The minimum is a task rule, not a research finding that three is optimal. If fewer than
three suitable full papers can be read, if the papers do not add distinct evidence, or
if they do not inform a product decision, report the research as incomplete and name
the unresolved decision. Do not pad the set or pretend a source changed the result.
Track time spent searching and reading. Keep the three-paper minimum across a chain,
not per workflow or worker; add papers only when an important decision remains open.
Evaluate whether this approach improves outcomes by comparing representative tasks,
including rework, correctness, human intervention, and time spent on research.

## Research basis and limits

These papers support purposeful integration of distinct evidence, but do not validate
this protocol for software changes or prove that three papers are enough. They explain
the research method; they do not count toward the task's domain-specific paper minimum:

- Breitmayer, Ayres, and Knafl distinguish triangulation used to confirm a finding from
  using it to make an account more complete. They illustrate qualitative and
  quantitative evidence about one construct. The paper is rooted in nursing research;
  it supports asking what each source contributes, not requiring the same two methods
  in every software task. [*Journal of Nursing Scholarship*, 1993](https://doi.org/10.1111/j.1547-5069.1993.tb00788.x).
- Tricco et al. reviewed 121 papers describing seven approaches to integrating
  qualitative and quantitative evidence. They found that synthesis can add context,
  but common weaknesses included subjectivity and missing or unclear steps. The review
  concerns healthcare evidence synthesis, not coding-agent instructions; it supports
  making the comparison and integration steps explicit. [*Journal of Clinical
  Epidemiology*, 2016](https://doi.org/10.1016/j.jclinepi.2015.12.011).
- Heesen, Bright, and Zucker use a formal voting-theory model to argue that multiple
  methods can help when the researcher is uncertain which method to trust. The result
  depends on assumptions; the authors discuss correlated errors as an open issue and
  acknowledge that triangulation can be worse than relying on a known superior method.
  This is theoretical work, not an empirical software study, and it argues against
  counting correlated papers as independent confirmation. [*Synthese*, 2019](https://doi.org/10.1007/s11229-016-1294-7).

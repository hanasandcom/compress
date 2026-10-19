# Writing habits to correct

Use this when reviewing agent-written reports, product copy, and instructions. These
examples target clarity, not authorship detection. Research finds repeated templates and
prompt-driven formulaic phrasing in some settings; it does not establish a universal AI
voice or prove that one phrase came from a model. Avoid forced human quirks and phrase
blacklists. The goal is to say what happened, what evidence supports it, and what follows.

| Habit | Avoid | Prefer |
| --- | --- | --- |
| Abstract labels where the object is known | The parser makes a claim about the source. | `claimedDataSize` is empty; the parser cannot show whether the actor posted a size. |
| Unsupported attribution | The actor did not disclose a size. | The size field is empty in this record. The saved source text has not been checked. |
| Empty contrast (“not X, but Y”) | This shows a missing field rather than deliberate withholding. | The record has no size value. The source may still contain one. |
| Generic evaluation | Evidence-backed code review. | The review found two duplicate handlers and one test that never checks the response body. |
| Confidence without a check | The checkout is fully verified. | The local test confirms the checkout link. A successful payment and entitlement were not tested. |
| Repeating a result as a conclusion | The route has no tests. This means testing is missing. | No test covers the route's empty-input response. |
| Inflated value language | This powerful dashboard empowers analysts with actionable insights. | The dashboard groups incidents by actor and links each record to its source. |
| Hedge pileup | It may perhaps be possible that the value could be missing. | The API response has no value for this field. |
| Stock opening | In today's evolving threat landscape, intelligence matters. | Analysts need to compare incident claims with their original sources. |
| Generic limitation | More research is needed. | The local copy has no production request logs, so recent use cannot be measured. |
| Vague source reference | Research says this approach is better. | [Paper] tested [method] on [sample] and found [result]; the study did not test this product. |
| Claiming product success from a surface | The pricing page proves the product is ready to sell. | The page displays plans. Payment completion, entitlement, and customer use were not checked. |
| Generic next step with missing context | Review for relevance to the selected actor or company. | Open [source] and check whether [company] is already on [watchlist]; close it if it duplicates [claim ID]. |
| Declaring the whole task done from one check | Verified; all fixed. | The empty-size fallback now reads “Size unavailable” in the activity feed and detail view; the FAQ and API output still need review. |
| Handoff that drops evidence | The feature is blocked. | The parser returns no size for [record ID]; I checked [source URL] and found no size claim. The other [N] records were not reviewed. |
| Dense jargon where a concrete result is clearer | Rising verbosity and structural erosion over iterative code-agent trajectories. | In these repeated coding tasks, agents added duplicate code and made some functions more complex. |

## Check before sending

- Name the real file, field, service, user action, or observed result when known.
- Remove a sentence if it adds no observation, reason, decision, or next action.
- Avoid routine “not X but Y” turns. Keep a contrast only when the two alternatives
  matter to the decision, and name them directly.
- State uncertainty at the missing evidence: what was not available, from which source,
  and which claim that prevents.
- Do not turn research into decoration. Tie each study to a product check or decision.
- Do not make prose longer to sound careful, unique, natural, or less AI-written.

## Research limits

Crosthwaite et al. (2026) found that explicit metadiscourse prompts changed rhetorical
features in a corpus of argumentative essays, with some repeated frames; their study used
one model and a limited essay setting. [*The Modern Language Journal*](https://doi.org/10.1111/modl.70089).
A 2023 *Scientific Reports* study found formulaic structures in the tested ChatGPT essays,
while also noting limits in its student comparison and model timeframe. [Study](https://www.nature.com/articles/s41598-023-45644-9).
PNAS research found people’s intuitions about AI-written language were unreliable, so
these examples are writing guidance, not an AI detector. [Study](https://www.pnas.org/doi/10.1073/pnas.2208839120).
These studies justify checking for repetition and prompt-shaped templates in their
contexts; they do not prove that the examples above are exclusive to AI writing.
SlopCodeBench reports that agents produced more verbose code and more complex functions
over repeated attempts in its tested tasks. It is a 2026 preprint using 36 Python tasks,
so treat it as an early signal, not settled evidence or a measure of Hanasand.
[Preprint](https://arxiv.org/abs/2603.24755).

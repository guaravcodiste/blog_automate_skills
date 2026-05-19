# SKILL: codiste-blog-audit.md

## Goal
Audit the generated Markdown blog file (.md / .txt) post-generation. Identify formatting violations, verify structural templates, and compute deterministic keyword integration metrics.

This skill check runs as a standalone post-generation audit tool. It outputs a PASS or flagged violation report. It never modifies files or rewrites content.

---

## AUDIT CATEGORIES

### Category 1: Voice Locks (Locks 1, 2, 4, 5, 6, 11)

|Check|Rule Reference|
|---|---|
|Em dash count = 0 in entire body & headings|Lock 1|
|Colon/Semicolon count = 0 in H1, H2, H3 (Exception: literal "TL;DR")|Lock 2|
|H1 character count ≤ 60 OR word count ≤ 10|Lock 2|
|H1 contains the primary keyword|Lock 2|
|At least 2 H2s framed as questions|Lock 2|
|Never-use list scan: zero matches (case-insensitive)|Lock 4|
|Sentence count where word count > 25: zero|Lock 5|
|Minimum 1 sentence fragment in body (Cluster, Pillar, Research Anchor)|Lock 5|
|Per major H2: minimum 2 sentences under 7 words in body prose|Lock 5|
|Semicolon count in body prose: zero|Lock 6|
|Per major H2: at least one "weird specific" present (heuristic)|Lock 11|
|Spelling check: zero "per cent" instances (strict "percent" / "%")|Project Rule|

### Category 2: Structural slots (Slots 1 to 15)

|Check|Rule|
|-|-|
|TL;DR present (ToFU/MoFU only, absent for BoFU)|Slot 1|
|TL;DR bullet count ≥ 3|Slot 1|
|Hook is exactly 3 to 4 sentences|Slot 2|
|Direct-answer summary box present (40 to 60 words, bolded)|Slot 3|
|H2 problem section present|Slot 4|
|H2 solution section present|Slot 5|
|H2 proof section present|Slot 6|
|Comparison table count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 1)|Slot 7|
|Each comparison table preceded by H3 title and intro sentence|Slot 7|
|Statistics count ≥ 3 in body prose|Slot 8|
|Mid-post CTA present if Funnel = MoFU (absent for ToFU/BoFU)|Slot 9|
|Codiste paragraph present, outcome-focused, no heading above it|Slot 10 / Lock 9|
|Primary CTA present (starts with H3 "Ready to [outcome]?", button whitelisted)|Slot 11|
|Closing statement present, no heading, max 3 sentences|Slot 13|
|Pull-out callout count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 2)|Slot 14|
|Each pull-out callout is 12 to 20 words, single sentence, bolded|Slot 14|
|Key Numbers block present if statistics count ≥ 3|Slot 15|
|Key Numbers block placed after proof section, before Codiste paragraph|Slot 15|

### Category 3: Bullet discipline (Lock 10)

|Check|Rule Reference|
|---|---|
|Bullet list count in body ≥ minimum (Cluster: 3, Pillar: 6, Research Anchor: 4)|Lock 10|
|No bullet lists in: hook, problem, Codiste paragraph, CTA, direct-answer box, closing statement|Lock 10|
|Each bullet is a complete sentence (subject-verb)|Lock 10|
|Each bulleted list has a setup paragraph above (1 to 3 sentences)|Lock 10|
|Each bulleted list has a tie-back paragraph below (1 to 2 sentences)|Lock 10|
|No bulleted list is the entire content of an H2 section|Lock 10|

### Category 4: CTA discipline (Lock 8 / CTA Matrix)

|Check|Rule Reference|
|---|---|
|Primary CTA supporting line word count ≤ 18|Lock 8|
|Mid-post CTA supporting line word count ≤ 18 (if present)|Lock 8|
|Primary CTA H3 starts with "Ready to" and ends with "?"|Slot 11|
|Button label is whitelisted ("Book a Call" or "Contact Us" only)|CTA Matrix|
|Button URL matches funnel per CTA Matrix (/book-a-call or /contact)|CTA Matrix|
|CTA supporting line contains zero references to specific US regulators or states|Project Rule|
|Closing CTA links to /book-a-call (MoFU/BoFU) or /contact (ToFU)|Slot 13|

### Category 5: FAQ discipline (Slot 12)

|Check|Rule|
|-|-|
|Visible FAQ count = 5 (Cluster, Research Anchor) or 8 (Pillar)|Slot 12|
|Schema-only FAQ count = 5|Slot 12|
|Total FAQ count = 10 (Cluster, Research Anchor) or 13 (Pillar)|Slot 12|
|Each FAQ Q+A is formatted inline (bold Question, regular answer, single space, single paragraph)|Slot 12|
|Each FAQ question ends with "?"|Slot 12|
|Each FAQ answer starts with subject-verb sentence (not "It's...")|Slot 12|
|Each visible FAQ answer is 40 to 60 words (schema FAQ is 25 to 40 words)|Slot 12|
|First visible FAQ answer contains primary keyword|Slot 12|
|At least one FAQ addresses US compliance specific to the vertical|Slot 12|

### Category 6: SEO and Meta

|Check|Rule|
|-|-|
|meta\_title ends with " \| Blog"|Hard Rule 7|
|description character count ≤ 155|Hard Rule 8|
|Primary keyword appears in description first 60 characters|Hard Rule 8|
|uid (slug) character count < 50|Hard Rule 8|
|status field = "draft" (JSON mode only)|Hard Rule 14|
|No img field anywhere in JSON|Hard Rule 9|
|No seo.image field|Hard Rule 9|
|No image slices in slices array|Hard Rule 9|
|Every H2 has anchor\_id (JSON) or Word bookmark (.docx)|Hard Rule 19|
|Every H3 has anchor\_id (JSON) or Word bookmark (.docx)|Hard Rule 19|
|heading2 always in its own content slice (JSON mode)|Hard Rule 12|

### Category 7: Brand and project rules

|Check|Rule Reference|
|---|---|
|Zero references to "Dialora"|Never-do list|
|Vertical is one of the 8 allowed vertical values|Project Rule|
|Zero co-founder, equity partner, or generic "trusted partner" phrasing in Codiste block|Lock 9|
|Word count is within range for the designated Content Type|Project Rule|

### Category 8: Keyword integration (Lock 12)

This category is deterministic. It greps the finished blog text against the feeder keyword pool and produces the number that fills the Keyword Integration line in Output 2. The audit never accepts a keyword count produced any other way.

**The pool.** One combined list: Primary keyword plus every Secondary keyword plus every LSI/NLP term from the feeder row. This is the denominator X.

**Match counting.** For each keyword in the pool, the audit scans the full blog text (case-insensitive):

* An exact contiguous substring match counts as a hit.
* A tokenized or natural-variant match counts as a hit. The audit checks the keyword with stop words inserted and with minor word-order variation. Example: feeder keyword "ai agents fintech" is a hit if the text contains "ai agents for fintech" or "ai agents in fintech". Feeder keyword "agentic ai fintech" is a hit if the text contains "agentic ai in fintech".
* A keyword found only inside the H1, direct-answer box, or hook still counts. A keyword found only inside an FAQ answer or a bullet list also counts as present, but the audit notes it, because Lock 12 says keywords should land in body prose, not be stuffed into lists or FAQs.
* Y is the count of pool keywords with at least one hit.
* Z is Y divided by X, as a percentage, rounded to the nearest whole number.

|Check|Rule|
|-|-|
|Keyword Integration line computed: Y used out of X provided (Z%)|Lock 12 / Hard Rule 35|
|Primary keyword readout: exact count and tokenized/variant count reported separately|Lock 12 / Hard Rule 36|
|If Z below 50: every missing keyword listed with a one-line reason|Lock 12 / Hard Rule 36|
|Keywords found only in FAQ answers or bullet lists: noted (possible stuffing, body-prose preferred)|Lock 12|
|Reported count matches actual grep of the file, not an estimate|Lock 12 / Hard Rule 35|

\---

## HEURISTIC CHECKS (Flagged as [approximate])

Some checks cannot be made fully deterministic from text alone. The audit runs a heuristic and labels the result with "\[approximate]":

* **Weird specific per H2 (Lock 11):** detects presence of named entities, specific numbers, or proper nouns in body prose for each H2 section. Flags H2 sections with no detected named-entity anchor as "possible missing weird specific \[approximate]." Verify manually.
* **Sentence fragment count (Lock 5):** detects sentences without a clear subject-verb pair. False positives possible (some short sentences are technically grammatical). Flags blogs with zero detected fragments as "no fragments detected \[approximate]."
* **Vendor-pitchy phrasing in Codiste paragraph (Lock 9):** keyword scan for "industry-leading," "trusted partner," "world-class," etc. Catches obvious cases. Subtle vendor tone may slip through.

These three are the heuristic checks. All other checks above are deterministic, including all of Category 8. The tokenized-variant match in Category 8 is deterministic: it tests a defined set of stop-word and word-order variants, it does not guess.

\---

## OUTPUT FORMAT

Every audit run, pass or fail, ends with the Keyword Integration block. It is not a violation list. It is the deterministic count that blog-creator-v8.5 lifts into the Output 2 Keyword Integration line. The block appears even when the blog passes every other check.

### Pass case (clean blog)
```
AUDIT [BLOG N]: PASS
All checks clean. [X] checks across 8 categories.

KEYWORD INTEGRATION
Keyword Integration: [Y] used out of [X] provided ([Z]%)
Primary keyword "[exact feeder string]": [N] exact, [M] tokenized/variant
[If Z below 50: Keywords not integrated: each missing keyword + one-line reason]
[If any keyword found only in FAQ/list: note it here]
```

### Partial pass / fail case (violations found)
Group the violations by their Category. Be explicit on where the issue is and what the exact fix should be.

```
AUDIT [BLOG N]: [Y] violations across [Z] categories

VOICE LOCKS
- Lock 2: Heading H2 "Why Do We Need AI?" is under 5 words. Rewrite to meet the 5-word minimum.
- Lock 5: No sentence fragments detected. Minimum 1 required for Cluster. [approximate]
- Lock 11: H2 "The Solution" missing weird specific anchor. Add named, concrete, non-load-bearing detail. [approximate]

STRUCTURAL SLOTS
- Slot 9: Mid-post CTA missing. Funnel = MoFU requires mid-post CTA after proof section.
- Slot 14: Pull-out callout count = 0. Cluster requires minimum 1.

BULLET DISCIPLINE
- Lock 10: The list under H2 "The Solution" has no tie-back paragraph. Add a 1-2 sentence paragraph underneath.

CTA DISCIPLINE
- CTA Matrix: Button label "Book a Technical Assessment" is not in whitelist. Use "Book a Call" or "Contact Us" only.
- Slot 11: Primary CTA missing "Ready to [outcome]?" H3 above the supporting line.

FAQ DISCIPLINE
- (clean)

SEO / META
- (clean)

BRAND / PROJECT RULES
- Project Rule 4: Three "per cent" instances detected. Region is USA, use "percent" or "%".

KEYWORD INTEGRATION
Keyword Integration: 9 used out of 14 provided (64%)
Primary keyword "ai agents fintech": 0 exact, 5 tokenized/variant
Keywords found only in FAQ: "kyc automation" appears in body and FAQ, body placement OK.

Fix flagged items in source and regenerate, or edit the file directly before upload.
```

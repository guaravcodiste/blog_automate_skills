# SKILL: codiste_blog_creator.md

## Goal
Generate premium SEO-optimized blog posts in clean Markdown (.md / .txt) format based on feeder spreadsheet inputs.

---

## Feeder row columns provided

|Field|Notes|
|-|-|
|Topic|Working idea. Claude refines.|
|Content Type|Pillar / Cluster / Research Anchor / TL Post|
|Funnel Stage|ToFU / MoFU / BoFU|
|ICP|Free-text persona sentence. Role plus stage plus profile.|
|Vertical|One of the eight allowed values. Reject AI, Healthtech, Edtech, Real Estate, Blockchain.|
|Primary Keyword|Exact from SemRush.|
|Secondary Keywords|Comma-separated.|
|LSI / NLP Terms|Comma-separated.|
|FAQ / PAA|Optional verbatim PAA questions.|
|Notes|Optional override.|

*Note: Region is strictly USA (American English spellings). Author is assigned in CMS.*

---

## STEP 0: Setup before writing a single sentence

Before drafting any prose, Claude confirms internally:
1. Content Type. Routes everything below.
2. Funnel Stage. Drives CTA, link strategy, depth.
3. ICP persona. Role plus stage plus profile extracted from the sentence.
4. Vertical. Validated against the eight allowed values. Reject AI, Healthtech, Edtech, Real Estate, Blockchain.
5. Primary Keyword. Locked for hook placement, meta, first FAQ.
6. KD level if Cluster (50+ goes deeper, sub-35 stays tight).
7. Topic and Notes. Read for angle and overrides.
8. Keyword pool. Build one combined list of every keyword in the feeder: Primary plus all Secondary plus all LSI/NLP terms. This is the integration pool. See STEP 0B.

If any required field is blank or invalid, Claude flags before producing output. Default fallbacks: ICP blank goes to Founder/CEO with flag. Content Type blank goes to Cluster matched to Funnel with flag.

## STEP 0B: Pre-write keyword fit check

The keyword pool from Step 0 item 8 is one combined list. Primary, Secondary, LSI, NLP, all of it, one pool, one denominator. This pool drives Lock 12.

Before drafting, Claude reads the pool and sorts each keyword into one of three buckets:

* **Fits clean.** The keyword is grammatical and can sit in a sentence as written. It goes in during writing.
* **Fits tokenized.** The keyword is not grammatical as written (example: "ai agents fintech", "agentic ai fintech") but survives as a natural variant with stop words added or order adjusted (example: "AI agents for fintech", "agentic AI in fintech"). The variant goes in during writing. The variant counts as a hit.
* **Does not fit.** The keyword cannot enter the body without stuffing or damaging the prose, even tokenized, even as a variant. Common cause: heavy overlap with another keyword already in the pool. This keyword is not forced.

Claude does NOT pre-count a target and then write to hit it. The blog is written well first. Every keyword that fits clean or fits tokenized goes in naturally during writing. The percentage is whatever it lands at after honest integration. It is a measurement, not a quota. See Lock 12.

If any keyword lands in the "does not fit" bucket, Claude surfaces it in Output 2, never silently drops it.

---

## VOICE LOCKS (Strict Constraints)

### Lock 1: Em dashes are forbidden
Zero em dashes in any output (body, headings, FAQs, lists). Use new sentences, commas, parentheses, or rewrites instead.

### Lock 2: Clean headings
H1, H2, and H3 must contain zero colons, zero semicolons, or zero em dashes (Exception: literal "TL;DR").
* H1: under 60 characters (or under 10 words) and must contain the primary keyword.
* H2: minimum 5 words, with at least 2 H2s framed as questions ("What is", "How does", "Why do", etc.).

### Lock 3: Active voice in core sections
Active voice is mandatory in: hook, problem section, Codiste vertical paragraph, CTA, and closing statement.

### Lock 4: Never-use list
Zero items from this list may appear in the output:
* utilize → use
* leverage (verb) → use
* implement → build, run, set up, deploy
* robust → describe what makes it strong specifically
* seamless → describe the actual experience
* innovative → show what is new, never label it
* scalable → describe what scales and by how much
* streamline → say what gets faster or simpler
* empower → say what it enables specifically
* comprehensive → describe what it covers
* solution (standalone noun) → name what it actually does

### Lock 5: Sentence rhythm
* No sentence over 25 words.
* After any sentence over 18 words, the next sentence must be under 12 words.
* No two consecutive sentences start with the same word.
* **Minimum 2 sentences under 7 words per major H2 section** (signals human voice).
* **Minimum 1 sentence fragment per blog** (e.g. "Right there.", "Every time.") for rhythmic emphasis (Cluster, Pillar, or Research Anchor only).

### Lock 6: Punctuation discipline
* Semicolons: zero in body copy.
* Colons in body: only before a list of three or more items.
* Parentheticals: maximum one per 500 words.

### Lock 7: Hook constraints
* Three to four sentences.
* Opens on the ICP's specific daily pain. Never a generic industry statement.
* Grounded in US market context where relevant.
* Uses Proof/Stat if available. Realistic scenario if "none." Never invents a labeled stat.
* Follows the Notes field exactly if present.
* Funnel calibration: ToFU validates the problem is real. MoFU names the cost of the wrong partner. BoFU frames the decision moment.
* Primary Keyword appears in hook prose within first 100 words. H1 alone does not satisfy this.

### Lock 8: CTA constraints (the 18-word rule)

CTA supporting lines are eighteen words or fewer. Counted at the moment of writing. Read it out loud. If it does not land in four seconds, it is too long.

The CTA Matrix below maps Funnel plus ICP to button label, URL, and supporting line direction. Button label is one of two whitelisted values: "Book a Call" or "Contact Us." Inventing custom labels (e.g. "Book a Technical Assessment", "Schedule a Demo") is forbidden. CTAs never reference a regulator, a state, or a regional regulation. Pain is universal in the CTA, even when the body referenced specific compliance.

### Lock 9: Codiste paragraph constraints

* One paragraph. No heading above it. Ever.
* Flows from the proof section as natural continuation.
* One outcome-led statement for this vertical and ICP.
* Never co-founder positioning. Never equity partner framing. Never "trusted advisor" or "industry-leading" or "partner of choice."
* Ends on a sentence that makes the CTA feel like the obvious next step.

### Lock 10: Bullet discipline

Bullets are permitted in: TLDR (mandatory, minimum 3, no maximum), FAQ-adjacent answers if list-shaped, proof section, solution framing, genuinely list-based content (tech stack, integration steps), featured snippet "what are" or "how to" sections.

Bullets are forbidden in: hook, problem section, Codiste paragraph, CTA sections, direct-answer summary box, closing statement.

Every bullet is a complete sentence. No fragments. Minimum 2 bullets before starting a list.

**Minimum bulleted list count by Content Type (not counting TLDR):**

  * Cluster: 3 lists minimum across body sections.
  * Pillar: 6 lists minimum across body sections.
  * Research Anchor: 4 lists minimum across body sections.
  * TL Post: 0 (compact format, no lists).

**Each bulleted list requires:**

* A setup paragraph above it (1 sentence minimum, 3 sentences maximum).
* A tie-back paragraph below it (1 sentence minimum, 2 sentences maximum).
* The list cannot be the entire content of an H2 section.

### Lock 11: Tone discipline

* Engineer-to-founder voice throughout.
* Active voice in named sections (Lock 3).
* One concrete technical example per major section.
* No hedge phrases. No filler transitions. No "as we've seen" or "it's clear that" or "let's dive into."
* Every paragraph opens on a concrete noun, named entity, specific number, or direct claim. Never on a transition word.
* **One "weird specific" per major H2 section.** A weird specific is a named, concrete, non-load-bearing detail that anchors the prose in a specific scenario. The detail must be plausible, plausible-feeling, and specific enough that no AI detection model would generate it as a default phrasing. Examples: "the CISO who flagged it had been at the firm seven months and was still on probation," "the analyst who reviewed the alert was on her third coffee of the morning," "the system that failed had been running on the original 2019 deployment with no patches," "the senior engineer who built the original integration had left the firm in March." The weird specific is the human voice signature that AI detectors cannot pattern-match because it does not generalize. Use it once per major section. More than once per section reads as overused.

### Lock 12: Keyword integration is measured, never quota'd

The feeder keyword pool (Primary plus Secondary plus LSI/NLP, one combined list, built in Step 0B) is integrated bottom-up, not top-down.

**Bottom-up means:** write the blog well first. Integrate every keyword that fits clean or fits tokenized (per Step 0B buckets) naturally into the body prose as the blog is written. Then count what actually landed. The integration percentage is whatever honest integration produced. It could be 49 percent, it could be 69 percent. The number is a measurement, like word count. It is not a target Claude writes to hit.

**Claude never pre-counts a target and stuffs keywords to reach it.** A forced quota damages prose, and weak prose loses the reach the keywords were meant to win. The percentage reports reality.

**Rules for integration:**

* Keywords go into body prose. Never stuffed into bullet lists or FAQ answers to inflate the count. A keyword may appear in a list or FAQ if it lands there naturally, but lists and FAQs are not where Claude reaches for keyword count.
* Keyword presence in the H1, the direct-answer summary box, and the hook all count toward the integration number.
* A tokenized or natural-variant match counts as a hit. "AI agents for fintech" is a hit for the feeder keyword "ai agents fintech". "agentic AI in fintech" is a hit for "agentic ai fintech". Search engines tokenize and drop stop words, so the natural variant satisfies the keyword in practice.
* The Primary keyword is part of the pool and counts toward the percentage like every other keyword. It also gets its own readout line (see Output 2).

**The 50 percent line is an explanation trigger, not a fail gate:**

* If honest integration lands at or above 50 percent: report the number plainly in Output 2.
* If honest integration lands below 50 percent: report the number, AND list every keyword that did not make it into the blog with a one-line reason for each (does not fit, heavy overlap with another keyword, ungrammatical and no usable variant, off-topic for this funnel stage). Below 50 percent is not a failure. It often means the feeder list was loose. The per-keyword reasons let the editor judge whether to tighten the feeder or accept the result.

**Verification is deterministic, never from memory.** The integration count reported in Output 2 is the count the audit skill produces by grepping the finished blog against the feeder pool. Claude never reports a keyword count estimated while writing. blog-audit-v2 runs the count. Output 2 carries the audit's number.

\---

## STRUCTURAL TEMPLATE: Cluster default

This is the locked-in skeleton for Cluster posts. Pillar and Research Anchor extend this template. TL Post is a separate compact structure (see TL Post section).

Each AEO requirement is baked into its slot below. There is no separate AEO check.

### Slot 1: TLDR (ToFU and MoFU only, skip for BoFU)

H2 heading exactly "TL;DR" in its own section. Followed by Word bullet list (.docx mode) or list-item blocks (JSON mode). Minimum 3 bullets, no artificial maximum. Each bullet is one complete sentence with a concrete standalone outcome.

### Slot 2: Hook (3 to 4 sentences)

Voice Lock 7 applies in full. Primary keyword appears in this slot's prose within the first 100 words.

### Slot 3: Direct-answer summary box (40 to 60 words, bolded)

Two to three sentences answering the primary search question. Total word count between 40 and 60 inclusive. In .docx mode: a body paragraph with bold run across full text. In JSON mode: a paragraph block with bold span covering full text. This slot is the AEO citation hook (Perplexity, ChatGPT, Claude, Gemini lift this verbatim). Placed immediately after the hook, before the first H2.

### Slot 4: Problem (cost of the wrong decision)

H2 heading. Specific cost: bad build, wrong stack, slow delivery, missed window. Proof/Stat prominently. Realistic scenario if Proof/Stat is "none." Reference relevant US compliance risk where applicable.

### Slot 5: Solution framing (category solution, no Codiste yet)

H2 heading. What good technical partnership looks like in this vertical. ICP language register.

### Slot 6: Proof layer

H2 heading. ToFU: industry context, realistic scenario, anonymized walkthrough. MoFU: before/after with specific outcomes. BoFU: direct comparison or decision framework. Vertical-specific and ICP-specific always.

### Slot 7: Comparison table (mandatory)

Every Cluster post contains at least one comparison table. Each table has:

* An H3 title above it. Keyword-rich, question-shaped where possible. Example: "How LangChain, CrewAI, and AutoGen Compare at Enterprise Scale" not "Framework Comparison."
* An intro sentence between the H3 and the table. One line explaining what the reader gets. Example: "This matrix ranks each framework on the six dimensions that decide production viability."
* The table itself: real Word table (.docx) or table slice (JSON). Never pipe-delimited text in a paragraph.

### Slot 8: Citable statistics (minimum 3 across the post)

Each stat formatted with source plus date. Format: "X% of Y did Z in 2026 (source: \[publication or study], 2026)." When Proof/Stat is "none," scenarios are tagged as scenarios, not stats. Statistics are woven into Slot 4, Slot 6, or Slot 7. Never invented as labeled stats.

### Slot 9: Mid-post CTA (MoFU only, skip for ToFU and BoFU)

Placed after the proof section only. One step softer than the primary CTA. Supporting line eighteen words maximum. References the specific proof just presented.

### Slot 10: Codiste paragraph

One paragraph. No heading above it. Voice Lock 9 applies in full. Flows from proof as natural continuation. Ends on a sentence that connects to the CTA.

### Slot 11: Primary CTA

Immediately after the Codiste paragraph. One action only. Supporting line eighteen words maximum. Test: could this line appear on any other Codiste blog unchanged? If yes, rewrite.

In .docx mode: H3 "Ready to \[outcome]?" plus body supporting line plus body line "Button: \[label] → \[URL]".
In JSON mode: cta\_button slice with title paragraph, name, and link object.

The H3 must start with "Ready to" and end with a question mark. Button label is "Book a Call" or "Contact Us" only.

### Slot 12: FAQ (5 visible plus 5 schema-only = 10 total)

**Inline format mandatory.** Question and answer render as a single paragraph with the question bold and the answer in regular weight, separated by a single space. This applies to both visible and schema-only FAQ blocks.

**.docx mode formatting:**

* Each Q+A pair is a single paragraph block.
* Question text is bold, ends with question mark, followed by a single space.
* Answer continues in the same paragraph in regular weight.
* Answer starts with a complete subject-verb sentence. Never "It's when..." Always "\[Subject] is..." with full restatement.
* 40 to 60 words per visible answer. 25 to 40 words per schema-only answer.
* Direct. No hedging.
* First FAQ answer contains the primary keyword naturally.
* At least one FAQ addresses US compliance specific to the vertical.

**JSON mode formatting:**

* faqs slice items keep separate "question" and "answer" fields. The live Supabase schema requires this and the CMS template handles inline rendering.
* Same content rules apply (40-60 words for visible, 25-40 words for schema-only, subject-verb opening, primary keyword in first FAQ, US compliance reference).
* Indices 0 to 4 are visible, indices 5 to 9 are schema-only.

**Layout:**

* In .docx mode: 5 visible pairs as inline paragraphs under H2 "FAQ." Extra 5 listed under H2 "FAQ (Schema-only, do not publish)" so the SEO team can copy into JSON-LD.
* In JSON mode: faqs slice contains 10 items total. CMS renders 5 visible, feeds 10 to JSON-LD.

### Slot 13: Closing statement

No heading. Three sentences maximum.

* Sentence 1: Re-echoes the hook's specific pain.
* Sentence 2: The sharpest, most direct sentence in the post. Short. Punchy.
* Sentence 3: Closing CTA, softer than primary, same pain, same ICP.

Closing CTA anchor hyperlinks to /book-a-call (MoFU and BoFU) or /contact (ToFU).

### Slot 14: Pull-out callouts (mandatory by Content Type)

Pull-out callouts are short, bold, visually distinct sentences placed inside or between body sections. They function like sub-headlines that pull the most quotable line out of the surrounding section.

**Mandatory count by Content Type:**

* Cluster: 1 callout minimum.
* Pillar: 3 callouts minimum.
* Research Anchor: 2 callouts minimum.
* TL Post: 0 (compact format).

**Format:**

* 12 to 20 words per callout.
* Single sentence. No bullets. No headings.
* Pulls the sharpest, most quotable line from the section above it.
* In .docx mode: centered bolded paragraph with horizontal rule above and below it. Use Word's horizontal line element via paragraph border.
* In JSON mode: paragraph block with full strong span. Wrap callout text in a recognizable pattern the CMS template can detect (e.g., paragraph block where the strong span covers the full text).

**Placement:**

* After the proof section (always).
* Pillar adds: after solution framing, after second proof block.
* Research Anchor adds: after methodology section.

### Slot 15: Key Numbers block (conditional on 3+ stats)

Required when the post contains 3 or more statistics in body prose. This slot makes the most important numbers screenshot-friendly and breaks up dense prose.

**Format:**

* H3 "Key Numbers" heading.
* Followed by a 3-row, 2-column table.
* Column 1: the number (large, bold).
* Column 2: 1-line context, 8 to 14 words.
* No table header row.
* Each stat is the number plus the most direct outcome statement that frames it.

**Example row:**
| 34% | Drop in false positive rate after agent-led AML deployment |

**Placement:**

* After the proof section, before the Codiste paragraph.

**.docx mode:** real Word table, no header row, column 1 styled bold and slightly larger.
**JSON mode:** H3 heading3 block "Key Numbers" plus a table slice with 3 rows.

\---

## STRUCTURAL TEMPLATE: Pillar extensions

All Cluster slots apply, plus:
* Word count 4,000 to 6,000.
* TOC placeholder at top (CMS generates from heading hierarchy).
* Executive summary box immediately after TOC: 50 words, bolded. (This is the Slot 3 direct-answer box, expanded.)
* Minimum 10 H2s. Minimum 3 H3s per major H2.
* Minimum 10 internal-link anchor spans in body. Each marked with PLACEHOLDER\_URL and anchor text matching a target cluster's primary keyword.
* ROI calculator mention within the first two H2s.
* At least 3 comparison tables across the post (Slot 7 expanded).
* 8 visible FAQ plus 5 schema-only equals 13 total in JSON-LD (Slot 12 expanded).
* Mid-post CTA after second proof section. Second soft CTA before FAQ.
* Bullet lists: minimum 6 across body (Lock 10).
* Pull-out callouts: minimum 3 (Slot 14).
* Key Numbers block: required (almost always 3+ stats in a Pillar).

## STRUCTURAL TEMPLATE: Research Anchor extensions

All Cluster slots apply, plus:
* Word count 2,500 to 3,500.
* Executive summary box: 60 words, bolded.
* Methodology H2 (mandatory): sample size, selection criteria, date range, disclosed limitations.
* Minimum 5 finding H2s, each opening with a standalone headline stat as the first sentence.
* Each stat formatted quote-ready: "X% of Y did Z in 2026, up from A% in 2025."
* Implications section before FAQ.
* Dual CTA: primary "Book a Call" plus secondary "Download the full report." This is the only Content Type where two primary-weight CTAs are allowed.
* Comparison table mandatory.
* Bullet lists: minimum 4 across body (Lock 10).
* Pull-out callouts: minimum 2 (Slot 14).
* Key Numbers block: required.

---

## STRUCTURAL TEMPLATE: TL Post

Different content type entirely. Compact structure:

* 180 to 350 words.
* No headings at all (.docx or JSON).
* Opening hook as first paragraph. Stop-the-scroll first sentence mandatory.
* 2 to 3 body paragraphs.
* One-line outcome statement.
* Single CTA: hyperlink to paired blog's H2 anchor on codiste.com.
* In .docx: file contains title metadata plus body prose only.
* In JSON: single content slice with paragraph blocks. No cta\_button slice (CTA is an inline hyperlink).
* TL Posts are exempt from Lock 5 fragment requirement, Lock 10 bullet minimums, Slot 14 callouts, Slot 15 Key Numbers block.

\---

## CTA MATRIX

|Funnel|ICP signal|Supporting line direction|Button Label|URL|
|-|-|-|-|-|
|ToFU|CTO / tech lead|Validate problem plus architecture insight|Contact Us|/contact|
|ToFU|Founder / CEO|Validate problem plus value-exchange resource|Contact Us|/contact|
|ToFU|Enterprise lead|Validate problem plus sector case study|Contact Us|/contact|
|MoFU|CTO / tech lead|Echo build pain plus free technical assessment|Book a Call|/book-a-call|
|MoFU|Founder / CEO|Echo scoping pain plus honest conversation|Book a Call|/book-a-call|
|MoFU|Enterprise lead|Echo delivery pain plus discovery call|Book a Call|/book-a-call|
|BoFU|CTO / tech lead|Remove friction plus technical roadmap outcome|Book a Call|/book-a-call|
|BoFU|Founder / CEO|Remove friction plus no-commitment framing|Book a Call|/book-a-call|
|BoFU|Enterprise lead|Remove friction plus solution architecture outcome|Book a Call|/book-a-call|

Full URLs: https://www.codiste.com/contact and https://www.codiste.com/book-a-call.

CTA supporting line: hard cap eighteen words. No exceptions.
Button label whitelist: "Book a Call" or "Contact Us" only. Custom labels are forbidden.

\---

## OUTPUT 1: Default .docx Mode

Label: BLOG \[N] OF \[TOTAL] | \[ACTUAL H1 TITLE]

Produce the .docx via the docx skill. Save to /mnt/user-data/outputs/. Surface via present\_files. After production, run blog-audit-v1 against the content and append audit output below the OUTPUT 2 flags block.

### .docx structure mapping

|Blog element|Word element|
|-|-|
|H1 title|Heading 1 style, single occurrence|
|H2 section heading|Heading 2 style + Word bookmark (anchor\_id)|
|H3 subheading or table title|Heading 3 style + Word bookmark (anchor\_id)|
|TLDR bullets|Word bullet list style (LevelFormat.BULLET, never unicode bullets)|
|Direct-answer box|Body paragraph with bold run across full text|
|Body paragraph|Normal style|
|Proof section bullets|Word bullet list with setup paragraph above and tie-back below|
|Comparison table|Real Word table with borders, header row shaded|
|Primary CTA|H3 "Ready to \[outcome]?" + body supporting line + body "Button: \[label] → \[URL]" line|
|Mid-post CTA|Same pattern, softer H3|
|FAQ (visible and schema-only)|Single paragraph per Q+A. Bold run on question portion only. Single space then regular run for answer.|
|FAQ (Schema-only) block|Heading 2 "FAQ (Schema-only, do not publish)" + 5 inline Q+A paragraphs|
|Pull-out callout|Centered bolded paragraph with horizontal rule above and below|
|Key Numbers table|H3 "Key Numbers" + 2-column table, no header row, column 1 bold|
|Internal links|Word hyperlinks with text `\[PLACEHOLDER: target-keyword]`|
|Closing statement|Body paragraphs, no heading|

Font: Arial throughout. Page: US Letter (12240 x 15840 DXA). 1-inch margins.

### Pillar internal links in .docx mode

Pillar posts contain 10+ placeholder links as bracketed text:
`\[PLACEHOLDER: ai agents fintech compliance]`
`\[PLACEHOLDER: python agent frameworks]`

Output 2 lists every placeholder plus its anchor-text keyword.

\---

## OUTPUT 1: JSON Mode (triggered by "json" keyword)

Label: JSON: BLOG \[N] OF \[TOTAL] | \[ACTUAL H1 TITLE]

Single valid JSON code block. No commentary inside. After production, run blog-audit-v1 against the JSON and append audit output below the OUTPUT 2 flags block.

### Root JSON structure

```json
{
  "uid": "<primary keyword slugified, stop words stripped, hyphens, under 50 chars>",
  "type": "blog",
  "status": "draft",
  "title": "<H1, plain text, no colon semicolon or em dash>",
  "group": "<YYYY-MM-DD>",
  "category": "<Artificial Intelligence | Blockchain | Product Engineering>",
  "category\_list": \["<same as category>"],
  "description": "<max 155 chars, primary keyword in first 60 chars, ad copy style>",
  "meta\_title": "<H1> | Blog",
  "readtime": "<X mins>",
  "date": "<today ISO 8601, e.g. 2026-05-06T10:00:00+0000>",
  "last\_modified": "<today ISO 8601 with ms, e.g. 2026-05-06T10:00:00.000Z>",
  "seo": {
    "title": "<same as meta\_title>",
    "description": "<same as description>"
  },
  "slices": \[]
}
```

No img field. No seo.image. status always "draft."

### Slice schema (condensed)

**content slice.** items: \[{}]. primary.content array of blocks. Block types: heading2, heading3, paragraph, list-item, o-list-item. Every heading2 and heading3 block carries field `"anchor\_id": "<slugified heading text>"`. Strong span on headings: `{"start": 0, "end": <text.length>, "type": "strong"}`. Bold span for direct-answer box and pull-out callouts: same structure, applied to paragraph type.

**cta\_button slice.** items: \[]. primary has title paragraph plus name plus link object. Supporting line eighteen words maximum. Button name "Book a Call" or "Contact Us" only.

**faqs slice.** items array. Field names "question" and "answer." 10 items total (5 visible at indices 0 to 4, 5 schema-only at indices 5 to 9). CMS renders 5 visible, feeds all 10 to JSON-LD. CMS template renders Q and A inline.

**table slice.** items: \[]. primary.blog\_table.content array. Heading and intro paragraph precede the table slice in their own content slice (per Slot 7). Same slice type used for Slot 15 Key Numbers block.

### Slice order (Cluster)

1. content: TLDR H2 (own slice, ToFU/MoFU)
2. content: TLDR bullets (own slice, ToFU/MoFU)
3. content: hook paragraph(s)
4. content: direct-answer paragraph (bold span)
5. content: H2 problem heading (own slice)
6. content: problem paragraph(s)
7. content: H2 solution heading (own slice)
8. content: solution paragraph(s)/bullets with setup and tie-back
9. content: H2 proof heading (own slice)
10. content: proof paragraph(s)/bullets with setup and tie-back
11. content: H3 table title plus intro sentence (own slice)
12. table: comparison table
13. content: pull-out callout (Slot 14)
14. content: H3 "Key Numbers" (if 3+ stats)
15. table: Key Numbers table (if 3+ stats)
16. cta\_button: mid-post CTA (MoFU only)
17. content: H2/H3 remaining body sections
18. content: Codiste paragraph (no heading above it)
19. cta\_button: primary CTA
20. faqs: 10 items total (5 visible plus 5 schema-only)
21. content: closing statement

Slice IDs: UUID4 format, 4 in third segment, unique per slice.

\---

## OUTPUT 1: Supabase Mode

Produce JSON internally (same as JSON Mode). Run blog-audit-v1 against the JSON. Hand off to codiste-supabase-push-v2. That skill shows one-line confirmation per blog plus waits for "yes," then pushes.

\---

## OUTPUT 2: Flags + Meta (per blog, immediately after Output 1)

The first line of the block is always the Keyword Integration line. It carries the count produced by blog-audit-v2's deterministic grep, never an estimate.

```
Keyword Integration: \[Y] used out of \[X] provided (\[Z]%)
Primary keyword "\[exact feeder string]": \[N] exact, \[M] tokenized/variant

Content Type: \[value]
Funnel stage: \[value]
ICP: \[extracted, or "defaulted to Founder/CEO" if blank]
Vertical: \[value]
Word count: \[X]
Read time: \[X mins]
Tables: \[N, or "none"]
Bulleted lists in body: \[N]
Pull-out callouts: \[N]
Key Numbers block: \[present / not required]

Meta title: \[text] (X chars before " | Blog")
Description: \[text] (X chars, must be ≤155)
Slug (uid): \[text] (X chars, must be <50)

FLAGS (only list if relevant):
- Keywords not integrated (REQUIRED if integration below 50%): \[each missing keyword + one-line reason]
- PLACEHOLDER\_URLs: \[list each anchor and target keyword, or "none"]
- Pillar internal-link placeholders: \[list all 10+ with target keywords, pillar only]
- /contact and /book-a-call: live, no action needed
- Cover image: assign in CMS after import
- status: "draft", publish via CMS after review (JSON mode only)
```

The Keyword Integration line: Y is the count of feeder keywords found in the finished blog (exact plus tokenized/variant matches both count). X is the total size of the feeder pool (Primary plus Secondary plus LSI/NLP combined). Z is Y divided by X as a percentage. The number is whatever honest bottom-up integration produced. It is not written to a target. If Z is below 50, the "Keywords not integrated" flag is mandatory and lists every missing keyword with a reason. If Z is 50 or above, the line stands on its own and the missing-keyword flag is optional.

## OUTPUT 3: Audit (per blog, runs automatically after Output 2)

The audit skill (codiste-blog-audit-v2) runs against the blog and produces either a single PASS line or a section-grouped violation list. It also produces the deterministic keyword count that fills the Keyword Integration line in Output 2. See blog-audit-v2.md for full check list and output format.

## OUTPUT 4: Batch Summary (once after all blogs complete)

|Blog #|Title|Content Type|Funnel|ICP|Vertical|Audit|Links TO|Links FROM|
|-|-|-|-|-|-|-|-|-|

FUNNEL GAPS: \[Vertical plus ICP] missing \[stage], recommend \[suggested title]
AUDIT SUMMARY: \[N clean] / \[N flagged] of \[total]

\---

## IMPORTED DRAFT MODE (humanizer fold-in)

Trigger: The user pastes a draft and types "humanize this draft" or "humanize this."

This mode applies Voice Locks 1 through 11 to an existing draft. It does not rewrite structure. It does not add or remove sections. It does not change FAQ questions. It does not move visual asset labels.

Process:

1. Read the entire draft.
2. Apply Lock 1 (em dashes): remove every em dash. Replace with period plus new sentence, comma, parens, or rewrite.
3. Apply Lock 2 (headings): remove colons, semicolons, em dashes from H1, H2, H3.
4. Apply Lock 3 (passive voice in named sections): rewrite passive constructions in hook, problem, Codiste paragraph, CTA, closing.
5. Apply Lock 4 (never-use list): replace every banned phrase per the substitution list.
6. Apply Lock 5 (sentence rhythm): split sentences over 25 words, vary length, break repeated openers, add short sentences and fragments where rhythm needs them.
7. Apply Lock 6 (punctuation): remove semicolons, fix colons, trim parentheticals.
8. Apply Lock 10 (bullets): remove bullets from forbidden sections. Verify TLDR has at least 3.
9. Apply Lock 11 (tone): tighten any vendor-pitchy sentence. Add a short punchy sentence after every long technical section. Add a weird specific to any major H2 missing one.

If the draft is missing the direct-answer summary box, comparison table H3+intro, pull-out callouts, or Key Numbers block, flag it but do not add. Imported Draft Mode does not add structure. It cleans voice.

Output:

1. Full humanized draft, complete, not excerpts.
2. Four-line change summary:

```
Voice: \[em dashes removed, colons fixed, banned phrases replaced, counts]
Headings: \[what was cleaned]
Rhythm: \[sentences split, fragments added, openers varied, counts]
Tone: \[vendor-pitchy phrases rewritten, weird specifics added, counts]
```

If drafts are labeled "BLOG 1 OF N," apply mode per blog, label outputs "BLOG 1 OF N HUMANIZED."

\---

## STANDALONE CTA MODE (CTA optimizer fold-in)

Trigger: The user types "fix the CTA," "write a CTA for \[post]," or "make this CTA convert."

Required answers before writing:

1. Funnel stage (ToFU / MoFU / BoFU).
2. ICP (role plus stage plus profile).
3. The hook's specific pain (CTA must echo this).

If any answer is unclear, ask before writing.

Apply the CTA Matrix (above) plus Voice Lock 8 (the 18-word rule). The diagnostic offer principle governs every BoFU and MoFU CTA: the buyer gets something tangible from the first conversation (technical roadmap, scoping document, honest assessment), whether they sign with Codiste or not. ToFU CTAs are value-exchange (checklist, case study, walkthrough).

Region rule: CTA supporting line is neutral on specific regulation, even though region is USA. The pain is specific. The language is universal. No regulator named in the CTA. No state referenced.

Audit checklist for fixing an existing CTA:

1. Is the supporting line ≤18 words? If not, cut first.
2. Does funnel stage match the content? BoFU on ToFU post: rewrite.
3. Does supporting line echo the hook's specific pain, not a generic benefit? If line could appear on any other Codiste post unchanged: rewrite.
4. Is there only one action? Two CTAs in one block: remove one.
5. Does button label match whitelist? "Book a Call" or "Contact Us" only.
6. Does button label start with an action verb and stay under 6 words? (Both whitelisted labels do.)
7. Does the closing CTA echo the same pain as primary, or introduce a new angle? New angle: rewrite to mirror primary's pain at softer commitment level.
8. Does supporting line reference a specific US regulation or state? Yes: rewrite to neutral.

Mid-post CTA rule: only after proof section, one step softer than end CTA, same pain echo, ≤18 words.

Output format:

1. End CTA: supporting line (≤18 words) plus button label.
2. Mid-post CTA (only if requested): softer version (≤18 words).
3. One-line note: funnel stage plus ICP plus pain point plus word count for each supporting line.

\---
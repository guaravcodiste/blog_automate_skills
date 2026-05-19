# SKILL: blog_create_skill.md
# Codiste Blog Creator — Essential Rules Only
# Region: USA locked. American spellings only. No em dashes anywhere, including conversation.

---

## MODE DETECTION (read before anything else)

| Message Contains | Mode |
|---|---|
| No keyword (feeder rows only) | Default .docx |
| "json" / "as json" / "convert to json" | JSON |
| "push to supabase" / "ship to supabase" | Supabase (JSON internally, then push skill) |

After each blog in Default and JSON modes: run blog_audit_skill automatically.

---

## FEEDER FIELDS

| Field | Rule |
|---|---|
| Topic | Working signal only. Claude generates final H1 from Topic + ICP + Funnel + Primary Keyword. |
| Content Type | Pillar / Cluster / Research Anchor / TL Post. Drives template + word count. |
| Funnel Stage | ToFU / MoFU / BoFU. Drives CTA, depth, link strategy. Single most important field. |
| ICP | Free-text persona. Role + stage + profile. Read fully before writing. |
| Vertical | Fintech, SaaS, Martech, AdTech, RegTech, Proptech, SportsTech, Cross-Vertical only. Reject: AI, Blockchain, Healthtech, Edtech, Real Estate. |
| Primary Keyword | Exact from SemRush. Never modified. |
| Secondary Keywords | Comma-separated. Part of keyword pool. |
| LSI / NLP Terms | Comma-separated. Part of keyword pool. |
| FAQ / PAA | Optional verbatim questions. If blank, Claude generates. |
| Notes | Optional override. Takes precedence over defaults when present. |

Claude never asks for: word count, headings, meta description, image URLs, region, author, CTA copy, confirmation.

---

## STEP 0: PRE-WRITE SETUP

Run internally before writing a single sentence.

1. Confirm Content Type, Funnel, ICP, Vertical. Reject invalid verticals immediately.
2. Lock Primary Keyword. Never modify it.
3. Set word count target:

| Content Type | Funnel | Word Count |
|---|---|---|
| Pillar | Any | 4,000–6,000 |
| Cluster | BoFU | 900–1,200 |
| Cluster | MoFU | 1,200–1,500 |
| Cluster | ToFU | 1,400–1,600 |
| Research Anchor | Any | 2,500–3,500 |
| TL Post | Any | 180–350 |

4. Build keyword pool: Primary + all Secondary + all LSI/NLP = one combined list. This is the integration denominator (X) for Lock 12.
5. Sort pool into buckets:
   - **Fits clean:** grammatical as written. Integrate during writing.
   - **Fits tokenized:** ungrammatical as written but usable with stop words added or minor order change ("ai agents fintech" → "AI agents for fintech"). Integrate the variant.
   - **Does not fit:** cannot enter prose without stuffing. Do not force. Surface in Output 2.
6. ICP role routing:
   - Technical role (CTO, engineer): architecture and delivery proof.
   - Founder / CEO: outcome and risk reduction proof.
   - Enterprise lead: compliance, long-term support, sector case study proof.

---

## VOICE LOCKS (apply at moment of writing, not post-write)

### Lock 1: Em Dashes — Zero Everywhere
No em dash in any output (body, headings, captions, FAQ, CTA) or in conversation.
Substitutes: period + new sentence / comma / parentheses / rewrite.

### Lock 2: Heading Rules
- H1: no colon, no semicolon, no em dash. ≤60 characters OR ≤10 words. Must contain Primary Keyword.
- H2/H3: no colon, no semicolon, no em dash.
- Exception: the literal heading "TL;DR" keeps its semicolon.
- At least 2 H2s framed as questions ("What is / How does / Why do / When should").

### Lock 3: Passive Voice Forbidden In
Hook, problem section, Codiste paragraph, CTA, closing statement. Active voice only in these five sections.

### Lock 4: Never-Use List (zero tolerance, case-insensitive)
cutting-edge, revolutionary, seamless, robust, in today's world, leverage (verb), utilize, game-changer, it is worth noting, one might argue, put simply, in other words, essentially, with that in mind, that said, at the end of the day, more than ever, needless to say, it goes without saying, as mentioned, innovative, synergy, world-class, best-in-class, digital transformation (unless critical), unlock the potential, harness the power, navigate the landscape, embark on, journey (metaphor), paradigm, holistic, dynamic (filler), comprehensive (filler), elevate, transform (filler), empower (filler)

Replacements: utilize → use | leverage → use or name the action | implement → build/run/set up/deploy | robust → describe what makes it strong | seamless → describe the actual experience | comprehensive → describe what it covers | empower → say what it enables specifically

### Lock 5: Sentence Rhythm (binary rules)
- No sentence over 25 words. Split at natural clause break.
- After any sentence over 18 words, next sentence is under 12 words.
- No two consecutive sentences start with the same word.
- No three consecutive sentences of similar length.
- **Minimum 2 sentences under 7 words per major H2** (counted in body prose only, not headings, bullets, table cells).
- **Minimum 1 sentence fragment per Cluster, Pillar, Research Anchor** (not in headings, bullets, FAQ answers, CTA lines, or direct-answer box). Examples: "Right there." "Every time." "Not even close."

### Lock 6: Punctuation
- Zero em dashes (Lock 1).
- Zero semicolons in body prose. Use two sentences instead.
- Colons in body: only before a genuine list of 3+ items.
- Maximum 1 parenthetical per 500 words.

### Lock 7: Hook
- Exactly 3–4 sentences.
- Sentence 1 opens on ICP's specific daily pain. Never a generic industry statement.
- Primary Keyword appears in hook prose within first 100 words. H1 alone does not satisfy this.
- Funnel calibration: ToFU validates the problem is real | MoFU names the cost of the wrong partner | BoFU frames the decision moment.
- Use Proof/Stat if available. Realistic scenario if "none." Never invent a labeled stat.

### Lock 8: CTA Constraints
- Supporting lines: hard cap 18 words. Count before publishing.
- Button label whitelist: **"Book a Call"** or **"Contact Us"** only. No custom labels.
- No regulator, state, or US law reference in any CTA line.
- Follow CTA Matrix (below).

### Lock 9: Codiste Paragraph
- One paragraph. No heading above it. Ever.
- Flows from proof section as natural continuation.
- One outcome-led statement for this vertical and ICP.
- Forbidden language: co-founder, equity partner, venture co-builder, trusted advisor, industry-leading, partner of choice.
- Ends on a sentence that makes the CTA feel like the obvious next step.

### Lock 10: Bullet Discipline
**Bullets allowed in:** TLDR (mandatory), proof section, solution framing, list-based content, FAQ-adjacent answers, featured-snippet "what are" / "how to" sections.
**Bullets forbidden in:** hook, problem section, Codiste paragraph, CTA sections, direct-answer box, closing statement.

Every bullet = complete sentence (subject + verb). Minimum 2 bullets per list.

**Minimum bulleted list count in body (excluding TLDR):**
| Content Type | Minimum Lists |
|---|---|
| Cluster | 3 |
| Pillar | 6 |
| Research Anchor | 4 |
| TL Post | 0 |

Each bulleted list requires:
- Setup paragraph above (1–3 sentences).
- Tie-back paragraph below (1–2 sentences).
- List cannot be the entire content of an H2 section.

### Lock 11: Tone
- Engineer-to-founder voice. Technically credible. Zero sales polish.
- One concrete technical example per major section.
- No hedge phrases. No filler transitions. No "as we've seen" / "it's clear that" / "let's dive into."
- Every paragraph opens on a concrete noun, named entity, specific number, or direct claim.
- **One "weird specific" per major H2:** a named, concrete, non-load-bearing detail that anchors the prose in a real scenario. Must be specific enough that no AI model generates it by default. Examples: "the CISO who flagged it had been at the firm seven months," "the analyst on her third coffee of the morning," "the system running on the original 2019 deployment with no patches." One per section. No more.

### Lock 12: Keyword Integration (measured, never quota'd)
- Write the blog well first. Integrate every keyword that fits clean or fits tokenized naturally during writing.
- Keywords go into body prose. Not stuffed into bullet lists or FAQ answers to inflate count.
- Tokenized/variant matches count as hits. "AI agents for fintech" = hit for feeder keyword "ai agents fintech."
- Primary keyword, H1, direct-answer box, hook all count toward integration number.
- The integration percentage is whatever honest writing produces. It is a measurement, not a target.
- **Below 50%:** list every missing keyword + one-line reason in Output 2. This is an explanation trigger, not a fail gate.
- The count in Output 2 comes from the audit grep of the finished blog. Never from a count estimated while writing.

---

## STRUCTURAL TEMPLATE: Cluster (default)

### Slot 1: TLDR
**Skip for BoFU. Include for MoFU and ToFU.**
H2 heading exactly "TL;DR" in its own section. Minimum 3 bullets. Each bullet = complete sentence with a concrete standalone outcome.
- **.docx:** H2 "TL;DR" + Word bullet list.
- **JSON:** Two slices — Slice A: content slice with heading2 block "TL;DR" (anchor_id: "tldr"). Slice B: content slice with list-item blocks only.

### Slot 2: Hook
See Lock 7.

### Slot 3: Direct-Answer Summary Box
- 40–60 words. Fully bolded. Placed after hook, before first H2.
- Answers the primary search question directly.
- **.docx:** body paragraph with bold run across full text.
- **JSON:** paragraph block with strong span: `{"start": 0, "end": <text.length>, "type": "strong"}`.

### Slot 4: Problem H2
Active voice. Specific cost of the wrong decision: bad build, wrong stack, slow delivery, missed window. Include stat + US compliance risk where relevant. Realistic scenario if no stat available.

### Slot 5: Solution H2
Category-level solution. No Codiste mention yet. ICP language register.

### Slot 6: Proof H2
- ToFU: industry context + anonymized scenario.
- MoFU: before/after with specific measurable outcomes.
- BoFU: direct comparison or decision framework.
Always vertical-specific and ICP-specific.

### Slot 7: Comparison Table (mandatory for every Cluster)
Structure:
1. H3 title (keyword-rich, question-shaped where possible).
2. One intro sentence between H3 and table ("This matrix covers X on the Y dimensions that...").
3. Real table.

- **.docx:** real Word table with borders, header row shaded.
- **JSON:** content slice (H3 + intro paragraph) followed by table slice. Never pipe-delimited text in a paragraph.

### Slot 8: Statistics (minimum 3 across the post)
Format: `X% of Y did Z in 2026 (source: [publication], 2026).`
Tag scenarios clearly as scenarios. Never invent a labeled statistic.

### Slot 9: Mid-Post CTA
**MoFU only. Skip for ToFU and BoFU.**
Placed after proof section. One step softer than primary CTA. Supporting line ≤18 words. References specific proof just presented.

### Slot 10: Codiste Paragraph
See Lock 9. Placed after proof, before primary CTA.

### Slot 11: Primary CTA
- H3 must start with "Ready to" and end with "?".
- Supporting line ≤18 words.
- Button label: "Book a Call" or "Contact Us" only.
- URL: `/book-a-call` (MoFU/BoFU) or `/contact` (ToFU).
- Full URLs: `https://www.codiste.com/book-a-call` / `https://www.codiste.com/contact`
- **.docx:** H3 "Ready to [outcome]?" + body supporting line + body line "Button: [label] → [URL]".
- **JSON:** cta_button slice.

### Slot 12: FAQ
| Mode | Visible | Schema-only | Total |
|---|---|---|---|
| Cluster / Research Anchor | 5 | 5 | 10 |
| Pillar | 8 | 5 | 13 |

**.docx format:**
- Each Q+A = one paragraph. Bold question (ends with ?), single space, regular-weight answer.
- Visible: 40–60 words per answer. Schema-only: 25–40 words per answer.
- Schema-only under H2 "FAQ (Schema-only, do not publish)".

**JSON format:**
- faqs slice. Field names: `"question"` and `"answer"` only.
- Indices 0–4 visible. Indices 5–9 schema-only.

**Both modes:**
- Every answer starts with complete subject-verb sentence. Never "It's when..." Always "[Subject] is/does/..."
- First visible FAQ answer contains Primary Keyword naturally.
- At least one FAQ addresses US compliance specific to the vertical.

### Slot 13: Closing Statement
No heading. Maximum 3 sentences.
- Sentence 1: re-echoes the hook's specific pain.
- Sentence 2: sharpest, most direct sentence in the post. Short.
- Sentence 3: closing CTA hyperlinked to `/book-a-call` (MoFU/BoFU) or `/contact` (ToFU).

### Slot 14: Pull-Out Callouts
| Content Type | Minimum |
|---|---|
| Cluster | 1 |
| Pillar | 3 |
| Research Anchor | 2 |
| TL Post | 0 |

Rules:
- 12–20 words. Single sentence. No bullets. No headings.
- Pulls the sharpest, most quotable line from the section above it.
- Placement: after proof section (always). Pillar adds: after solution + after second proof. Research Anchor adds: after methodology.
- **.docx:** centered bold paragraph with horizontal rule above and below.
- **JSON:** paragraph block with full strong span covering entire text.

### Slot 15: Key Numbers Block (required when post has 3+ statistics)
- H3 "Key Numbers".
- 3-row, 2-column table. No header row.
- Column 1: the number (bold). Column 2: 1-line context (8–14 words).
- Placement: after proof section, before Codiste paragraph.
- **JSON:** heading3 block (anchor_id: "key-numbers") + table slice.

---

## PILLAR EXTENSIONS (add to Cluster base)

- 4,000–6,000 words.
- TOC placeholder at top.
- Executive summary box: 50 words, bolded (expanded Slot 3).
- Minimum 10 H2s. Minimum 3 H3s per major H2.
- Minimum 10 internal-link anchor spans: `[PLACEHOLDER: target-keyword]` — listed in Output 2.
- ROI calculator mention within first 2 H2s.
- At least 3 comparison tables.
- FAQ: 8 visible + 5 schema-only = 13 total.
- Mid-post CTA after second proof section. Second soft CTA before FAQ.
- Bullet lists: minimum 6 in body.
- Pull-out callouts: minimum 3.
- Key Numbers block: required.

---

## RESEARCH ANCHOR EXTENSIONS (add to Cluster base)

- 2,500–3,500 words.
- Executive summary: 60 words, bolded.
- Methodology H2 (mandatory): sample size, selection criteria, date range, disclosed limitations.
- Minimum 5 finding H2s. Each opens with a standalone headline stat as first sentence.
- Stat format: `"X% of Y did Z in 2026, up from A% in 2025."`
- Implications section before FAQ.
- Dual CTA: "Book a Call" (primary) + "Download the full report" (secondary). Only Content Type where two primary-weight CTAs are allowed.
- Bullet lists: minimum 4 in body.
- Pull-out callouts: minimum 2.
- Key Numbers block: required.

---

## TL POST (separate compact structure)

- 180–350 words. No headings at all.
- Structure: hook paragraph → 2–3 body paragraphs → one-line outcome statement → inline CTA hyperlink to paired blog on codiste.com.
- No TLDR, no H2s, no bullet lists, no CTA slice, no comparison tables, no FAQ.
- Exempt from: Lock 5 fragment requirement, Lock 10 bullet minimums, Slot 14, Slot 15.

---

## CTA MATRIX

| Funnel | ICP Signal | Button | URL |
|---|---|---|---|
| ToFU | CTO / tech lead | Contact Us | /contact |
| ToFU | Founder / CEO | Contact Us | /contact |
| ToFU | Enterprise lead | Contact Us | /contact |
| MoFU | CTO / tech lead | Book a Call | /book-a-call |
| MoFU | Founder / CEO | Book a Call | /book-a-call |
| MoFU | Enterprise lead | Book a Call | /book-a-call |
| BoFU | CTO / tech lead | Book a Call | /book-a-call |
| BoFU | Founder / CEO | Book a Call | /book-a-call |
| BoFU | Enterprise lead | Book a Call | /book-a-call |

Supporting line direction: ToFU = validate problem + value-exchange. MoFU = echo build pain + free technical assessment. BoFU = remove friction + technical roadmap outcome.
Supporting line: ≤18 words. No regulator. No state. Pain is universal.

---

## OUTPUT FORMAT: .docx Mode

| Blog Element | Word Element |
|---|---|
| H1 title | Heading 1 style |
| H2 heading | Heading 2 style + Word bookmark (anchor_id) |
| H3 subheading / table title | Heading 3 style + Word bookmark (anchor_id) |
| TLDR bullets | Word bullet list style (LevelFormat.BULLET) |
| Direct-answer box | Body paragraph, bold run across full text |
| Body paragraphs | Normal style |
| Comparison table | Real Word table with borders, header row shaded |
| Primary CTA | H3 "Ready to [outcome]?" + body supporting line + body "Button: [label] → [URL]" |
| Mid-post CTA | Same pattern, softer H3 |
| FAQ visible | One paragraph per Q+A. Bold on question. Regular weight on answer. |
| FAQ schema-only | H2 "FAQ (Schema-only, do not publish)" + 5 paragraphs |
| Pull-out callout | Centered bold paragraph, horizontal rule above + below |
| Key Numbers | H3 "Key Numbers" + 2-column Word table, no header row, column 1 bold |
| Closing statement | Normal paragraphs, no heading |

Font: Arial. Page: US Letter (12240 × 15840 DXA). 1-inch margins.

---

## OUTPUT FORMAT: JSON Mode

### Root JSON Structure

```json
{
  "uid": "<primary keyword slugified, stop words stripped, hyphens, under 50 chars>",
  "type": "blog",
  "status": "draft",
  "title": "<H1 text, no colon/semicolon/em dash>",
  "group": "<YYYY-MM-DD>",
  "category": "<Artificial Intelligence | Blockchain | Product Engineering>",
  "category_list": ["<same as category>"],
  "description": "<max 155 chars, primary keyword in first 60 chars>",
  "meta_title": "<H1> | Blog",
  "readtime": "<X mins>",
  "date": "<today ISO 8601>",
  "last_modified": "<today ISO 8601 with ms>",
  "seo": {
    "title": "<same as meta_title>",
    "description": "<same as description>"
  },
  "slices": []
}
```

No `img` field. No `seo.image`. `status` always `"draft"`.

### Slice Types

**content slice** — `items: [{}]`
Block types: `heading2`, `heading3`, `paragraph`, `list-item`, `o-list-item`.
Every `heading2` and `heading3` carries `"anchor_id": "<slugified heading text>"`.
Strong span on headings: `{"start": 0, "end": <text.length>, "type": "strong"}`.
Bold span for direct-answer box and pull-out callouts: same span structure on paragraph block.
`heading2` always in its own content slice. Never shares with paragraphs.
`heading3` may share a slice with following paragraphs.

**cta_button slice** — `items: []`
Primary has title paragraph + name + link object. Supporting line ≤18 words. Button name: "Book a Call" or "Contact Us" only.

**faqs slice** — `items: [...]`
Field names: `"question"` and `"answer"` only.
10 items total (indices 0–4 visible, 5–9 schema-only).

**table slice** — `items: []`
`primary.blog_table.content` array. Preceded by its own content slice containing H3 + intro paragraph.

### Slice ID Format
`slice_type$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx` — third segment always starts with 4. Every ID unique.

### Cluster Slice Order
1. content: TLDR H2 heading (own slice, MoFU/ToFU only)
2. content: TLDR list-item bullets (own slice, MoFU/ToFU only)
3. content: hook paragraphs
4. content: direct-answer paragraph (full bold span)
5. content: H2 problem heading (own slice)
6. content: problem paragraphs
7. content: H2 solution heading (own slice)
8. content: solution paragraphs + bullets with setup/tie-back
9. content: H2 proof heading (own slice)
10. content: proof paragraphs + bullets with setup/tie-back
11. content: H3 table title + intro sentence
12. table: comparison table
13. content: pull-out callout paragraph (full bold span)
14. content: H3 "Key Numbers" (if 3+ stats)
15. table: Key Numbers table (if 3+ stats)
16. cta_button: mid-post CTA (MoFU only)
17. content: additional H2/H3 body sections
18. content: Codiste paragraph (no heading above it)
19. cta_button: primary CTA
20. faqs: 10 items
21. content: closing statement

---

## OUTPUT 2: FLAGS BLOCK (per blog, immediately after Output 1)

```
Keyword Integration: [Y] used out of [X] provided ([Z]%)
Primary keyword "[exact feeder string]": [N] exact, [M] tokenized/variant

Content Type: [value]
Funnel stage: [value]
ICP: [extracted persona]
Vertical: [value]
Word count: [X]
Read time: [X mins]
Tables: [N]
Bulleted lists in body: [N]
Pull-out callouts: [N]
Key Numbers block: [present / not required]

Meta title: [text] ([X] chars before " | Blog")
Description: [text] ([X] chars, must be ≤155)
Slug (uid): [text] ([X] chars, must be <50)

FLAGS (list only if relevant):
- Keywords not integrated (REQUIRED if Z below 50%): [keyword + one-line reason each]
- PLACEHOLDER_URLs: [list each + target keyword, or "none"]
- Pillar internal-link placeholders: [all 10+ with targets, Pillar only]
```

The Keyword Integration line is always first. Its number comes from the audit grep, never from an estimate.

---

## HARD RULES (zero exceptions)

1. No output without complete feeder data. Flag missing required fields before writing.
2. Tables: always real Word tables (.docx) or table slices (JSON). Never pipe-delimited text.
3. Every table: H3 title + intro sentence. No exceptions.
4. No invented URLs. Use `PLACEHOLDER_URL` or `[PLACEHOLDER: keyword]` for all interlinks except `/contact` and `/book-a-call`.
5. Every slice ID unique. UUID4 format. Third segment starts with 4.
6. No colon, semicolon, or em dash in any heading. Exception: "TL;DR" semicolon.
7. `meta_title` always ends with `" | Blog"`.
8. Meta description: ≤155 characters. Primary keyword in first 60 characters.
9. No `img` field. No `seo.image`. No image slices. No image URLs anywhere.
10. JSON only inside code block. No commentary inside the block.
11. Output 2 immediately after each Output 1.
12. `heading2` always in its own content slice. Never shared with paragraphs.
13. `status` always `"draft"` in JSON mode.
14. TLDR for MoFU/ToFU only. Never for BoFU. Minimum 3 bullets.
15. FAQ: 5 visible + 5 schema-only = 10 total (Cluster). Inline Q+A format in .docx. Separate fields in JSON. First answer contains primary keyword.
16. CTA supporting line ≤18 words. Button label: "Book a Call" or "Contact Us" only.
17. Primary CTA H3 starts with "Ready to" and ends with "?".
18. Every H2 + H3 has `anchor_id` (JSON) or Word bookmark (.docx).
19. AI is never a vertical. Healthtech, Edtech, Real Estate, Blockchain never appear in output.
20. Region is USA. American spellings only ("percent" not "per cent"). Never prompt for region.
21. Zero em dashes in output and in conversation.
22. Zero passive voice in: hook, problem, Codiste paragraph, CTA, closing.
23. Zero items from the never-use list.
24. Codiste paragraph: one paragraph, no heading above it, no co-founder/equity/advisor language.
25. Minimum 2 sentences under 7 words per major H2 (in body prose only).
26. Minimum 1 sentence fragment per Cluster, Pillar, Research Anchor. TL Posts exempt.
27. One weird specific per major H2 section.
28. Bullet list minimums: Cluster 3, Pillar 6, Research Anchor 4. Each list: setup + tie-back. List ≠ entire H2 content.
29. Pull-out callout minimums: Cluster 1, Pillar 3, Research Anchor 2. 12–20 words each.
30. Key Numbers block required when post has 3+ statistics.
31. Audit runs automatically after every blog in Default and JSON modes.
32. Keyword integration is bottom-up and measured. Write well first. Count what landed. Never write to a pre-set target.
33. The Keyword Integration line in Output 2 always carries the audit's grep count, never an estimate.
34. Batch limits: max 7 blogs per session, max 3 Pillars, max 6 TL Posts. Flag over-cap before producing output.
35. No Dialora references anywhere.
36. Author is never flagged or requested. Assigned in CMS.

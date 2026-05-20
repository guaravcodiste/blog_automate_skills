# CODISTE BLOG SKILL
# Unified creation + audit. USA locked. American spellings. Zero em dashes everywhere.

---

## MODE DETECTION

| Message | Mode |
|---|---|
| Feeder row only | Default (.docx) |
| "json" / "as json" | JSON |
| "push to supabase" | Supabase (JSON internally, then push) |

After every Default or JSON blog: run audit automatically and append result.
Standalone audit: user pastes draft + "audit this blog" — check only, never rewrite.

---

## FEEDER FIELDS

| Field | Rule |
|---|---|
| Topic | Working signal only. Generate H1 from Topic + ICP + Funnel + Primary Keyword. |
| Content Type | Pillar / Cluster / Research Anchor / TL Post. Drives template + word count. |
| Funnel Stage | ToFU / MoFU / BoFU. Single most important field. Drives CTA, depth, TLDR. |
| ICP | Free-text persona. Read fully before writing. |
| Vertical | Fintech, SaaS, Martech, AdTech, RegTech, Proptech, SportsTech, Cross-Vertical only. Reject: AI, Blockchain, Healthtech, Edtech, Real Estate. |
| Primary Keyword | Exact from SemRush. Never modified. |
| Secondary Keywords | Comma-separated. Part of keyword pool. |
| LSI / NLP Terms | Comma-separated. Part of keyword pool. |
| FAQ / PAA | Optional verbatim questions. Generate if blank. |
| Notes | Optional override. Takes precedence over defaults. |

Never ask for: word count, headings, meta description, image URLs, region, author, CTA copy.

---

## STEP 0: PRE-WRITE SETUP

Run before writing a single sentence.

1. Confirm Content Type, Funnel, ICP, Vertical. Reject invalid verticals immediately.
2. Lock Primary Keyword. Never modify it.
3. Set word count target:

| Content Type | Funnel | Word Count |
|---|---|---|
| Cluster | BoFU | 900–1,200 |
| Cluster | MoFU | 1,200–1,500 |
| Cluster | ToFU | 1,400–1,600 |
| Pillar | Any | 4,000–6,000 |
| Research Anchor | Any | 2,500–3,500 |
| TL Post | Any | 180–350 |

4. Build keyword pool: Primary + Secondary + LSI/NLP = denominator X for integration count.
5. Sort pool: fits clean (integrate as-is) / fits tokenized (add stop words or minor reorder) / does not fit (surface in Output 2).
6. ICP routing: Technical role → architecture + delivery proof. Founder/CEO → outcome + risk. Enterprise → compliance + sector case study.

---

## VOICE LOCKS

### Lock 1: Zero Em Dashes
No em dash anywhere: body, headings, bullets, FAQ, CTA, or in conversation. Use period + new sentence, comma, or parentheses.

### Lock 2: Heading Rules
- H1: no colon, no semicolon. ≤60 chars OR ≤10 words. Contains Primary Keyword.
- H2/H3: no colon, no semicolon.
- Exception: the literal heading "TL;DR" keeps its semicolon.
- Minimum 2 H2s framed as questions (What / How / Why / When).

### Lock 3: Active Voice Zones
Active voice only in: hook, problem section, Codiste paragraph, CTA, closing statement.

### Lock 4: Never-Use List (zero tolerance)
cutting-edge, revolutionary, seamless, robust, in today's world, leverage (verb), utilize, game-changer, it is worth noting, one might argue, put simply, in other words, essentially, with that in mind, that said, at the end of the day, more than ever, needless to say, it goes without saying, as mentioned, innovative, synergy, world-class, best-in-class, digital transformation (unless critical), unlock the potential, harness the power, navigate the landscape, embark on, journey (metaphor), paradigm, holistic, dynamic (filler), comprehensive (filler), elevate, transform (filler), empower (filler)

### Lock 5: Sentence Rhythm
- No sentence over 25 words. Split at natural clause break.
- After any sentence over 18 words, next sentence must be under 12 words.
- No two consecutive sentences start with the same word.
- No three consecutive sentences of similar length.
- Minimum 2 sentences under 7 words per major H2 (body prose only, not bullets or headings).
- Minimum 1 sentence fragment per Cluster, Pillar, Research Anchor (not in bullets, FAQ, CTA, or direct-answer box).

### Lock 6: Punctuation
- Zero semicolons in body prose. Use two sentences instead.
- Colons in body: only before a genuine list of 3+ items.
- Maximum 1 parenthetical per 500 words.

### Lock 7: Hook
- Exactly 3–4 sentences.
- Sentence 1: ICP's specific daily pain. Never a generic industry statement.
- Primary Keyword appears in hook prose within first 100 words.
- MoFU: names the cost of the wrong partner. ToFU: validates the problem. BoFU: frames the decision moment.
- Use a real proof/stat if available. Realistic scenario if none available. Never invent a labeled stat.

### Lock 8: CTA Constraints
- Supporting lines: hard cap 18 words.
- Button label: "Book a Call" or "Contact Us" only.
- No regulator, state, or US law reference in any CTA line.

### Lock 9: Codiste Paragraph
- One paragraph. No heading above it. Ever.
- One outcome-led statement for this vertical and ICP.
- Forbidden language: co-founder, equity partner, venture co-builder, trusted advisor, industry-leading, partner of choice.
- Ends on a sentence that makes the CTA feel like the obvious next step.

### Lock 10: Bullet Discipline
- Bullets forbidden in: hook, problem section, Codiste paragraph, CTA, direct-answer box, closing statement.
- Every bullet = complete sentence (subject + verb).
- Minimum bullet lists in body (excluding TLDR): Cluster 3 | Pillar 6 | Research Anchor 4 | TL Post 0.
- Each list: setup paragraph above (1–3 sentences) + tie-back paragraph below (1–2 sentences). List cannot be entire H2 content.

### Lock 11: Tone and Weird Specific
- Engineer-to-founder voice. Zero sales polish. No hedge phrases. No filler transitions.
- Every paragraph opens on a concrete noun, named entity, specific number, or direct claim.
- One weird specific per major H2: a named, concrete, non-load-bearing detail anchored in a real scenario (e.g., "the system still running on the 2019 deployment"). One per section only.

### Lock 12: Keyword Integration
- Write well first. Integrate every keyword that fits clean or fits tokenized naturally during writing.
- Tokenized/variant matches count as hits ("AI agents for fintech" = hit for "ai agents fintech").
- Primary Keyword, H1, direct-answer box, and hook all count toward integration.
- Keywords found only in FAQ answers or bullets count as hits but are noted in Output 2 (body prose preferred).
- Integration % is a measurement, not a target. Below 50%: list every missing keyword + one-line reason in Output 2.

---

## STRUCTURAL TEMPLATE: CLUSTER (DEFAULT)

**Slot 1: TLDR** — MoFU and ToFU only. H2 "TL;DR". Minimum 3 bullets, each a complete sentence with concrete standalone outcome.

**Slot 2: Hook** — See Lock 7.

**Slot 3: Direct-Answer Summary Box** — 40–60 words. Fully bolded. After hook, before first H2. Answers the primary search question directly.

**Slot 4: Problem H2** — Active voice. Specific cost of wrong decision. Include stat + US compliance risk where relevant. No bullets.

**Slot 5: Solution H2** — Category-level solution. No Codiste mention yet.

**Slot 6: Proof H2** — ToFU: industry context + anonymized scenario. MoFU: before/after with specific measurable outcomes. BoFU: direct comparison or decision framework. Always vertical-specific and ICP-specific.

**Slot 7: Comparison Table (mandatory, every Cluster)** — H3 title (keyword-rich) + one intro sentence between H3 and table + real table.

**Slot 8: Statistics** — Minimum 3 in body prose. Format: "X% of Y did Z in 2026 (source: [publication], 2026)." Never invent a labeled stat. Tag scenarios as scenarios.

**Slot 9: Mid-Post CTA** — MoFU only. After proof section. Supporting line ≤18 words. References proof just presented.

**Slot 10: Codiste Paragraph** — After proof, before primary CTA. See Lock 9.

**Slot 11: Primary CTA** — H3 starts with "Ready to" and ends with "?". Supporting line ≤18 words. Button: "Book a Call" / "Contact Us". URL: `/book-a-call` (MoFU/BoFU) or `/contact` (ToFU).

**Slot 12: FAQ** — Cluster: 5 visible + 5 schema-only = 10 total. Each question ends with "?". Each answer starts subject-verb (never "It's..."). Visible answers: 40–60 words. Schema-only: 25–40 words. First visible answer contains Primary Keyword. At least one FAQ addresses US compliance for the vertical. Schema-only under H2 "FAQ (Schema-only, do not publish)."

**Slot 13: Closing Statement** — No heading. Maximum 3 sentences. Sentence 1: re-echoes hook pain. Sentence 2: sharpest, shortest sentence in the post. Sentence 3: closing CTA hyperlinked to `/book-a-call` or `/contact`.

**Slot 14: Pull-Out Callouts** — Cluster minimum 1, Pillar 3, Research Anchor 2. Each: 12–20 words, single sentence, pulls sharpest line from section above. Placement: after proof section always.

**Slot 15: Key Numbers Block** — Required when post has 3+ statistics. H3 "Key Numbers". 3-row, 2-column table, no header row. Column 1: bold number. Column 2: 8–14 word context. Placed after proof section, before Codiste paragraph.

---

## CONTENT TYPE VARIANTS

**Pillar** (4,000–6,000w): TOC placeholder, executive summary box (50w), min 10 H2s, 3 comparison tables, 6+ bullet lists, 3 pull-out callouts, 10 internal-link placeholders `[PLACEHOLDER: target-keyword]`, FAQ 8+5=13, mid-post CTA after second proof section.

**Research Anchor** (2,500–3,500w): Methodology H2 (sample size, criteria, date range, limitations), 5+ finding H2s each opening with standalone stat, implications section before FAQ, dual CTA (Book a Call + Download report), 4+ bullet lists, 2 pull-out callouts.

**TL Post** (180–350w): No headings. Hook → 2–3 body paragraphs → outcome statement → inline CTA. No TLDR, bullets, comparison tables, FAQ. Exempt from fragment, bullet minimums, Slots 14–15.

---

## CTA MATRIX

| Funnel | Button | URL |
|---|---|---|
| ToFU | Contact Us | https://www.codiste.com/contact |
| MoFU | Book a Call | https://www.codiste.com/book-a-call |
| BoFU | Book a Call | https://www.codiste.com/book-a-call |

Supporting line direction: ToFU = validate problem + value-exchange. MoFU = echo build pain + free technical assessment. BoFU = remove friction + technical roadmap outcome.

---

## OUTPUT FORMAT: .DOCX

| Element | Word Style |
|---|---|
| H1 | Heading 1 + Word bookmark |
| H2 | Heading 2 + Word bookmark (anchor_id) |
| H3 | Heading 3 + Word bookmark (anchor_id) |
| TLDR bullets | Word bullet list |
| Direct-answer box | Normal paragraph, full bold run |
| Comparison table | Real Word table, borders, header row shaded |
| Primary / Mid-post CTA | H3 + body supporting line + "Button: [label] → [URL]" |
| FAQ visible | One paragraph per Q+A. Bold question. Regular answer. |
| FAQ schema-only | Under H2 "FAQ (Schema-only, do not publish)" |
| Pull-out callout | Centered bold paragraph, horizontal rule above + below |
| Key Numbers | H3 "Key Numbers" + 2-column Word table, column 1 bold |
| Closing | Normal paragraphs, no heading |

Font: Arial. Page: US Letter. 1-inch margins.

---

## OUTPUT FORMAT: JSON

### Root Fields
```json
{
  "uid": "<primary keyword slugified, stop words stripped, hyphens, under 50 chars>",
  "type": "blog",
  "status": "draft",
  "title": "<H1 text>",
  "group": "<YYYY-MM-DD>",
  "category": "<Artificial Intelligence | Blockchain | Product Engineering>",
  "category_list": ["<same>"],
  "description": "<max 155 chars, primary keyword in first 60 chars>",
  "meta_title": "<H1> | Blog",
  "readtime": "<X mins>",
  "date": "<ISO 8601>",
  "last_modified": "<ISO 8601 with ms>",
  "seo": { "title": "<same as meta_title>", "description": "<same as description>" },
  "slices": []
}
```
No `img` field. No `seo.image`. `status` always `"draft"`.

### Slice Types
- **content**: `items: [{}]`. Block types: `heading2`, `heading3`, `paragraph`, `list-item`, `o-list-item`. Every H2/H3 carries `anchor_id`. Strong span on all heading blocks: `{"start": 0, "end": <text.length>, "type": "strong"}`. Bold span on direct-answer box and pull-out callout paragraphs: same span structure. `heading2` always in its own slice, never shared with paragraphs. `heading3` may share a slice with following paragraphs.
- **cta_button**: Title paragraph + name + link. Button name: "Book a Call" or "Contact Us" only.
- **faqs**: `items: [{question, answer}]`. Indices 0–4 visible, 5–9 schema-only.
- **table**: `primary.blog_table.content` array. Always preceded by its own content slice with H3 + intro paragraph.
- Slice ID: `slice_type$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx`. Third segment starts with 4. Every ID unique.

### Cluster Slice Order
content: TLDR H2 (own slice) → content: TLDR bullets → content: hook → content: direct-answer (full bold span) → content: H2 problem (own slice) → content: problem body → content: H2 solution (own slice) → content: solution body + bullets → content: H2 proof (own slice) → content: proof body + bullets → content: H3 table title + intro → table: comparison → content: pull-out callout (full bold) → content: H3 Key Numbers → table: Key Numbers → cta_button: mid-post (MoFU) → content: remaining H2/H3 sections → content: Codiste paragraph → cta_button: primary CTA → faqs → content: closing statement

---

## OUTPUT 2: FLAGS BLOCK

Appended immediately after every blog output.

```
Keyword Integration: [Y] used out of [X] provided ([Z]%)
Primary keyword "[feeder string]": [N] exact | [M] tokenized/variant

Content Type: [value]
Funnel stage: [value]
ICP: [extracted]
Vertical: [value]
Word count: [X] (published, schema-only excluded)
Read time: [X mins]
Tables: [N] | Bulleted lists in body: [N] | Pull-out callouts: [N]
Key Numbers block: [present / not required]

Meta title: [text] ([X] chars before " | Blog")
Description: [text] ([X] chars)
Slug (uid): [text] ([X] chars)

FLAGS (only if applicable):
- Content Type inferred: [value]. Human review required.
- Keywords not integrated (only if Z below 50%): [keyword + one-line reason]
- Keywords found only in FAQ/bullets: [list] — informational
- PLACEHOLDER_URLs: [list or "none"]
```

---

## AUDIT CHECKLIST

Runs after every blog. Report violations grouped by category. Each violation cites: category, rule, location, fix direction. "(clean)" when category had checks but zero violations. Keyword Integration block appears in every run — low Z is never a violation. If a check cannot run (missing data, malformed JSON, unparseable file): report as violation under "AUDIT INFRASTRUCTURE." Audit never fails silently.

**Standalone inference** (if feeder not provided): Funnel from CTA pattern ("Contact Us" = ToFU, "Book a Call" = MoFU/BoFU). Content Type from word count (under 1,600 = Cluster, 4,000+ = Pillar, under 350 = TL Post). Skip Category 8 if no keyword pool — note "feeder pool not provided, keyword count skipped." Standalone output uses same format without "[BLOG N]" prefix.

### Category 1: Voice Locks
Zero em dashes anywhere | Zero colons in H1/H2/H3 | Zero semicolons in H1/H2/H3 (exception: "TL;DR") | H1 ≤60 chars OR ≤10 words | H1 contains Primary Keyword | Minimum 2 H2s question-framed | Zero never-use list matches | No sentence over 25 words | After sentence over 18 words, next under 12 words | No two consecutive sentences start same word | Minimum 2 sentences under 7 words per major H2 (body prose only) | Minimum 1 sentence fragment in body (Cluster/Pillar/Research Anchor) | One weird specific per major H2 [approximate] | Zero semicolons in body prose | Zero "per cent" instances

### Category 2: Structural Slots
TLDR present (MoFU/ToFU) or absent (BoFU), minimum 3 bullets | Hook 3–4 sentences | Direct-answer box present (40–60 words, fully bolded) | Problem H2, Solution H2, Proof H2 present | Minimum 1 comparison table (Cluster), each preceded by H3 + intro sentence | Minimum 3 statistics in body prose | Mid-post CTA present (MoFU) or absent (ToFU/BoFU) | Codiste paragraph present with no heading above it | Primary CTA present | Closing statement (no heading, max 3 sentences) | Pull-out callouts: Cluster ≥1, Pillar ≥3, Research Anchor ≥2; each 12–20 words, single sentence | Key Numbers block after proof, before Codiste (required if 3+ stats)

### Category 3: Bullet Discipline
Minimum lists: Cluster 3, Pillar 6, Research Anchor 4 | No bullets in hook, problem, Codiste para, CTA, direct-answer box, closing | Each bullet complete sentence | Each list has setup paragraph above + tie-back paragraph below | No list is entire H2 content

### Category 4: CTA Discipline
Primary CTA H3 starts "Ready to" ends "?" | Primary + mid-post supporting lines ≤18 words | Button label "Book a Call" or "Contact Us" only | Button URL matches CTA Matrix | Zero regulator/state references in CTA lines | Closing links to /book-a-call (MoFU/BoFU) or /contact (ToFU)

### Category 5: FAQ Discipline
Visible count: 5 (Cluster/Research Anchor) or 8 (Pillar) | Schema-only count: 5 | Visible answers 40–60 words | Schema-only answers 25–40 words | Every question ends "?" | Every answer starts subject-verb (not "It's...") | First visible answer contains Primary Keyword | At least one FAQ addresses US compliance for the vertical

### Category 6: SEO and Meta
`meta_title` ends " | Blog" | Description ≤155 chars, Primary Keyword in first 60 chars | UID under 50 chars | JSON: `status: "draft"`, no `img`, no `seo.image`, no image slices, `heading2` in own slice | Every H2/H3 has `anchor_id` (JSON) or Word bookmark (.docx)

### Category 7: Brand and Project Rules
Zero Dialora references | Vertical is one of 8 allowed values | Zero co-founder/equity partner/trusted advisor/industry-leading/partner of choice in Codiste paragraph | Word count within range for Content Type + Funnel

### Category 8: Keyword Integration
Pool = Primary + Secondary + LSI/NLP = X. Count Y keywords with ≥1 hit. Z = Y ÷ X %. Exact match: contiguous substring, case-insensitive. Tokenized: stop words inserted or minor word-order variation counts. Keywords in H1, direct-answer box, hook count as hits. Keywords only in FAQ/bullets count but are noted. Always report Z and Primary Keyword exact + variant counts. Below 50%: list every missing keyword + one-line reason (mandatory). Low Z is never a violation.

### Audit Output Format

**Pass:**
```
AUDIT BLOG [N]: PASS
All checks clean. [X] checks across 8 categories.
KEYWORD INTEGRATION: [Z]% — [Y] of [X] used. Primary: [N] exact | [M] variant.
[Keywords only in FAQ/bullets noted here if any.]
```

**Fail:**
```
AUDIT BLOG [N]: [Y] violations across [Z] categories

VOICE LOCKS / STRUCTURAL SLOTS / BULLET DISCIPLINE / CTA DISCIPLINE / FAQ DISCIPLINE / SEO META / BRAND PROJECT RULES
- [violation: rule ref / location / fix direction] or (clean)

KEYWORD INTEGRATION: [Z]% — [Y] of [X] used. Primary: [N] exact | [M] variant.
[Missing keyword list only if Z below 50%.]

Fix flagged items before upload.
```

---

## HARD RULES (zero exceptions)

1. No output without complete feeder data. Flag missing required fields first.
2. Tables always real Word tables (.docx) or JSON table slices. Never pipe-delimited text.
3. Every table has H3 title + intro sentence before it.
4. No invented URLs. Use `PLACEHOLDER_URL` or `[PLACEHOLDER: keyword]` for all interlinks except `/contact` and `/book-a-call`.
5. `meta_title` always ends with " | Blog".
6. Meta description: ≤155 chars. Primary Keyword in first 60 chars.
7. No `img` field, no `seo.image`, no image slices anywhere.
8. JSON output only inside code block. Output 2 immediately after every Output 1.
9. `heading2` always in its own content slice. `status` always `"draft"` in JSON.
10. TLDR for MoFU/ToFU only, minimum 3 bullets. Never for BoFU.
11. FAQ: first visible answer contains Primary Keyword. All answers start subject-verb.
12. CTA button: "Book a Call" or "Contact Us" only. Supporting line ≤18 words.
13. Primary CTA H3 starts "Ready to" and ends "?".
14. Every H2/H3 has `anchor_id` (JSON) or Word bookmark (.docx).
15. Region USA. "percent" not "per cent." Never prompt for region.
16. Zero em dashes in output and in conversation.
17. Zero passive voice in hook, problem, Codiste paragraph, CTA, closing.
18. Zero never-use list matches anywhere.
19. Codiste paragraph: one paragraph, no heading above it, no co-founder/equity/advisor language.
20. Minimum 2 sentences under 7 words per major H2. Minimum 1 sentence fragment per Cluster/Pillar/Research Anchor.
21. One weird specific per major H2. Bullet list minimums enforced with setup + tie-back.
22. Pull-out callout minimums enforced. 12–20 words each.
23. Key Numbers block required when post has 3+ statistics.
24. Audit runs automatically after every Default and JSON blog. Audit never rewrites. Audit never blocks output.
25. Keyword integration is bottom-up and measured. Write well first. Count what landed. Never write to a pre-set target.
26. Batch limits: max 7 blogs per session, max 3 Pillars, max 6 TL Posts.
27. Zero Dialora references. Author never assigned — handled in CMS.

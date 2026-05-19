# SKILL: blog_audit_skill.md
# Codiste Blog Audit — Essential Checks Only
# Runs automatically after every blog in Default and JSON modes.
# Standalone: Anurag pastes a draft + types "audit this blog".

---

## TRIGGER

| Condition | Behavior |
|---|---|
| After every Default or JSON mode blog | Automatic. Output appended after Output 2 flags block. |
| Anurag pastes draft + "audit this blog" | Standalone audit only. No rewrites. |

This skill checks. It never rewrites, never modifies files, never blocks output.

---

## CONTEXT INFERENCE (standalone mode only)

If Funnel / Content Type / ICP not declared in source, infer:
- **Funnel:** CTA pattern — "Contact Us" = ToFU; "Book a Call" + diagnostic = MoFU/BoFU; mid-post CTA present = MoFU only.
- **Content Type:** word count — under 1,600 = Cluster; 4,000+ = Pillar; methodology section present = Research Anchor; under 350 = TL Post.

Flag inferred values at top of report. Anurag corrects if wrong.
If feeder keyword pool is not provided: skip Category 8 keyword count. Note "feeder pool not provided, keyword count skipped."

---

## CHECK CATEGORIES (8 total)

### Category 1: Voice Locks

| Check | Rule |
|---|---|
| Em dash count = 0 in entire body | Lock 1 |
| Em dash count = 0 in all headings | Lock 1 |
| Colon count = 0 in H1 | Lock 2 |
| Colon count = 0 in any H2 | Lock 2 |
| Colon count = 0 in any H3 | Lock 2 |
| Semicolon count = 0 in H1, H2, H3 (exception: literal "TL;DR") | Lock 2 |
| H1 character count ≤60 OR word count ≤10 | Lock 2 |
| H1 contains primary keyword | Lock 2 |
| At least 2 H2s framed as questions | Lock 2 |
| Never-use list: zero matches (case-insensitive) | Lock 4 |
| No sentence over 25 words | Lock 5 |
| Minimum 1 sentence fragment in body (Cluster, Pillar, Research Anchor) | Lock 5 |
| Per major H2: minimum 2 sentences under 7 words in body prose | Lock 5 |
| Semicolon count in body prose = 0 | Lock 6 |
| Per major H2: at least one weird specific present | Lock 11 [approximate] |
| Zero "per cent" instances (USA locked) | Project Rule |

### Category 2: Structural Slots

| Check | Rule |
|---|---|
| TLDR present for MoFU/ToFU; absent for BoFU | Slot 1 |
| TLDR bullet count ≥3 | Slot 1 |
| Hook is 3–4 sentences | Slot 2 |
| Direct-answer summary box present (40–60 words, bolded) | Slot 3 |
| H2 problem section present | Slot 4 |
| H2 solution section present | Slot 5 |
| H2 proof section present | Slot 6 |
| Comparison table count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 1) | Slot 7 |
| Each comparison table preceded by H3 title and intro sentence | Slot 7 |
| Statistics count ≥3 in body prose | Slot 8 |
| Mid-post CTA present if Funnel = MoFU | Slot 9 |
| Mid-post CTA absent if Funnel = ToFU or BoFU | Slot 9 |
| Codiste paragraph present with no heading above it | Slot 10 |
| Primary CTA present | Slot 11 |
| Closing statement present (no heading, max 3 sentences) | Slot 13 |
| Pull-out callout count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 2) | Slot 14 |
| Each pull-out callout is 12–20 words, single sentence | Slot 14 |
| Key Numbers block present if statistics count ≥3 | Slot 15 |
| Key Numbers block placed after proof section, before Codiste paragraph | Slot 15 |

### Category 3: Bullet Discipline

| Check | Rule |
|---|---|
| Bullet list count in body ≥ minimum (Cluster: 3, Pillar: 6, Research Anchor: 4, TL Post: 0) | Lock 10 |
| No bullets in: hook, problem section, Codiste paragraph, CTA, direct-answer box, closing statement | Lock 10 |
| Each bullet is a complete sentence (subject + verb) | Lock 10 |
| Each bulleted list has a setup paragraph above (1–3 sentences) | Lock 10 |
| Each bulleted list has a tie-back paragraph below (1–2 sentences) | Lock 10 |
| No bulleted list is the entire content of an H2 section | Lock 10 |

### Category 4: CTA Discipline

| Check | Rule |
|---|---|
| Primary CTA supporting line word count ≤18 | Lock 8 |
| Mid-post CTA supporting line word count ≤18 (if present) | Lock 8 |
| Primary CTA H3 starts with "Ready to" and ends with "?" | Slot 11 |
| Button label is "Book a Call" or "Contact Us" only | Lock 8 |
| Button URL matches funnel per CTA Matrix | CTA Matrix |
| CTA supporting line contains zero regulator / state references | Project Rule 4 |
| Closing CTA links to /book-a-call (MoFU/BoFU) or /contact (ToFU) | Slot 13 |

### Category 5: FAQ Discipline

| Check | Rule |
|---|---|
| Visible FAQ count = 5 (Cluster, Research Anchor) or 8 (Pillar) | Slot 12 |
| Schema-only FAQ count = 5 | Slot 12 |
| Total FAQ count = 10 (Cluster/Research Anchor) or 13 (Pillar) | Slot 12 |
| Each visible FAQ answer is 40–60 words | Slot 12 |
| Each schema-only FAQ answer is 25–40 words | Slot 12 |
| Each FAQ question ends with "?" | Slot 12 |
| Each FAQ answer starts with subject-verb sentence (not "It's...") | Slot 12 |
| First visible FAQ answer contains primary keyword | Slot 12 |
| At least one FAQ addresses US compliance for the vertical | Slot 12 |
| .docx mode: each Q+A is one paragraph, bold question + regular answer | Slot 12 |
| JSON mode: faqs slice has separate "question" and "answer" fields | Slot 12 |

### Category 6: SEO and Meta

| Check | Rule |
|---|---|
| `meta_title` ends with `" \| Blog"` | Hard Rule 7 |
| `description` character count ≤155 | Hard Rule 8 |
| Primary keyword appears in `description` within first 60 characters | Hard Rule 8 |
| `uid` (slug) character count <50 | Hard Rule 8 |
| `status` field = `"draft"` (JSON mode only) | Hard Rule 13 |
| No `img` field anywhere in JSON | Hard Rule 9 |
| No `seo.image` field | Hard Rule 9 |
| No image slices in slices array | Hard Rule 9 |
| Every H2 has `anchor_id` (JSON) or Word bookmark (.docx) | Hard Rule 18 |
| Every H3 has `anchor_id` (JSON) or Word bookmark (.docx) | Hard Rule 18 |
| `heading2` always in its own content slice (JSON mode) | Hard Rule 12 |

### Category 7: Brand and Project Rules

| Check | Rule |
|---|---|
| Zero references to Dialora | Project Rule |
| Vertical is one of the 8 allowed values | Project Rule |
| Zero references to "co-founder", "equity partner", "venture co-builder" in Codiste paragraph | Lock 9 |
| Zero references to "trusted advisor", "industry-leading", "partner of choice" in Codiste paragraph | Lock 9 |
| Word count within range for Content Type + Funnel combination | Project Rule 2 |

### Category 8: Keyword Integration (deterministic grep)

**This category is a measurement, not a pass/fail check. A low percentage never adds to the violation count.**

**Pool:** Primary keyword + all Secondary keywords + all LSI/NLP terms from the feeder row = denominator X.

**Match counting:**
- Exact contiguous substring match (case-insensitive) = hit.
- Tokenized/natural-variant match = hit. Test keyword with stop words inserted and with minor word-order variation. "ai agents fintech" → "ai agents for fintech" or "ai agents in fintech" = hit. "agentic ai fintech" → "agentic ai in fintech" = hit.
- Keywords found in H1, direct-answer box, or hook count as hits.
- Keywords found only in FAQ answers or bullet lists count as hits but are noted (body prose preferred).
- Y = count of pool keywords with at least one hit.
- Z = Y ÷ X as a percentage, rounded to nearest whole number.

| Check | Threshold |
|---|---|
| Compute Z% | Always — report it regardless of value |
| Primary keyword: report exact count and tokenized/variant count separately | Always |
| If Z < 50%: list every missing keyword + one-line reason | Mandatory below 50% |
| Keywords found only in FAQ/bullets: note them | Informational |
| Count must match actual grep of finished blog, never an estimate | Always |

---

## HEURISTIC CHECKS (labeled [approximate] in output)

Three checks cannot be made fully deterministic. Audit runs them and labels results.

| Check | Method |
|---|---|
| Weird specific per H2 (Lock 11) | Detect named entities, specific numbers, proper nouns per H2. Flag H2 with none as "possible missing weird specific [approximate]." |
| Sentence fragment count (Lock 5) | Detect sentences without clear subject-verb pair. Flag blogs with zero as "no fragments detected [approximate]." |
| Vendor-pitchy phrasing in Codiste paragraph (Lock 9) | Keyword scan for "industry-leading," "trusted partner," "world-class," etc. Subtle tone may slip through. |

All other checks are deterministic. Category 8 tokenized-variant matching is deterministic: it tests a defined set of stop-word and word-order variants, it does not guess.

---

## OUTPUT FORMAT

### Pass Case

```
AUDIT [BLOG N]: PASS
All checks clean. [X] checks across 8 categories.

KEYWORD INTEGRATION
Keyword Integration: [Y] used out of [X] provided ([Z]%)
Primary keyword "[exact feeder string]": [N] exact, [M] tokenized/variant
[If Z below 50%: Keywords not integrated: each missing keyword + one-line reason]
[If any keyword found only in FAQ/list: note it here]
```

### Fail Case

```
AUDIT [BLOG N]: [Y] violations across [Z] categories

VOICE LOCKS
- [Lock ref]: [specific violation] / [location in blog] / [fix direction]

STRUCTURAL SLOTS
- [Slot ref]: [specific violation]

BULLET DISCIPLINE
- [Lock ref]: [specific violation]

CTA DISCIPLINE
- [ref]: [specific violation]

FAQ DISCIPLINE
- [ref]: [specific violation] or "(clean)"

SEO / META
- [ref]: [specific violation] or "(clean)"

BRAND / PROJECT RULES
- [ref]: [specific violation] or "(clean)"

KEYWORD INTEGRATION
Keyword Integration: [Y] used out of [X] provided ([Z]%)
Primary keyword "[exact feeder string]": [N] exact, [M] tokenized/variant
[Missing keywords listed only if Z below 50%]

Fix flagged items in source and regenerate, or edit the file directly before upload.
```

### Rules for Violation Entries
- Every violation cites: category name, specific rule reference, location in blog, fix direction.
- "(clean)" appears under a section only when that section had checks but zero violations.
- The KEYWORD INTEGRATION block appears in every audit run (pass or fail). It is a measurement. Low Z is never listed as a violation and never adds to the violation count.
- Below 50% Z triggers the mandatory per-keyword missing list inside the KEYWORD INTEGRATION block only.

### Standalone Mode Output
Same format as above but without "[BLOG N]" prefix. Category 8 runs only if feeder pool is provided. If no pool: note "Keyword Integration: feeder pool not provided, count skipped" and run all other 7 categories normally.

---

## HARD RULES

1. Audit never rewrites the blog. Check and report only.
2. Audit never modifies any file.
3. Audit runs automatically after every blog in Default and JSON modes.
4. Audit output is appended after Output 2 flags block, labeled "AUDIT [BLOG N]."
5. Heuristic checks are labeled "[approximate]" in output.
6. Pass case: single PASS line + KEYWORD INTEGRATION block. Fail case: section-grouped violation list + KEYWORD INTEGRATION block.
7. Each violation cites category, rule reference, location, fix direction.
8. If a check cannot run (missing data, malformed JSON, unparseable file): report as violation under "AUDIT INFRASTRUCTURE." Audit never fails silently.
9. Audit never blocks output. Anurag sees the file regardless of audit result.
10. Eight categories only. No new categories without project instruction update.
11. Category 8 keyword count is deterministic grep of finished blog against feeder pool. Never accept a count estimated during writing.
12. KEYWORD INTEGRATION block appears in every audit run. Low integration is a measurement, not a violation, and never adds to the violation count.
13. Tokenized and natural-variant matches count as hits. Below 50% triggers mandatory per-keyword missing list inside KEYWORD INTEGRATION block only.

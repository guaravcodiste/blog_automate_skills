# SKILL: codiste-blog-audit-v1.md
# ─────────────────────────────────────────────────────────────────────────────
# New skill. Deterministic post-write check.
# Runs automatically after every blog produced in default and JSON modes.
# Catches what Voice Locks leak. Section-grouped violation list.
# Standalone mode: Anurag pastes a draft and types "audit this blog".
# ─────────────────────────────────────────────────────────────────────────────

## Purpose

Voice Locks in blog-creator-v8 are prevention. This skill is the check. Two reasons it exists:

1. Voice Locks fire at the moment of writing. Some rules need verification after the full blog is produced (counts, presence of slots, cross-section consistency). Mid-write enforcement leaks because rule fires on local context, not the whole document.
2. Anurag should not have to scan the .docx or JSON for colon-in-H1 violations or missing mid-post CTAs every time. The audit catches them deterministically.

This skill never rewrites. It checks and reports. Anurag fixes flagged items in source and regenerates, or edits the file directly before upload.

## Triggers

**Automatic:** runs after every blog produced by blog-creator-v8 in default mode and JSON mode. Output is appended after OUTPUT 2 flags block and labeled "AUDIT [BLOG N]."

**Standalone:** Anurag pastes a draft (or attaches a .docx) and types "audit this blog" or "audit this draft." Output is the audit report only.

**Skipped:** Imported Draft Mode and Standalone CTA Mode in blog-creator-v8 do not trigger automatic audit. Anurag can still trigger standalone audit on those outputs if wanted.

## What this skill does

Runs every check listed below against the produced blog. Outputs either a single PASS line (clean) or a section-grouped violation list (flagged). Each violation cites the specific rule and the location in the blog.

## What this skill never does

- Rewrites the blog.
- Modifies any file.
- Asks Anurag for clarification mid-audit.
- Runs heuristic checks as if they were deterministic. Heuristics are flagged as such ("approximate match").

---

## CHECK CATEGORIES

The audit groups checks into seven categories. Each violation lists category, rule reference, and location.

### Category 1: Voice Locks (Lock 1, 2, 4, 5, 6, 11)

| Check | Rule |
|---|---|
| Em dash count = 0 in entire body | Lock 1 / Hard Rule 23 |
| Em dash count = 0 in headings | Lock 1 |
| Colon count = 0 in H1 | Lock 2 / Hard Rule 6 |
| Colon count = 0 in any H2 | Lock 2 |
| Colon count = 0 in any H3 | Lock 2 |
| Semicolon count = 0 in H1, H2, H3 (exception: literal "TL;DR") | Lock 2 |
| H1 character count ≤ 60 OR word count ≤ 10 | Lock 2 |
| H1 contains the primary keyword | Lock 2 |
| At least 2 H2s framed as questions | Lock 2 |
| Never-use list scan: zero matches case-insensitive | Lock 4 / Hard Rule 25 |
| Sentence count where word count > 25: zero | Lock 5 |
| Minimum 1 sentence fragment in body (Cluster, Pillar, Research Anchor) | Lock 5 / Hard Rule 28 |
| Per major H2: minimum 2 sentences under 7 words in body prose | Lock 5 / Hard Rule 27 |
| Semicolon count in body prose: zero | Lock 6 |
| Per major H2: at least one weird specific present (heuristic) | Lock 11 / Hard Rule 29 |
| Spelling check: zero "per cent" instances (USA locked) | Project Rule 4 / instructions |

### Category 2: Structural slots (Slots 1 to 15)

| Check | Rule |
|---|---|
| TL;DR present (ToFU/MoFU only, absent for BoFU) | Slot 1 / Hard Rule 15 |
| TL;DR bullet count ≥ 3 | Slot 1 |
| Hook is 3 to 4 sentences | Slot 2 / Lock 7 |
| Direct-answer summary box present (40 to 60 words, bolded) | Slot 3 |
| H2 problem section present | Slot 4 |
| H2 solution section present | Slot 5 |
| H2 proof section present | Slot 6 |
| Comparison table count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 1) | Slot 7 |
| Each comparison table preceded by H3 title and intro sentence | Slot 7 / Hard Rule 3 |
| Statistics count ≥ 3 in body prose | Slot 8 |
| Mid-post CTA present if Funnel = MoFU | Slot 9 |
| Mid-post CTA absent if Funnel = ToFU or BoFU | Slot 9 |
| Codiste paragraph present, no heading above it | Slot 10 / Lock 9 / Hard Rule 26 |
| Primary CTA present | Slot 11 |
| Closing statement present, no heading, max 3 sentences | Slot 13 |
| Pull-out callout count ≥ minimum (Cluster: 1, Pillar: 3, Research Anchor: 2) | Slot 14 / Hard Rule 31 |
| Each pull-out callout is 12 to 20 words, single sentence | Slot 14 |
| Key Numbers block present if statistics count ≥ 3 | Slot 15 / Hard Rule 32 |
| Key Numbers block placed after proof section, before Codiste paragraph | Slot 15 |

### Category 3: Bullet discipline (Lock 10)

| Check | Rule |
|---|---|
| Bullet list count in body ≥ minimum (Cluster: 3, Pillar: 6, Research Anchor: 4, TL Post: 0) | Lock 10 / Hard Rule 30 |
| No bullets in: hook, problem section, Codiste paragraph, CTA, direct-answer box, closing statement | Lock 10 |
| Each bullet is a complete sentence (subject-verb) | Lock 10 |
| Each bulleted list has a setup paragraph above (1 to 3 sentences) | Lock 10 |
| Each bulleted list has a tie-back paragraph below (1 to 2 sentences) | Lock 10 |
| No bulleted list is the entire content of an H2 section | Lock 10 |

### Category 4: CTA discipline (Lock 8 / CTA Matrix)

| Check | Rule |
|---|---|
| Primary CTA supporting line word count ≤ 18 | Lock 8 / Hard Rule 17 |
| Mid-post CTA supporting line word count ≤ 18 (if present) | Lock 8 |
| Primary CTA H3 starts with "Ready to" and ends with "?" | Slot 11 / Hard Rule 18 |
| Button label is "Book a Call" or "Contact Us" only | CTA Matrix / Hard Rule 17 |
| Button URL matches funnel per CTA Matrix | CTA Matrix |
| CTA supporting line contains zero references to specific US regulators or states | Project Rule 4 |
| Closing CTA links to /book-a-call (MoFU/BoFU) or /contact (ToFU) | Slot 13 |

### Category 5: FAQ discipline (Slot 12)

| Check | Rule |
|---|---|
| Visible FAQ count = 5 (Cluster, Research Anchor) or 8 (Pillar) | Slot 12 / Hard Rule 16 |
| Schema-only FAQ count = 5 | Slot 12 |
| Total FAQ count = 10 (Cluster, Research Anchor) or 13 (Pillar) | Slot 12 |
| Each visible FAQ answer is 40 to 60 words | Slot 12 |
| Each schema-only FAQ answer is 25 to 40 words | Slot 12 |
| Each FAQ question ends with "?" | Slot 12 |
| Each FAQ answer starts with subject-verb sentence (not "It's...") | Slot 12 |
| First visible FAQ answer contains primary keyword | Slot 12 |
| At least one FAQ addresses US compliance specific to the vertical | Slot 12 |
| .docx mode: each Q+A is a single paragraph with bold question + regular answer | Slot 12 / Hard Rule 16 |
| JSON mode: faqs slice has separate "question" and "answer" fields | Slot 12 |

### Category 6: SEO and meta (Hard Rules 6, 7, 8, 9, 14)

| Check | Rule |
|---|---|
| meta_title ends with " \| Blog" | Hard Rule 7 |
| description character count ≤ 155 | Hard Rule 8 |
| Primary keyword appears in description first 60 characters | Hard Rule 8 |
| uid (slug) character count < 50 | Hard Rule 8 |
| status field = "draft" (JSON mode only) | Hard Rule 14 |
| No img field anywhere in JSON | Hard Rule 9 |
| No seo.image field | Hard Rule 9 |
| No image slices in slices array | Hard Rule 9 |
| Every H2 has anchor_id (JSON) or Word bookmark (.docx) | Hard Rule 19 |
| Every H3 has anchor_id (JSON) or Word bookmark (.docx) | Hard Rule 19 |
| heading2 always in its own content slice (JSON mode) | Hard Rule 12 |

### Category 7: Brand and project rules

| Check | Rule |
|---|---|
| Zero references to Dialora | Never-do list |
| Vertical is one of the eight allowed values | Project Rule / Hard Rule 20 |
| Zero references to "co-founder", "equity partner", "venture co-builder" in Codiste paragraph | Lock 9 / Hard Rule 26 |
| Zero references to "trusted advisor", "industry-leading", "partner of choice" in Codiste paragraph | Lock 9 |
| Word count within range for Content Type | Project Rule 2 |

---

## Heuristic checks (flagged as approximate)

Some checks cannot be made fully deterministic from text alone. The audit runs a heuristic and labels the result with "[approximate]":

- **Weird specific per H2 (Lock 11):** detects presence of named entities, specific numbers, or proper nouns in body prose for each H2 section. Flags H2 sections with no detected named-entity anchor as "possible missing weird specific [approximate]." Anurag verifies manually.
- **Sentence fragment count (Lock 5):** detects sentences without a clear subject-verb pair. False positives possible (some short sentences are technically grammatical). Flags blogs with zero detected fragments as "no fragments detected [approximate]."
- **Vendor-pitchy phrasing in Codiste paragraph (Lock 9):** keyword scan for "industry-leading," "trusted partner," "world-class," etc. Catches obvious cases. Subtle vendor tone may slip through.

These three are the heuristic checks. All other checks above are deterministic.

---

## OUTPUT FORMAT

### Pass case (clean blog)

```
AUDIT [BLOG N]: PASS
All checks clean. [X] checks across 7 categories.
```

### Partial pass / fail case (violations found)

```
AUDIT [BLOG N]: [Y] violations across [Z] categories

VOICE LOCKS
- Lock 2 / Hard Rule 6: H1 contains a colon ("Private AI Agents for Regulated Fintech: The Build-vs-Managed Reference Stack"). Rewrite to remove colon.
- Lock 5 / Hard Rule 28: No sentence fragments detected. Minimum 1 required for Cluster. [approximate]
- Lock 11 / Hard Rule 29: H2 "The Solution" missing weird specific anchor. Add named, concrete, non-load-bearing detail. [approximate]

STRUCTURAL SLOTS
- Slot 9: Mid-post CTA missing. Funnel = MoFU requires mid-post CTA after proof section.
- Slot 14 / Hard Rule 31: Pull-out callout count = 0. Cluster requires minimum 1.

BULLET DISCIPLINE
- Lock 10 / Hard Rule 30: Bullet list count in body = 0. Cluster requires minimum 3.

CTA DISCIPLINE
- CTA Matrix / Hard Rule 17: Button label "Book a Technical Assessment" is not in whitelist. Use "Book a Call" or "Contact Us" only.
- Slot 11 / Hard Rule 18: Primary CTA missing "Ready to [outcome]?" H3 above the supporting line.

FAQ DISCIPLINE
- (clean)

SEO / META
- (clean)

BRAND / PROJECT RULES
- Project Rule 4: Three "per cent" instances detected. Region is USA, use "percent" or "%".

Fix flagged items in source and regenerate, or edit the file directly before upload.
```

### Standalone mode output

When triggered manually with "audit this blog," output is the audit report only with no Pass/Fail count line. Format identical to above but without "[BLOG N]" prefix.

---

## How the audit handles missing context

If audit runs in standalone mode and the source draft does not declare Funnel Stage, Content Type, or ICP explicitly, the audit infers from content:

- Funnel: looks at CTA pattern (Contact Us = ToFU, Book a Call with diagnostic = MoFU/BoFU, mid-post CTA = MoFU only).
- Content Type: looks at word count and structure (under 1,600 = Cluster, 4,000+ = Pillar, methodology section present = Research Anchor, under 350 = TL Post).
- ICP: looks at hook framing and proof type.

If inference is uncertain, the audit flags the inferred values at the top of the report and runs all checks against them. Anurag corrects in source if inference was wrong.

---

## Hard rules (zero exceptions)

1. Audit never rewrites the blog. Check and report only.
2. Audit never modifies any file.
3. Audit runs automatically after every blog in default and JSON modes (blog-creator-v8 invokes it).
4. Audit output is appended after OUTPUT 2 flags block, labeled "AUDIT [BLOG N]."
5. Heuristic checks are labeled "[approximate]" so Anurag knows to verify manually.
6. Pass case is a single line. Violation case is section-grouped.
7. Each violation cites: category, specific rule, location in blog, fix direction.
8. Audit never fails silently. If a check cannot run (missing data, malformed JSON, unparseable .docx), the audit reports the failure as a violation with category "AUDIT INFRASTRUCTURE."
9. Audit never blocks output. Anurag sees the .docx or JSON regardless of audit result.
10. Audit categories are: Voice Locks, Structural Slots, Bullet Discipline, CTA Discipline, FAQ Discipline, SEO/Meta, Brand/Project Rules. Seven categories total. No new categories without project instruction update.
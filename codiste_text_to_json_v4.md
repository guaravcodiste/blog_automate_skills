# SKILL: codiste-text-to-json.md
# ─────────────────────────────────────────────────────────────────────────────
# Replaces v3 in full. Shares JSON schema with blog-creator-v8.
# Handles finalized blog text → JSON conversion ONLY.
# Zero content alteration. Zero rewriting. Zero editorial judgment.
# v4 adds: inline FAQ source handling. Pull-out callout detection. Key Numbers detection.
# ─────────────────────────────────────────────────────────────────────────────

## Trigger

Anurag pastes a finished blog draft with the keyword "convert," "convert this to JSON," "turn this into JSON," "this is the final blog convert it," or "text to JSON."

This skill fires when the source is FINISHED text. It does NOT fire for batch feeder rows (those go to blog-creator-v8).

---

## THE ONE ABSOLUTE RULE

Every word, comma, punctuation mark, heading, paragraph, and sentence from the source text appears in the JSON exactly as written.

No exceptions. No editorial passes. No humanization. No restructuring. No rewriting headings. No dropping sections. No merging paragraphs. No splitting paragraphs. No adding content. No applying Voice Locks.

The source text is FINAL. It was approved before it reached this skill. This skill is a formatting tool only. Not a writing tool. Not an editing tool.

---

## What this skill does

Takes finalized plain text or .docx blog. Maps to the slice schema. Outputs a single valid JSON code block ready for Supabase import.

Adds three technical fields automatically without altering visible content:
1. anchor_id on every heading2 and heading3 (slugified from heading text).
2. Splits FAQ into 5 visible plus up to 5 schema-only if source has more than 5 pairs.
3. Validates that every table has a preceding H3 title plus intro sentence (flags if missing, never adds).

Recognizes new v8 structural elements without altering them:
- Pull-out callouts (bold standalone paragraphs in body, mapped as paragraph blocks with strong span).
- Key Numbers blocks (H3 "Key Numbers" plus 2-column table, mapped as content slice plus table slice).
- Inline FAQ format (bold question + regular answer in single paragraph, split at first question mark for JSON fields).

Structure only. Words untouched.

---

## What this skill never does

- Rewrites any heading, even to fix punctuation.
- Drops any section, even if it seems redundant.
- Merges or splits paragraphs. Source paragraph count equals JSON paragraph block count.
- Adds content. No extra intro sentences. No transition sentences.
- Applies Voice Locks. Those are for blog creation, not conversion.
- Applies SEO rules. The text is final, SEO was handled upstream.
- Applies CTA rules. CTA text is used verbatim from source.
- Changes TLDR format. Source has 5 bullet lines, JSON gets 5 list-item blocks.
- Paraphrases. Never. Under any circumstance.
- Moves a comma. Literally not one punctuation mark changes.

---

## How to read the source

### Identify sections in this order:
1. Title (first line or clearly marked H1).
2. TLDR block (lines after "TL;DR" or "TLDR" before the first paragraph).
3. Hook (paragraphs before the first H2).
4. Direct-answer summary box (if present, a bolded 40 to 60 word paragraph after hook, before first H2).
5. H2 sections (every bold or clearly marked section heading).
6. H3 subsections (any subheadings within a section, including table titles and "Key Numbers" headings).
7. Pull-out callouts (bolded standalone paragraphs of 12 to 20 words placed between body sections).
8. Key Numbers tables (H3 "Key Numbers" followed by a 2-column table).
9. CTA closing (final paragraph(s) with Codiste call to action).
10. FAQ (if present, labeled questions and answers).

### Paragraph boundaries
One blank line in source equals paragraph break equals separate paragraph block in JSON. No blank line equals same paragraph equals same paragraph block. Never merge two paragraphs into one block. Never split one paragraph into two blocks.

### TLDR lines
Each bullet or line in TLDR equals one list-item block in the TLDR content slice. Never merged. Never converted to paragraph blocks. Always list-item type.

TLDR always maps to TWO slices in JSON:
- Slice 1: TLDR H2 heading. Own dedicated content slice. heading2 block, text exactly "TL;DR." Strong span: `{"start": 0, "end": 5, "type": "strong"}`. anchor_id: `"tldr"`.
- Slice 2: TLDR bullets. Separate content slice. One list-item block per bullet line from source.

If source does not format TLDR as H2, this skill still maps it as heading2 "TL;DR" in slice 1. Source formatting does not override this rule.

### FAQ format detection
v8 source format is inline: bold question + space + regular answer, all in one paragraph.
Older source format is block: question on its own line, answer on the next paragraph.

Detection rule: if a paragraph starts with bold text ending in a question mark followed by non-bold text, treat as inline format. Otherwise treat as block format.

For inline format conversion to JSON:
- Split the paragraph at the first question mark.
- "question" field: text from start of paragraph through and including the question mark.
- "answer" field: text starting at the first non-whitespace character after the question mark.

For block format conversion to JSON:
- "question" field: the question line, including the question mark.
- "answer" field: the answer paragraph(s) following.

JSON output is identical regardless of source format. Field names are always "question" and "answer." CMS template handles inline rendering of separate fields.

### Pull-out callout detection
A pull-out callout is a paragraph in body sections (between H2s, not inside a table, not inside a list) that is fully bolded and contains 12 to 20 words in a single sentence. Map as a paragraph block with full strong span: `{"start": 0, "end": <text.length>, "type": "strong"}`.

Do not move, alter, or merge callouts with surrounding paragraphs. They sit in their own paragraph block within whichever content slice contains the surrounding section.

### Key Numbers block detection
An H3 with text "Key Numbers" followed by a 2-column table with no header row maps to:
- Content slice: heading3 block "Key Numbers" with anchor_id "key-numbers".
- Table slice: standard table slice with the 2-column structure preserved.

If source has Key Numbers H3 but no table, flag in output. Do not invent the table.

---

## Slice mapping

### Title → root "title" field
Exact text. No changes.

### TLDR → always two slices (H2 + list-items)
As above.

### Hook paragraphs → content slice
Each paragraph equals one paragraph block. All hook paragraphs in one content slice. Placed after TLDR slices (if present).

### Direct-answer summary box (bolded paragraph after hook) → content slice
Single paragraph block with bold span covering full text:
`{"start": 0, "end": <text.length>, "type": "strong"}`

### H2 heading → own dedicated content slice, always

```json
{
  "type": "heading2",
  "text": "<exact heading text>",
  "spans": [{"start": 0, "end": <text.length>, "type": "strong"}],
  "direction": "ltr",
  "anchor_id": "<slugified heading text>"
}
```

Never share a content slice with paragraphs. anchor_id generated from heading text (lowercase, hyphens, no special chars).

### Paragraphs under an H2 → content slice
All paragraphs for that section in one content slice following the H2 slice. Each paragraph equals one paragraph block.

### Bulleted lists under an H2/H3 → list-item blocks
Each bullet equals one `list-item` block in the content slice. Bullets sit in the same content slice as surrounding paragraphs for that section.

### Numbered lists under an H2/H3 → o-list-item blocks
Each numbered item equals one `o-list-item` block. Strip the number prefix from text. CMS renderer handles numbering.

### H3 heading → shares content slice with following paragraphs

```json
{
  "type": "heading3",
  "text": "<exact heading text>",
  "spans": [{"start": 0, "end": <text.length>, "type": "strong"}],
  "direction": "ltr",
  "anchor_id": "<slugified heading text>"
}
```

Followed immediately by its paragraph block(s) in the same slice.

### Table title plus intro sentence → content slice before table slice
Every table in source should have an H3 title immediately above it and an intro sentence between the H3 and the table.
- H3 → heading3 block with anchor_id.
- Intro sentence → paragraph block in the same content slice.
- Table follows in its own table slice.

If source is missing the H3 title OR the intro sentence: FLAG in output, do NOT add. This skill reports missing structure but never invents content.

Exception: Key Numbers table does not require an intro sentence. The H3 "Key Numbers" precedes the table directly.

### Pull-out callout → paragraph block with full strong span
Single paragraph block placed in the content slice for whichever section it appears in. Full text wrapped in strong span. Position preserved exactly as in source.

### Tables → table slice
Standard table slice schema. Cell text equals exact text from source.

### Key Numbers table → table slice with standard schema
Same table slice schema. 3 rows, 2 columns, no header row distinction needed in the schema (CMS template styles column 1 bold).

### CTA closing paragraph → content slice
Exact text. One paragraph block. No heading above it.

### CTA button → cta_button slice
If source contains a clear CTA with a button action (Book a Call / Contact Us), map to cta_button slice using exact supporting line text. Funnel-match the URL:
- "Book a Call" → https://www.codiste.com/book-a-call
- "Contact Us" → https://www.codiste.com/contact

If source uses a custom button label (e.g. "Book a Technical Assessment", "Schedule a Demo"), preserve the label as-is in the cta_button slice. Flag in output as a violation. Do NOT rewrite to whitelist label. This skill flags, never fixes.

### FAQ → faqs slice with 5+5 structure
- Source has exactly 5 FAQ pairs: all 5 visible. No schema-only section needed.
- Source has 6 to 10 FAQ pairs: first 5 visible (indices 0 to 4), remaining schema-only (indices 5 to 9).
- Source has more than 10: take first 10, flag excess in output.

Each FAQ item:
```json
{
  "question": "<exact question, ends with ?>",
  "answer": "<exact answer, starts with complete subject-verb sentence>"
}
```

Field names always "question" and "answer." This is the live Supabase schema.

For inline source format (bold question + regular answer in single paragraph), split at the first question mark per the detection rule above.

FAQ separation check: verify each answer starts with a full subject-verb sentence (not "It's when..." but "[Subject] is..."). If source violates this, flag in output, do NOT rewrite.

---

## Root JSON fields

| Field | Source |
|---|---|
| uid | H1 title slugified, stop words stripped, hyphens, under 50 chars |
| type | always "blog" |
| status | always "draft" |
| title | exact H1 text |
| group | today's date YYYY-MM-DD |
| category | infer from content: AI/ML/Agents → "Artificial Intelligence"; Blockchain/Web3 → "Blockchain"; everything else → "Product Engineering" |
| category_list | same value as category, in array |
| description | if not in source, generate ≤155 char meta description from H1 plus first paragraph. Primary keyword front-loaded. |
| meta_title | exact H1 plus " \| Blog" |
| readtime | word count divided by 200, rounded, "X mins" |
| date | today ISO 8601 |
| last_modified | today ISO 8601 with ms |
| seo.title | same as meta_title |
| seo.description | same as description |

No img field. No seo.image. status always "draft." group is YYYY-MM-DD only.

---

## Slice IDs

Format: `slice_type$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx`. Third segment always starts with 4. Every ID unique.

---

## Output format

Single valid JSON code block. No commentary inside. Label above the block: JSON: [EXACT H1 TITLE]

After the JSON block, output:

```
Conversion confirmed
Sections mapped: [list every H2 found in source]
Paragraphs: [total count]
Slices: [total count]
Visible FAQ: [count of 5] + Schema-only FAQ: [count of 0 to 5]
FAQ source format: [inline / block]
Tables: [count], [each: "H3 title + intro OK" or "MISSING H3 title" or "MISSING intro sentence"]
Pull-out callouts: [count]
Key Numbers block: [present / not present / H3 present but table missing (FLAG)]
Anchor IDs generated: [count, all headings]
Zero content alterations, source text preserved verbatim.

FLAGS (only if issues found):
- Missing table titles: [list]
- Missing table intro sentences: [list]
- FAQ answers violating subject-verb opening rule: [list]
- Custom button label preserved (whitelist violation): [label, blog name]
- Content above 10 FAQ cap: [count dropped]
- Key Numbers H3 without table: [yes/no]
```

---

## Verification step (run internally before outputting JSON)

Before writing a single slice, read the entire source and list internally:
1. Every H2 heading (exact text).
2. Every H3 heading (exact text), including "Key Numbers" if present.
3. Total paragraph count.
4. TLDR line count.
5. FAQ pair count and source format (inline / block).
6. Table count plus whether each has an H3 title and intro sentence above it.
7. Pull-out callout count.
8. Key Numbers block presence.
9. CTA type (Book a Call / Contact Us / custom).

Then map each item to its slice. Only then write JSON. This prevents dropped sections.

---

## Hard rules (zero exceptions)

1. Not one word of source text changes.
2. Not one comma, apostrophe, or punctuation mark changes.
3. Not one section drops.
4. Not one paragraph merges or splits.
5. Not one heading rewrites.
6. Voice Locks DO NOT run on text-to-JSON conversion.
7. Blog-creator SEO rules DO NOT apply. Text is already final.
8. If a section exists in source, it exists in JSON. Always.
9. The only creative decisions: inferring category if not obvious, generating meta description if missing, generating anchor_ids on headings (structural, not content).
10. status always "draft."
11. group field YYYY-MM-DD only. No time component.
12. No img field. No seo.image. No image slices. Ever.
13. JSON only inside code block. No commentary inside.
14. content slice items always [{}].
15. cta_button slice items always [].
16. table slice items always [].
17. heading2 always in its own content slice. Never shared with paragraphs.
18. heading3 may share a slice with following paragraphs.
19. faqs slice field names: "question" and "answer" only.
20. Every slice ID unique. UUID4 format.
21. TLDR always H2 plus list-items across two slices. Source formatting does not override.
22. FAQ structure: 5 visible plus up to 5 schema-only equals max 10 items. First 5 visible.
23. Every heading2 and heading3 gets anchor_id (slugified heading text).
24. Missing table titles or intro sentences are FLAGGED, not fixed. This skill never adds content.
25. Custom button labels are PRESERVED and FLAGGED. Never rewritten to whitelist labels.
26. Inline FAQ source format splits at first question mark for question/answer fields.
27. Pull-out callouts preserved as paragraph blocks with full strong span. Never altered.
28. Key Numbers H3 plus table mapped to content slice plus table slice. Missing table flagged.
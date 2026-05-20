# SKILL: codiste-text-to-json-v5
# Replaces v4 in full.
# Handles finalized blog text → Supabase-ready JSON conversion ONLY.
# Zero content alteration. Zero rewriting. Zero editorial judgment.
# v5 fixes: correct slice envelope (variation + version), correct table cell schema,
#           hyperlink span on closing CTA, Key Numbers table as data-only (no header row).

---

## Trigger

Paste a finished blog draft with the keyword "convert," "convert this to JSON," "turn this into JSON," or "text to JSON."

This skill fires only when the source is FINISHED text. It does not fire for batch feeder rows.

---

## The One Absolute Rule

Every word, comma, punctuation mark, heading, paragraph, and sentence from the source text appears in the JSON exactly as written. No exceptions. No editorial passes. No rewriting. No dropping sections. No merging or splitting paragraphs. No adding content.

The source text is FINAL. This skill is a formatting tool only.

---

## What This Skill Does

Takes finalized plain text or .docx blog. Maps every section to the slice schema. Outputs a single valid JSON code block ready for Supabase import.

Adds three technical fields automatically without altering visible content:
1. `anchor_id` on every `heading2` and `heading3` block (slugified from heading text).
2. Splits FAQ into 5 visible + up to 5 schema-only if source has more than 5 pairs.
3. Validates that every standard table has a preceding H3 title + intro sentence (flags if missing, never adds).

Recognises structural elements:
- Pull-out callouts: bold standalone paragraphs in body, 12–20 words.
- Key Numbers block: H3 "Key Numbers" + 2-column data-only table (no header row).
- Inline FAQ: bold question + regular answer in a single paragraph.

---

## What This Skill Never Does

- Rewrites any heading, even to fix punctuation.
- Drops any section, even if it seems redundant.
- Merges or splits paragraphs. Source paragraph count equals JSON paragraph block count.
- Adds content. No extra intro sentences, no transition sentences.
- Applies Voice Locks, SEO rules, or CTA rules. The text is final. Those ran upstream.
- Paraphrases. Never. Under any circumstance.

---

## How to Read the Source

### Identify sections in this order:
1. Title (first line or H1).
2. TLDR block (lines after "TL;DR" or "TLDR," before the first paragraph).
3. Hook (paragraphs before the first H2).
4. Direct-answer summary box (bolded 40–60 word paragraph after hook, before first H2).
5. H2 sections.
6. H3 subsections (including table titles and "Key Numbers").
7. Pull-out callouts (fully bolded standalone paragraphs of 12–20 words between body sections).
8. Key Numbers block (H3 "Key Numbers" followed by a 2-column table).
9. CTA (H3 + supporting line + button).
10. FAQ.
11. Closing statement (final paragraph, no heading, contains hyperlinked CTA).

### Paragraph boundaries
One blank line in source = paragraph break = separate paragraph block in JSON.
No blank line = same paragraph = same block. Never merge. Never split.

### TLDR
Always maps to TWO slices:
- Slice 1: `heading2` block, text exactly `"TL;DR"`, anchor_id `"tldr"`, in its own content slice.
- Slice 2: One `list-item` block per bullet line in a separate content slice.

### FAQ format detection
**Inline format**: paragraph starts with bold text ending in `?` followed by non-bold text.
Split at the first `?`: everything up to and including `?` = `question`; everything after (strip leading whitespace) = `answer`.

**Block format**: question on its own line/paragraph, answer in the next paragraph.

JSON output is identical for both formats. Fields are always `"question"` and `"answer"`.

### Pull-out callout detection
Fully bolded paragraph, 12–20 words, single sentence, sitting between body sections (not inside a list, not inside a table). Maps as a `paragraph` block with full strong span.

### Key Numbers block
H3 with text `"Key Numbers"` followed by a 2-column table with no header row.
Maps to: content slice (heading3 block) + table slice (data rows only, all `tableCell` type).
No intro sentence required between the H3 and table.

### Closing statement CTA link
The closing statement typically ends with a hyperlinked CTA phrase (e.g. "Book a call").
Map as a `paragraph` block with a `hyperlink` span on the linked text:
```json
{
  "start": <char index where linked text starts>,
  "end": <char index where linked text ends>,
  "type": "hyperlink",
  "data": {
    "link_type": "Web",
    "url": "https://www.codiste.com/book-a-call",
    "target": "_blank"
  }
}
```

---

## Slice Envelope

**Every slice, regardless of type, must carry these two fields:**
```json
"variation": "default",
"version": "initial"
```

Missing these fields causes the CMS import to fail.

---

## Slice Mapping

### content slice

Blocks go in `primary.content`. `items` is always `[{}]`.

```json
{
  "variation": "default",
  "version": "initial",
  "items": [{}],
  "primary": {
    "content": [ <block>, <block>, ... ]
  },
  "id": "content$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
  "slice_type": "content",
  "slice_label": null
}
```

**Block types inside `primary.content`:**

`heading2` — always in its own content slice, never shared with paragraphs:
```json
{
  "type": "heading2",
  "text": "<exact heading text>",
  "spans": [{"start": 0, "end": <text.length>, "type": "strong"}],
  "direction": "ltr",
  "anchor_id": "<slugified heading text>"
}
```

`heading3` — may share a content slice with following paragraph blocks:
```json
{
  "type": "heading3",
  "text": "<exact heading text>",
  "spans": [{"start": 0, "end": <text.length>, "type": "strong"}],
  "direction": "ltr",
  "anchor_id": "<slugified heading text>"
}
```

`paragraph`:
```json
{
  "type": "paragraph",
  "text": "<exact text>",
  "spans": [],
  "direction": "ltr"
}
```
Full strong span for direct-answer box and pull-out callout paragraphs:
`"spans": [{"start": 0, "end": <text.length>, "type": "strong"}]`

`list-item` and `o-list-item`:
```json
{
  "type": "list-item",
  "text": "<exact bullet text>",
  "spans": [],
  "direction": "ltr"
}
```

---

### table slice

`items` is always `[]`.

Rows go in `primary.blog_table.content` as an array of `tableRow` objects.

**Standard table (has a header row):**
```json
{
  "variation": "default",
  "version": "initial",
  "items": [],
  "primary": {
    "blog_table": {
      "content": [
        {
          "key": "row-header",
          "type": "tableRow",
          "content": [
            {"key": "h1", "type": "tableHeader", "content": [{"type": "paragraph", "text": "<col 1 header>", "spans": []}]},
            {"key": "h2", "type": "tableHeader", "content": [{"type": "paragraph", "text": "<col 2 header>", "spans": []}]},
            {"key": "h3", "type": "tableHeader", "content": [{"type": "paragraph", "text": "<col 3 header>", "spans": []}]}
          ]
        },
        {
          "key": "row-<slugified first cell text>",
          "type": "tableRow",
          "content": [
            {"key": "c1-1", "type": "tableCell", "content": [{"type": "paragraph", "text": "<cell text>", "spans": []}]},
            {"key": "c1-2", "type": "tableCell", "content": [{"type": "paragraph", "text": "<cell text>", "spans": []}]},
            {"key": "c1-3", "type": "tableCell", "content": [{"type": "paragraph", "text": "<cell text>", "spans": []}]}
          ]
        }
      ]
    }
  },
  "id": "table$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
  "slice_type": "table",
  "slice_label": null
}
```

**Key Numbers table (no header row — data rows only):**
```json
{
  "variation": "default",
  "version": "initial",
  "items": [],
  "primary": {
    "blog_table": {
      "content": [
        {
          "key": "row-<slugified stat value>",
          "type": "tableRow",
          "content": [
            {"key": "c1-1", "type": "tableCell", "content": [{"type": "paragraph", "text": "<stat>", "spans": []}]},
            {"key": "c1-2", "type": "tableCell", "content": [{"type": "paragraph", "text": "<context>", "spans": []}]}
          ]
        }
      ]
    }
  },
  "id": "table$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
  "slice_type": "table",
  "slice_label": null
}
```

**Table key naming:**
- Header row key: always `"row-header"`
- Data row key: `"row-"` + slugified first cell text (lowercase, hyphens, max 40 chars)
- Header cell keys: `"h1"`, `"h2"`, `"h3"`, `"h4"` ...
- Data cell keys: `"c{row_index}-{col_index}"` (1-based, e.g. `"c1-1"`, `"c1-2"`, `"c2-1"`)

---

### cta_button slice

`items` is always `[]`. Link includes `"target": "_blank"`.

```json
{
  "variation": "default",
  "version": "initial",
  "items": [],
  "primary": {
    "title": [
      {"type": "paragraph", "text": "<supporting line — exact text>", "spans": [], "direction": "ltr"}
    ],
    "name": "Book a Call",
    "link": {
      "link_type": "Web",
      "url": "https://www.codiste.com/book-a-call",
      "target": "_blank"
    }
  },
  "id": "cta_button$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
  "slice_type": "cta_button",
  "slice_label": null
}
```

Button name values: `"Book a Call"` → URL `/book-a-call`. `"Contact Us"` → URL `/contact`.
If source uses a custom button label, preserve it and FLAG. Never rewrite to whitelist label.

---

### faqs slice

FAQ items go directly in `items`. `primary` is always `{}`.

```json
{
  "variation": "default",
  "version": "initial",
  "items": [
    {"question": "<exact question ending with ?>", "answer": "<exact answer starting subject-verb>"},
    ...
  ],
  "primary": {},
  "id": "faqs$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
  "slice_type": "faqs",
  "slice_label": null
}
```

- Source has exactly 5 FAQ pairs → all 5 go in `items` (visible). No schema-only needed.
- Source has 6–10 FAQ pairs → indices 0–4 visible, indices 5–9 schema-only.
- Source has more than 10 → take first 10, flag excess.
- Field names: `"question"` and `"answer"` only. No other keys.

---

## Root JSON Fields

| Field | Value |
|---|---|
| `uid` | H1 slugified, stop words stripped, hyphens, under 50 chars |
| `type` | always `"blog"` |
| `status` | always `"draft"` |
| `title` | exact H1 text |
| `group` | `YYYY-MM-DD` only — no time component |
| `category` | AI/ML/Agents → `"Artificial Intelligence"` · Blockchain/Web3 → `"Blockchain"` · everything else → `"Product Engineering"` |
| `category_list` | `["<same as category>"]` |
| `description` | if not in source, generate ≤155 chars; primary keyword in first 60 chars |
| `meta_title` | `<H1> \| Blog` — always ends with ` \| Blog` |
| `readtime` | word count ÷ 200, rounded, `"X mins"` |
| `date` | today ISO 8601 |
| `last_modified` | today ISO 8601 with milliseconds |
| `seo.title` | same as `meta_title` |
| `seo.description` | same as `description` |

No `img` field. No `seo.image`. No image slices. Ever.

---

## Slice ID Format

`slice_type$xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx`

- Third UUID segment always starts with `4` (UUID v4 spec).
- Every slice ID unique across the document.

---

## Slice Order (Cluster)

```
content: TLDR H2 (own slice)
content: TLDR bullets
content: hook paragraphs
content: direct-answer box (full bold span)
content: H2 problem (own slice)
content: problem body paragraphs
content: H2 solution (own slice)
content: solution body + list-items
content: H2 proof (own slice)
content: proof body + list-items
content: H3 table title + intro paragraph
table: comparison table
content: pull-out callout (full bold span)
content: H3 Key Numbers (alone)
table: Key Numbers (data rows only)
content: Codiste paragraph
content: H3 CTA heading + supporting paragraph
cta_button: primary CTA
content: H2 FAQ (own slice)
faqs: 5 visible + 5 schema-only
content: closing statement (with hyperlink span)
```

TLDR slices are absent for BoFU blogs. Mid-post `cta_button` is present for MoFU only (after proof section).

---

## Output Format

Single valid JSON code block. No commentary inside the block.

Label above the block:
```
JSON: [EXACT H1 TITLE]
```

After the JSON block:
```
Conversion confirmed
Sections mapped: [list every H2 in source]
Paragraphs: [total paragraph block count]
Slices: [total slice count]
Visible FAQ: [count] + Schema-only FAQ: [count]
FAQ source format: [inline / block]
Tables: [count] — [each: "H3 title + intro OK" or "MISSING H3 title" or "MISSING intro sentence"]
Pull-out callouts: [count]
Key Numbers block: [present / not present / H3 present but table missing (FLAG)]
Anchor IDs generated: [count]
Zero content alterations, source text preserved verbatim.

FLAGS (only if issues found):
- Missing table H3 titles: [list]
- Missing table intro sentences: [list]
- FAQ answers not starting subject-verb: [list]
- Custom button label preserved (not on whitelist): [label]
- FAQ pairs above 10 cap: [count dropped]
- Key Numbers H3 without table: [yes/no]
```

---

## Internal Verification (run before writing any JSON)

Before writing the first slice, list internally:

1. Every H2 heading — exact text.
2. Every H3 heading — exact text.
3. Total paragraph count.
4. TLDR line count (0 if absent).
5. FAQ pair count and format (inline / block).
6. Table count — does each have an H3 title and intro sentence immediately above?
7. Pull-out callout count.
8. Key Numbers block: present or absent.
9. CTA type: `"Book a Call"` / `"Contact Us"` / custom.

Map each item to its slice. Only then write JSON.

---

## Hard Rules (zero exceptions)

1. Not one word of source text changes.
2. Not one comma, apostrophe, or punctuation mark changes.
3. Not one section drops. If it exists in source, it exists in JSON.
4. Not one paragraph merges or splits.
5. Not one heading rewrites.
6. `variation: "default"` and `version: "initial"` on every slice. Missing either field breaks CMS import.
7. `heading2` always in its own content slice. Never shared with paragraphs.
8. `heading3` may share a content slice with following paragraphs.
9. Content slices: blocks in `primary.content`. `items` always `[{}]`.
10. Table slices: rows in `primary.blog_table.content` as `tableRow` objects containing `tableHeader` or `tableCell` objects — never flat arrays. `items` always `[]`.
11. Standard tables: first row uses `tableHeader` cells with key `"row-header"`. Data rows use `tableCell` cells with key `"row-<slug>"`.
12. Key Numbers table: data rows only, all `tableCell` type, no `tableHeader` row.
13. CTA button slices: `items` always `[]`. Link includes `"target": "_blank"`.
14. CTA button `name`: `"Book a Call"` or `"Contact Us"` only. Custom labels preserved and flagged.
15. FAQs slice: items are the FAQ objects directly. `primary` always `{}`. Field names `"question"` and `"answer"` only.
16. FAQ structure: 5 visible (indices 0–4) + up to 5 schema-only (indices 5–9). Max 10.
17. First visible FAQ answer must contain the Primary Keyword. Flag if it does not — never rewrite.
18. Every `heading2` and `heading3` block carries `anchor_id` (slugified heading text).
19. Closing statement CTA: hyperlink span on the linked text, with `link_type`, `url`, `target: "_blank"`.
20. Slice IDs: `slice_type$uuid4`. Third UUID segment starts with `4`. Every ID unique.
21. `status` always `"draft"`.
22. `group` field: `YYYY-MM-DD` only. No time component.
23. No `img` field. No `seo.image`. No image slices. Ever.
24. `meta_title` always ends with ` | Blog`.
25. `description` ≤155 chars. Primary keyword in first 60 chars.
26. `uid` under 50 chars.
27. JSON only inside code block. No commentary inside the block.
28. TLDR: absent for BoFU. Present for MoFU/ToFU — always two slices (H2 own slice + list-items slice).
29. Standard table must be preceded by a content slice containing an H3 title + intro paragraph. Exception: Key Numbers table is preceded by its H3 heading alone (no intro sentence required).
30. Missing table H3 titles or intro sentences are FLAGGED, never added. This skill never invents content.

# SKILL: codiste-supabase-push-v2.md
# ─────────────────────────────────────────────────────────────────────────────
# Replaces v1 in full. Trimmed to focused operational doc.
# Pushes generated blog JSON to Supabase as draft records.
# Triggered by "push to supabase" / "ship to supabase" in Anurag's batch message.
# ─────────────────────────────────────────────────────────────────────────────

## Trigger

Fires only when Anurag's message contains one of:
- "push to supabase"
- "ship to supabase"
- "send to supabase"
- "supabase push"

When triggered, blog-creator-v7 generates JSON internally (same as JSON Mode) and hands off each blog's JSON to this skill. This skill pushes each record to the Codiste Supabase blog table as a draft.

## What this skill does

1. Receives finalized JSON from blog-creator-v7.
2. Shows Anurag a one-line summary per blog with a single confirmation prompt at the end of the batch.
3. On "yes" confirmation: pushes each record to Supabase via MCP.
4. On "no," "wait," or anything else: stops, keeps the JSON available, does not push.

Per-batch confirmation, never automatic. A human glance between generation and production is the last line of defense.

## What this skill never does

- Push without explicit "yes" confirmation in the chat.
- Push records with status other than "draft."
- Overwrite existing records with the same uid (raises an error instead).
- Use Supabase to fetch or modify published content. Draft insert only.
- Log API keys or credentials to the chat.

## Prerequisites

This skill needs Supabase MCP connected. If it's not, output:
"Supabase MCP is not connected. Enable it in Settings → Connectors, then rerun. JSON preserved for manual import."

First run only: Claude calls `list_projects` and `list_tables` via the Supabase MCP to identify the blog project and table, then caches the column mapping. Subsequent runs use the cached mapping.

Schema mapping (cached after first push):
| JSON root field | Supabase column |
|---|---|
| uid | uid (unique constraint, reject on duplicate) |
| type | type (always "blog") |
| status | status (always "draft") |
| title | title |
| group | group_date |
| category | category |
| category_list | category_list (JSONB) |
| description | description |
| meta_title | meta_title |
| readtime | readtime |
| date | date (ISO 8601) |
| last_modified | last_modified (ISO 8601 with ms) |
| seo | seo (JSONB) |
| slices | slices (JSONB) |

## Batch flow

1. blog-creator-v7 produces JSON for each blog in the batch (internal, Anurag does not see the JSON).
2. This skill receives all JSON records.
3. Output to Anurag:

```
Ready to push [N] blogs to Supabase:
- Blog 1: "[H1 title]" | uid: [slug] | funnel: [stage]
- Blog 2: "[H1 title]" | uid: [slug] | funnel: [stage]
- Blog 3: "[H1 title]" | uid: [slug] | funnel: [stage]

Confirm push? Reply "yes" to ship all [N] as drafts.
```

4. Wait for Anurag's reply.

5. On "yes": execute pushes sequentially via Supabase MCP `execute_sql`. Insert each record with status="draft." Capture the returned record ID. On uid collision: stop the batch, report the collision, ask whether to skip, update, or cancel.

6. After all pushes complete:

```
Pushed to Supabase:
✓ Blog 1: "[title]" / record id [xxx]
✓ Blog 2: "[title]" / record id [xxx]
✓ Blog 3: "[title]" / record id [xxx]

Review each in the CMS, add cover image, assign author, publish when ready.
```

7. On any push failure: report which blog failed and the error. Do NOT roll back successful pushes. Anurag decides whether to retry or fix manually.

## Duplicate uid handling

uid is the unique identifier. If a uid already exists in Supabase:

1. Stop the push for that blog.
2. Report: "uid `[slug]` already exists in Supabase. Probably a re-run of a previous batch. Options: (a) skip this blog, (b) update the existing record, (c) cancel the whole batch."
3. Wait for reply. Do not guess.

Updating an existing draft is allowed when Anurag says so. Never update a published record from this skill. Publishing is always a CMS-side action.

## Error handling

- Supabase MCP not connected: clear message, skill exits, JSON preserved.
- Table name not found: list available tables, ask Anurag to confirm.
- Column mismatch (JSON field has no matching column): report the missing field, ask whether to skip the field or abort.
- Rate limit or timeout: retry once, then report.
- JSON validation error: report which blog, which slice, what's malformed.

All errors keep Anurag in control. No silent drops. No silent retries beyond the single built-in retry.

## Output format

Before push: list of blogs with title, uid, funnel, plus confirmation prompt.

After "yes" (success): per-blog confirmation line with record ID, then session-close line.

After "yes" (partial success): per-blog status (✓ or ✗ with error), clear next action.

After "no": "Push cancelled. JSON preserved in chat context for this session. Re-run with 'push to supabase' when ready."

## Session close line

"Batch complete. [N] blogs pushed to Supabase as drafts. IDs listed above. Funnel gaps flagged. Review in the CMS and add cover images before publishing."

## Hard rules (zero exceptions)

1. Never push without "yes" confirmation.
2. Never push anything that isn't status="draft".
3. Never overwrite existing records without explicit "yes, update uid [slug]."
4. Always surface errors. Never silently drop or silently retry beyond the single built-in retry.
5. Never log API keys, tokens, or credentials.
6. Never push from JSON Anurag has not seen the summary of.
7. If MCP is disconnected or credentials invalid: exit cleanly, never attempt workarounds.
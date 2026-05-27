# DELIVERY PIPELINE
# Blog Automation — Complete Working Reference
# Last validated: 2026-05-27

---

## ⚠️ Network Constraints (Remote Execution Environment)

These hosts are **BLOCKED** by the CCR network policy (direct HTTP fails with `Host not in allowlist`):
- `codisteteam.app.n8n.cloud` → cannot call n8n webhooks or REST API directly via curl/Python
- `www.codiste.com` → cannot POST to CMS API directly via curl/Python

These are **ACCESSIBLE**:
- `chat.googleapis.com` → Google Chat notifications ✅
- Google Drive via MCP tools (`mcp__Google-Drive__*`) ✅
- n8n via MCP tools (`mcp__n8n__*`) ✅ — MCP protocol bypasses HTTP allowlist

**Rule of thumb:** Use MCP tools for n8n and Drive. Use curl only for Google Chat.

---

## Key IDs & Config

### Google Drive Folders
| Folder | ID |
|---|---|
| **JsonFiles** (JSON delivery destination) | `11qhEj83s2KFxIDgcoKJnyUx9BjEEbEj9` |
| **CMS Search Root** (CMS workflow scans here) | `1fqabVUpMkdiISazaKitXlrzF1rcoIDFB` |

### n8n Workflows
| Workflow | ID | Trigger |
|---|---|---|
| Get Blog From Drive | `jQfJBSXe75Vl5Jnx` | Manual |
| Upload Blog JSON to Codiste CMS | `pY5Trd7FpzhKcD9p` | Webhook `{ fileName }` |
| ~~Converted Json Blog to Drive and Draft~~ | `3QWsnlNkgDE4CupS` | ❌ Webhook blocked — not usable |
    
### Google Chat Webhook
```
https://chat.googleapis.com/v1/spaces/AAQAT72CHuU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Qe1ssjpk7FXlZhov6PI89T3akTY-Brg3dDBQgX8_7J8
```

### Codiste CMS API (only reachable via n8n workflow — not directly)
- Endpoint: `https://www.codiste.com/api/admin/upload-blog`
- Auth: `Bearer 6fac3e65a528a8ffcd237651ed514d773266882a124d0564326aeb951afd0e75`
- Method: POST multipart/form-data, field name: `files`

---

## File Naming Convention
```
<slugified-topic-name>.json
Example: development-for-fintech-trading-desks.json
```
**Only the converted JSON file is uploaded to Drive and CMS. Never the source .docx.**

---

## Complete Step-by-Step Pipeline

---

### STEP 1 — Get Blog Content from Google Drive

**Primary:** Execute the n8n workflow (manual mode):
```
mcp__n8n__execute_workflow
  workflowId: jQfJBSXe75Vl5Jnx
  executionMode: manual
```
Then poll: `mcp__n8n__get_execution` (workflowId: `jQfJBSXe75Vl5Jnx`, executionId, includeData: true)

⚠️ **Known issue:** The "Download file" node in this workflow will likely fail with HTTP 403
(`Export only supports Docs Editors files`) because it tries to download the **folder**
`Blog_To_JsonFiles` instead of a file inside it.

**Fallback (use this when workflow fails):**
Find the `.docx` file, then read it:
```
mcp__Google-Drive__read_file_content
  fileId: <id of the .docx file>
```
This returns the full blog text. Use it for conversion.

**If multiple topics exist, process only the first one (lowest row / oldest created date).**

---

### STEP 2 — Fetch Reference Files from GitHub

```bash
curl -sL https://raw.githubusercontent.com/guaravcodiste/blog_automate_skills/main/codiste_text_to_json_v5.md
curl -sL https://raw.githubusercontent.com/guaravcodiste/blog_automate_skills/main/enterprise_ai_agent_deployment_blog.json
```

- Read `codiste_text_to_json_v5.md` **fully** — it is the conversion skill
- Use `enterprise_ai_agent_deployment_blog.json` for **structure reference only** — never copy its content

---

### STEP 3 — Convert Blog to JSON

Follow `codiste_text_to_json_v5.md` exactly. Run the internal verification checklist before writing JSON:
1. List every H2 and H3 — exact text
2. Count total paragraphs
3. Detect TLDR bullets, FAQ format (inline/block), table count, Key Numbers block
4. Map all CTAs

Save output to: `/tmp/<topic-name>.json`

Validate before proceeding:
- All slices have `"variation": "default"` and `"version": "initial"`
- `heading2` blocks are always in their own content slice
- `items: [{}]` on content slices, `items: []` on table and cta_button slices
- FAQ slice: `primary: {}`, 5 visible + up to 5 schema-only
- `uid` under 50 chars, `status: "draft"`, no `img` field

---

### STEP 4 — Upload JSON to Google Drive

⚠️ **Upload JSON only. Never upload the source .docx.**

#### 4a. Upload to JsonFiles delivery folder
```
mcp__Google-Drive__create_file
  title: <topic-name>.json
  parentId: 11qhEj83s2KFxIDgcoKJnyUx9BjEEbEj9
  contentMimeType: application/json
  disableConversionToGoogleType: true
  textContent: <full JSON string — pass directly, no base64 needed>
```
Save the returned `id` as `<json_drive_id>`.

#### 4b. Copy JSON to CMS Search Root (required for CMS workflow to find the file)
```
mcp__Google-Drive__copy_file
  fileId: <json_drive_id>
  parentId: 1fqabVUpMkdiISazaKitXlrzF1rcoIDFB
  title: <topic-name>.json
```

---

### STEP 5 — Upload to Codiste CMS via n8n

The CMS API at `www.codiste.com` is not directly reachable. The n8n workflow `pY5Trd7FpzhKcD9p`
runs on n8n's servers which ARE allowlisted for `www.codiste.com`. Route through it.

The workflow payload is just a filename — tiny, safe to pass via MCP tool call directly.

#### 5a. Publish the CMS workflow
```
mcp__n8n__publish_workflow
  workflowId: pY5Trd7FpzhKcD9p
```

#### 5b. Execute via MCP tool (NOT via Python or curl — webhook URL is blocked)
```
mcp__n8n__execute_workflow
  workflowId: pY5Trd7FpzhKcD9p
  executionMode: production
  inputs:
    type: webhook
    webhookData:
      method: POST
      body:
        fileName: <topic-name>.json
```
Save the returned `executionId`.

#### 5c. Poll until complete
```
mcp__n8n__get_execution
  workflowId: pY5Trd7FpzhKcD9p
  executionId: <from 5b>
  includeData: true
  nodeNames: ["POST to Codiste API"]
```
Poll every 5–10 seconds until `status = "success"`.

Expected CMS response in `POST to Codiste API` node output:
```json
{"success": true, "created": 1, "failed": 0, "results": [{"slug": "...", "status": "draft", "success": true}]}
```

#### 5d. Unpublish the CMS workflow
```
mcp__n8n__unpublish_workflow
  workflowId: pY5Trd7FpzhKcD9p
```

---

### STEP 6 — Send Google Chat Notification

`chat.googleapis.com` is accessible via direct curl. Send after both Drive upload and CMS upload succeed.

```bash
curl -s -X POST \
  "https://chat.googleapis.com/v1/spaces/AAQAT72CHuU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Qe1ssjpk7FXlZhov6PI89T3akTY-Brg3dDBQgX8_7J8" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"✅ Blog processed & uploaded:\n- Drive (JsonFiles): <json-filename>\n- Codiste CMS: draft created\nTopic: <topic-name>\nSlug: <slug>\nFunnel: <funnel> | Vertical: <vertical>\"}"
```

---

## Summary Checklist

```
[ ] Blog .docx fetched from Google Drive (via MCP or workflow fallback)
[ ] codiste_text_to_json_v5.md and reference JSON fetched from GitHub
[ ] Blog converted to JSON, validated
[ ] /tmp/<topic-name>.json saved
[ ] JSON uploaded to Drive: JsonFiles folder (11qhEj83s2KFxIDgcoKJnyUx9BjEEbEj9)
[ ] JSON copied to Drive: CMS Search Root (1fqabVUpMkdiISazaKitXlrzF1rcoIDFB)
[ ] CMS workflow published (pY5Trd7FpzhKcD9p)
[ ] CMS workflow executed — status: success
[ ] Blog created in Codiste CMS as draft — slug confirmed
[ ] CMS workflow unpublished (pY5Trd7FpzhKcD9p)
[ ] Google Chat notification sent
```

---

## Why the Original Step 3 (Python + Session Token MCP) No Longer Works

The original pipeline routed the large base64 payload through the Anthropic CCR session MCP endpoint
(`https://api.anthropic.com/v2/ccr-sessions/.../mcp`). This approach fails in practice because:

1. The payload (~108 KB combined docx + JSON base64) exceeds safe inline tool call limits
2. The `/mcp` endpoint URL requires a dynamically resolved MCP config file path that may not exist
3. The Drive upload workflow (`3QWsnlNkgDE4CupS`) expects **both** docx and JSON — but we only upload JSON now

**Replacement approach (this pipeline):**
- Use `mcp__Google-Drive__create_file` with `textContent` — no base64, no size issue
- Use `mcp__n8n__execute_workflow` with just `{fileName}` — the n8n workflow fetches the file itself
- Send Google Chat directly via curl (chat.googleapis.com is in the allowlist)

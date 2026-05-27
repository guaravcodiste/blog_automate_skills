# DELIVERY PIPELINE

File Naming
<slugified-topic>.json

Step 1 — Encode files to base64
import base64, json
payload = {
  'jsonBase64': base64.b64encode(open('<file>.json','rb').read()).decode(),
  'jsonName': '<file>.json'
}
json.dump(payload, open('/tmp/webhook_payload.json','w'))
Step 2 — Publish the upload workflow
mcp__n8n__publish_workflow   workflowId: 3QWsnlNkgDE4CupS
Step 3 — Execute via Python (NOT via model tool call)
Files are ~100KB base64 combined — too large to pass inline through a model tool call. Use the session token to call the MCP endpoint directly from Python:

import json, requests

TOKEN = open('/home/claude/.claude/remote/.session_ingress_token').read().strip()

# Get SESSION_ID from the MCP config file at runtime
import glob
cfg = json.load(open(glob.glob('/tmp/mcp-config-cse_*.json')[0]))
n8n_url = cfg['mcpServers']['n8n']['url']
SESSION_ID = n8n_url.split('ccr-sessions/')[1].split('/mcp')[0]
MCP_SERVER_ID = cfg['mcpServers']['n8n']['headers']['X-MCP-Server-ID']

MCP_URL = (
  f"https://api.anthropic.com/v2/ccr-sessions/{SESSION_ID}/mcp"
  "?mcp_url=https%3A%2F%2Fcodisteteam.app.n8n.cloud%2Fmcp-server%2Fhttp"
  f"&mcp_server_id=bbd7687a-b399-575e-ac8f-20f542790161"
  f"&toolbox_mcp_server_id={MCP_SERVER_ID}"
)

HEADERS = {
  "Authorization": f"Bearer {TOKEN}",
  "X-Session-UUID": SESSION_ID,
  "X-MCP-Server-ID": MCP_SERVER_ID,
  "Content-Type": "application/json"
}

payload = json.load(open('/tmp/webhook_payload.json'))
body = {
  "jsonrpc": "2.0", "id": 2, "method": "tools/call",
  "params": {
    "name": "execute_workflow",
    "arguments": {
      "workflowId": "3QWsnlNkgDE4CupS",
      "executionMode": "production",
      "inputs": {
        "type": "webhook",
        "webhookData": {
          "method": "POST",
          "body": payload
        }
      }
    }
  }
}
r = requests.post(MCP_URL, headers=HEADERS, json=body, timeout=60)
# Parse SSE response
for line in r.text.split('\n'):
    if line.startswith('data:'):
        data = json.loads(line[5:].strip())
        if 'result' in data:
            print(data['result'])
Step 4 — Poll until done
mcp__n8n__get_execution   workflowId: 3QWsnlNkgDE4CupS
                          executionId: <from step 3>
                          includeData: false
Poll every 5 seconds until status = "success".

Step 5 — Unpublish after upload
mcp__n8n__unpublish_workflow   workflowId: 3QWsnlNkgDE4CupS
step 6: Upload JSON to Codiste CMS via n8n
The remote container is NOT allowlisted for direct curl to www.codiste.com. Instead, route the API call through the n8n workflow (n8n servers ARE allowlisted).

Auth fix: Use Authorization: Bearer <key> header — NOT x-api-key.

n8n Workflow to use: pY5Trd7FpzhKcD9p ("Upload Blog JSON to Codiste API")

How it works:

The JSON file must already be uploaded to Google Drive folder 1Zu4tQpWIDsJBjC4YVHtnkzdeLeWp6M5Z (done in Step 3–5)
Publish the workflow, execute it via Python using the same session token pattern as Step 3: body = {"fileName": "your-blog-filename.json"} Use workflowId: pY5Trd7FpzhKcD9p, executionMode: production, type: webhook
Poll mcp__n8n__get_execution (workflowId: pY5Trd7FpzhKcD9p) until status = "success"
Confirm "success": true in the POST to Codiste API node output
Unpublish the workflow after use
No Google Chat notification is sent by this workflow. The chat message is sent only by the Drive upload workflow (Step 3–5).

API Key (Authorization: Bearer):

Google Chat Webhook
Sent automatically by the upload workflow's final node. No separate call needed. Space: spaces/AAQAT72CHuU URL: https://chat.googleapis.com/v1/spaces/AAQAT72CHuU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Qe1ssjpk7FXlZhov6PI89T3akTY-Brg3dDBQgX8_7J8

Google Drive Folder
Upload destination folder ID: 1Zu4tQpWIDsJBjC4YVHtnkzdeLeWp6M5Z Credential to use: Google Drive Gaurav (ID: P1LgLB809wHimpia)
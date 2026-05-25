import os, base64, urllib.request, json, sys

# We'll read base64 data URLs via Supabase REST API using SUPABASE creds in env,
# but since we don't have a key here, this script is invoked with the data
# passed as stdin JSON: [{name, data_url}].
data = json.load(sys.stdin)
out_dir = "/home/user/blog_automate_skills/assets"
os.makedirs(out_dir, exist_ok=True)
for item in data:
    name = item["name"]
    url = item["data_url"]
    # data URL format: data:<mime>;base64,<payload>
    payload = url.split(",", 1)[1]
    raw = base64.b64decode(payload)
    path = os.path.join(out_dir, name)
    with open(path, "wb") as f:
        f.write(raw)
    print(f"wrote {path} ({len(raw)} bytes)")

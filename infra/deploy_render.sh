#!/usr/bin/env bash
set -euo pipefail

# This script triggers deployments on Render.com for only the apps that changed.
# Required secrets: RENDER_API_KEY, RENDER_SERVICES_JSON
# Inputs:
#   1) ENVIRONMENT  -> staging | production
#   2) CHANGED_APPS -> space-separated list like: "homecouver startbaz"
#
# Notes:
# - Put your app folders under apps/<app-name>/
# - Map each app-name to a Render service_id for each environment via RENDER_SERVICES_JSON (a GitHub Repository Secret).

ENVIRONMENT="${1:-staging}"
CHANGED_APPS="${2:-}"

if [[ -z "${RENDER_API_KEY:-}" ]]; then
  echo "[ERROR] Missing RENDER_API_KEY"; exit 1
fi
if [[ -z "${RENDER_SERVICES_JSON:-}" ]]; then
  echo "[ERROR] Missing RENDER_SERVICES_JSON (JSON map of env->app->service_id)"; exit 1
fi

# jq-lite using python (since runners always have python3)
python3 - << 'PY'
import os, json, sys
services = os.environ.get("RENDER_SERVICES_JSON","")
env = os.environ.get("ENVIRONMENT","staging")
apps_in = os.environ.get("CHANGED_APPS","").split()
try:
    data = json.loads(services)
except Exception as e:
    print("[ERROR] RENDER_SERVICES_JSON is not valid JSON:", e)
    sys.exit(2)

selected = []
for app in apps_in:
    try:
        sid = data[env][app]
        selected.append((app, sid))
    except KeyError:
        print(f"[WARN] No service_id mapping for app='{app}' in env='{env}'. Skipping.")

if not selected:
    print("[INFO] No services to deploy (empty selection).")
else:
    for app, sid in selected:
        print(f"{app}:{sid}")
PY

DEPLOY_LIST=$(python3 - << 'PY'
import os, json
services = os.environ.get("RENDER_SERVICES_JSON","")
env = os.environ.get("ENVIRONMENT","staging")
apps_in = os.environ.get("CHANGED_APPS","").split()
data = json.loads(services)
out = []
for app in apps_in:
    sid = data.get(env, {}).get(app)
    if sid: out.append(f"{app}:{sid}")
print(" ".join(out))
PY
)

if [[ -z "${DEPLOY_LIST}" ]]; then
  echo "[INFO] Nothing to deploy."
  exit 0
fi

echo "[INFO] Deploy targets: ${DEPLOY_LIST}"

for pair in ${DEPLOY_LIST}; do
  app="${pair%%:*}"
  sid="${pair##*:}"
  echo "[INFO] Triggering Render deploy for ${app} (service_id=${sid}) on env=${ENVIRONMENT}..."
  curl -sS -X POST "https://api.render.com/v1/services/${sid}/deploys"     -H "Authorization: Bearer ${RENDER_API_KEY}"     -H "Content-Type: application/json"     -d '{"clearCache":false}' > /tmp/render_${sid}.json
  echo "[INFO] Response saved to /tmp/render_${sid}.json"
done

echo "[SUCCESS] Deploy requests sent to Render."

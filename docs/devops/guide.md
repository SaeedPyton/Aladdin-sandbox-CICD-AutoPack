# Aladdin-sandbox CI/CD AutoPack — Render.com Edition

This pack installs a production-grade CI/CD for a monorepo.

## Structure
- `.github/workflows/`
  - `Build (Monorepo)` — build all apps
  - `Test (Monorepo)` — test all apps
  - `Deploy (Render)` — deploy only changed apps to Render staging/production
  - `Release (GitHub)` — create a release when pushing `v*` tags
- `infra/deploy_render.sh` — triggers Render deploys via API
- `infra/render.services.json` — example mapping of app->service_id
- `env.example` — required secrets

## Prerequisites
- Each app resides in `apps/<app-name>/` and has its own `package.json`.
- You already created services on Render.com for each app (staging & production).

## GitHub Setup (one-time)
1. Go to **Settings → Environments** and create two environments:
   - `staging` (no approval)
   - `production` (enable required reviewers for safety)
2. Go to **Settings → Secrets and variables → Actions** and add these **Repository Secrets**:
   - `RENDER_API_KEY` — from your Render account (Dashboard → Account Settings → API Keys).
   - `RENDER_SERVICES_JSON` — paste JSON mapping like:
     ```json
     {
       "staging":   { "homecouver": "srv-xxxxxxxx", "startbaz": "srv-yyyyyyyy" },
       "production":{ "homecouver": "srv-aaaaaaaa", "startbaz": "srv-bbbbbbbb" }
     }
     ```
3. (Optional) For releases on tags, nothing else is required.

## How Deploy Works
- On push to `develop` → environment = `staging`
- On push to `main` → environment = `production` (will respect environment approvals)
- The workflow calculates **which apps changed** using `git diff` and only deploys those.
- If only shared files changed (e.g., infra/packages), it triggers a root deploy (you can map "root" in secrets if needed).

## Local Tips
- Keep shared libraries under `packages/` and apps under `apps/`.
- If you add a new app, add its Render service IDs to the `RENDER_SERVICES_JSON` secret.

## Troubleshooting
- **No services to deploy**: Ensure your changes touched `apps/<app>/...` or map `root` in the secret if you want global redeploys.
- **403/401 from Render**: Check `RENDER_API_KEY` and service permissions.
- **Unknown app name**: Make sure the app key exists in the JSON mapping.

Enjoy a fully automated pipeline with minimal maintenance.

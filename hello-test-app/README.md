# Hello Test App for Render CI/CD

This is a simple static site used to test automatic deployment with Render and GitHub Actions.

## Folder
- `apps/hello-test/` → contains a minimal static web app
- `render.yaml` → defines how Render should deploy this app

## Deployment
When you push changes to `develop` branch, the Render staging environment will auto-deploy.

When you merge or push to `main`, production deployment will trigger.

# Render FastAPI Test

Minimal FastAPI service for Render.

## Files
- `main.py` — FastAPI app with healthcheck and sample routes.
- `requirements.txt` — Python deps.
- `render.yaml` — Render blueprint config.

## Deploy on Render
1. Push these files to a new GitHub repo (root level).
2. In Render, **New > Blueprint** and select your repo.
3. Confirm the plan and deploy.

### Verify
- `/` — HTML landing page
- `/healthz` — returns `ok` (good for health checks)
- `/version` — app name & version
- `/time` — current UTC time
- `/echo` — POST JSON to echo back
- `/env` — shows a few environment vars (safe)

# Charity's Measure — FastAPI on Render

This repo serves the provided working HTML version of Charity's Measure through a FastAPI app, deployable to Render.

## Structure
- `main.py` — FastAPI app
- `templates/charitys_measure.html` — your supplied HTML (unaltered logic)
- `assets/Charity_Sheets.xlsx` — supplied spreadsheet (downloadable at `/download/xlsx`)
- `requirements.txt` — dependencies
- `render.yaml` — Render blueprint (free plan)

## Local run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 then click **Open the App**.

## Deploy to Render
1. Push these files to a **new GitHub repo** (root level).
2. In Render: **New → Blueprint** → select your repo → Deploy.
3. After build completes, open the service URL and visit `/healthz` (should return `ok`), then `/app`.

## Notes
- The app keeps your original HTML/JS intact, so behavior matches your working static version.
- `/docs` exposes FastAPI docs (not required by the UI but helpful during dev).

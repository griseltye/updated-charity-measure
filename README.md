# Charity's Measure — FastAPI (no templating)

This version serves your HTML as a raw file (**no Jinja**), preventing any {{ }} collisions that can break the page.

Routes:
- `/` — landing page
- `/app` — serves `templates/charitys_measure.html` via FileResponse
- `/download/xlsx` — downloads the spreadsheet
- `/healthz` — ok
- `/docs` — Swagger

Deploy on Render with `render.yaml`.

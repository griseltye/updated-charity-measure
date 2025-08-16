from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Charity's Measure", version="1.0.0")

# Templates/static
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
if (BASE_DIR / "static").exists():
    app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return HTMLResponse("""
    <!doctype html>
    <html>
      <head>
        <meta charset='utf-8' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <title>Charity's Measure</title>
        <style>
          body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; padding: 1.5rem; line-height:1.5; }
          a { color: #2563eb; text-decoration: none; }
          .card { max-width: 780px; border:1px solid #e5e7eb; border-radius: 12px; padding: 20px; }
          .btn { display:inline-block; padding:10px 14px; border:1px solid #e5e7eb; border-radius:10px; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>✅ Charity's Measure</h1>
          <p>This is the FastAPI version serving your working HTML app.</p>
          <p><a class="btn" href="/app">Open the App</a></p>
          <p><a class="btn" href="/download/xlsx">Download Spreadsheet</a></p>
          <p>Health: <a href="/healthz">/healthz</a> • Docs: <a href="/docs">/docs</a></p>
        </div>
      </body>
    </html>
    """)

@app.get("/app", response_class=HTMLResponse)
def app_view(request: Request):
    return templates.TemplateResponse("charitys_measure.html", {"request": request})

@app.get("/download/xlsx")
def download_xlsx():
    xlsx = BASE_DIR / "assets" / "Charity_Sheets.xlsx"
    return FileResponse(str(xlsx), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="Charity_Sheets.xlsx")

@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "ok"

@app.get("/env")
def env():
    return {
        "port": os.getenv("PORT"),
        "render_service": os.getenv("RENDER_SERVICE_NAME"),
        "render_region": os.getenv("RENDER_REGION"),
    }

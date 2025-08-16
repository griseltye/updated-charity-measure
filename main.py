from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

app = FastAPI(title="Render FastAPI Test", version="0.1.0")

# CORS (helpful for quick frontend tests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Render FastAPI Test</title>
        <style>
          body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; padding: 2rem; line-height: 1.5; }
          code { background: #f4f4f4; padding: 0.2rem 0.4rem; border-radius: 4px; }
          .card { max-width: 680px; border: 1px solid #eaeaea; border-radius: 10px; padding: 1rem 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
          h1 { margin-top: 0; }
          a { color: #2563eb; text-decoration: none; }
          a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>✅ Render FastAPI Test</h1>
          <p>Your service is up. Try a few endpoints:</p>
          <ul>
            <li><a href="/healthz"><code>GET /healthz</code></a></li>
            <li><a href="/version"><code>GET /version</code></a></li>
            <li><a href="/time"><code>GET /time</code></a></li>
          </ul>
          <p>Send a POST to <code>/echo</code> with JSON, e.g.:</p>
          <pre>curl -s -X POST "$HOST/echo" -H "Content-Type: application/json" -d '{"message":"hello"}'</pre>
        </div>
      </body>
    </html>
    """

@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "ok"

@app.get("/version")
def version():
    return {"app": app.title, "version": app.version}

@app.get("/time")
def time():
    return {"utc": datetime.utcnow().isoformat() + "Z"}

@app.post("/echo")
async def echo(req: Request):
    payload = await req.json()
    return JSONResponse({"received": payload})

@app.get("/env")
def env():
    # Helpful debugging info when running on Render
    return {
        "port": os.getenv("PORT"),
        "render_service": os.getenv("RENDER_SERVICE_NAME"),
        "render_region": os.getenv("RENDER_REGION"),
    }

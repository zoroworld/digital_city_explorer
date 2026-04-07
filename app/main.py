from fastapi import FastAPI
from .routers import poi

app = FastAPI(title="Digital City Explorer API")

# Mount router with versioning
app.include_router(poi.router, prefix="/api/v1")
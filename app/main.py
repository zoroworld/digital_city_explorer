from fastapi import FastAPI
from .routers import poi
from .database import Base, engine
from . import models


# Create all tables
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Digital City Explorer API")

# Mount router with versioning
app.include_router(poi.router, prefix="/api/v1")


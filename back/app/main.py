from fastapi import FastAPI

from .config.database_connect import db
from .router.routers import router as api_router

app = FastAPI()

app.include_router(api_router)

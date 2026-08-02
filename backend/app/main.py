from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.api.routes.health import router as health_router
from app.api.routes.root import router as root_router

app = FastAPI(
    title="Virexa API",
    version="0.1.0",
    description="AI-Powered Content Intelligence Platform",
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(auth_router)
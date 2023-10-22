from fastapi import APIRouter
from app.api.endpoints import hello

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello")
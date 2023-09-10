from fastapi import APIRouter

from core.api.v1 import v1_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(v1_router)

from fastapi import APIRouter

from core.api.v1.generatives import generatives_router
from core.api.v1.items import items_router
from core.api.v1.pictures import pictures_router
from core.api.v1.posts import posts_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(items_router)
v1_router.include_router(pictures_router)
v1_router.include_router(generatives_router)
v1_router.include_router(posts_router)

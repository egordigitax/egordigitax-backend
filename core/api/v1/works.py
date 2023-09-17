from fastapi import APIRouter

from core.api.v1.enums import works

works_router = APIRouter(prefix="/works")


@works_router.get("/all")
def get_all_works():
    return works
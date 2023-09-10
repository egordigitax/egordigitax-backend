from fastapi import APIRouter

from core.api.v1.enums import all_pictures

pictures_router = APIRouter(prefix="/pictures")


@pictures_router.get("/all")
def get_all_pictures():
    return all_pictures

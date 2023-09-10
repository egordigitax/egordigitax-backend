from fastapi import APIRouter

from core.api.v1.enums import all_items

items_router = APIRouter(prefix="/items")


@items_router.get("/all")
def get_all_items():
    return all_items

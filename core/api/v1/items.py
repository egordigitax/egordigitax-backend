from fastapi import APIRouter

from core.api.v1.enums import all_items

items_router = APIRouter(prefix="/items")


@items_router.get("/all")
def get_all_items():
    return all_items


@items_router.get("/{id}")
def get_item(id: str):
    for item in all_items['items']:
        if item['id'] == id:
            return item
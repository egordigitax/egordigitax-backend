from fastapi import APIRouter

from core.api.v1.enums import all_generatives

generatives_router = APIRouter(prefix="/generatives")


@generatives_router.get("/all")
def get_all_pictures():
    return all_generatives


@generatives_router.get("/{id}")
def get_post(id: str):
    for item in all_generatives['items']:
        if item['id'] == id:
            return item
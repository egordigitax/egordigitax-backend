from fastapi import APIRouter

from core.api.v1.enums import all_generatives

generatives_router = APIRouter(prefix="/generatives")


@generatives_router.get("/all")
def get_all_pictures():
    return all_generatives

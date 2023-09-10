from fastapi import APIRouter

from core.api.v1.enums import all_posts

posts_router = APIRouter(prefix="/posts")


@posts_router.get("/all")
def get_all_pictures():
    return all_posts

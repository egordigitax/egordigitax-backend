from fastapi import APIRouter
from fastapi.responses import FileResponse


from core.api.v1.enums import all_posts
from core.services.generator import generate_square

punch_router = APIRouter(prefix="/punch")

bearer = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYXJsb3diZWF0cyIsImF1dGhvcml0aWVzIjpbIjM0NTE2NTE2Nzk5NjMwMjUiLCJtYXJsb3diZWF0cyIsIjQ0Y2MyNzUwLWE0MzYtNDU1OS1hOGJlLTljZWE5ZmU4MGUzNyIsIlJPTEVfVVNFUiIsImZhbHNlIiwiMjAyMy0xMS0wOFQxODozMjoxNFoiXSwiaWF0IjoxNjk5MzgxOTM0LCJleHAiOjE2OTk0NjgzMzR9.-HpbGKgnbLweyQA2lbnt_nNSTQ869qx896C2zoJEcHk"

@punch_router.get("/{char_id}")
def generate_char(char_id: int):
    return FileResponse(generate_square(char_id, bearer))

@punch_router.get("/update_bearer/{bearer_token}")
def generate_char(bearer_token: str):
    global bearer
    bearer = bearer_token
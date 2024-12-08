from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", include_in_schema=False, response_class=HTMLResponse)
def read_root(request: Request) -> str:
    return f"Welcome to the AI/ML FastAPI Starter Template! <a href='{request.url}docs'>Go to the docs</a>"


@router.get("/ping")
def app_ping() -> bool:
    return True

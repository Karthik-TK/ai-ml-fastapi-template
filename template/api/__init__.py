from fastapi import APIRouter

from template.api import ping

api_router = APIRouter()

api_router.include_router(ping.router)

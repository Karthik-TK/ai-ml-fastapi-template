import json
import logging
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.api import api_router as enigma_api_router
from app.config import settings

TEMPLATE_TITLE = "AI/ML FastAPI Starter Template"

TEMPLATE_DESCRIPTION = "AI/ML FastAPI Starter Template is a template for building AI/ML APIs using FastAPI. It includes a basic structure for building APIs, logging, error handling, and more."

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title=TEMPLATE_TITLE,
    description=TEMPLATE_DESCRIPTION,
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.DOMAIN_WHITELISTED,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

refresh_openapi_docs = True

app.include_router(enigma_api_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=TEMPLATE_TITLE,
        version="0.1.0",
        description=TEMPLATE_DESCRIPTION,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.middleware("http")
async def log_request_stats(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print(start_time, request)
    return response


def app_startup():
    logger.info("Starting the AI/ML Playground!")
    if refresh_openapi_docs:
        app.openapi = custom_openapi
        # Export OpenAPI schema to JSON file
        with open("./api_docs/openapi.json", "w+") as f:
            json.dump(app.openapi(), f)

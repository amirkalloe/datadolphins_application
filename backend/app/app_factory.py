import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import secure

logger = logging.getLogger(__name__)
API_DESCRIPTION = "Met deze API is het mogelijk om volledig geautomatiseerd gebruikers toe te voegen, verwijderen en aan te passen. "


def create_app():

    secure_headers = secure.Secure()

    logger.info("Creating app.")
    app = FastAPI(
        title="Datadolphins Applicatie",
        description=API_DESCRIPTION,
        docs_url="/docs",
        redoc_url=None,
    )

    logger.info("Adding middlewares.")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logger.info("Adding API router.")
    from app.api.api import router as api_router

    app.include_router(api_router, prefix="/api")

    @app.middleware("http")
    async def set_secure_headers(request, call_next):
        """
        Middleware that adds security headers to each request.
        """
        response = await call_next(request)
        secure_headers.framework.fastapi(response)
        return response

    return app

import logging
from os import path
from starlette.responses import PlainTextResponse
from fastapi import Request

from fastapi.exceptions import RequestValidationError
import logging.config

from app.app_factory import create_app

# Setup logging and initialize logger for main
log_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.conf")
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = create_app()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: Exception):
    """
    Exception handler that handles requests that fail to validate before entering our
    code (e.g. Pydantic ValidationError).

    Returns: Plaintext response containing a brief description of the validation error with 422 status code.
    """
    logger.warning(
        f"Received a request with invalid body. \n Endpoint: {request.url}. \n Error: {str(exception)}"
    )
    return PlainTextResponse(
        "Failed to validate request. Request contains invalid data.",
        status_code=422,
    )

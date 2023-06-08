from typing import Generator
from app.database.database import SessionLocal
import logging


logger = logging.getLogger(__name__)


def get_db() -> Generator:
    """
    Generator function to be used via dependency injection in the endpoints.
    Creates a db connection to postgres and closes when the method call is
    terminated.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

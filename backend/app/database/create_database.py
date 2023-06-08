import logging
from sqlalchemy.sql import text

from app.database.database import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    try:
        db = SessionLocal()

        # Try to create session to check if DB is awake
        db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing database")
    init()
    logger.info("Database finished initializing")


if __name__ == "__main__":
    main()

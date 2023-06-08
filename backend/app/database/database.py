from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

import os

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "postgres")
server = os.getenv("POSTGRES_SERVER", "localhost")
port = os.getenv("POSTGRES_PORT", "5434")
db = os.getenv("POSTGRES_DB", "datadolphins_applicatie")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{user}:{password}@{server}:{port}/{db}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, poolclass=NullPool
)

# Check whether or not the database exists yet, if not, create it.
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

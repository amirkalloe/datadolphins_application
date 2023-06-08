import logging
from typing import List, Literal
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import exc

import app.schemas as schemas
import app.models as models
from app.api import exceptions


# Setup logger
logger = logging.getLogger(__name__)


def get_all(db: Session, skip: int = 0, limit: int = 1000) -> List:
    """
    Gets all gebruikers.
    Returns: List of gebruikers object
    """
    return db.query(models.gebruiker.Gebruiker).offset(skip).limit(limit).all()


def update_one(
    db: Session,
    achternaam: str,
    body: schemas.gebruiker.GebruikerIn,
) -> schemas.gebruiker.Gebruiker:
    model = models.gebruiker.Gebruiker
    payload = {
        **body.dict(exclude_unset=True),
        "ts_create": datetime.now(),
    }
    db.query(model).filter(model.achternaam == achternaam).update(
        payload, synchronize_session="fetch"
    )
    db.commit()

    return db.query(model).filter(model.achternaam == achternaam).first()


def create_one(
    db: Session,
    body: schemas.gebruiker.GebruikerIn,
) -> schemas.gebruiker.Gebruiker:
    model = models.gebruiker.Gebruiker
    payload = {
        **body.dict(exclude_unset=True),
        "ts_create": datetime.now(),
    }
    gebruiker = model(**payload)
    db.add(gebruiker)
    db.commit()
    return gebruiker


def delete_one(db: Session, achternaam: str) -> Literal[True]:
    model = models.gebruiker.Gebruiker
    query = db.query(model).filter(model.achternaam == achternaam).first()
    try:
        db.delete(query)
        db.commit()
        return True
    except exc.IntegrityError as e:
        logging.info(e)
        raise exceptions.ForeignKeyError()

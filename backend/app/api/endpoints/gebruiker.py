import logging
from typing import List, Literal
from fastapi import Depends, APIRouter, Query
from sqlalchemy.orm import Session

from app.api import dependencies
import app.schemas as schemas
import app.crud as crud

# Setup logger
logger = logging.getLogger(__name__)

# Create router for login functionalities
router = APIRouter()


@router.get("/all", response_model=List[schemas.gebruiker.Gebruiker])
async def get_all(
    db: Session = Depends(dependencies.get_db),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=1000, ge=1),
) -> List[schemas.gebruiker.Gebruiker]:
    """
    Met deze endpoint kunt u alle **gebruikers** ophalen
    """
    return crud.gebruiker.get_all(db=db, skip=skip, limit=limit)


@router.post("/new", response_model=schemas.gebruiker.Gebruiker)
async def create_one(
    body: schemas.gebruiker.GebruikerIn,
    db: Session = Depends(dependencies.get_db),
) -> schemas.gebruiker.Gebruiker:
    """
    Met deze endpoint kunt u een **gebruiker** toevoegen
    """
    return crud.gebruiker.create_one(db=db, body=body)


@router.delete("/{achternaam}")
async def delete_one(
    achternaam: str,
    db: Session = Depends(dependencies.get_db),
) -> Literal[True]:
    """
    Met deze endpoint kunt u een **gebruiker** toevoegen
    """
    return crud.gebruiker.delete_one(db=db, achternaam=achternaam)


@router.put("/{achternaam}", response_model=schemas.gebruiker.Gebruiker)
async def update_one(
    body: schemas.gebruiker.GebruikerIn,
    achternaam: str,
    db: Session = Depends(dependencies.get_db),
) -> schemas.gebruiker.Gebruiker:
    """
    Met deze endpoint kunt u een **gebruiker** bewerken
    """
    return crud.gebruiker.update_one(db=db, achternaam=achternaam, body=body)


@router.get(
    "/relations", response_model=List[schemas.gebruiker.GebruikerRelations]
)
async def get_relations(
    db: Session = Depends(dependencies.get_db),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=1000, ge=1),
) -> List[schemas.gebruiker.GebruikerRelations]:
    """
    Met deze endpoint kunt u alle **gebruikers** inclusief **functie**
    en **bedrijf** ophalen
    """
    return crud.gebruiker.get_all(db=db, skip=skip, limit=limit)

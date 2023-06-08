from pydantic import BaseModel
from datetime import datetime

from app.schemas.functie import Functie
from app.schemas.bedrijf import Bedrijf


class Gebruiker(BaseModel):
    id_gebruiker: int
    achternaam: str
    voornaam: str
    id_functie: int
    id_bedrijf: int
    ts_create: datetime

    class Config:
        orm_mode = True


class GebruikerRelations(Gebruiker):
    functie: Functie
    bedrijf: Bedrijf


class GebruikerIn(BaseModel):
    achternaam: str
    voornaam: str
    id_functie: int
    id_bedrijf: int

    class Config:
        orm_mode = True

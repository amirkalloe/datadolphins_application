from pydantic import BaseModel


class Functie(BaseModel):
    id_functie: int
    functie: str

    class Config:
        orm_mode = True

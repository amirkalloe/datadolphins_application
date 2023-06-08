from pydantic import BaseModel


class Bedrijf(BaseModel):
    id_bedrijf: int
    bedrijfs_naam: str

    class Config:
        orm_mode = True

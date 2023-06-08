from app.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Gebruiker(Base):
    """
    Alle gebruikers in het systeem
    """

    __tablename__ = "gebruiker"

    id_gebruiker = Column(Integer, primary_key=True, index=True)
    achternaam = Column(String)
    voornaam = Column(String)
    id_functie = Column(String, ForeignKey("functie.id_functie"))
    id_bedrijf = Column(String, ForeignKey("bedrijf.id_bedrijf"))
    ts_create = Column(DateTime(timezone=False))

    functie = relationship("Functie", foreign_keys=[id_functie])
    bedrijf = relationship("Bedrijf", foreign_keys=[id_bedrijf])

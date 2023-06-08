from app.database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Functie(Base):
    """
    Alle gebruikers in het systeem
    """

    __tablename__ = "functie"

    id_functie = Column(Integer, primary_key=True, index=True)
    functie = Column(String)
from app.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Bedrijf(Base):
    """
    Alle gebruikers in het systeem
    """

    __tablename__ = "bedrijf"

    id_bedrijf = Column(Integer, primary_key=True, index=True)
    bedrijfs_naam = Column(String)

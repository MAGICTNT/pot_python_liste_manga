from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database_definitions import Base

class Attribut(Base):
    __tablename__ = 'attribut'
    id = Column(Integer, primary_key=True)
    nom = Column(String(255))
    type = Column(String(50))
    valeurs = relationship('Valeur')

    def __repr__(self):
        return f"<Attribut(id={self.id}, nom='{self.nom}', type='{self.type}')>"

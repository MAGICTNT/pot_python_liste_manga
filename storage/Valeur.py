from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database_definitions import Base
from .Attribut import Attribut
class Valeur(Base):
    __tablename__ = 'valeur'
    collection_id = Column(Integer, ForeignKey('collection.id'), primary_key=True)
    attribut_id = Column(Integer, ForeignKey('attribut.id'), primary_key=True)
    valeur = Column(String(255))
    collection = relationship('Collection', back_populates='valeurs')
    attribut = relationship('Attribut', back_populates='valeurs')

    def __repr__(self):
        return f"<Valeur(collection_id={self.collection_id}, attribut_id={self.attribut_id}, valeur='{self.valeur}')>"

# Importation différée pour éviter une circularité
from . import Collection
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from .database_definitions import Base, utilisateur_collection

from .Valeur import Valeur  # Importation déplacée ici pour résoudre la circularité

class Collection(Base):
    __tablename__ = 'collection'
    from .Valeur import Valeur
    id = Column(Integer, Sequence('collection_id_seq'), primary_key=True)
    nom = Column(String(255))
    utilisateurs = relationship('Utilisateur', secondary=utilisateur_collection, back_populates='collections')

    valeurs = relationship('Valeur', back_populates='collection')
    
    def __init__(self,id,nom):
        self.id = id
        self.nom = nom

    def __repr__(self):
        return f"<Collection(id={self.id}, nom='{self.nom}')>"

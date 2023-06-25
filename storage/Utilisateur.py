from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database_definitions import Base, utilisateur_collection
from .Role import Role

class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id = Column(Integer, primary_key=True)
    pseudo = Column(String(255), nullable=False)
    age = Column(Integer)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role', back_populates='utilisateurs')
    collections = relationship('Collection', secondary=utilisateur_collection, back_populates='utilisateurs')

    def __repr__(self):
        return f"<Utilisateur(id={self.id}, pseudo='{self.pseudo}', age={self.age})>"


from.Collection import Collection
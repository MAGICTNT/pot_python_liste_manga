from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database_definitions import Base

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    label = Column(String(255))
    utilisateurs = relationship('Utilisateur', back_populates='role')

    def __repr__(self):
        return f"<Role(id={self.id}, label='{self.label}')>"

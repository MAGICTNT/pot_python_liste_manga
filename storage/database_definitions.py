from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

# Création de l'engine SQLAlchemy
engine = create_engine('sqlite:///database.db')

# Création de la base de classe SQLAlchemy
Base = declarative_base()

# Définition de la table de liaison utilisateur_collection
utilisateur_collection = Table('utilisateur_collection', Base.metadata,
                               Column('utilisateur_id', Integer, ForeignKey('utilisateur.id')),
                               Column('collection_id', Integer, ForeignKey('collection.id'))
)
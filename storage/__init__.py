from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL, Engine
from config import MY_CONFIG

base = declarative_base()

# Création de l'objet Engine SQLAlchemy
db_uri = f"{MY_CONFIG.get('bdd_conect').get('driver')}://{MY_CONFIG.get('bdd_conect').get('user')}:{MY_CONFIG.get('bdd_conect').get('password')}@{MY_CONFIG.get('bdd_conect').get('host')}:{MY_CONFIG.get('bdd_conect').get('port')}/{MY_CONFIG.get('bdd_conect').get('database')}"
engine = create_engine(db_uri)

# Création de la session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
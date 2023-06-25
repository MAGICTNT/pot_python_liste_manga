from storage import Session
from storage.Collection import Collection


def collections() -> str:
    with Session() as session:
        collections = session.query(Collection).order_by(Collection.id).all()
        list_collection = 'Voici la liste des collection trouver:\n'
        for collection in collections:
            list_collection += f'id: {collection.id}   nom: {collection.nom}\n'
        return list_collection
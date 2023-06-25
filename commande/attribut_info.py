from storage import Session
from storage.Attribut import Attribut


def attributs():
    with Session() as session:
        all_attribut = session.query(Attribut).all()
        message = 'voici la liste des attribut:\n'
        for attribut in all_attribut:
            message += f'id: {attribut.id}   nom:{attribut.nom} type: {attribut.type} \n'
        return message
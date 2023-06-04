import csv


def lecteur(path_fichier):
    lignes = []
    with open(path_fichier, newline='') as fichier:
        # on crée un objet reader
        lecture = csv.reader(fichier, delimiter=',')

        # on transforme l'itérateur en liste:
        lignes = list(lecture)

    return lignes


def ecriture_new_livre(path_fichier, livres, new_libre):
    with open(path_fichier, 'w', newline='') as csvfile:
        fieldnames = ['nom', 'volume', 'format']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        for livre in livres:
            writer.writerow({'nom': livre.get_nom(), 'volume': livre.get_volume(), 'format': livre.get_style()})

        writer.writerow({'nom': new_libre.get_nom(), 'volume': new_libre.get_volume(), 'format': new_libre.get_style()})

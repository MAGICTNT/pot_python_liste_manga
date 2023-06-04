from storage.Livre import Livre
from storage.Style import Style


def ajout_style(liste_label):

    boucle = 0
    liste = []

    for label in liste_label:
        style = Style()
        style.set_label(label)
        style.set_code(boucle)
        liste.append(style)

    return liste


def ajout_livre(liste_livre):

    liste = []

    for ligne in liste_livre:
        livre = Livre()
        livre.set_nom(ligne[0])
        livre.set_volume(ligne[1])
        livre.set_style(ligne[2])
        liste.append(livre)

    return liste

from storage.Livre import Livre
from storage.Style import Style


def ajout_style(liste_label):

    boucle = 0
    liste = []
    i = 0
    for label in liste_label:
        style = Style()
        style.set_id(i)
        style.set_label(label)
        style.set_code(boucle)
        liste.append(style)
        i += 1
    return liste


def ajout_livre(liste_livre):

    liste = []
    i = 0
    for ligne in liste_livre:
        livre = Livre()
        livre.set_id(i)
        livre.set_nom(ligne[0])
        livre.set_volume(ligne[1])
        livre.set_style(ligne[2])
        liste.append(livre)
        i += 1
    return liste

import numpy as np
import affichage_graphique


def sinus(xmin, xmax, nom_fichier, p=0.1):
    """
    Permet de remplir un fichier dont le nom est passé en paramètre avec les valeurs de x, et la distance entre
    (x,sin(x)) et (0,0).
    :param xmin: valeur minimum de x
    :param xmax: valeur maximum de x
    :param nom_fichier: nom du fichier dans lequelle nous allons stocker les valeurs
    """
    with open(nom_fichier, "w") as file:
        while xmin <= xmax+p:
            distance = np.sqrt(xmin**2 + np.sin(xmin)**2)
            file.write(f"{xmin};{distance}\n")
            xmin += p


def afficher(nom_fichier, elt_sep=";", title="Affichage de y par x", titre_x="Valeur de x", titre_y="Valeur de y"):
    valeur_x = []
    valeur_y = []
    with open(nom_fichier) as file:
        for ligne in file:
            line = ligne.split(elt_sep)
            valeur_x.append(float(line[0]))
            valeur_y.append(float(line[1].strip()))

    affichage_graphique.affiche_courbe(valeur_x, valeur_y, title, titre_x, titre_y)


if __name__ == "__main__":
    sinus(-5, 5, "sinus.txt")
    afficher("sinus.txt")
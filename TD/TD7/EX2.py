import csv
import panda as pd
import affichage_graphique


def ex2():
    liste_annee = []
    liste_co2 = []
    try:
        with open("co2-annmean-mlo.csv") as file:
            myreader = csv.reader(file)
            next(myreader)
            for ligne in myreader:
                date = ligne[0].split("-")
                liste_annee.append(int(date[0]))
                liste_co2.append(float(ligne[1]))
    except OSError as e:
        print(e)

    affichage_graphique.affiche_courbe(liste_annee, liste_co2, "Taux CO2", "Année", "CO2")


def ex2bis():
    try:
        data = pd.read_csv("co2-annmean-mlo.csv")
        years = []
        co2 = []
        years = [int(d[0:4]) for d in data['Year'].tolist()]
        c02= [float(c) for c in data["Mean"].tolist()]
        affichage_graphique.affiche_courbe(years, co2, "Taux", "Annee", "C02")
    except OSError as e:
        print(e)
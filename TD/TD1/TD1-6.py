if __name__ == "__main__":
    INF2 = {"etudiant_1": 13, "etudiant_2": 5}
    admis = {}
    non_admis = {}
    somme_admis = 0
    somme_non_admis = 0
    # On suppose que les moyennes sont inférieures ou = à 20 et supérieures ou égales à 20

    for etudiant in INF2:
        if INF2[etudiant] >= 10:
            admis[etudiant] = INF2[etudiant]
            somme_admis += INF2[etudiant]
        else:
            non_admis[etudiant] = INF2[etudiant]
            somme_non_admis += INF2[etudiant]

    moyenne_admis = somme_admis / len(admis)
    moyenne_non_admis = somme_non_admis / len(non_admis)

    print(admis)
    print(non_admis)
    print(moyenne_admis)
    print(moyenne_non_admis)



def main():
    annee = input("Saisissez une année : ")  # On attend que l'utilisateur saisisse l'année qu'il désire tester
    annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    bissextile = False  # On crée un booléen qui vaut vrai ou faux
    # selon que l'année est bissextile ou non

    if annee % 400 == 0:
        bissextile = True
    elif annee % 100 == 0:
        bissextile = False
    elif annee % 4 == 0:
        bissextile = True
    else:
        bissextile = False

    if bissextile:  # Si l'année est bissextile
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")


if __name__ == '__main__':
    main()

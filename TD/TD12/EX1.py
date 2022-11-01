import numpy as np


def matrice_aleatoire(n,m):
    """
    fonction qui prend en paramètres n et m et qui retourne une matrice aléatoire de dimension (n,m+1) avec une 
    colonne biais remplie de 1 tout à droite.
    :param n: nombre de lignes
    :param m: nombre de colonnes
    :return: une matrice aléatoire
    """
    matrice = np.random.rand(n, m)
    colonne_de_un = np.ones((n, 1))
    return_matrice = np.concatenate((matrice, colonne_de_un), axis=1)
    return return_matrice


def main():
    n = int(input('Entrez le nombre de lignes : '))
    m = int(input('Entrez le nombre de colonnes : '))
    print(matrice_aleatoire(n, m))


if __name__ == '__main__':
    main()

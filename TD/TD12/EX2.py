import numpy as np
import matplotlib.pyplot as plt


def calcul_exo2(n):
    mat_r = np.random.randn(n, n)

    plt.hist(mat_r.flatten(), bins=1000)
    plt.show()

    mat_m = mat_r @ mat_r.T
    term_1 = mat_m @ np.linalg.inv(mat_m)
    term_2 = np.linalg.inv(mat_m) @ mat_m

    mat_i = np.eye(n)

    print(term_1 == term_1)
    print(np.allclose(term_1,term_2))


def main():
    n = int(input("Entrez la taille de la matrice :"))
    calcul_exo2(n)


if __name__ == '__main__':
    main()
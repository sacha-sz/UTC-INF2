from 2-3.py import *

def affiche_test_cm(*args):
    for i in range(len(args)):
        if magique(args[i]):
            print(f'La matrice c{i} est magique, ')
            if carre_magique_normal(args[i]):
                print('et est également normalle')
            print()
        else:
            print("La matrice n'est pas magique")
        print()


if __name__ == '__main__':
    c1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    c2 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    c3 = [[30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29], [46, 6, 8, 17, 26, 35, 37],
          [5, 14, 16, 25, 34, 36, 45], [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41, 43, 3, 12],
          [22, 31, 40, 49, 2, 11, 20]]
    c4 = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]

    affiche_test_cm(c1, c2, c3, c4)

def somme_ligne(mat, i):
    somme = 0
    for j in range(len(mat)):
        somme += mat[i][j]
    return somme


def somme_colonne(mat, j):
    somme = 0
    for i in range(len(mat)):
        somme += mat[i][j]
    return somme


# def somme_diag1(mat):
#     somme = 0
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             if i == j:
#                 somme += mat[i][j]
#     return somme

def somme_diag1(mat):
    somme = 0
    for i in range(len(mat)):
        somme += mat[i][i]
    return somme


def somme_diag2(mat):
    somme = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j + i + 1 == len(mat):
                somme += mat[i][j]
    return somme


def magique(mat):
    ref = somme_ligne(mat, 0)
    for i in range(len(mat)):
        if somme_ligne(mat, i) != ref or somme_colonne(mat, i) != ref:
            return False
    if somme_diag1(mat) == somme_diag2(mat) == ref:
        return True
    return False


def carre_magique_normal(mat):
    list = []
    for i in range(1, (len(mat)**2 + 1)):
        list.append(i)
    for ligne in mat:
        for elt in ligne:
            if elt in list:
                list.remove(elt)
    if not list:
        return True
    else:
        return False


if __name__ == "__main__":
    mat = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    for elt in range(len(mat)):
        print(mat[elt])
    print(somme_diag2(mat))
    print(somme_diag1(mat))
    print(magique(mat))
    print(carre_magique_normal(mat))

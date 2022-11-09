# def somme_chiffre (nb):
#     somme = 0
#     while nb != 0:
#         somme += nb % 10
#         nb = nb // 10
#     return somme


def somme_chiffre (nb):
    somme = 0
    nb = str(nb)
    for ch in nb:
        somme += int(ch)
    return somme


def nombre_chiffre (nb):
    somme = 0
    nb = str(nb)
    for _ in nb:
        somme += 1
    return somme


def decorator(function):
    def new_function(nb):
        if nombre_chiffre(nb) % 2 ==1:
            return 0, 0
        else:
            return function(nb)
    return new_function



@decorator
def separe_nombre(nb):
    nb = str(nb)
    i = len(nb) // 2
    x1 = int(nb[:i])
    x2 = int(nb[i:])
    return x1, x2


def couicable(nb):
    g, d = separe_nombre(nb)
    if (g, d) != (0, 0):
        return somme_chiffre(g) == somme_chiffre(d)
    return False


def rec_somme_chiffre(nb):
    if nb == 0:
        return 0
    return nb % 10 + rec_somme_chiffre(nb // 10)


if __name__ == "__main__":
    nb = int(input("Entrez un nombre entier : "))
    print(somme_chiffre(nb))
    print(nombre_chiffre(nb))
    print(separe_nombre(nb))

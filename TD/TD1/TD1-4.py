if __name__ == "__main__":
    x1 = int(input("Entrez le premier entier : "))
    x2 = int(input("Entrez le second entier : "))
    div_commun = []
    for i in range(1, min(x1, x2) + 1):
        if ((x1 % i) == 0) and ((x2 % i) == 0):
            div_commun.append(i)

    print(div_commun)
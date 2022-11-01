import math


def main():
    rayon = float(input('Entrez le rayon du cercle (cm) : '))
    resultat = round(math.pi * rayon * rayon, 2)

    print("La surface du cercle est" , resultat, "cm2")


if __name__ == '__main__':
    main()

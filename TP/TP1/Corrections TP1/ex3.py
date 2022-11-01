import math


def main():
    a = int(input("saisir un nombre :"))
    f = 1
    for i in range(2, a + 1):
        f *= i
    print("le factoriel de ", a, " est ", f)


if __name__ == '__main__':
    main()

from random import randint
from collections import *


def elimination(liste_joueur):
    joueurs = deque(liste_joueur)
    while len(joueurs) > 1:
        x = randint(1, 10)
        for i in range(0, x):
            y = joueurs.popleft()
            joueurs.append(y)  # équivaut à : joueurs.rotate(-x)
        print(f"Le joueur {joueurs.popleft()} est éliminé.")
        print(list(joueurs))
    print(f"Le gagnant est : {joueurs.popleft()}")


if __name__ == "__main__":
    liste = ["Paul", "Jean", "Juan", "Pierre"]
    elimination(liste)
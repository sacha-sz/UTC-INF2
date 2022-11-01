class Sommet:
    __nbSommets = 0

    def __init__(self, identificateur):
        if identificateur.__hash__ is None:
            raise TypeError("L'identificateur n'est pas hashable.")
        else:
            self.__identificateur = identificateur
        Sommet.__nbSommets += 1

    def __str__(self):
        return f'{self.__identificateur}'

    def __del__(self):
        Sommet.__nbSommets -= 1

    def __hash__(self):
        return hash(self.__identificateur)

    def __eq__(self, other):
        return hash(self.__identificateur) == hash(other.__identificateur)

    def getId(self):
        return self.__identificateur

    def getNbSommet():
        return Sommet.__nbSommets


if __name__ == "__main__":
    n1 = Sommet("INF2")
    n2 = Sommet(26)
    n3 = Sommet("INF1")
    print(f"nb sommets={Sommet.getNbSommet()}")  # 3 sommets
    del n2  # destruction du sommet n2
    print(f"nb sommets={Sommet.getNbSommet()}")  # 2 sommets
    fini = False
    while not fini:
        name = [1,2,3]
        try:
            name = Sommet(name)
        except TypeError:
            print("Le nom du sommet n'est pas hashable")
        else:
            print("Sommmet créé")
        finally:
            print("Continuez")

        fini = input("Avez vous fini (Y/N) : ").lower()
        if fini == "y":
            fini = True
        else:
            fini = False

class Sommet:
    def __init__(self, ident):
        self.__ident = ident
        __nbSommets = self.getNbSommets()

    def __str__(self):
        return f'{self.__ident}'

    def __del__(self):
        __nbSommets = self.getNbSommets() - 1

    def getId(self):
        return self.__ident

    def setId(self, id):
        __ident = id
        __nbSommets = self.getNbSommets() + 1

    def getNbSommets(self):
        return self.__nbSommets

    def setNbSommmets(self):
        __nbSommets = 0


if __name__ == "__main__":
    n1 = Sommet("INF2")
    n2 = Sommet(26)
    n3 = Sommet("INF1")
    print(n1)
    print(n2)
    print(n3)
    # print(f"nb sommets={Sommet.getNbSommets()}")  # 3 sommets
    # del (n2)  # destruction du sommet n2
    # print(f"nb sommets={Sommet.getNbSommets()}")  # 2 sommets

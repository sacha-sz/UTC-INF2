class Graphe:
    def __init__(self, id, dico):
        self.__nom = id
        self.__succ = dico

    def getNom(self):
        return self.__nom

    def getSommets(self):
        return len(self.__succ)
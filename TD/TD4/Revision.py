class Duree:
    def __init__(self, h, m):
        __heure = h
        __minute = m

    def getHeure(self):
        return self.__heure

    def setHeure(self, h):
        if not 0 <= h <= 23:
            raise ValueError("L'heure n'est pas comprise entre 0 et 23.")
        else:
            self.__heure = h

    heure = property(getHeure, setHeure)

    # ou
    #
    # @property
    # def heure(self):
    #     return self.getHeure()
    #
    # @heure.setter
    # def heure(self, h):
    #     self.setHeure(h)


def mon_decorateur(fonction):  # nom de la fonction qui décore (paramètre : fonction à décorer)
    # on fabrique une autre fonction
    def fonction_de_coree(x):  # 1 ou + paramètre de la fonction à décorer
        print("Avant")  # élément de décoration
        y = fonction(x)
        print(y)# application de la vraie fonction
        print("Après")  # élément de décoration
        return y  # retourne le résultat de la fonction

    # fin de la décoration
    return fonction_de_coree


# def carre(x):
#     return x ** 2
#
#
# carre = mon_decorateur(carre)
#
# ou
#
@mon_decorateur
def carre(x):
    return x ** 2
#
# @mon_decorateur
# def double(x):
#     return x * 2
# class A():
#     def __init__(self, v):
#         self.__value = v
#
#     def affiche(self):
#         print(self.__value)
#
#     nom = 'classe A'
#     __nb = 0
#
#     def getNb():  # pas de self car c'est une méthode de classe
#         return  __nb
# x = A(4)
#     x.affiche()
#     # A.affiche(x) pareil qu'au dessus
#     print(A.nom)
#     print(A.getNB)


if __name__ == "__main__":
    # d = Duree(2, 6)
    # print(d)
    y = carre(4)
    print(y)
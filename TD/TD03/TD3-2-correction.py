class Horaire():
    def get_H(self):
        return self.__heure

    def set_H(self, h):
        if not isinstance(h, int):
            raise TypeError("L'heure doit être un int")
        if h < 0 or h > 23:
            raise ValueError("L'heure doit être comprise entre 0 et 23")
        self.__heure = h
    heure = property(get_H, set_H)

    def get_M(self):
        return self.__minute

    def set_M(self, m):
        if not isinstance(m, int):
            raise TypeError("Les minutes doivent être un int")
        if m < 0 or m > 59:
            raise ValueError("Les minutes doivent être comprises entre 0 et 59")
        self.__minute = m
    minute = property(get_H, set_H)

    def __init__(self, h, m):
        self.heure, self.minute = h, m

    def __str__(self):
        return f'{self.heure}h {self.minute}min'

    def __add__(self, d):
        dur = Horaire(int(d.get_H()), int(d.get_M()))
        h2 = self.__heure + dur.get_H()
        min2 = self.__minute + dur.get_M()
        if min2 > 60:
            min2 %= 60
            h2 += 1
        if h2 > 24:
            h2 %= 24
        return Horaire(h2, min2)


class Duree():
    def get_H(self):
        return self.__heure

    def set_H(self, h):
        if not isinstance(h, int):
            raise TypeError("L'heure doit être un int")
        if h < 0 or h > 23:
            raise ValueError("L'heure doit être comprise entre 0 et 23")
        self.__heure = h
    heure = property(get_H, set_H)

    def get_M(self):
        return self.__minute

    def set_M(self, m):
        if not isinstance(m, int):
            raise TypeError("Les minutes doivent être un int")
        if m < 0 or m > 59:
            raise ValueError("Les minutes doivent être comprises entre 0 et 59")
        self.__minute = m
    minute = property(get_H, set_H)

    def __init__(self, h, m):
        self.heure, self.minute = h, m

    def __str__(self):
        return f'{self.heure}h {self.minute}min'


class Vol():
    def __init__(self, id, h, d):
        self.__nom = id
        self.__depart = h
        self.__duree = d
        self.__arrivee = h + d

    def __str__(self):
        return f"Vol : {self.__nom}, départ : {self.__depart}, duree : {self.__duree}, arrivee : {self.__duree}"


if __name__ == "__main__":
    v = Vol("747", Horaire(5, 1), Duree(1, 2))
    print(v)
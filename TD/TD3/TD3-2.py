class Horaire:
    def __init__(self, hh, mn):
        self.set_heure(hh)
        self.set_min(mn)

    def __str__(self):
        return f'{self.__heure}h {self.__min}mn'

    def get_heure(self):
        return self.__heure

    def set_heure(self, hh):
        if hh > 24:
            self.__heure = hh
        else:
            raise ValueError("L'heure entrez n'est pas comprise entre 0 et 24.")

    def get_min(self):
        return self.__min

    def set_min(self, mn):
        if not 0 <= mn < 60:
            self.__min = mn
        else:
            raise ValueError("Le nombre de minutes n'est pas compris entre 0 et 59.")

    def somme(self, hh, min):
        if self.get_min() + min >= 60:
            self.set_min((self.get_min + min)//60)
            self.set_heure((self.get_min + min) % 60)
        else:
            self.set_min(self.get_min + min)
        if self.get_heure() + hh >= 24:
            self.set_heure((self.get_heure+hh)//24)

    heure = property(get_heure, set_heure)
    min = property(get_min, set_min)


class Duree:
    def __init__(self, hh, mn):
        self._heure = hh
        self._min = mn

    def __str__(self):
        return f'{self._heure}h {self._min}mn'

    def _getheure(self):
        return self._heure

    def _setheure(self, hh):
        self._heure = hh

    def _getmin(self):
        return self._min

    def _setmin(self, mn):
        self.min = mn

    heure = property(_getheure, _setheure)
    min = property(_getmin, _setmin)

class Vol:
    def __init__(self,nom, horaire_d, duree):
        self.__nom = nom
        self._horaire_d = horaire_d.Horaire
        self.__duree = duree.Duree
        self.__horaire_a = horaire_d.Horaire.somme(horaire_d, duree.Duree._getheure(), duree.Duree._getmin())

    def __str__(self):
        return f"Vol : {self.__nom}, départ : {self._horaire_d}, duree : {self.__duree}, arrivee : {self.__duree}"



if __name__ == "__main__":
    h = Horaire(12, 30)
    d = Duree(1, 30)
    v = Vol("AF 123", h, d)
    print(v)
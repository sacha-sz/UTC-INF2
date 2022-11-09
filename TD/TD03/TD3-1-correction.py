class Date:
    def __init__(self, jj, mm, yyyy):
        self.set_year = yyyy
        self.set_month = mm
        self.set_day = jj

    def __str__(self):
        return f'{self._day}/{self._month}/{self._year}'

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

    def set_day(self, jj):
        if self.get_month() in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= jj <= 31:
                self._day = jj
            else:
                raise ValueError(f"Pour le mois {self.get_month()} le jour doit être compris entre 1 et 31")
        elif self.get_month() in [4, 6, 9, 11]:
            if 1 <= jj <= 30:
                self._day = jj
            else:
                raise ValueError(f"Pour le mois {self.get_month()} le jour doit être compris entre 1 et 30")
        elif self.get_month() == 2:
            if 1 <= jj <= 28:
                self._day = jj
            else:
                raise ValueError(f"Pour le mois {self.get_month()} le jour doit être compris entre 1 et 28")

    def set_month(self, mm):
        if 1 <= mm <= 12:
            self._month = mm
        else:
            raise ValueError("Le mois doit être compris entre 1 et 12")

    def set_year(self, yyyy):
        self._year = yyyy

    def jour_du_lendemain(self):
        if self._day == 31 and self._month in [1, 3, 5, 7, 8, 10]:
            self._day = 1
            self._month += 1
        elif self._day == 30 and self._month in [4, 6, 9, 11]:
            self._day = 1
            self._month += 1
        elif self._day == 31 and self._month == 12:
            self._day = 1
            self._month += 1
            self._year += 1
        elif self._day == 28 and self._month == 2:
            self._day = 1
            self._month += 1
        else:
            self._day += 1
    jour = property(get_day, set_day)
    mois = property(get_month, set_month)
    annee = property(get_year, set_year)


if __name__ == '__main__':
    day = (int(input('Entrez un jour : ')))
    month = (int(input('Entrez un mois : ')))
    year = (int(input('Entrez une année : ')))
    d1 = Date(day, month, year)
    print(d1)
    d1.set_day(int(input('Entrez un jour : ')))
    d1.set_month(int(input('Entrez un mois : ')))
    d1.set_year(int(input('Entrez une année : ')))
    print(d1)
    print(d1.get_day())
    print(d1.get_month())
    print(d1.get_year())
    print(d1.jour)
    print(d1.mois)
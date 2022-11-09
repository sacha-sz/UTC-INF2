class Date:
    def __init__(self, jj, mm, yyyy):
        self.set_year(yyyy)
        self.set_month(mm)
        self.set_day(jj)

    def __str__(self):
        return f'{self._day} / {self._month} / {self._year}'

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
        if (self.get_day() == 31 and self.get_month() in [1, 3, 5, 7, 8, 10]) or (self._day == 30 and self._month in [4, 6, 9, 11]):
            return Date(1, self.get_month() + 1, self.get_year())
        elif self.get_day() == 31 and self.get_month() == 12:
            return Date(1, 1, self.get_year() + 1)
        elif self.get_day() == 28 and self.get_month() == 2:
            return Date(1, 3, self.get_year())
        else:
            return Date(self.get_day() + 1, self.get_month(), self.get_year())


if __name__ == '__main__':
    d1 = Date(1, 1, 2020)
    m = 1
    while d1.get_year() == 2020:
        print(d1, end=";")
        d1 = d1.jour_du_lendemain()
        if d1.get_month() != m:
            print()
            m += 1

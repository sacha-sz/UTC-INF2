class Catalogue:
    def __init__(self):
        self.__catalogue = {}

    def ajouter_cours(self, code_court, description, resp, effectif):
        if code_court in self.__catalogue.keys():
            raise ValueError("L'UV est déjà présente dans le catalogue.")
        if not isinstance(code_court, str) or len(code_court) > 5 or len(code_court) <= 0:
            raise ValueError("Le code court n'est pas une chaîne de caractère de taille < à 5")
        if not isinstance(description, str) or description == '':
            raise ValueError("La description n'est pas de type str ou est vide.")
        if not isinstance(resp, str) or resp == '':
            raise ValueError("Le responsable n'est pas de type str ou est vide.")
        if not isinstance(effectif, int) or effectif < 0:
            raise ValueError("L'effectif n'est pas une entier positif")
        self.__catalogue[code_court] = [description, resp, effectif]

    def supprimer_cours(self, code_court):
        if code_court not in self.__catalogue.keys():
            raise ValueError("L'UV n'est pas présente dans le catalogue.")
        self.__catalogue.pop(code_court)

    def recuperer_cours(self, code_court):
        if code_court not in self.__catalogue.keys():
            raise ValueError("L'UV n'est pas présente dans le catalogue.")
        return self.__catalogue[code_court]

    def modifier_cours(self, code_court, **kwargs):
        if code_court not in self.__catalogue.keys():
            raise ValueError("L'UV n'est pas présente dans le catalogue.")
        if kwargs.get('description'):
            self.__catalogue[code_court][0] = kwargs.get('description')
        if kwargs.get('responsable'):
            self.__catalogue[code_court][0] = kwargs.get('responsable')
        if kwargs.get('effectif'):
            self.__catalogue[code_court][0] = kwargs.get('effectif')

    def changement_code_cours(self, code_court, new_code_court):
        if code_court not in self.__catalogue.keys():
            raise ValueError("L'UV n'est pas présente dans le catalogue.")
        information = self.__catalogue[code_court]
        self.supprimer_cours(code_court)
        self.__catalogue[new_code_court] = information


if __name__ == "__main__":
    print("dlrow olleH")

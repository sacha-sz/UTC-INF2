import os
from PIL import Image as pimage


class Note:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'Le titre est : {self.title}'

    @property
    def title(self):
        return self.__titre

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Le titre n'est pas une chaîne de caractère.")
        self.__titre = title

    def print(self):
        print(f'titre : {self.__titre}')


class Article(Note):
    def __init__(self, title, texte):
        Note.__init__(self, title)
        self.texte = texte

    @property
    def texte(self):
        return self.__texte

    @texte.setter
    def texte(self, texte):
        if not isinstance(texte, str):
            raise TypeError("Le texte n'est pas une chaîne de caractère.")
        self.__texte = texte

    def print(self):
        print(f'titre {self.title} \ntexte : {self.texte}')


class Image(Note):
    def __init__(self, titre, description, cheminRacine):
        Note.__init__(self, titre)
        self.description = description
        self.path = cheminRacine

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("La description n'est pas une chaîne de caractère.")
        self.__description = description

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, cheminRacine):
        if not os.path.isfile(cheminRacine):
            raise ValueError("Le chemin n'existe pas.")
        self.__path = cheminRacine

    def print(self):
        img = pimage.open(self.__path)
        print(f'titre {self.title} \ntexte : {self.description} \n{img.show()}')


class Document(Note):
    def __init__(self, titre):
        super().__init__(titre)
        self.__grpNote = []

    def ajouterNote(self, note):
        if not isinstance(note, Note):
            raise TypeError("Ce n'est pas une note.")
        self.__grpNote.append(note)

    def delNote(self, note):
        if note in self.__grpNote:
            self.__grpNote.remove(note)
        else:
            raise ValueError("La note n'est pas dans le document")

    def print(self):
        super().print()
        for note in self.__grpNote:
            note.print()

    def __iter__(self):
        self.__indice_iter = 0
        return self

    def __next__(self):
        if self.__indice_iter >= len(self.__grpNote):
            raise StopIteration
        res = self.__grpNote[self.__indice_iter]
        self.__indice_iter += 1
        return res


if __name__ == "__main__":
    note1 = Note('titre')
    article1 = Article('titre', 'texte')
    image1 = Image('titre','ping','pingouin.jpg')
    document1 = Document('titreDoc')
    document1.ajouterNote(note1)
    document1.ajouterNote(article1)
    document1.ajouterNote(image1)
    document1.print()
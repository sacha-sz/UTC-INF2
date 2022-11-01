from tkinter import *
from PIL import Image, ImageTk


class Fenetre(Tk):
    def __init__(self, largeur=500, hauteur=500):
        Tk.__init__(self)

        ecranX = self.winfo_screenwidth()
        ecranY = self.winfo_screenheight()
        posX = ecranX // 2 - largeur // 2
        posY = ecranY // 2 - hauteur // 2

        geometrie = f"{largeur}x{hauteur}+{posX}+{posY}"
        self.geometry(geometrie)

        self.label = {}
        self.create_label("Nom", "Nom : ", 0, 0)
        self.create_label("Prenom", "Prenom : ", 1, 0)
        self.create_label("Domaine", "Domaine : ", 2, 0)
        self.create_label("Adresse_mail", "", 3, 0)

        self.entry = {}
        self.create_entry("Prenom", 0, 1)
        self.create_entry("Nom", 1, 1)
        self.create_entry("Domaine", 2, 1)

        self.create_button("Quitter", 4, 2, "Quitter")
        self.create_button("Valider", 4, 0, "Valider")
        self.create_button("Reinitialiser", 4, 1, "Reinitialiser")

        self.show_image("france.jpg")

    def create_label(self, nom, texte, ligne, colonne):
        if nom == 'Adresse_mail':
            self.label[nom] = Label(self, text=texte, anchor="w")
            self.label[nom].grid(row=ligne, column=colonne, sticky="E", padx=10, pady=10, columnspan=3)
        else:
            self.label[nom] = Label(self, text=texte, anchor="w")
            self.label[nom].grid(row=ligne, column=colonne, sticky="E", padx=10, pady=10)

    def create_entry(self, type, ligne, colonne):
        self.entry[type] = Entry(self)
        self.entry[type].grid(row=ligne, column=colonne, sticky="E", padx=10, pady=10)

    def create_button(self, texte, ligne, colonne, type):
        self.button = Button(self, text=texte, command=self.command(type), activebackground="red")
        self.button.grid(row=ligne, column=colonne, sticky="E", padx=10, pady=10)

    def command(self, type):
        if type == "Quitter":
            return self.destroy
        elif type == "Valider":
            return self.show_mail
        elif type == "Reinitialiser":
            return self.label_delete

    def label_delete(self):
        self.entry["Prenom"].delete(0, END)
        self.entry["Nom"].delete(0, END)
        self.entry["Domaine"].delete(0, END)
        self.label["Valider"].config(text='')

    def show_mail(self):
        texte = f'{self.entry["Prenom"].get()}.{self.entry["Nom"].get()}@{self.entry["Domaine"].get()}'
        self.label["Adresse_mail"].config(text=texte)
        self.entry["Prenom"].delete(0, END)
        self.entry["Nom"].delete(0, END)
        self.entry["Domaine"].delete(0, END)

    def show_image(self, filename):
        self.image = Image.open(filename)
        self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width=100, height=100)
        self.canvas.create_image(0, 0, image=self.photo)
        self.canvas.grid(row=0, column=2, rowspan=3)


if __name__ == "__main__":
    maFenetre = Fenetre()
    maFenetre.mainloop()
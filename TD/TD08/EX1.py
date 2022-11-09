from tkinter import *


class Fenetre(Tk):
    def __init__(self, largeur=100, hauteur=100):
        Tk.__init__(self)
        self.title('EXERICE 1')

        # Dimensionnement et positionnement de la fenêtre
        ecranX = self.winfo_screenwidth()
        ecranY = self.winfo_screenheight()
        posX = ecranX // 2 - largeur // 2
        posY = ecranY // 2 - hauteur // 2

        geometrie = f"{largeur}x{hauteur}+{posX}+{posY}"
        self.geometry(geometrie)

        self.config(bg="yellow")
        # alternative : self["bg"] = "yellow"

        # Creation et positionnement de deux labels et un bouton

        self.label1 = Label(self, text="Bienvenue en INF2")  # label de chaîne
        self.label1.pack()

        self.label2 = Label(self, text="Première fenètre")  # label de chaîne
        self.label2.pack()

        self.button_quitter = Button(self, text="Quitter", command=self.destroy, activebackground="red")
        self.button_quitter.pack(side=BOTTOM)


if __name__ == '__main__':
    LARG = int(input("Entrez la largeur de la fenêtre : "))
    HAUT = int(input("Entrez la hauteur de la fenêtre : "))
    maFenetre = Fenetre(LARG, HAUT)
    maFenetre.mainloop()



from tkinter import *
from tkinter import messagebox
from random import randint


class Fenetre(Tk):
    def __init__(self, largeur=400, hauteur=400):
        Tk.__init__(self)
        self.dict_button = {}
        self.nb_coups = 0

        ecranX = self.winfo_screenwidth()
        ecranY = self.winfo_screenheight()
        posX = ecranX // 2 - largeur // 2
        posY = ecranY // 2 - hauteur // 2

        geometrie = f"{largeur}x{hauteur}+{posX}+{posY}"
        self.geometry(geometrie)
        self.title("EX3-TD8")

        self.label_titre = Label(self, text="Jeu du 421")
        self.label_titre.grid(row=0, column=1, padx=5, pady=5)

        self.create_button("Lancer dé 1 :", 1)
        self.create_button("Lancer dé 2 :", 2)
        self.create_button("Lancer dé 3 :", 3)

        self.entree_1 = StringVar()
        self.entree_2 = StringVar()
        self.entree_3 = StringVar()
        self.output = StringVar()

        self.affiche_de_1 = Label(self, textvariable=self.entree_1)
        self.affiche_de_1.grid(row=1, column=1)

        self.affiche_de_2 = Label(self, textvariable=self.entree_2)
        self.affiche_de_2.grid(row=2, column=1)

        self.affiche_de_3 = Label(self, textvariable=self.entree_3)
        self.affiche_de_3.grid(row=3, column=1)

        self.affiche_coups = Label(self, textvariable=self.output)
        self.affiche_coups.grid(row=4, column=0)

        self.quit_button = Button(self, text="Quitter", command=self.destroy)
        self.quit_button.grid(row=4, column=1)

    def create_button(self, txt, num_des):
        self.dict_button[txt] = Button(self, text=txt, command=lambda:self.lancer_des(num_des))
        self.dict_button[txt].grid(row=num_des, column=0, padx=5, pady=5)

    def lancer_des(self, num_des):
        temp = randint(1, 6)
        self.nb_coups += 1
        if num_des == 1:
            self.entree_1.set(f'-> {temp}')
        elif num_des == 2:
            self.entree_2.set(f'-> {temp}')
        else:
            self.entree_3.set(f'-> {temp}')
        self.verif_421()

    def verif_421(self):
        if self.entree_1.get() and self.entree_2.get() and self.entree_3.get():
            list_result_1 = self.entree_1.get().split(" ")
            list_result_2 = self.entree_2.get().split(" ")
            list_result_3 = self.entree_3.get().split(" ")
            list_result_3_des = set(list([list_result_1[1].strip(), list_result_2[1].strip(), list_result_3[1].strip()]))

            # deux ensembles égaux sont deux ensembles qui possèdent exactement les mêmes objets (pas de relation d’ordre)
            if list_result_3_des == {"1", "2", "4"}:
                self.output.set(f'-> {self.nb_coups}')
                self.fenetre_gagnante()
                self.nb_coups = 0

    def fenetre_gagnante(self):
        messagebox.showinfo("Fenêtre gagnante", "Bien joué beau gosse\nTu as gagné mon coeur")


if __name__ == "__main__":
    mafenetre = Fenetre()
    mafenetre.mainloop()
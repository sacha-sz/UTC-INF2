from tkinter import *


class Fenetre(Tk):
    def __init__(self, largeur=340, hauteur=300):
        Tk.__init__(self)
        self.case = dict()

        ecranX = self.winfo_screenwidth()
        ecranY = self.winfo_screenheight()
        posX = ecranX // 2 - largeur // 2
        posY = ecranY // 2 - hauteur // 2

        geometrie = f"{largeur}x{hauteur}+{posX}+{posY}"
        self.geometry(geometrie)
        self.title("EX4-TD8")
        self.config(padx=5, pady=5, bg="light blue")
        self.creer_plateau()

    def creer_plateau(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if (i + j) % 2 == 0:
                    self.creer_case(i, j, "black")
                else:
                    self.creer_case(i, j, "white")

    def creer_case(self, i, j, bg):
        temp=f'{i},{j}'
        self.case[temp] = Label(width=5, height=2,bg=bg)
        self.case[temp].grid(row=i, column=j)


if __name__ == "__main__":
    mafenetre = Fenetre()
    mafenetre.mainloop()
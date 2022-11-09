if __name__ == '__main__':
    texte = input("Entrez votre texte : ")
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    list = []
    temp = 0
    len = 0
    taille_mot = []
    nombre_mot = 1


    def freq(elt, txt):
        freq = 0
        temp = 0
        for ch in txt:
            if ch in alphabet:
                temp += 1
                if ch == elt:
                    freq += 1
        return (freq / temp) * 100


    for elt in alphabet:
        list.append((elt, freq(elt, texte)))

    for ch in texte:
        if ch == ' ':
            nombre_mot += 1
        elif ch in alphabet:
            len += 1

    print(list)
    list.sort(key=lambda x: x[1], reverse=True)
    print(list)
    print(nombre_mot)
    print(len / nombre_mot)

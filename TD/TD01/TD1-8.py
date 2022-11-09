if __name__ == "__main__":
    texte = input("Entrez votre texte : ")
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    list = []
    temp = 0


    def freq(elt, txt):
        elt = 0
        temp = 0
        for ch in txt:
            if ch in alphabet:
                temp += 1
                if ch == elt:
                    elt += 1
        return (elt / temp) * 100


    for elt in alphabet:
        list.append((elt, freq(elt, texte)))

    print(list)

    print(list)
    frequence = list(dict.items())
    frequence = sorted(frequence)
    print(frequence)

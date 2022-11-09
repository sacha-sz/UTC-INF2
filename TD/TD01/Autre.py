if __name__ == "__main__":
    texte = input("Entrez votre texte : ")
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    dict = {}


    def second_element(dict):
        return dict[1]


    for elt in alphabet:
        dict[elt] = 0

    for ch in texte:
        if ch in alphabet:
            dict[ch] += 1

    for elt in dict:
        dict[elt] = (dict[elt] / len(texte)) * 100

    for elt in dict:
        print(f"La fréquence d'apparition de la lettre {elt} est {dict[elt]}% .")

    dict = sorted(dict.items(), key=dict[], reverse=True)

    print(dict)

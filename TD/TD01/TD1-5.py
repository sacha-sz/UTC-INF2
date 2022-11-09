if __name__ == "__main__":
    texte = str(input("Entrez votre texte : "))
    nombre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    voyelle = ["a", "e", "i", "o", "u", "y"]
    nombre_carac = 0
    nombre_nbr = 0
    nombre_ltr = 0
    nombre_vy = 0

    for ch in texte.lower():
        nombre_carac += 1
        if ch in alphabet: nombre_ltr += 1
        if ch in nombre: nombre_nbr += 1
        if ch in voyelle: nombre_vy += 1

    print(
        f'nombre carac : {nombre_carac}, nombre_vy : {nombre_vy}, nombre_nbr : {nombre_nbr}, nombre_ltr : {nombre_ltr}')

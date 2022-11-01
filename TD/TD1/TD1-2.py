if __name__ == "__main__":
    n = int(input("Combien y a t il de valeur ?, Entrez n : "))
    t = []
    for i in range(1, n + 1):
        temp = float(input(f'Entrez la valeur {i} : '))
        t.append(temp)
    t.sort()
    somme = 0
    for i in range(len(t)):
        somme += t[i]
    moyenne = somme / n
    print(f'La moyenne est de : {moyenne}')
    somme -= t[0]
    somme -= t[n - 1]
    moyenne_c = somme / (n - 2)
    print(f'La moyenne centrale est de : {moyenne_c}')

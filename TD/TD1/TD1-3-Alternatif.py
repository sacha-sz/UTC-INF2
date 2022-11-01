if __name__ == "__main__":
    import random as rd

    t = []
    for i in range(12):
        t.append(rd.randrange(-20, 20, 1))
        # float(input(f'Quelle est la température n {i + 1} : ')))

    t.sort()
    print(f'La température maximale est : {t[11]}')
    print(f'La température minimale est : {t[0]}')
    print(t)
    b = t[0]
    for i in range(1, 12):
        if abs(t[i]) < abs(b):
            b = t[i]
        elif abs(t[i]) == abs(b):
            b = min(b, t[i])

    print(b)

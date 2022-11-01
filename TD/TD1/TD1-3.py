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

    if 0 in t:
        print('La valeur la plus proche de 0 est : 0)')
    else:
        if t[0] >= 0:
            print(f'La valeur la plus proche de 0 est : {t[0]}')
        elif t[11] <= 0:
            print(f'La valeur la plus proche de 0 est : {t[11]}')
        else:
            i = 0
            while t[i] < 0:
                i += 1
            if (t[i] - t[i - 1]) == 2 * t[i]:
                print(f'La valeur la plus proche de 0 est : {t[i - 1]}')
            elif (abs(t[i - 1]) - t[i]) > 0:
                print(f'La valeur la plus proche de 0 est : {t[i]}')
            elif (abs(t[i - 1]) - t[i]) < 0:
                print(f'La valeur la plus proche de 0 est : {t[i - 1]}')

noms = ['boris', 'jean', 'simon', 'anna', 'jeanne', 'brandon', 'theo', 'brahim', 'marion', 'leila', 'lancelot',
'quentin', 'kevin', 'john', 'louise', 'paul', 'sarah', 'christophe','marielle', 'oriane', 'luc']
dict = {}
temp = 0, ''

if __name__ == "__main__":
    for elt in noms:
        i = 0
        for ch in elt:
            temp = (i, ch)
            if temp not in dict.keys():
                dict[temp] = [elt]
            else:
                dict[temp].append(elt)
            i += 1

    couple = int(input("Entrez la position souhaitée : ")), input("Entrez la lettre souhaitée : ")
    print(f'Les mots comprenant cette lettre à la position souhaitée ({couple}) : {dict[couple]}')

    for elt in dict:
        print(elt, dict[elt])

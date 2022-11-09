noms = ['boris', 'jean', 'simon', 'anna', 'jeanne', 'brandon', 'theo', 'brahim', 'marion', 'leila', 'lancelot',
'quentin', 'kevin', 'john', 'louise', 'paul', 'sarah', 'christophe','marielle', 'oriane', 'luc']
dict = {}
temp = 0, ''

if __name__ == "__main__":
    for elt in noms:
        for i, ch in enumerate(elt):
            temp = (i, ch)
            if dict.get(temp, False):
                dict[temp].append(elt)
            else:
                dict[temp] = [elt]

    couple = int(input("Entrez la position souhaitée : ")), input("Entrez la lettre souhaitée : ")
    print(f'Les mots comprenant cette lettre à la position souhaitée ({couple}) : {dict[couple]}')

    for elt in dict:
        print(elt, dict[elt])

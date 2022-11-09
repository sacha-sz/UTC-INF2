import collections


def verifier(chaine):
    couples = {"{": "}", "(": ")", "[": "]"}
    pile = collections.deque()
    for x in chaine:
        if x in couples.keys():
            pile.append(x)
        if x in couples.values():
            y = pile.pop()
            if couples[y] != x:
                return False
    if len(pile) != 0:
        return False
    return True

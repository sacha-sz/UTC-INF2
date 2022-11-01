def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def affiche_fibo(lim):
    i = 0
    while fibo(i) < lim:
        print(fibo(i))
        i += 1


def retourne_fibo(lim):
    fib = []
    i = 0
    while fibo(i) < lim:
        fib.append(fibo(i))
        i += 1
    return fib


if __name__ == "__main__":
    lim = int(input("Entrez la limite : "))
    affiche_fibo(lim)
    list = retourne_fibo(lim)
    print(list)
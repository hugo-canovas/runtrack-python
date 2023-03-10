x = int(input("Entrez un nombre entier : "))
n = int(input("Entrez une puissance(nbr entier) : "))


def derivees(x, n):
    if n == 0:
        return 1
    else:
        return x*derivees(x, n-1)

print(derivees(x,n))
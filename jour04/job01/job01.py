nbr = int(input("Veuillez entrer un nombre entier : "))
def factorielle(nbr):
    if nbr == 0:
        return 1
    else:
        return nbr*factorielle(nbr - 1)

print(factorielle(nbr))

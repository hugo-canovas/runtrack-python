nbr = int(input("Entrez un nombre entier : "))

def derivees(nbr):
    x="x"
    if nbr == 0 or nbr == 1:
        return x
    elif nbr == 2:
        return str(nbr)+x
    else:
        return str(nbr)+x+"^"+str((nbr-1))


print(derivees(nbr))
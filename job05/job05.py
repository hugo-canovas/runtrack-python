
nbr_1 = int(input("Entrez valeur 1 :"))
nbr_2 = int(input("Entrez valeur 2 :"))

if nbr_1 == nbr_2:
    print("Les deux valeurs sont égales")
elif nbr_1 > nbr_2:
    for i in range(nbr_1 - 1, nbr_2, -1):
        print(i)
else:
    for i in range(nbr_1+1, nbr_2):
        print(i)

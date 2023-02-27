hauteur = int(input("Entrez la hauteur :"))
largeur = int(input("Entrez la largeur :"))

for i in range(hauteur-1):
    print("|" + ("-" * (largeur)) + "|")
    for x in range(2, hauteur):
        print("|" + (" " * (largeur)) + "|")
    print("|" + ("-" * (largeur)) + "|")
    break



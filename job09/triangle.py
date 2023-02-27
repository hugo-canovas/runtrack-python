hauteur = int(input("Entrez La hauteur de votre triangle :"))
largeur = hauteur * 2
space = " "



for i in range(hauteur):
    for x in range(hauteur-1):
        print(space * (hauteur-1) + "/" + space * (x * 2) + '\\')
        hauteur = hauteur -1
        x = x+1
    print('/' + ('_' * (x*2)) + '\\')
    break
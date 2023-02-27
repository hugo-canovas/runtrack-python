text = str(input("Entrez votre texte :"))
choice = str(input("Veuillez choisir votre fonction :"))


if choice == "upper":
    def myUpper(text):
        print(text.upper())
    myUpper(text)
elif choice == "lower":
    def myLower(text):
        print(text.lower())
    myLower(text)
elif choice == "title":
    def myTitle(text):
        print(text.capitalize())
    myTitle(text)
elif choice == "clean":
    def myClean(text):
        print(text.replace("  ", " "))
    myClean(text)




text = str(input("Entrez votre texte :"))
choice = str(input("Veuillez choisir votre fonction :"))


def myUpper(text):
    lowercase = [chr(i) for i in range(97, 122)]
    newText = ""
    for x in text:
        if x in lowercase:
            x = chr(ord(x) - 32)
            newText = newText + x
    return newText


def myLower(text):
    uppercase = [chr(i) for i in range(65, 91)]
    newText = ""
    for x in text:
        if x in uppercase:
            x = chr(ord(x) + 32)
            newText = newText + x
    return newText


def myTitle(text):
    lowercase = [chr(i) for i in range(97, 122)]
    uppercase = [chr(i) for i in range(65, 91)]
    newText = ""
    for i in range(len(text)):
        if i == 0:
            if text[i] in lowercase:
                newText += chr(ord(text[i]) - 32)
        elif text[i-1] == " ":
            if text[i] in lowercase:
                newText += chr(ord(text[i]) - 32)
        else:
            newText += text[i]
    return newText


def myClean(text):
    myList = text.split()
    newText = " ".join(myList)
    return newText


if choice == "upper":
    print(myUpper(text))
elif choice == "lower":
    print(myLower(text))
elif choice == "title":
    print(myTitle(text))
elif choice == 'clean':
    print(myClean(text))

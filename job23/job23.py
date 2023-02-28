text = str(input("Entrez un mot :"))


def findWords(text):
    myList = []
    newList = []
    for x in text:
        myList.append(ord(x))
        for i in myList:
            if i == 0:
                return myList[i]



print(findWords(text))
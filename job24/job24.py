def readFile():
    with open('dico_france.txt', 'r') as file:
        myList = file.read().split()
        newList = []
        total = int()
        lastList = []
        for i in range(len(myList)):
            for x in myList[i]:
                newList.append(ord(x))
            for value in newList:
                total = value
                lastList.append(total)
            print(lastList)
            break


            #return file.read(words)




print(readFile())
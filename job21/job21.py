def mySort(myList):
    myNewList = []
    while myList:
        minus = min(myList)
        myList.remove(minus)
        myNewList.append(minus)
    return myNewList


mySort([3, 4, 8, 2])


def myDisplay(myList_2):
    return myList_2


print(myDisplay([2, 4, 5]))

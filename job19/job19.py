myList = []


def indefineParameter(*parameters):
    parameter = 0
    for value in parameters:
        parameter = value
        myList.append(parameter)


indefineParameter(3, 5, 1, 5, 8, 3)

def trier(myList):
    myNewList = []
    while myList:
        minus = min(myList)
        myList.remove(minus)
        myNewList.append(minus)
    return myNewList

print(trier(myList))
myList = []


def indefineParameter(*parameters):
    parameter = 0
    for value in parameters:
        parameter = value
        myList.append(parameter)


indefineParameter(5, 3, 4, 5)
myList.sort()
print(myList)

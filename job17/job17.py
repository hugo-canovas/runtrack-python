myList = []
def indefineParameter(*parameters):
    count = 0
    for value in parameters:
        count = value
        myList.append(count)
indefineParameter(2,6,20)

print(myList)

for nbr_pair in myList:
    if nbr_pair % 2 == 0:
        print(nbr_pair)


def indefineParameter(*parameter):
    count = 0
    for value in parameter:
        count += value
    return count

print(indefineParameter(1,2,3))
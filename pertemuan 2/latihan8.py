def getBagi(myList):
    result = myList[0]
    for item in myList[1:]:
        result /= item
    return result

print(getBagi([100, 10, 2])) # output = 5.0
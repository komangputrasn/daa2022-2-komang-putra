def getBagi(myList):
    flattened = []
    for i in myList:
        for j in i:
            flattened.append(j)
    result = flattened[0]
    for item in flattened[1:]:
        result /= item
    return result

print(getBagi([[100, 5], [4, 5]])) # output = 1
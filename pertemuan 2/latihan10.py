def getKurang(myList):
    result = 0
    for i in myList:
        for j in i:
            result -= j
    return result

print(getKurang([[1, 2, 3], [4, 5, 6]])) # output = -21
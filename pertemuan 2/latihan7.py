def getKali(myList):
    product = 1
    for item in myList:
        product *= item
    return product

print(getKali([1, 2, 3, 4])) # output = 24
def dSelect(arrA, queryIndex, lIndex=0, rIndex=None):
    # returns value of arrA[queryIndex]
    
    if rIndex is None:
        rIndex = len(arrA)
    if lIndex == rIndex:
        # terminate if array length reaches 0
        return

    if rIndex-lIndex <= 5:
        # select first element as pivVal if array size is <= 5
        pivVal = arrA[lIndex]
    else:
        # deterministic pivot selection
        arrC = []
        for i in range(lIndex, rIndex, 5):             # each 5 element subarray in arrA:
            temp = arrA[i:i+5]
            arrC.append(dSelect(arrA[i:i+5], 2))    # find, append it's median to c
        # pivVal is "median of medians"
        pivVal = dSelect(arrC, len(arrC)//2)

        # put pivVal at beginning of array
        arrA[arrA.index(pivVal)], arrA[lIndex] = arrA[lIndex], arrA[arrA.index(pivVal)]

    # partition arrA around pivVal
    boundIndex = lIndex+1
    for currentIndex in range(boundIndex, rIndex):
        if arrA[currentIndex] < pivVal:
            arrA[boundIndex], arrA[currentIndex] = arrA[currentIndex], arrA[boundIndex]
            boundIndex += 1

    pivIndex = boundIndex-1     #find currentIndex value of pivVal

    # place pivVal in rightful position
    arrA[lIndex], arrA[pivIndex] = arrA[pivIndex], arrA[lIndex]
    
    # recursive call to make is determined by 
    # location of queryIndex relative to pivIndex
    if queryIndex < pivIndex:
        return dSelect(arrA, queryIndex, lIndex, pivIndex)
    if pivIndex == queryIndex:
        return arrA[pivIndex]
    if queryIndex > pivIndex:
        return dSelect(arrA, queryIndex, pivIndex+1, rIndex)


array = [0, 9, 7, 4, 2, 3, 5, 1, 6, 8]
print(dSelect(array, 2))

import random


def partition(arr, pivotIndex, testing=False):
    if pivotIndex != 0:
        arr[pivotIndex], arr[0] = arr[0], arr[pivotIndex]  # move pivot to start of array
    pivot = arr[0]                                         # get pivot value
    border = 1                                             # set border just beyond pivot

    for i in range(1, len(arr)):
        if arr[i] < pivot:                             # if current element is less than pivot
            arr[i], arr[border] = arr[border], arr[i]  # swap value to border index
            border += 1                                # advance border
    arr[0], arr[border-1] = arr[border-1], arr[0]      # move pivot to rightful position

    if testing:
        pivot = arr[border-1]
        assert all(x < pivot for x in arr[:border-1])
        assert all(x > pivot for x in arr[border:])

    return border-1

    # array is now partitioned around pivot, with pivot at position [border - 1]


def randomizedSelection(arr, queryIndex, start=0, end=None, testing=False):
    if end is None:
        end = len(arr)

    if len(arr) == 1:
        return arr[0]

    randIndex = random.randrange(start, end)  # find random pivot index

    if testing:
        assert arr[randIndex] in arr

    pivotIndex = partition(arr, randIndex)    # partition array around pivot

    if queryIndex == pivotIndex:
        return arr[pivotIndex]
    elif queryIndex < pivotIndex:  # query in first half
        return randomizedSelection(arr[:pivotIndex], queryIndex)
    elif queryIndex > pivotIndex:  # query in second half
        return randomizedSelection(arr[pivotIndex+1:], queryIndex-pivotIndex-1)


def main():
    array_in = [0, 5, 20, 50, 66, 100, 150, 172]
    # array_in = [3, 8, 2, 5, 1, 4, 7, 6, 10, 3, 2, 5]
    query = 3
    print(randomizedSelection(array_in, query))


main()

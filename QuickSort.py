def main():
    array_in = [3, 8, 2, 5, 1, 4, 7, 6]
    left = 0
    right = 7
    quickSort(array_in, left, right)
    print("final output: ", array_in)


def quickSort(array, l, r):
    pivot = array[l]
    index = l + 1
    for j in range(index, r):
        if array[j] < pivot:
            mem = array[j]
            array[j] = array[index]
            array[index] = mem
            index += 1
    array[l] = array[index - 1]
    array[index - 1] = pivot
    quickSort(array, l, index - 1)
    quickSort(array, index, r)

main()

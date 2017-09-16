import random


def swap(array, index1, index2):
    # swap values of indices 1 and 2 in array
    mem = array[index1]
    array[index1] = array[index2]
    array[index2] = mem


def find_pivot(array, left, right):
    # find random pivot, then moves it to first position in array
    pivot_index = random.randrange(left, right + 1)
    pivot = array[pivot_index]
    swap(array, left, pivot_index)
    pivot_boundary = left + 1

    return pivot, pivot_boundary


def quick_sort(array, left, right):
    if (right - left) > 0:

        pivot, pivot_boundary = find_pivot(array, left, right)

        # iterate through array, moving elements < pivot behind
        # pivot_boundary, incrementing pivot_boundary as necessary
        for i in range(pivot_boundary, right + 1):
            if array[i] < pivot:
                swap(array, i, pivot_boundary)
                pivot_boundary += 1

        # put pivot in final position (behind pivot boundary)
        swap(array, array.index(pivot), pivot_boundary - 1)

        # recurse on left and right partitions
        quick_sort(array, left, pivot_boundary - 1)
        quick_sort(array, pivot_boundary, right)


def main():
    array_in = [3, 8, 2, 5, 1, 4, 7, 6, 10, 3, 2, 5]
    left = 0
    right = len(array_in) - 1
    quick_sort(array_in, left, right)
    print("final output:\n", array_in)


main()

import random


class Counter:
    def __init__(self, n=0):
        self.total = n

    def increment(self, amt=0):
        self.total += amt

    def print_total(self):
        print("comparisons:\n", self.total)


def swap(array, index1, index2):
    # swap values of indices 1 and 2 in array
    mem = array[index1]
    array[index1] = array[index2]
    array[index2] = mem


def choose_pivot(arr, start, end, pivot_type):

    def first_element(left):
        # select first item in array as pivot
        index = left
        return index

    def random_element(left, right):
        # select random pivot
        index = random.randrange(left, right + 1)
        return index

    def median_element(array, left, right):
        # select median of array[left], array[mid], and array[right] as pivot
        mid = (right + left) // 2
        sorted_ar = sorted([(array[left],  left),
                            (array[mid],   mid),
                            (array[right], right)])

        index = sorted_ar[1][1]
        return index

    if pivot_type == "first":
        pivot_index = first_element(end)
    elif pivot_type == "random":
        pivot_index = random_element(start, end)
    elif pivot_type == "median":
        pivot_index = median_element(arr, start, end)

    pivot = arr[pivot_index]
    swap(arr, start, pivot_index)
    pivot_boundary = start + 1

    return pivot, pivot_index, pivot_boundary


def quick_sort(array, counter, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if (right - left) > 0:
        # find pivot and move to front of array, then set pivot_boundary
        pivot, pivot_index, pivot_boundary = choose_pivot(array, left, right, "median")

        # iterate through array, moving elements < pivot behind
        # pivot_boundary, incrementing pivot_boundary as necessary
        for i in range(pivot_boundary, right + 1):
            if array[i] < pivot:
                swap(array, i, pivot_boundary)
                pivot_boundary += 1

        # put pivot in final position (behind pivot boundary)
        swap(array, array.index(pivot), pivot_boundary - 1)

        # recurse on left and right partitions
        counter.increment(pivot_boundary - 1 - left)
        quick_sort(array, counter, left, pivot_boundary - 1)

        counter.increment(right - pivot_boundary)
        quick_sort(array, counter, pivot_boundary, right)


def main():
    numlist_file = "/Users/justin/PycharmProjects/StanfordLagunitaAlgorithms1/txt files/QuickSort.txt"
    in_file = open(numlist_file, 'r')
    array_in = [int(nums.strip()) for nums in in_file.readlines()]

    # array_in = [3, 8, 2, 5, 1, 4, 7, 6, 10, 3, 2, 5]
    comparison_count = Counter()

    quick_sort(array_in, comparison_count)

    print("final output:\n", array_in)
    comparison_count.print_total()


main()

# ALGORITHM STILL INCORRECT

c = 0


def main():
    file = open('/Users/justin/PycharmProjects/Stanford Lagunita - Algorithms/txt files/IntegerArray.txt', 'r')
    array = file.read().split()
    print("done reading")
    count_inversions(array)
    print(c)


def count_inversions(array):
    global c
    if len(array) > 1:
        mid = len(array) // 2
        first_half = array[:mid]
        second_half = array[mid:]

        count_inversions(first_half)  # left inversions
        count_inversions(second_half)  # right inversions

        i, j, k = 0, 0, 0

        while k < len(first_half) + len(second_half):
            while i < len(first_half) and j < len(second_half):  # neither list exhausted
                if first_half[i] <= second_half[j]:  # not an inversion
                    array[k] = first_half[i]
                    i += 1
                else:
                    c += len(first_half[i:])  # inversion
                    array[k] = second_half[j]
                    j += 1
                k += 1
            while i < len(first_half):  # second list exhausted
                array[k] = first_half[i]
                i += 1
                k += 1
            while j < len(second_half):  # first list exhausted
                array[k] = second_half[j]
                j += 1
                k += 1

    return array

main()



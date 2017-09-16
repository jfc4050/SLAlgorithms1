def main():
    list_to_sort = [0, 7, 2, 4, 6, 5, 1, 3]
    print("sorted list:\n", merge_sort(list_to_sort))


def merge_sort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2

        # define and recurse on first and second halves
        first_half = lst[:middle]
        second_half = lst[middle:]
        merge_sort(first_half)
        merge_sort(second_half)

        i, j, k = 0, 0, 0

        while k < len(lst):
            while i < len(first_half) and j < len(second_half):
                if first_half[i] < second_half[j]:
                    lst[k] = first_half[i]
                    i += 1
                else:
                    lst[k] = second_half[j]
                    j += 1
                k += 1
            while i < len(first_half):
                lst[k] = first_half[i]
                i += 1
                k += 1
            while j < len(second_half):
                lst[k] = second_half[j]
                j += 1
                k += 1
    return lst


main()



def merge(lst, s_half1, s_half2):
    # indices for half1, half2, lst
    i = 0  # index for half 1
    j = 0  # index for half 2
    i_lst = 0  # index for lst

    while i_lst < len(lst):
        # if elements left in both halves
        if i < len(s_half1) and j < len(s_half2):
            if s_half1[i] < s_half2[j]:
                lst[i_lst] = s_half1[i]
                i += 1
            else:
                lst[i_lst] = s_half2[j]
                j += 1
        # if half 2 exhausted
        elif i < len(s_half1):
            lst[i_lst] = s_half1[i]
            i += 1
        # if half 1 exhausted
        elif j < len(s_half2):
            lst[i_lst] = s_half2[j]
            j += 1

        i_lst += 1


def merge_sort(lst):
    # stop recursing if len(lst) == 1
    if len(lst) == 1:
        return lst

    # define and recurse on first and second halves
    middle = len(lst) // 2
    s_half1 = merge_sort(lst[:middle])
    s_half2 = merge_sort(lst[middle:])

    # begin merge
    merge(lst, s_half1, s_half2)

    # finished merging
    return lst


def main():
    list_to_sort = [0, 7, 2, 4, 6, 5, 1, 3]
    expected_list = [0, 1, 2, 3, 4, 5, 6, 7]
    print("sorted list:\n", merge_sort(list_to_sort))
    print(merge_sort(list_to_sort) == expected_list)


main()



# still wasting time in merge step

count = 0


def merge(lst, s_half1, s_half2):
    global count
    # indices for half1, half2, lst
    i = 0  # index for half 1
    j = 0  # index for half 2
    i_lst = 0  # index for lst

    while i_lst < len(lst):
        # if elements left in both halves
        if i < len(s_half1) and j < len(s_half2):
            if s_half1[i] <= s_half2[j]:
                lst[i_lst] = s_half1[i]
                i += 1
            else:
                count += len(s_half1[i:])
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
    numlist_file = "/Users/justin/PycharmProjects/StanfordLagunitaAlgorithms1/txt files/IntegerArray.txt"
    in_file = open(numlist_file, 'r')
    numlist = [int(nums.strip()) for nums in in_file.readlines()]

    merge_sort(numlist)
    print(count)


main()



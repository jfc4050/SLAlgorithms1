def main():
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    test_query = 31
    print(binary_search(testlist, 0, len(testlist) - 1, test_query))


def binary_search(list_in, first, last, query):
    mid = (first + last) // 2

    if list_in[mid] == query:
        return mid

    if first == last:
        return "not found"

    else:
        # if query is in first half of list
        if query < list_in[mid]:
            return binary_search(list_in, first, mid, query)

        # if query is in second half of list
        if query > list_in[mid]:
            return binary_search(list_in, mid+1, last, query)


main()

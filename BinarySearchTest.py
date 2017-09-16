def main():
    test_query = int(input("enter test_query\n"))
    test_list = [0, 5, 20, 50, 66, 100, 150, 172]
    first = 0
    last = len(test_list) - 1

    print(binary_search(test_query, test_list, first, last))


def binary_search(query_in, list_in, first, last):

    # stop recursion if list size = 0
    if first == last:
        return str(query_in) + " not found"

    mid = (first + last) // 2
    # if query_in is found
    if list_in[mid] == query_in:
        return mid
    else:
        # if query_in is in first half of list
        if query_in < list_in[mid]:
            return binary_search(query_in, list_in, first, mid)

        # if query_in is in second half of list
        if query_in > list_in[mid]:
            return binary_search(query_in, list_in, mid+1, last)


main()

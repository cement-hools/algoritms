# 45546295


def search_in_broken_array(broken_array, start, end, target):
    mid = (start + end) // 2

    if end < start:
        return -1

    if target == broken_array[mid]:
        return mid

    if broken_array[start] < broken_array[mid]:
        if broken_array[start] <= target < broken_array[mid]:
            return search_in_broken_array(broken_array, start, mid - 1, target)
        return search_in_broken_array(broken_array, mid + 1, end, target)

    elif broken_array[start] > broken_array[mid]:
        if broken_array[mid] < target <= broken_array[end]:
            return search_in_broken_array(broken_array, mid + 1, end, target)
        return search_in_broken_array(broken_array, start, mid - 1, target)

    else:
        if broken_array[mid] != broken_array[end]:
            return search_in_broken_array(broken_array, mid + 1, end, target)
        result = search_in_broken_array(broken_array, start, mid - 1, target)
        if result == -1:
            return search_in_broken_array(broken_array, mid + 1, end, target)
        return result

    return -1


def main():
    _ = input()
    desired_element = int(input())
    input_array = [int(i) for i in input().split()]
    start_index = 0
    end_index = len(input_array) - 1
    print(
        search_in_broken_array(
            input_array,
            start_index,
            end_index,
            desired_element
        )
    )


if __name__ == '__main__':
    main()

# 45872239


from functools import cmp_to_key


def large_number(numbers_arr):
    def compare(x, y):
        if x + y >= y + x:
            return 1
        return -1

    if not numbers_arr:
        return '0'
    numbers = list(map(str, numbers_arr))
    numbers.sort(key=cmp_to_key(compare), reverse=True)
    return ''.join(numbers)


def main():
    count_of_numbers = int(input())
    if count_of_numbers:
        input_numbers = [i for i in input().split()]
        print(large_number(input_numbers))


if __name__ == '__main__':
    main()

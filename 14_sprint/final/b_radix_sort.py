# id 45856013


def radix_sort(numbers_array):
    digit_capacity = len(str(max(numbers_array)))
    for discharge in range(digit_capacity):
        array_of_bits = [[] for _ in range(10)]
        for number in numbers_array:
            digit_for_sorting = (number // 10 ** discharge) % 10
            array_of_bits[digit_for_sorting].append(number)
        numbers_array = []
        for bit in range(10):
            numbers_array.extend(array_of_bits[bit])

    return numbers_array


def main():
    count_of_numbers = int(input())
    if count_of_numbers:
        input_numbers = [int(_) for _ in input().split()]
        print(*radix_sort(input_numbers))


if __name__ == '__main__':
    main()

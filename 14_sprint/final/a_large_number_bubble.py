# 45812420


def large_number(numbers_arr):
    if not numbers_arr:
        return '0'
    numbers = list(map(str, numbers_arr))
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return "".join(numbers)


def main():
    numbers = int(input())
    if numbers:
        input_numbers = [i for i in input().split()]
        print(large_number(input_numbers))


if __name__ == '__main__':
    main()

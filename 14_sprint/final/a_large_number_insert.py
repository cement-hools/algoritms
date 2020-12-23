n = 1
if n:
    input_str = '15 56 2 0 3 578 569 8 0 0 0 399 74 58 397 379 99 990'

    x = [int(i) for i in input_str.split()]


def large_number(input_nums):
    if not input_nums:
        return "0"
    nums = list(map(str, input_nums))
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] + key < key + nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return ''.join(nums)

    print(large_number(x))

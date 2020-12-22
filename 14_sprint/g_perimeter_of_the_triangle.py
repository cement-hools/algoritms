def max_perimeter(arr):
    arr.sort()
    while len(arr) > 2:
        c = arr.pop()
        a = arr[-1]
        b = arr[-2]

        if c < a + b:
            perimeter = a + b + c
            return perimeter
    return -1


x = [int(i) for i in '5 3 7 2 8 3'.split()]

print(max_perimeter(x))

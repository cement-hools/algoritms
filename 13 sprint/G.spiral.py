m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
n = 1
k1 = 0
k2 = -2
n1 = len(m[0]) - 1
n2 = -n1
while n <= len(m) ** 2:
    for i in range(k1, n1):
        print(m[k1][i])

    for i in range(k1, n1 + 1):
        print(m[i][n1])

    for i in range(k2, n2, -1):
        print(m[i][])

    n += 1

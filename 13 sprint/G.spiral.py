m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(len(m)):
    for j in range(len(m[0]) - 1):
        if i == 0:
            print(m[i][j])

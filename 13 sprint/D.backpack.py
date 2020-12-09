w = 36
n = 4
enter = [
    '25 50',
    '30 40',
    '10 80',
    '2 3',
]
obj = []
obj_par = []
for i in range(n):
    obj_par = [int(j) for j in f'{i} {enter[i]}'.split()]
    obj += [tuple(obj_par)]
res = []
print(obj)
sort_obj = sorted(obj, key=lambda x: (x[1], x[2]), reverse=True)
print(sort_obj)
for i in sort_obj:
    if i[2] <= w:
        res += [i[0]]
        w -= i[2]
print(' '.join(map(str, sorted(res))))

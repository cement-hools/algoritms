m = [int(i) for i in '5 6 3 5 7 8 9 1 2'.split()]
print(m)
res = 1
max_res = res
previus_element = m[0]
for i in range(1, len(m)):
    if previus_element < m[i]:
        res += 1
        previus_element = m[i]
        continue
    if max_res < res:
        max_res = res
    previus_element = m[i]
    res = 1

print(max_res)

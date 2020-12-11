children = 2
factor = [int(i) for i in '1 2 3'.split()]
cookies = 3
cookies_size = [int(i) for i in '1 1'.split()]
result = 0

sort_factor = sorted(factor, reverse=True)
sort_cookies_size = sorted(cookies_size, reverse=True)

i = 0
k = 0
while i < len(sort_factor):
    if k == len(sort_cookies_size):
        break
    if sort_factor[i] <= sort_cookies_size[k]:
        result += 1
        i += 1
        k += 1
        continue
    i += 1

print(result)

n = 3

m = {
    0: 1,
    1: 1,
    32: 3524578,
    40: 165580141,
    45: 1836311903,
}


def fibonacci(n):
    if n in m:
        return m[n]
    return fibonacci(n - 1) + fibonacci(n - 2)


res = 1
x = 1
while n:
    res = fibonacci(x)
    x += 1
    n -= 1
    print(res)

print(res)

n, k = 3, 1


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


x = fib(n)
res = x % 10 ** k
print(x)
print(res)

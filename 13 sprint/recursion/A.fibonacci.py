n = 10

m = {
    32: 3524578,
    40: 165580141,
    45: 1836311903,
}


def fibonacci(n):
    if n in m:
        return m[n]
    if n <= 1:
        return 1
    return (fibonacci(n - 1) + fibonacci(n - 2))


print(fibonacci(n))
x = fibonacci(n)
res = x % 10 ** 1
print(res)

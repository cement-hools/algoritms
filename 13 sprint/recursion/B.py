import sys

n, k = 506277, 1
sys.setrecursionlimit(5000)

M = {0: 1, 1: 1}


def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]


x = fib(n)
res = x % 10 ** k
print(x)

def generate_ps(n, co, cc, ans):
    if (co + cc == 2 * n):
        print(ans)
        return
    if (co < n):
        generate_ps(n, co + 1, cc, ans + '(')
    if (cc < co):
        generate_ps(n, co, cc + 1, ans + ')')


n = int(input())

generate_ps(n, 0, 0, '')

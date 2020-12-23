# Кондратий ввел новый метод сортировки - Относительная сортировка.
# Идея метода следующая. С помощью образца - массива уникальных чисел,
# задается порядок. В соответствии с этим порядком и должны сортироваться числа.
# Но метод еще требует доработки. Пока не известно, как сортировать числа,
# которые не входят в образец. Так что такие числа нужно выводить в конце
# в соответствии со стандартной сортировкой.
#
# res 2 4 3 5 6 0 7 7 8 9
# II x = 2 3 1 3 2 4 6 7 9 2 19 temp = 2 1 4 3 9 6 res 2 2 2 1 4 3 3 9 6 7 19
# III res = 3 3 10 5 9 2 7 6 0 4 8 x = 3 10 5 9 2 7 6 0 8 3 4 temp = 3 10 5 9 2 7 6 0
n = 1
if n:
    x = [int(i) for i in '2 3 1 3 2 4 6 7 9 2 19'.split()]

    temple = [int(i) for i in '2 1 4 3 9 6'.split()]

    res = []
    end = []

    print(x)
    pushed = False
    j = 0

    for temp in temple:

        for i in range(len(x)):
            element = x[i]
            if element == temp:
                res.append(element)

    print(res, end, x)

    for e in x:
        if e not in res:
            end.append(e)

    print(res, end, x)

    finish = res + sorted(end)

    print(' '.join(map(str, finish)))

# Кондратий издал новый закон. Во всех списках четные числа должны стоять на четных позициях,
# а нечетные числа - на нечетных. Уже существующие списки придется пересортировать.
# В списках, которые вам достанутся, одинаковое количество четных и нечетных элементов.
# Нужно отсортировать его в соответствии с новым законом.
# Исходный порядок внутри групп четных и нечетных элементов менять нельзя.
n = 1

if n:

    x = [int(i) for i in '4 2 5 7'.split()]  # res 4 5 2 7
    x = '4 2 5 7'.split()
    x = list(map(int, x))

    res = []
    print(x)
    len_x = len(x)

    for i in range(len_x):
        if not i % 2:
            for j in range(len(x)):
                element = x[j]
                if not element % 2:
                    res += [element]
                    x.pop(j)
                    break
        else:
            for j in range(len(x)):
                element = x[j]
                if element % 2:
                    res += [element]
                    x.pop(j)
                    break

    print(res)
    print(' '.join(map(str, res)))

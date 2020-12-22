s = [int(i) for i in '5 3 7 2 8 26 -12 -30 -10 27 13 -20 -30 18'.split()]
print(s)
change = True

while change:

    change = False
    for i in range(len(s) - 1):

        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
            change = True

print(s)
print('-30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27')
print(' '.join(map(str, s)))

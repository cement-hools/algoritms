s = [int(i) for i in '1 2 3 4 '.split()]
print(s)
change = False
c = 1

for i in range(len(s)):
    change = False
    for j in range(len(s) - 1):

        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
            change = True
            c = 0
    if not change:
        break
    print(' '.join(map(str, s)))

if c:
    print(' '.join(map(str, s)))

# print(s)
# print('-30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27')
# print(' '.join(map(str, s)))

# n = input()
# s = [int(i) for i in input().split()]
#
#
# for i in range(len(s)):
#     for j in range(len(s) - i - 1):
#
#         if s[j] > s[j + 1]:
#             s[j], s[j + 1] = s[j + 1], s[j]
#     print(' '.join(map(str, s)))

n = 59
times = [
    '15 22',
    '17 20',
    '12 13',
    '21 23',
    '15 15',
    '3 23',
    '20 23',
    '7 18',
    '11 13',
    '2 16',
    '7 19',
    '1 10',
    '16 23',
    '15 17',
    '15 19',
    '12 14',
    '8 9',
    '8 17',
    '19 23',
    '12 15',
    '3 10',
    '3 8',
    '17 20',
    '20 21',
    '0 0',
    '17 21',
    '13 17',
    '2 23',
    '20 20',
    '18 19',
    '9 10',
    '7 10',
    '23 23',
    '22 22',
    '8 10',
    '4 9',
    '21 21',
    '18 22',
    '14 19',
    '19 20',
    '22 23',
    '12 22',
    '3 9',
    '15 23',
    '2 21',
    '8 8',
    '10 15',
    '13 13',
    '0 7',
    '11 19',
    '0 22',
    '2 6',
    '15 16',
    '5 8',
    '20 23',
    '18 23',
    '11 22',
    '17 20',
    '12 14',
]

lessons = []

for i in range(n):
    lessons += [tuple(float(q) for q in times[i].split())]
print(lessons)
sort_lessons = sorted(lessons, key=lambda x: (x[1], x[0]))
print(sort_lessons)
res = []
res += [sort_lessons[0]]
i = 1

previous_lesson = res[-1]
while i != (len(lessons)):
    lesson = sort_lessons[i]
    print('previous_lesson:', previous_lesson, 'lesson:', lesson)
    if lesson[0] < previous_lesson[1]:
        i += 1
        continue
    print('add', lesson)
    res += [lesson]
    previous_lesson = res[-1]
    i += 1
print(res)

print(len(res))
for i in res:
    for j in i:
        print(str(j).rstrip('0').rstrip('.'), end=' ')
    print()

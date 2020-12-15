data = [int(i) for i in '1 1 1 1 1 1'.split()]
print(data)

photo = 0
print()
while data:
    if len(data) == 1:
        print('final', data)
        break

    if data[0] == 0:
        data.pop(0)
        continue

    print(data, 'photo', photo)
    data.sort(reverse=True)

    data[0] -= 1
    data[-1] -= 1
    photo += 1

    if data[-1] == 0:
        data.pop()

print(photo)

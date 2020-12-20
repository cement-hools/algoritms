class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.maxim = []

    def push(self, item):
        self.items += [item]

        if len(self.items) == 1:
            self.maxim += [item]
            return

        if item > self.maxim[-1]:
            self.maxim += [item]
        else:
            self.maxim += [self.maxim[-1]]

    def pop(self):
        if self.items:
            self.items.pop()
            self.maxim.pop()
            return
        print('error')

    def get_max(self):

        if self.maxim:
            result = self.maxim[-1]
            return print(result)
        print(None)


a = StackMaxEffective()

a.pop()
a.pop()
a.push(4)
a.push(-5)
a.push(7)
a.pop()
a.pop()
a.get_max()
a.pop()
a.get_max()
# n = int(input())
#
# for _ in range(n):
#     com = input()
#     if com == 'get_max':
#         a.get_max()
#     elif com == 'pop':
#         a.pop()
#     else:
#         com_arg = com.split()
#         a.push(int(com_arg[1]))

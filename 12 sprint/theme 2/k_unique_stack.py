class StackSet:
    def __init__(self):
        self.items = []
        self.unique = {}

    def push(self, item):

        if not self.items:
            self.items += [item]
            self.unique[item] = 1
            return

        if not self.unique.get(item) or self.unique[item] == 0:
            self.items += [item]
            self.unique[item] = 1
            return

    def pop(self):
        if self.items:
            x = self.items.pop()
            self.unique[x] = 0
            return
        print('error')

    def peek(self):
        if self.items:
            return print(self.items[-1])
        print('error')

    def size(self):
        size = len(self.items)
        return print(size)


a = StackSet()

a.push(1)
a.pop()
a.push(2)
a.size()
a.push(1)
a.push(2)
a.pop()
a.push(2)
a.peek()
a.pop()

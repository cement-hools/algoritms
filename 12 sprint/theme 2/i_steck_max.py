class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items += [item]

    def pop(self):
        if self.items:
            self.items.pop()
        return print('error')

    def get_max(self):
        if self.items:
            result = max(self.items)
            return print(result)
        return print(None)


a = StackMax()

a.get_max()
a.pop()
a.pop()
a.pop()
a.push(10)
a.get_max()

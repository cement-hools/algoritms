class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue:
            result = self.queue[0]
            self.queue = self.queue[1:]
            return print(result)
        return print(None)

    def peek(self):
        if self.queue:
            first = self.queue[0]
            return print(first)
        return print(None)

    def size(self):
        size = len(self.queue)
        return print(size)


a = MyQueue()

a.size()
a.push(0)
a.pop()
a.push(2)
a.size()
a.push(-2)
a.pop()
a.push(8)
a.push(4)
a.push(6)

class MyQueueSized:
    def __init__(self, limit):
        self.queue = []
        self.limit = limit

    def push(self, item):
        if len(self.queue) < self.limit:
            self.queue.append(item)
            return
        return print('error')

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


a = MyQueueSized(2)

a.peek()
a.push(5)
a.push(2)
a.peek()
a.size()
a.size()
a.push(1)
a.size()

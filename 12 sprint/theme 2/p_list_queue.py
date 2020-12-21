class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None
        self.size_queue = 0

    def is_empty(self):
        return self.front is None

    # Способ добавления элемента в очередь

    def put(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            self.size_queue += 1
            return

        self.rear.next = temp
        self.rear = temp
        self.size_queue += 1

    def get(self):
        if self.is_empty():
            return print('error')

        temp = self.front
        self.front = temp.next
        self.size_queue -= 1

        if self.front is None:
            self.rear = None
        return print(str(temp.data))

    def size(self):
        ln = self.size_queue
        return print(ln)


a = Queue()

a.put(-34)
a.put(-23)
a.get()
a.size()
a.get()
a.size()
a.get()
a.get()
a.put(80)
a.size()

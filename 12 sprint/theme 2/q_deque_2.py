class MyDeque:
    def __init__(self, max_size=None):
        self.deque = []
        self.max_size = max_size

    def push_back(self, value):
        if len(self.deque) == self.max_size:
            return print('error')
        self.deque.append(value)

    def push_front(self, value):
        if len(self.deque) == self.max_size:
            return print('error')

        self.deque = [value] + self.deque

    def pop_front(self):
        if not self.deque:
            return print('error')
        result = self.deque[0]
        self.deque = self.deque[1:]
        return print(result)

    def pop_back(self):
        if not self.deque:
            return print('error')
        result = self.deque.pop()
        return print(result)


a = MyDeque(6)

# a.push_front(-201)
# a.push_back(959)
# a.push_back(102)
# a.push_front(20)
# a.pop_front()
# a.pop_back()

# push_back value – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
# push_front value – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
# pop_front – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
# pop_back – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
# value — целое число, по модулю не превосходящее 1000.
command = [
    'push_front -201',
    'push_back 959',
    'push_back 102',
    'push_front 20',
    'pop_front',
    'pop_back',
]
n = 6

# res 20, 102

for i in command:
    com = i
    if com == 'pop_front':
        a.pop_front()
    elif com == 'pop_back':
        a.pop_back()
    elif com == 'peek':
        a.peek()
    elif 'push_back' in com:
        com_arg = com.split()
        value = int(com_arg[1])
        a.push_back(value)
    else:
        com_arg = com.split()
        value = int(com_arg[1])
        a.push_front(value)

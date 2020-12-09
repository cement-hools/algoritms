# id 43788599
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items:
            return self.__items.pop()
        raise Exception('Stack is empty')


def is_int(symbol):
    try:
        int(symbol)
        return True
    except ValueError:
        return False


def polish_notation(text):
    symbols = text.split()
    stack = Stack()

    for symbol in symbols:
        if is_int(symbol):
            stack.push(int(symbol))
            continue
        operand_b = stack.pop()
        operand_a = stack.pop()
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
        }
        result = operations[symbol](operand_a, operand_b)
        stack.push(result)

    return stack.pop()


def main():
    input_text = input()
    print(polish_notation(input_text))


if __name__ == '__main__':
    main()

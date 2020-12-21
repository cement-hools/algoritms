class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    index = 0
    temp = node

    while temp:
        if temp.value == elem:
            return index
        temp = temp.next_item
        index += 1

    return -1


so = Node(7, )
sa = Node(6, so)
fr = Node(5, sa)
th = Node(4, fr)
we = Node(3, th)
tu = Node(2, we)
mo = Node(1, tu)

print(solution(mo, 2))

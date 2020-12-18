class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


so = Node(7, )
sa = Node(6, so)
fr = Node(5, sa)
th = Node(4, fr)
we = Node(3, th)
tu = Node(2, we)
mo = Node(1, tu)

print(sa.value, sa.next_item.value)


def solution(head, index):
    temp = head

    if index == 0:
        head = temp.next_item
        temp = None
        return head

    for i in range(index - 1):
        temp = temp.next_item
        if temp is None:
            break

    if temp is None:
        return head

    if temp.next_item is None:
        return head

    next = temp.next_item.next_item
    temp.next_item = None
    temp.next_item = next
    return head


a = solution(mo, 3)
# a = mo
while a.next_item is not None:
    print(a.value)
    a = a.next_item

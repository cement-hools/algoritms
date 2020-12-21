def solution(head):
    if head is None or head.next is None:
        return head
    cur = head

    def reverse_node(node):
        if node is None:
            return node
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            return node
        return reverse_node(node.prev)

    res_head = reverse_node(cur)
    return res_head

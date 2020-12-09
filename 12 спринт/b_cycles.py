# id 43717679
def hasCycle(head):
    next_element, previous_element = head, head
    while next_element and next_element.next:
        next_element = next_element.next.next
        previous_element = previous_element.next
        if next_element is previous_element:
            return True
    return False

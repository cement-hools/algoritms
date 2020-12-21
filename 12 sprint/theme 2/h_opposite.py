def solution(head):
    left = head
    right = head

    # Пройдите по списку и установите прямо
    # указатель на конец списка

    while right.next:
        right = right.next

    # Поменять местами данные левого и правого указателя
    # и двигать их навстречу друг другу
    # пока они не встретятся или не пересекаются

    while left != right and left.prev != right:
        # Поменять местами данные левого и правого указателя
        t = left.value
        left.value = right.value
        right.value = t

        # Предварительный левый указатель
        left = left.next
        # Предварительный правый указатель
        right = right.prev

    return head

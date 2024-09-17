"""

Return Nth to Last

Implement an algorithm to find the nth to last element of a singly linked list.

"""

from linked_list_class import LinkedList


def nthToLast(linked_list, n):
    first_pointer, second_pointer = linked_list.head, linked_list.head

    for _ in range(n):
        if not second_pointer:
            return None
        second_pointer = second_pointer.next

    while second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return first_pointer


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.generate(n=10, min_value=0, max_value=99)
    print(linked_list)
    print(nthToLast(linked_list=linked_list, n=3))

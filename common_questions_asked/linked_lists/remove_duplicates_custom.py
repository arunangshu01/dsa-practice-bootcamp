"""

Remove Duplicates

Write a function to remove duplicates from an unsorted linked list.

Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

"""

from linked_list_class import LinkedList


def remove_duplicates(ll):
    if ll is None:
        return None
    previous_node = None
    current_node = ll.head
    duplicates = []
    while current_node:
        if current_node.value in duplicates:
            previous_node.next = current_node.next
        else:
            duplicates.append(current_node.value)
            previous_node = current_node
        current_node = current_node.next
    return ll

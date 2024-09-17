"""

Intersection

Given two (singly) linked lists, determine if the two list intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.

"""

from linked_list_class import LinkedList, Node


def intersection(first_linked_list, second_linked_list):
    if first_linked_list.tail is not second_linked_list.tail:
        return False

    first_linked_list_length, second_linked_list_length = len(first_linked_list), len(second_linked_list)
    shorter = first_linked_list if first_linked_list_length < second_linked_list_length else second_linked_list
    longer = second_linked_list if first_linked_list_length < second_linked_list_length else first_linked_list

    difference = len(longer) - len(shorter)
    longer_node, shorter_node = longer.head, shorter.head

    for _ in range(difference):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


# Helper addition function
def addSameNode(first_linked_list, second_linked_list, value):
    temp_node = Node(value=value)
    first_linked_list.tail.next = temp_node
    first_linked_list.tail = temp_node
    second_linked_list.tail.next = temp_node
    second_linked_list.tail = temp_node


if __name__ == "__main__":
    first_linked_list = LinkedList()
    first_linked_list.generate(n=3, min_value=0, max_value=10)

    second_linked_list = LinkedList()
    second_linked_list.generate(n=4, min_value=0, max_value=10)

    addSameNode(first_linked_list=first_linked_list, second_linked_list=second_linked_list, value=11)
    addSameNode(first_linked_list=first_linked_list, second_linked_list=second_linked_list, value=14)

    print(first_linked_list)
    print(second_linked_list)

    print(intersection(first_linked_list=first_linked_list, second_linked_list=second_linked_list))

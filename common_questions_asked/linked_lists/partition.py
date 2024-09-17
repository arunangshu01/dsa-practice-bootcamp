"""

Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x.

"""

from linked_list_class import LinkedList


def partition(linked_list, x):
    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node

    if linked_list.tail.next:
        linked_list.tail.next = None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.generate(n=10, min_value=0, max_value=99)
    print(linked_list)
    partition(linked_list=linked_list, x=30)
    print(linked_list)

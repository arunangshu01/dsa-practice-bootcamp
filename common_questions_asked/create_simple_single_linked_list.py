"""

Create Simple Singly Linked List DS -

Write a code in the language of your choice to implement a singly linked list. A singly linked list has the
following properties:

    1. Each node contains a piece of data. Node class constructor  takes a value as an argument and initializes
       the value attribute of the node.

    2. Each node also holds a reference (or link) to the next node in the list. A  next attribute, initialized to None,
       which will store a reference to the next node in the list.

    3. LinkedList class constructor  takes a value as an argument and creates new node object based on Node
       class with that value.

    4. head and tail attributes of the linked list to point to the new node.

    5. A length attribute, initialized to 1, which represents the current number of nodes in the list.

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


if __name__ == "__main__":
    linked_list = LinkedList(value=10)
    print(linked_list.head.value)
    print(linked_list.tail.value)
    print(linked_list.length)

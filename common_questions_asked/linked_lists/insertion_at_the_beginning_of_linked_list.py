"""

Insertion at the Beginning of a Singly Linked List

Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are
already provided.

Note: Function name must be prepend

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Implement Here
    def prepend(self, value):
        new_node = Node(value=value)
        if self.length == 0 or not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.prepend(value=10)
    linked_list.prepend(value=20)
    linked_list.prepend(value=30)
    linked_list.prepend(value=40)


"""

Implement a Circular Singly Linked List -

Create a circular singly linked list with methods to insert a new node at the beginning, end, and print to display the list.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            if current_node.next is self.head:
                break
            current_node = current_node.next
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


if __name__ == "__main__":
    cs_linked_list = CSLinkedList()
    cs_linked_list.append(value=10)
    cs_linked_list.append(value=20)
    cs_linked_list.prepend(value=30)
    cs_linked_list.prepend(value=40)
    print(cs_linked_list)


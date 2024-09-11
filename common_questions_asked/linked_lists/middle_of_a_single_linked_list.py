"""

Middle of a Singly Linked List -

Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes,
return the second of the two middle nodes.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        slow_node, fast_node = self.head, self.head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(value=10)
    linked_list.append(value=20)
    linked_list.append(value=30)
    linked_list.append(value=40)
    linked_list.append(value=50)

    print(linked_list.find_middle())

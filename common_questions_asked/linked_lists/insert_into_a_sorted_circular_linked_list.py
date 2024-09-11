"""

Insert into a Sorted Circular Linked List -

Write a function to insert a new node into a sorted circular linked list.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def insert_into_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        elif data <= self.head.data:
            self.prepend(data)
        else:
            current_node = self.head
            while current_node.next != self.head and current_node.next.data < data:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node


if __name__ == "__main__":
    cs_linked_list = CircularLinkedList()
    cs_linked_list.append(data=10)
    cs_linked_list.append(data=20)
    cs_linked_list.prepend(data=30)
    cs_linked_list.prepend(data=40)
    cs_linked_list.insert_into_sorted(data=50)
    cs_linked_list.insert_into_sorted(data=60)
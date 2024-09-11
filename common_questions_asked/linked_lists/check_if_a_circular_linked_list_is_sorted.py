"""

Check if a Circular Linked List is Sorted -

Implement a function to check if the circular linked list is sorted in ascending order.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        if self.head is None or self.head == self.tail:
            return True
        current_node = self.head
        while current_node.next is not self.head:
            if current_node.data > current_node.next.data:
                return False
            current_node = current_node.next
        return True


if __name__ == "__main__":
    cs_linked_list = CircularLinkedList()
    cs_linked_list.append(data=10)
    cs_linked_list.append(data=20)
    cs_linked_list.append(data=30)
    cs_linked_list.append(data=40)
    cs_linked_list.print_list()
    is_sorted = cs_linked_list.is_sorted()
    print(is_sorted)

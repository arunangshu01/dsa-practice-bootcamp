"""

Count the Number of Nodes -

Add a method to count the number of nodes in the circular singly linked list.

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
            self.tail.next = self.head
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def count_nodes(self):
        return self.length


if __name__ == "__main__":
    cs_linked_list = CSLinkedList()
    cs_linked_list.append(value=10)
    cs_linked_list.append(value=20)
    cs_linked_list.prepend(value=30)
    cs_linked_list.prepend(value=40)
    cs_linked_list.insert(index=2, value=50)
    cs_linked_list.insert(index=4, value=60)
    count_nodes = cs_linked_list.count_nodes()
    print(count_nodes)

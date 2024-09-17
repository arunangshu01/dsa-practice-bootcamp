"""

Create a Custom Linked List Class

"""


from random import randint


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        current_node = self.head
        while current_node:
            result += 1
            current_node = current_node.next
        return result

    def add(self, value):
        if not self.head:
            new_node = Node(value=value)
            self.head = self.tail = new_node
        else:
            self.tail.next = Node(value=value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(value=randint(min_value, max_value))
        return self


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.generate(n=10, min_value=0, max_value=99)
    print(linked_list)
    print(len(linked_list))

"""

Deletion from a Singly Linked List -

Write a function to delete a node from a singly linked list and return deleted_node. The function should take the
index(starting from 0) of the node to be deleted as a parameter.

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

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if self.length == 1:
            deleted_node = self.head
        elif index == 0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
        elif index == (self.length - 1) or index == -1:
            deleted_node = self.tail
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        else:
            previous_node = self.head
            for _ in range(index - 1):
                previous_node = previous_node.next
            deleted_node = previous_node.next
            previous_node.next = deleted_node.next
            deleted_node.next = None
        self.length -= 1
        return deleted_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(value=10)
    linked_list.append(value=20)
    linked_list.append(value=30)
    linked_list.append(value=40)

    print(linked_list.remove(index=0))
    print(linked_list.remove(index=2))
    print(linked_list.remove(index=1))

    print(linked_list)

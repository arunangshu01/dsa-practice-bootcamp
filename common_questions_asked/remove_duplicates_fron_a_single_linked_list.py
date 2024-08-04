"""

Remove Duplicates from a Singly Linked List

Given a singly linked list, write a function that removes all the duplicates. use this linked list.

Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"
Result Linked List - "1 -> 2 -> 4 -> 3

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

    def remove_duplicates(self):
        if self.head is None:
            return None
        current_node, previous_node = self.head, None
        duplicate_values = []
        while current_node:
            if current_node.value in duplicate_values:
                previous_node.next = current_node.next
                current_node.next = None
            else:
                duplicate_values.append(current_node.value)
                previous_node = current_node
            current_node = previous_node.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(value=10)
    linked_list.append(value=20)
    linked_list.append(value=30)
    linked_list.append(value=40)
    linked_list.append(value=50)
    linked_list.append(value=40)
    linked_list.append(value=50)
    linked_list.append(value=60)

    print(linked_list)

    linked_list.remove_duplicates()

    print(linked_list)

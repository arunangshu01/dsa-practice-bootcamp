"""

Reverse a Singly Linked List -

Write a function to reverse a singly linked list. The function should reverse the original linked list.

Example:
    Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5
    Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1

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

    def reverse(self):
        previous_node, current_node, next_node = None, self.head, None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(value=10)
    linked_list.append(value=20)
    linked_list.append(value=30)
    linked_list.append(value=40)
    linked_list.reverse()

    print(linked_list)

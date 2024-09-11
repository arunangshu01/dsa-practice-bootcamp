"""

Delete a Node from a Circular Singly Linked List -

Implement a method in the CircularLinkedList class to delete a node by value.

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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
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
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def delete_by_value(self, value):
        if self.length == 0:
            return False
        elif self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        else:
            previous_node = None
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    if current_node == self.head:
                        self.head = self.head.next
                        self.tail = self.head
                    else:
                        previous_node.next = current_node.next
                        if current_node == self.tail:
                            self.tail = previous_node
                    self.length -= 1
                    return True
                previous_node = current_node
                current_node = current_node.next
                if current_node == self.head:
                    break
            return False


if __name__ == "__main__":
    cs_linked_list = CSLinkedList()
    cs_linked_list.append(value=10)
    cs_linked_list.append(value=20)
    cs_linked_list.append(value=30)
    cs_linked_list.append(value=40)
    cs_linked_list.append(value=50)
    cs_linked_list.append(value=60)
    result1 = cs_linked_list.delete_by_value(value=40)
    result2 = cs_linked_list.delete_by_value(value=100)
    print(result1)
    print(result2)

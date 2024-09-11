"""

Split a Circular Linked List into Two Equal Halves -

Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list.

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

    def split_list(self):
        if self.length == 0:
            return None, None
        elif self.length == 1:
            return self.head, None
        mid_index = (self.length + 1) // 2
        count = 1
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        current_node = self.head
        last_first_list = None
        while count <= mid_index:
            first_list.append(current_node)
            last_first_list = current_node
            current_node = current_node.next
            count += 1
        if last_first_list:
            first_list.tail = last_first_list
            first_list.tail.next = self.head
        while current_node != self.head:
            second_list.append(current_node)
            current_node = current_node.next
        if second_list.length > 0:
            second_list.tail = self.tail
            second_list.tail.next = second_list.head
        return first_list, second_list


if __name__ == "__main__":
    cs_linked_list = CSLinkedList()
    cs_linked_list.append(value=10)
    cs_linked_list.append(value=20)
    cs_linked_list.append(value=30)
    cs_linked_list.append(value=40)
    cs_linked_list.append(value=50)
    cs_linked_list.append(value=60)
    first_list, second_list = cs_linked_list.split_list()
    print(first_list)
    print(second_list)

class CircularDoubleNode:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        result = str(self.value)
        return result


class CircularDoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node.next is self.head:
                break
            result += ' <-> '
        return result

    def insert_at_the_beginning(self, value):
        new_node = CircularDoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
        return

    def insert_at_the_end(self, value):
        new_node = CircularDoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
        return

    def traverse_the_list_from_the_beginning(self):
        current_node = self.head
        while current_node:
            print(current_node.next)
            current_node = current_node.next
            if current_node is self.head:
                break

    def traverse_the_list_from_the_end(self):
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev
            if current_node is self.tail:
                break

    def search_in_the_linked_list_by_index(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        elif index < -1:
            raise IndexError("Index is less than 0.")
        elif index >= self.length:
            raise IndexError("Index is out of bounds.")
        elif index == 0:
            searched_node = self.head
            return searched_node, index
        elif index == (self.length - 1):
            searched_node = self.tail
            return searched_node, index
        else:
            searched_node, i = self.head, 0
            while i < index:
                searched_node = searched_node.next
                i += 1
                if searched_node is self.head:
                    break
            return searched_node, i

    def search_in_the_linked_list_by_value(self, value):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        else:
            searched_node, index = self.head, 0
            while searched_node:
                if searched_node.value == value:
                    return searched_node, index
                searched_node = searched_node.next
                index += 1
                if searched_node is self.head:
                    break
            raise ValueError(f"The Node Value: {value} is not present in the Linked List.")

    def get_node(self, index):
        if self.length == 0 or (not self.head and self.tail):
            raise ValueError("There is no element in the Linked List.")
        elif index < -1:
            raise IndexError("Index is less than 0.")
        elif index >= self.length:
            raise IndexError("Index is out of bounds.")
        elif index == 0:
            fetched_node = self.head
            return fetched_node
        elif index == (self.length - 1) or index == -1:
            fetched_node = self.tail
            return fetched_node
        elif 1 <= index < (self.length // 2):
            fetched_node = self.head
            for _ in range(index):
                fetched_node = fetched_node.next
            return fetched_node
        elif (self.length // 2) <= index < (self.length - 1):
            fetched_node = self.tail
            for _ in range((self.length - 1), index, -1):
                fetched_node = fetched_node.prev
            return fetched_node

    def set_node(self, index, value):
        node_to_set = self.get_node(index=index)
        while node_to_set:
            node_to_set.value = value

    def insert_at_anywhere(self, index, value):
        new_node = CircularDoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.length += 1
            return
        elif index < 0:
            raise IndexError("Index is less than 0.")
        elif index > self.length:
            raise IndexError("Index is out of bounds.")
        elif index == 0:
            self.insert_at_the_beginning(value=value)
        elif index == self.length:
            self.insert_at_the_end(value=value)
        else:
            temp_node = self.get_node(index=(index - 1))
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
            self.length += 1
            return

    def delete_from_beginning(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node

    def delete_from_end(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node

    def delete_from_anywhere(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        elif self.length == 1:
            popped_node = self.head
            self.head = self.tail = None
            self.length -= 1
            return popped_node
        elif index < -1:
            raise IndexError("Index is less than 0.")
        elif index >= self.length:
            raise IndexError("Index is out of bounds.")
        elif index == 0:
            popped_node = self.delete_from_beginning()
            return popped_node
        elif index == (self.length - 1) or index == -1:
            popped_node = self.delete_from_end()
            return popped_node
        else:
            popped_node = self.get_node(index=index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.length -= 1
            return popped_node

    def delete_all_nodes(self):
        self.head = self.tail = None
        self.length = 0


if __name__ == "__main__":
    pass


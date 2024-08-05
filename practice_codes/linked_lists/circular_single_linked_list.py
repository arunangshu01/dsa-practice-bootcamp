class CircularSingleNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = str(self.value)
        return result


class CircularSingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            if current_node.next is self.head:
                break
            result += ' -> '
            current_node = current_node.next
        return result

    def insert_at_the_beginning(self, value):
        new_node = CircularSingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
        return

    def insert_at_the_end(self, value):
        new_node = CircularSingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1
        return

    def insert_at_anywhere(self, index, value):
        new_node = CircularSingleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            self.tail.next = self.head
            self.length += 1
            return
        elif index < 0:
            raise IndexError("Index is less than 0.")
        elif index > self.length:
            raise IndexError("index is out of bounds.")
        elif index == 0:
            self.insert_at_the_beginning(value=value)
        elif index == self.length:
            self.insert_at_the_end(value=value)
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            return

    def traverse_the_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next
            if current_node.next is self.head:
                break

    def search_in_the_linked_list_by_index(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif index < -1:
            raise IndexError("Index is less than 0.")
        elif index >= self.length:
            raise IndexError("Index is out of bounds.")
        elif index == 0:
            searched_node = self.head
            return searched_node.value, index
        elif index == (self.length - 1) or index == -1:
            searched_node = self.tail
            return searched_node.value, index
        else:
            searched_node, i = self.head, 0
            while i < index:
                searched_node = searched_node.next
                i += 1
                if searched_node is self.head:
                    break
            return searched_node.value, i

    def search_in_the_linked_list_by_value(self, value):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        else:
            searched_node, index = self.head, 0
            while searched_node:
                if searched_node.value == value:
                    return searched_node.value, index
                searched_node = searched_node.next
                index += 1
                if searched_node is self.head:
                    break
            raise ValueError(f"The Node Value: {value} is not present in the Linked List.")

    def get_node(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif index < -1:
            raise ValueError("Index is less than 0.")
        elif index >= self.length:
            raise ValueError("Index is out of bounds.")
        elif index == 0:
            fetched_node = self.head
            return fetched_node
        elif index == (self.length - 1) or index == -1:
            fetched_node = self.tail
            return fetched_node
        else:
            fetched_node = self.head
            for _ in range(index):
                fetched_node = fetched_node.next
            return fetched_node

    def set_node(self, index, value):
        node_to_set = self.get_node(index=index)
        if node_to_set:
            node_to_set.value = value

    def delete_from_the_beginning(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_from_the_end(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_from_anywhere(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif self.length == 1:
            popped_node = self.head
            self.head = self.tail = None
            return popped_node
        elif index < -1:
            raise ValueError("Index is less than 0.")
        elif index >= self.length:
            raise ValueError("Index is out of bounds.")
        elif index == 0:
            popped_node = self.delete_from_the_beginning()
            return popped_node
        elif index == (self.length - 1) or index == -1:
            popped_node = self.delete_from_the_end()
            return popped_node
        else:
            previous_node = self.get_node(index=(index - 1))
            popped_node = previous_node.next
            previous_node.next = popped_node.next
            popped_node.next = None
            return popped_node

    def delete_all_nodes(self):
        self.head = self.tail = None
        self.length = 0


if __name__ == '__main__':
    try:

        circular_single_linked_list = CircularSingleLinkedList()

        circular_single_linked_list.insert_at_the_beginning(value=10)
        circular_single_linked_list.insert_at_the_beginning(value=20)
        circular_single_linked_list.insert_at_the_beginning(value=30)
        circular_single_linked_list.insert_at_the_beginning(value=40)
        circular_single_linked_list.insert_at_the_beginning(value=50)

        print(circular_single_linked_list)

        circular_single_linked_list.insert_at_the_end(value=60)
        circular_single_linked_list.insert_at_the_end(value=70)
        circular_single_linked_list.insert_at_the_end(value=80)
        circular_single_linked_list.insert_at_the_end(value=90)
        circular_single_linked_list.insert_at_the_end(value=100)

        print(circular_single_linked_list)

        circular_single_linked_list.insert_at_anywhere(index=0, value=110)
        circular_single_linked_list.insert_at_anywhere(index=1, value=120)
        circular_single_linked_list.insert_at_anywhere(index=2, value=130)
        circular_single_linked_list.insert_at_anywhere(index=3, value=140)
        circular_single_linked_list.insert_at_anywhere(index=4, value=150)

        print(circular_single_linked_list)

        circular_single_linked_list.traverse_the_linked_list()

        print(circular_single_linked_list.search_in_the_linked_list_by_index(index=5))
        print(circular_single_linked_list.search_in_the_linked_list_by_index(index=6))
        print(circular_single_linked_list.search_in_the_linked_list_by_index(index=7))

        print(circular_single_linked_list.search_in_the_linked_list_by_value(value=10))
        print(circular_single_linked_list.search_in_the_linked_list_by_value(value=110))
        print(circular_single_linked_list.search_in_the_linked_list_by_value(value=100))

        print(circular_single_linked_list.get_node(index=12))
        circular_single_linked_list.set_node(index=12, value=140)

        print(circular_single_linked_list)

        print(circular_single_linked_list.delete_from_the_beginning())
        print(circular_single_linked_list)
        print(circular_single_linked_list.delete_from_the_beginning())
        print(circular_single_linked_list)
        print(circular_single_linked_list.delete_from_the_end())
        print(circular_single_linked_list)
        print(circular_single_linked_list.delete_from_the_end())
        print(circular_single_linked_list)
        print(circular_single_linked_list.delete_from_anywhere(index=3))
        print(circular_single_linked_list)
        circular_single_linked_list.delete_all_nodes()
        print(circular_single_linked_list.delete_from_anywhere(index=5))

    except Exception as e:
        print(e.__str__())

class DoubleNode:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        result = str(self.value)
        return result


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            if current_node.next is not None:
                result += ' <-> '
            current_node = current_node.next
        return result

    def insert_at_the_beginning(self, value):
        new_node = DoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return

    def insert_at_the_end(self, value):
        new_node = DoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return

    def traverse_the_list_from_the_beginning(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def traverse_the_list_from_the_end(self):
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev

    def search_in_the_linked_list_by_index(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        elif index < -1:
            raise IndexError("Index is less than 0.")
        elif index >= self.length:
            raise Exception("Index is out of bounds.")
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
            return searched_node.value, i

    def search_in_the_linked_list_by_value(self, value):
        if self.length == 0 or (not self.head and not self.tail):
            raise ValueError("There is no element in the Linked List.")
        else:
            searched_node, index = self.head, 0
            while searched_node:
                if searched_node.value == value:
                    return searched_node.value, index
                searched_node = searched_node.next
                index += 1
            raise ValueError(f"The Node Value: {value} is not present in the Linked List.")

    def get_node(self, index):
        if self.length == 0 or (not self.head and not self.tail):
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
        node_to_set = self.get_node(index)
        if node_to_set:
            node_to_set.value = value

    def insert_at_anywhere(self, index, value):
        new_node = DoubleNode(value=value)
        if self.length == 0 or (not self.head and not self.tail):
            self.head = self.tail = new_node
            self.length += 1
            return
        elif index < 0:
            raise IndexError("Index is less than 0.")
        elif index > self.length:
            raise IndexError("Index is out of bounds")
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

    def delete_from_the_beginning(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def delete_from_the_end(self):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_from_anywhere(self, index):
        if self.length == 0 or (not self.head and not self.tail):
            raise Exception("There is no element in the Linked List.")
        elif self.length == 1:
            popped_node = self.head
            self.head = self.tail = None
            self.length -= 1
            return popped_node
        elif index < -1:
            raise Exception("Index is less than 0.")
        elif index >= self.length:
            raise Exception("Index is out of bounds.")
        elif index == 0:
            return self.delete_from_the_beginning()
        elif index == (self.length - 1) or index == -1:
            return self.delete_from_the_end()
        else:
            popped_node = self.get_node(index=index)
            popped_node.next.prev = popped_node.prev
            popped_node.prev.next = popped_node.next
            popped_node.next = None
            popped_node.prev = None
            self.length -= 1
            return popped_node

    def delete_all_nodes(self):
        self.head = self.tail = None
        self.length = 0


if __name__ == '__main__':
    try:
        double_linked_list = DoubleLinkedList()

        double_linked_list.insert_at_the_end(value=10)
        double_linked_list.insert_at_the_end(value=20)
        double_linked_list.insert_at_the_end(value=30)
        double_linked_list.insert_at_the_end(value=40)

        double_linked_list.insert_at_the_beginning(value=50)
        double_linked_list.insert_at_the_beginning(value=60)
        double_linked_list.insert_at_the_beginning(value=70)
        double_linked_list.insert_at_the_beginning(value=80)

        print(double_linked_list)

        double_linked_list.traverse_the_list_from_the_beginning()
        double_linked_list.traverse_the_list_from_the_end()

        print(double_linked_list.search_in_the_linked_list_by_index(index=0))
        print(double_linked_list.search_in_the_linked_list_by_index(index=7))
        print(double_linked_list.search_in_the_linked_list_by_index(index=-1))
        # print(double_linked_list.search_in_the_linked_list_by_index(index=99))

        print(double_linked_list.search_in_the_linked_list_by_value(value=20))
        print(double_linked_list.search_in_the_linked_list_by_value(value=80))
        print(double_linked_list.search_in_the_linked_list_by_value(value=40))
        # print(double_linked_list.search_in_the_linked_list_by_value(value=400))

        print(double_linked_list.get_node(index=-1))
        print(double_linked_list.get_node(index=0))
        print(double_linked_list.get_node(index=7))
        # print(double_linked_list.get_node(index=100))

        double_linked_list.set_node(index=-1, value=90)
        double_linked_list.set_node(index=3, value=100)
        double_linked_list.set_node(index=6, value=110)
        # double_linked_list.set_node(index=100, value=120)

        print(double_linked_list)

        # double_linked_list.insert_at_anywhere(index=-1, value=120)
        double_linked_list.insert_at_anywhere(index=0, value=130)
        double_linked_list.insert_at_anywhere(index=8, value=140)
        double_linked_list.insert_at_anywhere(index=9, value=150)
        double_linked_list.insert_at_anywhere(index=11, value=160)

        print(double_linked_list)

        print(double_linked_list.delete_from_the_beginning())
        print(double_linked_list.delete_from_the_beginning())

        print(double_linked_list)

        print(double_linked_list.delete_from_the_end())
        print(double_linked_list.delete_from_the_end())

        print(double_linked_list)

        print(double_linked_list.delete_from_anywhere(index=-1))
        print(double_linked_list.delete_from_anywhere(index=5))
        print(double_linked_list.delete_from_anywhere(index=2))

        print(double_linked_list)

        double_linked_list.delete_all_nodes()

        print(double_linked_list.delete_from_the_end())

    except Exception as e:
        print(e.__str__())

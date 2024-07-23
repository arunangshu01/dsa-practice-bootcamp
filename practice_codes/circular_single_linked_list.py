class CircularSingleNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = f"{self.value}"
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
            result += '->'
            current_node = current_node.next
        return result

    def insert_at_the_beginning(self, value):
        new_node = CircularSingleNode(value)
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
        new_node = CircularSingleNode(value)
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
        new_node = CircularSingleNode(value)
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
            self.insert_at_the_beginning(value)
        elif index == self.length:
            self.insert_at_the_end(value)
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


if __name__ == '__main__':
    try:
        circular_single_linked_list = CircularSingleLinkedList()

        circular_single_linked_list.insert_at_the_beginning(10)
        circular_single_linked_list.insert_at_the_beginning(20)
        circular_single_linked_list.insert_at_the_beginning(30)
        circular_single_linked_list.insert_at_the_beginning(40)
        circular_single_linked_list.insert_at_the_beginning(50)

        print(circular_single_linked_list)

        circular_single_linked_list.insert_at_the_end(60)
        circular_single_linked_list.insert_at_the_end(70)
        circular_single_linked_list.insert_at_the_end(80)
        circular_single_linked_list.insert_at_the_end(90)
        circular_single_linked_list.insert_at_the_end(100)

        print(circular_single_linked_list)

        circular_single_linked_list.insert_at_anywhere(0, 110)
        circular_single_linked_list.insert_at_anywhere(1, 120)
        circular_single_linked_list.insert_at_anywhere(2, 130)
        circular_single_linked_list.insert_at_anywhere(3, 140)
        circular_single_linked_list.insert_at_anywhere(4, 150)

        print(circular_single_linked_list)

        circular_single_linked_list.traverse_the_linked_list()

        print(circular_single_linked_list.search_in_the_linked_list_by_index(5))
        print(circular_single_linked_list.search_in_the_linked_list_by_index(6))
        print(circular_single_linked_list.search_in_the_linked_list_by_index(7))

        print(circular_single_linked_list.search_in_the_linked_list_by_value(10))
        print(circular_single_linked_list.search_in_the_linked_list_by_value(110))
        print(circular_single_linked_list.search_in_the_linked_list_by_value(100))
    except Exception as e:
        print(e.__str__())



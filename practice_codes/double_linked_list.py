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
                result += '<->'
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
            searched_node = self.head
            i = 0
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

    # def get_node(self, index):
    #     current_node = self.head
    #     for _ in range(index):

    #
    # def insert_at_anywhere(self, index, value):
    #     new_node = DoubleNode(value=value)
    #     if self.length == 0 or (not self.head and not self.tail):
    #         self.head = self.tail = new_node
    #     elif index < 0:
    #         raise IndexError("Index is less than 0.")
    #     elif index > self.length + 1:
    #         raise IndexError("Index is out of bounds")
    #     elif index == 0:
    #         self.insert_at_the_beginning(value=value)
    #     elif index == self.length:
    #         self.insert_at_the_end(value=value)
    #     else:
    #         current_node = self.head
    #         for _ in range(index - 1):
    #             current_node = current_node.next


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

    except Exception as e:
        print(e.__str__())

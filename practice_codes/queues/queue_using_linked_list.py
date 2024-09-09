class SingleNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = str(self.value)
        return result


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class QueueUsingLinkedList:

    def __init__(self):
        self.linked_list_queue = SingleLinkedList()

    def __str__(self):
        if self.linked_list_queue.head:
            queue_items = [str(queue_item) for queue_item in self.linked_list_queue]
            result = " ".join(queue_items)
            return result
        return "The Queue has been deleted."

    def is_queue_empty(self):
        if not self.linked_list_queue.head and not self.linked_list_queue.tail:
            return True
        return False

    def enqueue_element(self, value):
        new_node_element = SingleNode(value=value)
        if self.is_queue_empty():
            self.linked_list_queue.head = self.linked_list_queue.tail = new_node_element
        else:
            self.linked_list_queue.tail.next = new_node_element
            self.linked_list_queue.tail = new_node_element
        return f"Element Value: {new_node_element} has been enqueued in the Queue."

    def dequeue_element(self, need_print=True):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        dequeued_node_element = self.linked_list_queue.head
        if self.linked_list_queue.head == self.linked_list_queue.tail:
            self.linked_list_queue.head = self.linked_list_queue.tail = None
        else:
            self.linked_list_queue.head = self.linked_list_queue.head.next
            dequeued_node_element.next = None
        if need_print:
            print(f"The first element of value: {dequeued_node_element} has been dequeued from the Queue.")
        return dequeued_node_element

    def peek_element(self, need_print=True):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        peeked_node_element = self.linked_list_queue.head
        if need_print:
            print(f"The first element of the Queue is of value: {peeked_node_element}.")
        return peeked_node_element

    def delete_queue(self):
        self.linked_list_queue.head = self.linked_list_queue.tail = None


if __name__ == "__main__":
    try:
        queue_using_linked_list = QueueUsingLinkedList()
        print(queue_using_linked_list.enqueue_element(value=10))
        print(queue_using_linked_list.enqueue_element(value=20))
        print(queue_using_linked_list.enqueue_element(value=30))
        print(queue_using_linked_list.enqueue_element(value=40))
        print(queue_using_linked_list.enqueue_element(value=50))
        print(queue_using_linked_list.enqueue_element(value=60))
        print(queue_using_linked_list.enqueue_element(value=70))
        print(queue_using_linked_list.enqueue_element(value=80))
        print(queue_using_linked_list.enqueue_element(value=90))
        print(queue_using_linked_list.enqueue_element(value=100))
        # print(queue_using_linked_list.enqueue_element(110))

        # queue_using_linked_list.delete_queue()
        # print(queue_using_linked_list)

        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

        print(queue_using_linked_list.peek_element())
        print(queue_using_linked_list.dequeue_element())
        print(queue_using_linked_list)

    except Exception as e:
        print(e.__str__())

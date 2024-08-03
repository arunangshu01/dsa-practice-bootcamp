from typing import List


class QueueWithoutSizeLimit:

    def __init__(self):
        self.list_queue: List[int] = []

    def __str__(self):
        if self.list_queue:
            queue_items = [str(queue_item) for queue_item in self.list_queue]
            result = " ".join(queue_items)
            return result
        return "The Queue has been deleted."

    def is_queue_empty(self):
        if self.list_queue == [] or len(self.list_queue) == 0:
            return True
        return False

    def enqueue_element(self, value):
        self.list_queue.append(value)
        return f"Element Value: {value} has been enqueued in the Queue."

    def dequeue_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        dequeued_element = self.list_queue[0]
        self.list_queue.pop(0)
        return f"The first element of value: {dequeued_element} has been dequeued from the Queue."

    def peek_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        peeked_element = self.list_queue[0]
        return f"The first element of the Queue is of value: {peeked_element}."

    def delete_queue(self):
        self.list_queue = None


if __name__ == "__main__":
    try:
        queue_without_size_limit = QueueWithoutSizeLimit()
        print(queue_without_size_limit.enqueue_element(value=10))
        print(queue_without_size_limit.enqueue_element(value=20))
        print(queue_without_size_limit.enqueue_element(value=30))
        print(queue_without_size_limit.enqueue_element(value=40))
        print(queue_without_size_limit.enqueue_element(value=50))

        # queue_without_size_limit.delete_queue()
        # print(queue_without_size_limit)

        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

        print(queue_without_size_limit.peek_element())
        print(queue_without_size_limit.dequeue_element())
        print(queue_without_size_limit)

    except Exception as e:
        print(e.__str__())

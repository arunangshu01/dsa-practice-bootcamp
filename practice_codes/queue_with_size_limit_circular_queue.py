from typing import List, Optional


class QueueWithSizeLimit:

    def __init__(self, max_size):
        self.max_size = max_size
        self.list_queue: List[Optional[int]] = self.max_size * [None] 
        self.start = -1
        self.top = -1

    def __str__(self):
        if self.list_queue:
            queue_items = [str(queue_item) for queue_item in self.list_queue]
            result = " ".join(queue_items)
            return result
        return "The Queue has been deleted."

    def is_queue_empty(self):
        if self.top == -1:
            return True
        return False

    def is_queue_full(self):
        if self.top == self.start - 1 or self.top + 1 == self.start:
            return True
        elif self.start == 0 and (self.top == self.max_size - 1 or self.top + 1 == self.max_size):
            return True
        return False

    def enqueue_element(self, value):
        if self.is_queue_full():
            raise Exception("Size Limit of the Queue is exceeded. So, can't add any new element.")
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list_queue[self.top] = value
            return f"Element Value: {value} has been enqueued in the Queue."

    def dequeue_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        else:
            dequeued_element = self.list_queue[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.list_queue[start] = None
            return f"The first element of value: {dequeued_element} has been dequeued from the Queue."

    def peek_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        else:
            peeked_element = self.list_queue[self.start]
            return f"The first element of the Queue is of value: {peeked_element}."

    def delete_queue(self):
        self.list_queue = self.max_size * [None]
        self.top = -1
        self.start = -1


class CircularQueue(QueueWithSizeLimit):
    pass
        

if __name__ == "__main__":
    try:
        queue_with_size_limit = QueueWithSizeLimit(max_size=10)    # Object can be declared as instance of CircularQueue
        print(queue_with_size_limit.enqueue_element(value=10))
        print(queue_with_size_limit.enqueue_element(value=20))
        print(queue_with_size_limit.enqueue_element(value=30))
        print(queue_with_size_limit.enqueue_element(value=40))
        print(queue_with_size_limit.enqueue_element(value=50))
        print(queue_with_size_limit.enqueue_element(value=60))
        print(queue_with_size_limit.enqueue_element(value=70))
        print(queue_with_size_limit.enqueue_element(value=80))
        print(queue_with_size_limit.enqueue_element(value=90))
        print(queue_with_size_limit.enqueue_element(value=100))
        # print(queue_with_size_limit.enqueue_element(110))

        # queue_with_size_limit.delete_queue()
        # print(queue_with_size_limit)

        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

        print(queue_with_size_limit.peek_element())
        print(queue_with_size_limit.dequeue_element())
        print(queue_with_size_limit)

    except Exception as e:
        print(e.__str__())

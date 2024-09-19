"""

Queue via Stacks

Implement Queue class which implements a queue using two stacks.

"""


class Stack:

    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()


class QueueViaStack:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item=item)

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(item=self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(item=self.out_stack.pop())
        return result


if __name__ == "__main__":
    queue_via_stack = QueueViaStack()
    queue_via_stack.enqueue(item=1)
    queue_via_stack.enqueue(item=2)
    queue_via_stack.enqueue(item=3)
    print(queue_via_stack.dequeue())
    queue_via_stack.enqueue(item=4)
    print(queue_via_stack.dequeue())

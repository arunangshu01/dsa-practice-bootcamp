"""

Stack Minimum

How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1).

"""


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string


class Stack:

    def __init__(self):
        self.top = None
        self.minimum_node = None

    def min(self):
        if not self.minimum_node:
            return None
        return self.minimum_node.value

    def push(self, item):
        if self.minimum_node and (self.minimum_node.value < item):
            self.minimum_node = Node(value=self.minimum_node.value, next=self.minimum_node)
        else:
            self.minimum_node = Node(value=item, next=self.minimum_node)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minimum_node = self.minimum_node.next
        item = self.top.value
        self.top = self.top.next
        return item


if __name__ == "__main__":
    stack = Stack()
    stack.push(item=5)
    print(stack.min())
    stack.push(item=6)
    print(stack.min())
    stack.push(item=3)
    print(stack.min())
    stack.pop()
    print(stack.min())

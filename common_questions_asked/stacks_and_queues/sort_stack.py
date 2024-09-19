"""

Sort Stack

Sort a stack with the smallest on top using only a single temporary stack.

"""


class Current:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self and self.data) + ',' + str(self and self.next)


class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.top)

    def push(self, item):
        self.top = Current(data=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        item = self.top
        self.top = self.top.next
        return item.data


def sort_stack(stack):
    previous = stack.pop()
    current = stack.pop()
    temp = Stack()
    while current:
        if previous < current:
            temp.push(previous)
            previous = current
            current = stack.pop()
        else:
            temp.push(current)
            current = stack.pop()
        if not current and previous:
            temp.push(previous)
    sorted = True
    previous = temp.pop()
    current = temp.pop()
    while current:
        if previous > current:
            stack.push(previous)
            previous = current
            current = temp.pop()
        else:
            stack.push(current)
            current = temp.pop()
            sorted = False
        if not current and previous:
            stack.push(previous)
    if sorted:
        return stack
    else:
        return sort_stack(stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(item=10)
    stack.push(item=30)
    stack.push(item=70)
    stack.push(item=40)
    stack.push(item=80)
    stack.push(item=20)
    stack.push(item=90)
    stack.push(item=50)
    stack.push(item=60)
    print(stack)
    print(sort_stack(stack=stack))

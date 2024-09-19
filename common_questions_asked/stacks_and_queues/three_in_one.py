"""

Three in One

Describe how you could use a single Python list to implement three stacks.

"""


class MultiStack:

    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_list = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def is_stack_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        return False

    def is_stack_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        return False

    def index_of_top(self, stack_number):
        offset = stack_number * self.stack_size
        return offset + self.sizes[stack_number] - 1

    def push(self, item, stack_number):
        if self.is_stack_full(stack_number=stack_number):
            return "The Stack is Full"
        else:
            self.sizes[stack_number] += 1
            self.stack_list[self.index_of_top(stack_number=stack_number)] = item

    def pop(self, stack_number):
        if self.is_stack_empty(stack_number=stack_number):
            return "The Stack is Empty"
        else:
            value = self.stack_list[self.index_of_top(stack_number=stack_number)]
            self.stack_list[self.index_of_top(stack_number=stack_number)] = 0
            self.sizes[stack_number] -= 1
            return value

    def peek(self, stack_number):
        if self.is_stack_empty(stack_number=stack_number):
            return "The Stack is Empty"
        else:
            value = self.stack_list[self.index_of_top(stack_number=stack_number)]
            return value


if __name__ == "__main__":
    multi_stack = MultiStack(stack_size=6)
    print(multi_stack.is_stack_full(stack_number=0))
    print(multi_stack.is_stack_empty(stack_number=1))
    multi_stack.push(item=1, stack_number=0)
    multi_stack.push(item=2, stack_number=0)
    multi_stack.push(item=3, stack_number=2)
    print(multi_stack.peek(stack_number=1))
    print(multi_stack.peek(stack_number=0))
    print(multi_stack.pop(stack_number=0))


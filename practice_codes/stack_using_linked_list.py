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

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class StackUsingLinkedList:

    def __init__(self):
        self.linked_list_stack = SingleLinkedList()

    def __str__(self):
        if self.linked_list_stack.head:
            stack_items = [str(stack_item.value) for stack_item in self.linked_list_stack]
            result = "\n".join(stack_items)
            return result
        return "The Stack has been deleted."

    def is_stack_empty(self):
        if not self.linked_list_stack.head:
            return True
        return False

    def push_element(self, value):
        new_node_element = SingleNode(value=value)
        if self.is_stack_empty():
            self.linked_list_stack.head = new_node_element
        else:
            new_node_element.next = self.linked_list_stack.head
            self.linked_list_stack.head = new_node_element
        return f"Element Value: {new_node_element} is being pushed into the Stack."

    def pop_element(self):
        if self.is_stack_empty():
            raise Exception("There is no element in the Stack.")
        else:
            popped_node_element = self.linked_list_stack.head
            self.linked_list_stack.head = popped_node_element.next
            popped_node_element.next = None
        return f"The last element of value: {popped_node_element} has been popped out of the Stack."

    def peek_element(self):
        if self.is_stack_empty():
            raise Exception("There is no element in the Stack.")
        else:
            peeked_node_element = self.linked_list_stack.head
        return f"The last element of the Stack is of value: {peeked_node_element}."

    def delete_stack(self):
        self.linked_list_stack.head = None


if __name__ == "__main__":
    try:
        stack_using_linked_list = StackUsingLinkedList()
        print(stack_using_linked_list.push_element(10))
        print(stack_using_linked_list.push_element(20))
        print(stack_using_linked_list.push_element(30))
        print(stack_using_linked_list.push_element(40))
        print(stack_using_linked_list.push_element(50))
        print(stack_using_linked_list.push_element(60))
        print(stack_using_linked_list.push_element(70))
        print(stack_using_linked_list.push_element(80))
        print(stack_using_linked_list.push_element(90))
        print(stack_using_linked_list.push_element(100))
        # print(stack_using_linked_list.push_element(110))

        # stack_using_linked_list.delete_stack()
        # print(stack_using_linked_list)

        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

        print(stack_using_linked_list.peek_element())
        print(stack_using_linked_list.pop_element())
        print(stack_using_linked_list)

    except Exception as e:
        print(e.__str__())

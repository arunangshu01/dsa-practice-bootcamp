from typing import Any


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
        return None

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
        return

    def dequeue_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        dequeued_node_element = self.linked_list_queue.head
        if self.linked_list_queue.head == self.linked_list_queue.tail:
            self.linked_list_queue.head = self.linked_list_queue.tail = None
        else:
            self.linked_list_queue.head = self.linked_list_queue.head.next
            dequeued_node_element.next = None
        return dequeued_node_element

    def peek_element(self):
        if self.is_queue_empty():
            raise Exception("There is no element in the Queue.")
        peeked_node_element = self.linked_list_queue.head
        return peeked_node_element

    def delete_queue(self):
        self.linked_list_queue.head = self.linked_list_queue.tail = None


class BinaryTreeNodeUsingLinkedList:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal_of_binary_tree(root_node=root_node.left_child)
    pre_order_traversal_of_binary_tree(root_node=root_node.right_child)


def in_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    in_order_traversal_of_binary_tree(root_node=root_node.left_child)
    print(root_node.data)
    in_order_traversal_of_binary_tree(root_node=root_node.right_child)


def post_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    post_order_traversal_of_binary_tree(root_node=root_node.left_child)
    post_order_traversal_of_binary_tree(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    else:
        queue_for_binary_tree = QueueUsingLinkedList()
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element()
            print(root.value.data)
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)


def search_in_binary_tree(root_node: BinaryTreeNodeUsingLinkedList, node_value: Any):
    if not root_node:
        return
    else:
        queue_for_binary_tree = QueueUsingLinkedList()
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element()
            if root.value.data == node_value:
                return f"The Node with value: {root.value.data} is present in the Binary Tree."
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)
        raise ValueError(f"The Node with value: {node_value} is not present in the Binary Tree.")


def insert_node_in_binary_tree(root_node: BinaryTreeNodeUsingLinkedList, new_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        root_node = new_node
        return f"The Node with value: {root_node.data} is inserted into the Binary Tree."
    else:
        queue_for_binary_tree = QueueUsingLinkedList()
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element()
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            else:
                root.value.left_child = new_node
                return f"The Node with value: {new_node.data} is inserted into the Binary Tree."
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)
            else:
                root.value.right_child = new_node
                return f"The Node with value: {new_node.data} is inserted into the Binary Tree."


if __name__ == "__main__":
    try:
        binary_tree_using_linked_list = BinaryTreeNodeUsingLinkedList(data="Drinks")
        left_child, right_child = BinaryTreeNodeUsingLinkedList(data="Hot"), BinaryTreeNodeUsingLinkedList(data="Cold")
        binary_tree_using_linked_list.left_child, binary_tree_using_linked_list.right_child = left_child, right_child

        left_child_of_left_child, right_child_of_left_child = BinaryTreeNodeUsingLinkedList(data="Tea"), BinaryTreeNodeUsingLinkedList(data="Coffee")
        left_child.left_child, left_child.right_child = left_child_of_left_child, right_child_of_left_child

        left_child_of_right_child, right_child_of_right_child = BinaryTreeNodeUsingLinkedList(data="Cola"), BinaryTreeNodeUsingLinkedList(data="Fanta")
        print(insert_node_in_binary_tree(binary_tree_using_linked_list, left_child_of_right_child))
        print(insert_node_in_binary_tree(binary_tree_using_linked_list,  right_child_of_right_child))

        print("Pre-Order Traversal of the Binary Tree:")
        pre_order_traversal_of_binary_tree(root_node=binary_tree_using_linked_list)
        print("\nIn-Order Traversal of the Binary Tree:")
        in_order_traversal_of_binary_tree(root_node=binary_tree_using_linked_list)
        print("\nPost-Order Traversal of the Binary Tree:")
        post_order_traversal_of_binary_tree(root_node=binary_tree_using_linked_list)
        print("\nLevel-Order Traversal of the Binary Tree:")
        level_order_traversal_of_binary_tree(root_node=binary_tree_using_linked_list)
        print("\nSearching a Node in Binary Tree:")
        print(search_in_binary_tree(root_node=binary_tree_using_linked_list, node_value="Cola"))
    except Exception as e:
        print(e.__str__())

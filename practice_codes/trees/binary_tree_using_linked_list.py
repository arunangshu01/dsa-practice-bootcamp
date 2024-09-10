from typing import Any, AnyStr
from practice_codes.queues.queue_using_linked_list import QueueUsingLinkedList


class BinaryTreeNodeUsingLinkedList:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    print(root_node.data)
    pre_order_traversal_of_binary_tree(root_node=root_node.left_child)
    pre_order_traversal_of_binary_tree(root_node=root_node.right_child)


def in_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    in_order_traversal_of_binary_tree(root_node=root_node.left_child)
    print(root_node.data)
    in_order_traversal_of_binary_tree(root_node=root_node.right_child)


def post_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    post_order_traversal_of_binary_tree(root_node=root_node.left_child)
    post_order_traversal_of_binary_tree(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    else:
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
            print(root.value.data)
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)


def search_in_binary_tree(root_node: BinaryTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return "There is no root node in the Binary Tree."
    else:
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
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
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
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


def get_deepest_node_in_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    else:
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)
        deepest_node = root.value
        return deepest_node


def delete_deepest_node_from_binary_tree(root_node: BinaryTreeNodeUsingLinkedList, deepest_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Tree."
    else:
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
            if root.value is deepest_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is deepest_node:
                    root.value.right_child = None
                    return
                else:
                    queue_for_binary_tree.enqueue_element(value=root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is deepest_node:
                    root.value.left_child = None
                    return
                else:
                    queue_for_binary_tree.enqueue_element(value=root.value.left_child)


def delete_node_from_binary_tree(root_node: BinaryTreeNodeUsingLinkedList, node: Any | AnyStr):
    if not root_node:
        return "There is no root node in the Binary Tree."
    else:
        queue_for_binary_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_tree.enqueue_element(value=root_node)
        while not queue_for_binary_tree.is_queue_empty():
            root = queue_for_binary_tree.dequeue_element(need_print=False)
            if root.value.data == node:
                deepest_node = get_deepest_node_in_binary_tree(root_node=root_node)
                root.value.data = deepest_node.data
                delete_deepest_node_from_binary_tree(root_node=root_node, deepest_node=deepest_node)
                return f"The Node with value: {node} has been successfully deleted from the Binary Tree."
            if root.value.left_child:
                queue_for_binary_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_tree.enqueue_element(value=root.value.right_child)
        raise ValueError(f"Failed to delete the node with value: {node} is not present in the Binary Tree.")


def delete_entire_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    root_node.data = root_node.left_child = root_node.right_child = None
    return "The entire Binary Tree has been deleted successfully."


if __name__ == "__main__":
    try:
        drinks = BinaryTreeNodeUsingLinkedList(data="Drinks")

        hot, cold = BinaryTreeNodeUsingLinkedList(data="Hot"), BinaryTreeNodeUsingLinkedList(data="Cold")
        print(insert_node_in_binary_tree(root_node=drinks, new_node=hot))
        print(insert_node_in_binary_tree(root_node=drinks, new_node=cold))

        tea, coffee = BinaryTreeNodeUsingLinkedList(data="Tea"), BinaryTreeNodeUsingLinkedList(data="Coffee")
        print(insert_node_in_binary_tree(root_node=drinks, new_node=tea))
        print(insert_node_in_binary_tree(root_node=drinks, new_node=coffee))

        cola, fanta = BinaryTreeNodeUsingLinkedList(data="Cola"), BinaryTreeNodeUsingLinkedList(data="Fanta")
        print(insert_node_in_binary_tree(root_node=drinks, new_node=cola))
        print(insert_node_in_binary_tree(root_node=drinks, new_node=fanta))

        print("Pre-Order Traversal of the Binary Tree:")
        pre_order_traversal_of_binary_tree(root_node=drinks)

        print("\nIn-Order Traversal of the Binary Tree:")
        in_order_traversal_of_binary_tree(root_node=drinks)

        print("\nPost-Order Traversal of the Binary Tree:")
        post_order_traversal_of_binary_tree(root_node=drinks)

        print("\nLevel-Order Traversal of the Binary Tree:")
        level_order_traversal_of_binary_tree(root_node=drinks)

        print("\nSearching a Node in Binary Tree:")
        print(search_in_binary_tree(root_node=drinks, node_value="Cola"))

        deepest_node = get_deepest_node_in_binary_tree(root_node=drinks)
        print(f"\nDeepest Node in Binary Tree: {deepest_node.data}")

        delete_deepest_node_from_binary_tree(root_node=drinks, deepest_node=deepest_node)
        print("\nLevel-Order Traversal of the Binary Tree after deleting the deepest node:")
        level_order_traversal_of_binary_tree(root_node=drinks)

        print("\nDeleting a node from a Binary Tree:")
        node_to_delete = "Tea"
        print(delete_node_from_binary_tree(root_node=drinks, node=node_to_delete))

        print(f"\nLevel-Order Traversal of the Binary Tree after deleting the node with value - {node_to_delete}:")
        level_order_traversal_of_binary_tree(root_node=drinks)

        print(f"\n{delete_entire_binary_tree(root_node=drinks)}")
        print(f"\nLevel-Order Traversal of the Binary Tree after deleting it entirely:")
        level_order_traversal_of_binary_tree(root_node=drinks)

    except Exception as e:
        print(e.__str__())

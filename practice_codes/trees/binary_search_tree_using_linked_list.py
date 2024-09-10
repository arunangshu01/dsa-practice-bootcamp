from typing import Any, AnyStr
from practice_codes.queues.queue_using_linked_list import QueueUsingLinkedList


class BinarySearchTreeNodeUsingLinkedList:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node_in_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node.data:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if not root_node.left_child:
            root_node.left_child = BinarySearchTreeNodeUsingLinkedList(data=node_value)
        else:
            insert_node_in_binary_search_tree(root_node=root_node.left_child, node_value=node_value)
    else:
        if not root_node.right_child:
            root_node.right_child = BinarySearchTreeNodeUsingLinkedList(data=node_value)
        else:
            insert_node_in_binary_search_tree(root_node=root_node.right_child, node_value=node_value)
    return f"The Node with value: {node_value} has been successfully inserted in the Binary Search Tree."


def pre_order_traversal_of_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    print(root_node.data)
    pre_order_traversal_of_binary_search_tree(root_node=root_node.left_child)
    pre_order_traversal_of_binary_search_tree(root_node=root_node.right_child)


def in_order_traversal_of_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    in_order_traversal_of_binary_search_tree(root_node=root_node.left_child)
    print(root_node.data)
    in_order_traversal_of_binary_search_tree(root_node=root_node.right_child)


def post_order_traversal_of_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    post_order_traversal_of_binary_search_tree(root_node=root_node.left_child)
    post_order_traversal_of_binary_search_tree(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal_of_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    else:
        queue_for_binary_search_tree, root = QueueUsingLinkedList(), None
        queue_for_binary_search_tree.enqueue_element(value=root_node)
        while not queue_for_binary_search_tree.is_queue_empty():
            root = queue_for_binary_search_tree.dequeue_element(need_print=False)
            print(root.value.data)
            if root.value.left_child:
                queue_for_binary_search_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_binary_search_tree.enqueue_element(value=root.value.right_child)


def search_in_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    elif root_node.data == node_value:
        return f"The Node with value: {root_node.data} is is present in the Binary Search Tree."
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            return f"The Node with value: {root_node.left_child.data} is is present in the Binary Search Tree."
        else:
            return search_in_binary_search_tree(root_node=root_node.left_child, node_value=node_value)
    elif node_value > root_node.data:
        if root_node.right_child.data == node_value:
            return f"The Node with value: {root_node.right_child.data} is is present in the Binary Search Tree."
        else:
            return search_in_binary_search_tree(root_node=root_node.right_child, node_value=node_value)
    raise ValueError(f"The Node with value: {node_value} is is present in the Binary Search Tree.")


def minimum_value_node_in_binary_search_tree(binary_search_tree_node: BinarySearchTreeNodeUsingLinkedList):
    current_node = binary_search_tree_node
    while current_node.left_child:
        current_node = current_node.left_child
    return current_node


def delete_node_from_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return "There is no root node in the Binary Search Tree."
    elif node_value < root_node.data:
        root_node.left_child = delete_node_from_binary_search_tree(root_node=root_node.left_child,
                                                                   node_value=node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node_from_binary_search_tree(root_node=root_node.right_child,
                                                                    node_value=node_value)
    else:
        if not root_node.left_child:
            temp_node, root_node = root_node.right_child, None
            print(f"The Node with value: {node_value} has been successfully deleted from the Binary Tree.")
            return temp_node
        if not root_node.right_child:
            temp_node, root_node = root_node.left_child, None
            print(f"The Node with value: {node_value} has been successfully deleted from the Binary Tree.")
            return temp_node
        temp_node = minimum_value_node_in_binary_search_tree(root_node.right_child)
        root_node.data = temp_node.data
        root_node.right_child = delete_node_from_binary_search_tree(root_node.right_child, temp_node.data)
    return root_node


def delete_entire_binary_search_tree(root_node: BinarySearchTreeNodeUsingLinkedList):
    root_node.data = root_node.left_child = root_node.right_child = None
    return "The entire Binary Tree has been deleted successfully."


if __name__ == "__main__":
    try:
        binary_search_tree_using_linked_list = BinarySearchTreeNodeUsingLinkedList(data=None)

        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=70))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=50))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=90))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=30))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=60))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=80))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=100))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=20))
        print(insert_node_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=40))

        print("Pre-Order Traversal of the Binary Search Tree:")
        pre_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

        print("\nIn-Order Traversal of the Binary Search Tree:")
        in_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

        print("\nPost-Order Traversal of the Binary Search Tree:")
        post_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

        print("\nLevel-Order Traversal of the Binary Search Tree:")
        level_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

        print("\nSearching a Node in Binary Search Tree:")
        print(search_in_binary_search_tree(root_node=binary_search_tree_using_linked_list, node_value=40))

        print("\nDeleting a node from a Binary Tree:")
        node_to_delete = 100
        print(delete_node_from_binary_search_tree(root_node=binary_search_tree_using_linked_list,
                                                  node_value=node_to_delete))

        print(f"\nLevel-Order Traversal of the Binary Search Tree after deleting the node with value - {node_to_delete}:")
        level_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

        print(f"\n{delete_entire_binary_search_tree(root_node=binary_search_tree_using_linked_list)}")
        print(f"\nLevel-Order Traversal of the Binary Search Tree after deleting it entirely:")
        level_order_traversal_of_binary_search_tree(root_node=binary_search_tree_using_linked_list)

    except Exception as e:
        print(e.__str__())

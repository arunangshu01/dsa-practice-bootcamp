class BinaryTreeNodeUsingLinkedList:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal_of_binary_tree(root_node.left_child)
    pre_order_traversal_of_binary_tree(root_node.right_child)


def in_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    in_order_traversal_of_binary_tree(root_node.left_child)
    print(root_node.data)
    in_order_traversal_of_binary_tree(root_node.right_child)


def post_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    if not root_node:
        return
    post_order_traversal_of_binary_tree(root_node.left_child)
    post_order_traversal_of_binary_tree(root_node.right_child)
    print(root_node.data)


def level_order_traversal_of_binary_tree(root_node: BinaryTreeNodeUsingLinkedList):
    pass


if __name__ == "__main__":
    binary_tree_using_linked_list = BinaryTreeNodeUsingLinkedList("Drinks")
    left_child, right_child = BinaryTreeNodeUsingLinkedList("Hot"), BinaryTreeNodeUsingLinkedList("Cold")
    left_child_of_left_child, right_child_of_left_child = BinaryTreeNodeUsingLinkedList("Tea"), BinaryTreeNodeUsingLinkedList("Coffee")
    left_child_of_right_child, right_child_of_right_child = BinaryTreeNodeUsingLinkedList("Cola"), BinaryTreeNodeUsingLinkedList("Fanta")
    binary_tree_using_linked_list.left_child, binary_tree_using_linked_list.right_child = left_child, right_child
    left_child.left_child, left_child.right_child = left_child_of_left_child, right_child_of_left_child
    right_child.left_child, right_child.right_child = left_child_of_right_child, right_child_of_right_child

    print("Pre-Order Traversal of the Binary Tree:")
    pre_order_traversal_of_binary_tree(binary_tree_using_linked_list)
    print("\nIn-Order Traversal of the Binary Tree:")
    in_order_traversal_of_binary_tree(binary_tree_using_linked_list)
    print("\nPost-Order Traversal of the Binary Tree:")
    post_order_traversal_of_binary_tree(binary_tree_using_linked_list)
    print("\nLevel-Order Traversal of the Binary Tree:")

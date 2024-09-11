from typing import Any, AnyStr
from practice_codes.queues.queue_using_linked_list import QueueUsingLinkedList


class AVLTreeNodeUsingLinkedList:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def pre_order_traversal_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the AVL Tree."
    print(root_node.data)
    pre_order_traversal_of_avl_tree(root_node=root_node.left_child)
    pre_order_traversal_of_avl_tree(root_node=root_node.right_child)


def in_order_traversal_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the AVL Tree."
    in_order_traversal_of_avl_tree(root_node=root_node.left_child)
    print(root_node.data)
    in_order_traversal_of_avl_tree(root_node=root_node.right_child)


def post_order_traversal_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the AVL Tree."
    post_order_traversal_of_avl_tree(root_node=root_node.left_child)
    post_order_traversal_of_avl_tree(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        return "There is no root node in the AVL Tree."
    else:
        queue_for_avl_tree, root = QueueUsingLinkedList(), None
        queue_for_avl_tree.enqueue_element(value=root_node)
        while not queue_for_avl_tree.is_queue_empty():
            root = queue_for_avl_tree.dequeue_element(need_print=False)
            print(root.value.data)
            if root.value.left_child:
                queue_for_avl_tree.enqueue_element(value=root.value.left_child)
            if root.value.right_child:
                queue_for_avl_tree.enqueue_element(value=root.value.right_child)
      
                
def search_in_avl_tree(root_node: AVLTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return "There is no root node in the AVL Tree."
    elif root_node.data == node_value:
        return f"The Node with value: {root_node.data} is is present in the AVL Tree."
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            return f"The Node with value: {root_node.left_child.data} is is present in the AVL Tree."
        else:
            return search_in_avl_tree(root_node=root_node.left_child, node_value=node_value)
    elif node_value > root_node.data:
        if root_node.right_child.data == node_value:
            return f"The Node with value: {root_node.right_child.data} is is present in the AVL Tree."
        else:
            return search_in_avl_tree(root_node=root_node.right_child, node_value=node_value)
    raise ValueError(f"The Node with value: {node_value} is is present in the AVL Tree.")


def get_height_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        height = 0
    else:
        height = root_node.height
    return height


def rotate_to_the_right_of_avl_tree(disbalanced_node: AVLTreeNodeUsingLinkedList):
    new_root_node = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root_node.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height_of_avl_tree(root_node=disbalanced_node.left_child), get_height_of_avl_tree(root_node=disbalanced_node.right_child))
    new_root_node.height = 1 + max(get_height_of_avl_tree(root_node=new_root_node.left_child), get_height_of_avl_tree(root_node=new_root_node.right_child))
    return new_root_node


def rotate_to_the_left_of_avl_tree(disbalanced_node: AVLTreeNodeUsingLinkedList):
    new_root_node = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root_node.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height_of_avl_tree(root_node=disbalanced_node.left_child), get_height_of_avl_tree(root_node=disbalanced_node.right_child))
    new_root_node.height = 1 + max(get_height_of_avl_tree(root_node=new_root_node.left_child), get_height_of_avl_tree(root_node=new_root_node.right_child))
    return new_root_node


def get_balance_of_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node:
        balance = 0
    else:
        balance = get_height_of_avl_tree(root_node=root_node.left_child) - get_height_of_avl_tree(root_node=root_node.right_child)
    return balance


def insert_node_in_avl_tree(root_node: AVLTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return AVLTreeNodeUsingLinkedList(data=node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node_in_avl_tree(root_node=root_node.left_child, node_value=node_value)
    else:
        root_node.right_child = insert_node_in_avl_tree(root_node=root_node.right_child, node_value=node_value)
    root_node.height = 1 + max(get_height_of_avl_tree(root_node=root_node.left_child), get_height_of_avl_tree(root_node=root_node.right_child))
    balance_of_avl_tree = get_balance_of_avl_tree(root_node=root_node)
    if balance_of_avl_tree > 1 and node_value < root_node.left_child.data:
        return rotate_to_the_right_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree > 1 and node_value > root_node.left_child.data:
        root_node.left_child = rotate_to_the_left_of_avl_tree(disbalanced_node=root_node.left_child)
        return rotate_to_the_right_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree < -1 and node_value > root_node.right_child.data:
        return rotate_to_the_left_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree < -1 and node_value < root_node.right_child.data:
        root_node.right_child = rotate_to_the_right_of_avl_tree(disbalanced_node=root_node.right_child)
        return rotate_to_the_left_of_avl_tree(disbalanced_node=root_node)
    return root_node


def get_minimum_value_node_in_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    if not root_node or not root_node.left_child:
        return root_node
    return get_minimum_value_node_in_avl_tree(root_node=root_node.left_child)


def delete_node_from_avl_tree(root_node: AVLTreeNodeUsingLinkedList, node_value: Any | AnyStr):
    if not root_node:
        return root_node
    elif node_value < root_node.data:
        root_node.left_child = delete_node_from_avl_tree(root_node=root_node.left_child, node_value=node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node_from_avl_tree(root_node=root_node.right_child, node_value=node_value)
    else:
        if not root_node.left_child:
            temp_node, root_node = root_node.right_child, None
            print(f"The Node with value: {node_value} has been successfully deleted from the AVL Tree.")
            return temp_node
        elif not root_node.right_child:
            temp_node, root_node = root_node.left_child, None
            print(f"The Node with value: {node_value} has been successfully deleted from the AVL Tree.")
            return temp_node
        temp_node = get_minimum_value_node_in_avl_tree(root_node=root_node.right_child)
        root_node.data = temp_node.data
        root_node.right_child = delete_node_from_avl_tree(root_node=root_node.right_child, node_value=temp_node.data)
    balance_of_avl_tree = get_balance_of_avl_tree(root_node=root_node)
    if balance_of_avl_tree > 1 and get_balance_of_avl_tree(root_node.left_child) >= 0:
        return rotate_to_the_right_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree < -1 and get_balance_of_avl_tree(root_node=root_node.right_child) <= 0:
        return rotate_to_the_left_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree > 1 and get_balance_of_avl_tree(root_node=root_node.left_child) < 0:
        root_node.left_child = rotate_to_the_left_of_avl_tree(disbalanced_node=root_node.left_child)
        return rotate_to_the_right_of_avl_tree(disbalanced_node=root_node)
    if balance_of_avl_tree < -1 and get_balance_of_avl_tree(root_node=root_node.right_child) > 0:
        root_node.right_child = rotate_to_the_right_of_avl_tree(disbalanced_node=root_node.right_child)
        return rotate_to_the_left_of_avl_tree(disbalanced_node=root_node)
    return root_node


def delete_entire_avl_tree(root_node: AVLTreeNodeUsingLinkedList):
    root_node.data = root_node.left_child = root_node.right_child = None
    return "The AVL Tree has been deleted successfully."


if __name__ == "__main__":
    try:
        node0 = 70
        avl_tree_using_linked_list = AVLTreeNodeUsingLinkedList(data=node0)
        print(f"The Node with value: {node0} has been successfully inserted in the Binary Search Tree.")

        node1, node2, node3, node4, node5, node6, node7, node8 = 50, 90, 30, 60, 80, 100, 20, 40
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node1)
        print(f"The Node with value: {node1} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node2)
        print(f"The Node with value: {node2} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node3)
        print(f"The Node with value: {node3} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node4)
        print(f"The Node with value: {node4} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node5)
        print(f"The Node with value: {node5} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node6)
        print(f"The Node with value: {node6} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node7)
        print(f"The Node with value: {node7} has been successfully inserted in the Binary Search Tree.")
        insert_node_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=node8)
        print(f"The Node with value: {node8} has been successfully inserted in the Binary Search Tree.")

        print("Pre-Order Traversal of the AVL Tree:")
        pre_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

        print("\nIn-Order Traversal of the AVL Tree:")
        in_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

        print("\nPost-Order Traversal of the AVL Tree:")
        post_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

        print("\nLevel-Order Traversal of the AVL Tree:")
        level_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

        print("\nSearching a Node in AVL Tree:")
        print(search_in_avl_tree(root_node=avl_tree_using_linked_list, node_value=40))

        print("\nDeleting a node from a Binary Tree:")
        node_to_delete = 40
        print(delete_node_from_avl_tree(root_node=avl_tree_using_linked_list, node_value=40))

        print(f"\nLevel-Order Traversal of the AVL Tree after deleting the node with value - {node_to_delete}:")
        level_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

        print(f"\n{delete_entire_avl_tree(root_node=avl_tree_using_linked_list)}")
        print(f"\nLevel-Order Traversal of the Binary Search Tree after deleting it entirely:")
        level_order_traversal_of_avl_tree(root_node=avl_tree_using_linked_list)

    except Exception as e:
        print(e.__str__())

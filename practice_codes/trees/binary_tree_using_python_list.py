class BinaryTreeUsingPythonList:

    def __init__(self, size):
        self.max_size = size
        self.binary_tree_list = size * [None]
        self.last_index_used = 0

    def insert_node_in_binary_tree(self, node_value):
        if self.last_index_used + 1 == self.max_size:
            raise Exception("Size Limit of the Binary Tree is exceeded. So, can't add any new node.")
        self.binary_tree_list[self.last_index_used + 1] = node_value
        self.last_index_used += 1
        return f"The Node with value: {node_value} has been successfully inserted."

    def search_node_in_binary_tree(self, node_value):
        for i in range(len(self.binary_tree_list)):
            if self.binary_tree_list[i] == node_value:
                return f"The Node with value: {node_value} is present in the Binary Tree."
        raise ValueError(f"The Node with value: {node_value} is not present in the Binary Tree.")

    def pre_order_traversal_of_binary_tree(self, index):
        if self.binary_tree_list:
            if index > self.last_index_used:
                return "There is no root node in the Binary Tree."
            print(self.binary_tree_list[index])
            self.pre_order_traversal_of_binary_tree(index=(index * 2))
            self.pre_order_traversal_of_binary_tree(index=((index * 2) + 1))
        print("The Binary Tree doesn't have any node.")

    def in_order_traversal_of_binary_tree(self, index):
        if self.binary_tree_list:
            if index > self.last_index_used:
                return "There is no root node in the Binary Tree."
            self.in_order_traversal_of_binary_tree(index=(index * 2))
            print(self.binary_tree_list[index])
            self.in_order_traversal_of_binary_tree(index=((index * 2) + 1))
        print("The Binary Tree doesn't have any node.")

    def post_order_traversal_of_binary_tree(self, index):
        if self.binary_tree_list:
            if index > self.last_index_used:
                return "There is no root node in the Binary Tree."
            self.post_order_traversal_of_binary_tree(index=(index * 2))
            self.post_order_traversal_of_binary_tree(index=((index * 2) + 1))
            print(self.binary_tree_list[index])
        print("The Binary Tree doesn't have any node.")

    def level_order_traversal_of_binary_tree(self, index):
        if self.binary_tree_list:
            for i in range(index, self.last_index_used + 1):
                print(self.binary_tree_list[i])
        print("The Binary Tree doesn't have any node.")

    def delete_node_from_binary_tree(self, node_value):
        if self.last_index_used == 0:
            return "There is no root node in the Binary Tree."
        for i in range(1, self.last_index_used + 1):
            if self.binary_tree_list[i] == node_value:
                self.binary_tree_list[i] = self.binary_tree_list[self.last_index_used]
                self.binary_tree_list[self.last_index_used] = None
                self.last_index_used -= 1
                return f"The Node with value: {node_value} has been successfully deleted."

    def delete_entire_binary_tree(self):
        self.binary_tree_list = None
        return "The entire Binary Tree has been deleted successfully."


if __name__ == "__main__":
    try:
        binary_tree_using_python_list = BinaryTreeUsingPythonList(size=8)

        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Drinks"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Hot"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Cold"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Tea"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Coffee"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Cola"))
        print(binary_tree_using_python_list.insert_node_in_binary_tree(node_value="Fanta"))

        print(binary_tree_using_python_list.search_node_in_binary_tree(node_value="Hot"))
        # print(binary_tree_using_python_list.search_node_in_binary_tree(node_value="Sprite"))

        print("\nPre-Order Traversal of the Binary Tree:")
        binary_tree_using_python_list.pre_order_traversal_of_binary_tree(index=1)

        print("\nIn-Order Traversal of the Binary Tree:")
        binary_tree_using_python_list.in_order_traversal_of_binary_tree(index=1)

        print("\nPost-Order Traversal of the Binary Tree:")
        binary_tree_using_python_list.post_order_traversal_of_binary_tree(index=1)

        print("\nLevel-Order Traversal of the Binary Tree:")
        binary_tree_using_python_list.level_order_traversal_of_binary_tree(index=1)

        node_to_delete = "Hot"
        print(binary_tree_using_python_list.delete_node_from_binary_tree(node_value=node_to_delete))
        print(f"\nLevel-Order Traversal of the Binary Tree after deleting the node with value - {node_to_delete}:")
        binary_tree_using_python_list.level_order_traversal_of_binary_tree(index=1)

        print(f"\n{binary_tree_using_python_list.delete_entire_binary_tree()}")
        print(f"\nLevel-Order Traversal of the Binary Tree after deleting it entirely:")
        binary_tree_using_python_list.level_order_traversal_of_binary_tree(index=1)

    except Exception as e:
        print(e.__str__())

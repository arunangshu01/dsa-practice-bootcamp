from __future__ import annotations
from typing import List, Any


class BasicTreeNode:

    def __init__(self, data, children=None):
        if children is None:
            children: List[Any] = []
        self.data = data
        self.children = children

    def __str__(self, level=0):
        result = "  " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level=(level + 1))
        return result

    def add_child_to_the_tree(self, child_tree_node: BasicTreeNode):
        self.children.append(child_tree_node)


if __name__ == "__main__":

    drinks, hot, cold = BasicTreeNode(data="Drinks", children=[]), BasicTreeNode(data="Hot", children=[]), BasicTreeNode(data="Cold", children=[])

    drinks.add_child_to_the_tree(hot)
    drinks.add_child_to_the_tree(cold)

    print(drinks)

    tea, coffee = BasicTreeNode(data="Tea", children=[]), BasicTreeNode(data="Coffee", children=[])

    hot.add_child_to_the_tree(tea)
    hot.add_child_to_the_tree(coffee)

    print(drinks)

    cola, fanta = BasicTreeNode(data="Cola", children=[]), BasicTreeNode(data="Fanta", children=[])

    cold.add_child_to_the_tree(cola)
    cold.add_child_to_the_tree(fanta)

    print(drinks)





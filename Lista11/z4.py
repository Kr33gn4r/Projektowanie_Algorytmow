from roboty import Roboty
from z2 import BST


class BST3(BST):
    def __init__(self):
        super().__init__()

    def left_rotation(self, data, key=1):
        node = self.search_node(data, key)
        if node is None:
            return

        if node.right is None:
            return

        pivot = node.right
        node.right = pivot.left
        if pivot.left is not None:
            pivot.left.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot

        pivot.left = node
        node.parent = pivot

    def right_rotation(self, data, key=1):
        node = self.search_node(data, key)
        if node is None:
            return

        if node.left is None:
            return

        pivot = node.left
        node.left = pivot.right
        if pivot.right is not None:
            pivot.right.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot

        pivot.right = node
        node.parent = pivot


def main():
    robots = Roboty.read_robots_list_from_file('robots.csv')
    bst = BST3()
    bst.generate_binary_search_tree(robots, 1)
    bst.graph.clear()
    bst.generate_graph_helper(bst.root)
    bst.display_tree()
    bst.left_rotation(5.00)
    bst.graph.clear()
    bst.generate_graph_helper(bst.root)
    bst.display_tree()
    print(bst.root)
    bst.right_rotation(10.00)
    bst.graph.clear()
    bst.generate_graph_helper(bst.root)
    bst.display_tree()


if __name__ == '__main__':
    main()

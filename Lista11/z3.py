from roboty import Roboty
from z2 import BST
import networkx as nx
import matplotlib.pyplot as plt

class BST2(BST):
    def __init__(self):
        super().__init__()
        self.node_colors = {}
        self._current_node = None

    def visualize_tree(self):
        pos = {}
        occupied_positions = set()
        self.assign_positions(self.root, 0, 0, pos, occupied_positions)

        # plt.figure(figsize=(10, 8))
        nodes = self.graph.nodes()
        # node_colors = {}
        node_colors = []
        for node in nodes:
            if self.current_node and node == self.current_node.data[1]:
                node_colors.append('green')
                continue
            node_colors.append('lightblue')
        plt.clf()
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12,
                font_weight='bold', arrows=False)
        plt.pause(0.5)

    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        self.current_node = node
        self.inorder_traversal(node.right)
        # self.visualize_tree()

    @property
    def current_node(self):
        return self._current_node

    @current_node.setter
    def current_node(self, value):
        self._current_node = value
        self.visualize_tree()

    def preorder_traversal(self, node):
        if node is None:
            return
        self.current_node = node
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
        # self.visualize_tree()

    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        self.current_node = node
        # self.visualize_tree()

    def visualize_tree_traversal(self, traversal_method):
        plt.figure(figsize=(10, 8))
        self.current_node = None
        if traversal_method == 'inorder':
            self.inorder_traversal(self.root)
        elif traversal_method == 'preorder':
            self.preorder_traversal(self.root)
        elif traversal_method == 'postorder':
            self.postorder_traversal(self.root)
        self.visualize_tree()
        plt.axis('off')
        plt.show()


def main():
    robots = Roboty.read_robots_list_from_file('robots.csv')
    bst = BST2()
    bst.generate_binary_search_tree(robots, 1)
    bst.visualize_tree_traversal('preorder')
    # print(bst.search_node(65.25))
    # bst.display_tree()
    # bst.insert_node(('ASV', 62.25, 4, 1))
    # bst.display_tree()
    # bst.remove_node(92.82)
    # bst.display_tree()


if __name__ == '__main__':
    main()

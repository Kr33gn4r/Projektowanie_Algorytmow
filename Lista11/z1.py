import json

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.depth = 1
        self.color = 'RED'

    def __repr__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.graph = nx.Graph()

    def add_node(self, data, parent_data, is_left):
        if not self.root:
            self.root = Node(data)
        else:
            parent = self.find_node(self.root, parent_data)
            if parent:
                new_node = Node(data)
                new_node.parent = parent
                if is_left:
                    if parent.left:
                        print(f'node: {data}, zajęte miejsce (lewo), rodzic: {parent}')
                        return
                    parent.left = new_node
                else:
                    if parent.right:
                        print(f'node: {data}, zajęte miejsce (prwo), rodzic: {parent}')
                        return
                    parent.right = new_node
                self.graph.add_edge(parent, new_node)
            else:
                print("Parent node not found.")

    def find_node(self, current_node, data):
        if not current_node:
            return None
        if current_node.data == data:
            return current_node
        node = self.find_node(current_node.left, data)
        if node:
            return node
        return self.find_node(current_node.right, data)

    def assign_positions(self, node, x, y, pos, occupied_positions):
        if node is None:
            return

        if (x, y) in occupied_positions:
            x += 0.5

        pos[node] = (x, y)
        occupied_positions.add((x, y))

        self.assign_positions(node.left, x - 1, y - 1, pos, occupied_positions)
        self.assign_positions(node.right, x + 1, y - 1, pos, occupied_positions)

    def display_tree(self):
        pos = {}
        occupied_positions = set()
        self.assign_positions(self.root, 0, 0, pos, occupied_positions)

        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12,
                font_weight='bold', arrows=False)
        plt.axis('off')
        plt.show()

    def remove_node(self, data):
        if self.root and self.root.data == data:
            self.root = None
            self.graph.clear()
            return

        stack = [(self.root, None)]
        while stack:
            node, parent = stack.pop()
            if node.data == data:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                if node.left:
                    self.remove_subtree(node.left)
                if node.right:
                    self.remove_subtree(node.right)

                self.graph.remove_node(node)
                return

            if node.right:
                stack.append((node.right, node))
            if node.left:
                stack.append((node.left, node))

        node_to_remove = self.graph.nodes.get(data)
        if node_to_remove:
            self.graph.remove_node(node_to_remove)

    def remove_subtree(self, node):
        if node:
            self.remove_subtree(node.left)
            self.remove_subtree(node.right)
            self.graph.remove_node(node)


def save_tree(tree, filename):
    connections = {'root': tree.root.data}

    def build_tree_connections(node, parent=None, is_left=False):
        if node is None:
            return

        connections[node.data] = (parent.data if parent else None, is_left)
        build_tree_connections(node.left, node, True)
        build_tree_connections(node.right, node, False)

    build_tree_connections(tree.root)
    # print(connections)
    with open(filename, 'w') as file:
        json.dump(connections, file, indent=4)


def load_tree(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    def build_tree_node(node_data):
        if node_data is None:
            return None

        node = Node(node_data[0])
        node.left = build_tree_node(data.get(node_data[0]))
        node.right = build_tree_node(data.get(node_data[1]))
        return node

    tree = BinaryTree()
    root = data['root']
    tree.root = Node(root)
    # print(data)
    for key, val in data.items():
        if key == 'root':
            continue
        parent, is_left = val
        if parent is None:
            continue
        tree.add_node(int(key), int(parent), is_left)

    return tree


def main():
    tree = BinaryTree()
    tree.add_node(0, None, False)
    tree.add_node(1, 0, True)
    tree.add_node(2, 0, False)
    tree.add_node(3, 2, True)
    tree.add_node(4, 2, False)
    tree.add_node(5, 1, True)
    tree.add_node(6, 1, False)
    tree.add_node(7, 5, True)
    tree.add_node(8, 5, False)
    tree.add_node(9, 4, True)
    tree.display_tree()
    tree.add_node(10, 4, False)
    tree.display_tree()

    tree.remove_node(5)
    tree.display_tree()
    save_tree(tree, 'test.json')
    t2 = load_tree('test.json')
    t2.display_tree()

def zadanie():
    tree = BinaryTree()
    tree.add_node(0, None, False)
    tree.add_node(1, 0, True)
    tree.add_node(2, 0, False)
    tree.add_node(3, 1, True)
    tree.add_node(4, 1, False)
    tree.add_node(5, 2, True)
    tree.add_node(6, 2, False)
    tree.add_node(7, 4, True)
    tree.add_node(8, 5, True)
    tree.add_node(9, 6, True)
    tree.add_node(10, 8, False)
    tree.add_node(11, 10, True)
    tree.add_node(12, 10, False)
    tree.display_tree()

    tree.remove_node(7)
    tree.display_tree()

    tree.remove_node(2)
    tree.display_tree()


if __name__ == '__main__':
    # main()
    zadanie()

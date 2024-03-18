from roboty import Roboty
from z1 import BinaryTree, Node


class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def assign_positions(self, node, x, y, pos, occupied_positions, key=1):
        if node is None:
            return

        while (x, y) in occupied_positions:
            x += 5

        pos[node.data[key]] = (x, y)
        occupied_positions.add((x, y))
        spacing = 15 if node == self.root else 5
        self.assign_positions(node.left, x - spacing, y - 1, pos, occupied_positions, key)
        self.assign_positions(node.right, x + spacing, y - 1, pos, occupied_positions, key)

    def insert_node(self, data, key=1):
        if self.root is None:
            self.root = Node(data)
            return

        node = self.root
        new_node = Node(data)
        while True:
            if data < node.data:
                if node.left is None:
                    node.left = new_node
                    new_node.parent = node
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    new_node.parent = node
                    break
                else:
                    node = node.right
        self.graph.add_edge(new_node.data[key], new_node.parent.data[key])

    def generate_binary_search_tree(self, robots, key):
        for robot in robots:
            node = self.root
            parent = None

            while node is not None:
                # przeszukiwanie w głąb
                parent = node
                if robot[key] < node.data[key]:
                    node = node.left
                else:
                    node = node.right

            new_node = Node(robot)
            new_node.parent = parent
            if parent is None:
                self.root = new_node
                continue
            elif robot[key] < parent.data[key]:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.depth = parent.depth + 1
            self.root.parent = None
            self.graph.add_edge(parent.data[key], new_node.data[key])

    def search_node(self, data, key=1):
        # przeszukiwanie w głąb
        node = self.root
        while node is not None:
            if data == node.data[key]:
                return node
            elif data < node.data[key]:
                node = node.left
            else:
                node = node.right
        return None

    def remove_node(self, data, key=1):
        self.root = self.delete_node(self.root, data, key)
        self.graph.clear()
        self.generate_graph_helper(self.root)

    def generate_graph_helper(self, node, key=1):
        if node is None:
            return

        if node.parent is not None:
            self.graph.add_edge(node.parent.data[key], node.data[key])
        if node.left:
            self.generate_graph_helper(node.left, key)
        if node.right:
            self.generate_graph_helper(node.right, key)

    def delete_node(self, root, data, key):
        if root is None:
            return root
        if data < root.data[key]:
            root.left = self.delete_node(root.left, data, key)
            if root.left is not None:
                root.left.parent = root  # Aktualizacja parent dla lewego poddrzewa
        elif data > root.data[key]:
            root.right = self.delete_node(root.right, data, key)
            if root.right is not None:
                root.right.parent = root  # Aktualizacja parent dla prawego poddrzewa
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp
            temp = self.find_min_node(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data[key], key)
            if root.right is not None:
                root.right.parent = root  # Aktualizacja parent dla prawego poddrzewa po usunięciu węzła
        return root

    @staticmethod
    def find_min_node(node):
        current = node
        while current.left:
            current = current.left
        return current


def main():
    robots = Roboty.read_robots_list_from_file('robots.csv')
    bst = BST()
    bst.generate_binary_search_tree(robots, 1)
    print(bst.search_node(65.25))
    bst.display_tree()
    bst.insert_node(('ASV', 62.25, 4, 1))
    bst.display_tree()
    bst.remove_node(92.82)
    bst.display_tree()

def zadanie():
    robots = Roboty.read_robots_list_from_file('robots.csv')
    bst = BST()
    bst.generate_binary_search_tree(robots, 1)
    bst.display_tree()
    bst.remove_node(3.00)
    bst.display_tree()
    bst.remove_node(5.00)
    bst.display_tree()


if __name__ == '__main__':
    #main()
    zadanie()

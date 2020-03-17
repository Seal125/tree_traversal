class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

def insert_left(tree, value):
    curr = tree.left
    tree.left = Node(value)
    tree.left.left = curr
    return tree.left.value

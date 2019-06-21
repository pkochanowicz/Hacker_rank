class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val, parent=None):
        if not self.root:
            self.root = Node(val)
            return

        if not parent:
            parent = self.root

        if val < parent.info:
            if not parent.left:
                parent.left = Node(val)
            else:
                self.insert(val, parent.left)

        if val > parent.info:
            if not parent.right:
                parent.right = Node(val)
            else:
                self.insert(val, parent.right)

# Enter you code here.

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

#116
#37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3
# exp output: 37 23 108 14 31 59 111 4 17 25 34 55 86 109 115 2 6 15 22 24 27 32 35 50 56 64 94 110 114 116 1 3 5 9 16 18 26 29 33 36 46 54 57 62 65 90 105 112 7 12 20 28 30 40 48 52 58 60 63 79 88 91 97 107 113 8 10 13 19 21 38 41 47 49 51 53 61 78 81 87 89 93 95 104 106 11 39 42 66 80 82 92 96 98 44 68 83 103 43 45 67 77 84 100 74 85 99 101 69 75 102 72 76 70 73 71

def levelOrder1(root, depth=0):
    if not root:
        return
    if depth == 0:
        print(root.info, end=" ")
    if root.left:
        print(root.left.info, end=" ")
    if root.right:
        print(root.right.info, end=" ")
    levelOrder(root.left)
    levelOrder(root.right)
# Write your code here


def levelOrder(root):
    if not root:
        return
    nodes_list = []
    nodes_list.append(root)
    while nodes_list:
        current_node = nodes_list.pop()
        print(current_node.info, end=" ")
        if current_node.left:
            nodes_list.append(current_node.left)
        if current_node.right:
            nodes_list.append(current_node.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)

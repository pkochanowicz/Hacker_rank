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

top_view_position_to_node_value = {}
top_view_position_to_node_depth = {}


def topView3(root, depth = 0, top_view_position = 0):
    if not root:
        return

    #children nodes!
    topView(root.left, depth + 1, top_view_position - 1)
    topView(root.right, depth + 1, top_view_position + 1)

    #this node!
    old_depth = 99999999
    if top_view_position in top_view_position_to_node_value.keys():
        old_depth = top_view_position_to_node_depth[top_view_position]

    if depth  > old_depth:
        return

    top_view_position_to_node_value[top_view_position] = root.info
    top_view_position_to_node_depth[top_view_position] = depth

    if depth == 0:
        max_depth = max(top_view_position_to_node_depth.values())
        for printed_depth in range(max_depth):
            for pos in top_view_position_to_node_value.keys():
                if top_view_position_to_node_depth[pos] == printed_depth:
                    print(top_view_position_to_node_value[pos], end=" ")

# 50
# 47 2 40 20 38 30 14 28 10 16 19 44 39 27 7 9 31 12 43 21 5 41 34 49 13 33 3 4 25 22 29 15 32 35 6 24 23 26 1 11 42 36 37 17 18 8 45 48 50 46
#3 5 7 10 1 2 47 49 50 46 37
#47 2 49 1 50 10 46 7 5 3



answers = []
def topView2(root):
    nodes_to_visit = []
    nodes_to_visit.append([root, 0, 0])

    while len(nodes_to_visit) > 0:
        node, top_pos, level =  nodes_to_visit.pop(0)

        if not node:
            continue

        nodes_to_visit.append([node.left, top_pos - 1])
        nodes_to_visit.append([node.right, top_pos  + 1])

        if top_pos in top_view_position_to_node_value.keys():
            continue
        top_view_position_to_node_value[0] = node.info


def go_left(root):
    if not root:
        return

    go_left(root.left)
    print(root.info, end=' ')


def go_right(root):
    if not root:
        return

    print(root.info, end=' ')
    go_right(root.right)


def topView(root):
    if not root:
        return

    go_left(root.left)
    print(root.info, end=' ')
    go_right(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView2(tree.root)

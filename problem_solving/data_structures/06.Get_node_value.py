#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
    while True:
        if not llist1 and not llist2:
            return 1
        elif (llist1 and llist2) and (llist1.data == llist2.data):
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def getNode(head, positionFromTail):
    nodes = 0
    current_node = head
    while current_node:
        current_node = current_node.next
        nodes += 1
    wanted_node = nodes-positionFromTail
    for i in range(0, wanted_node-1):
        head = head.next
    return head.data


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        print(str(result) + '\n')
        # fptr.write(str(result) + '\n')

    # fptr.close()

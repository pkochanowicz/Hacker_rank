#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    inserted_node = DoublyLinkedListNode
    inserted_node.data = data

    if head is None:
        return inserted_node
    if head.data > inserted_node.data:
        inserted_node.next = head
        head.prev = inserted_node
        return inserted_node

    current_node = head
    while (current_node.next is not None) and (current_node.next.data < data):
        current_node = current_node.next
    inserted_node.next = current_node.next
    if current_node.next:
        inserted_node.next.prev = inserted_node
    current_node.next = inserted_node
    inserted_node.prev = current_node
    return head
# 1
# 3
# 2
# 3
# 4
# 1
def sortedInsert1(head, data):
    if head is None:
        head.data = data
        return head
    current_node = head
    while current_node is not None:
        if current_node.data >= data:
            inserted_node = DoublyLinkedListNode
            inserted_node.data = data
            inserted_node.prev = current_node.prev
            inserted_node.next = current_node
            current_node.prev = inserted_node
            if inserted_node.prev is None:
                return inserted_node
            else:
                inserted_node.prev.next = inserted_node
                return head
        if current_node.next is None:
            inserted_node = DoublyLinkedListNode
            inserted_node.data = data
            inserted_node.prev = current_node
            inserted_node.next = None
            current_node.next = inserted_node
            break
        current_node = current_node.next
    return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)
        print(llist1)

        # print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')

    # fptr.close()

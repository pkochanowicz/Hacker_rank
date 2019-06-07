def reverse(head):
    if head is None:
        return None
    else:
        this_node = head
        next_node = this_node.next
        this_node.next = None
        while next_node:
            next_next_node = next_node.next
            next_node.next = this_node
            head = this_node = next_node
            next_node = next_next_node
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

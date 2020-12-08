class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


def reverse_dll(head):

    # if empty or linked list with single node is passed
    if head is None or head.next is None:
        return head

    curr_node = head
    next_node = head.next

    while(next_node is not None):
        # flipping previous and next
        curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
        curr_node = next_node
        next_node = next_node.next

    # when we reach here next_node is none
    # that is node next to curr_node is none
    # which implies curr_node is the last node in the dll

    # flip for last node that is current_node
    # also put head as current_node
    curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
    head = curr_node
    return head


def nth_node_or_end(head, n):
    # returns the nth node in the dll or the last node
    # if nodes in the dll are less than n

    cnt = 1
    curr = head

    while curr.next is not None:
        if(cnt == n):
            return curr
        curr = curr.next
        cnt += 1
    return curr


def print_dll(head):

    if head is None:
        print("empty doubly linked list")

    curr = head
    print("None", end=" ")
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print("None", end=" ")
    print()


def rotate_dll_in_groups_of_k(head, k):
    ans_dll = None
    curr_head = head
    prev_node = None   # as previous node of current node is None
    nth_node = nth_node_or_end(curr_head, k)
    n1thnode = nth_node.next

    first_group = True

    while(n1thnode is not None):

        # we first sperrate the current group of dll
        # from the rest of the bigger dll
        # thereby making a smaller dll

        curr_head.prev = None
        nth_node.next = None
        n1thnode.prev = None

        # storin pointers to some node that will be used later
        # after reversal curr_head becomes the last node of the broken dll
        last_node = curr_head

        # reverse the broken dll
        new_head = reverse_dll(curr_head)

        # join the broken dll back into the bigger dll
        new_head.prev = prev_node
        if prev_node is not None:
            prev_node.next = new_head
        last_node.next = n1thnode
        if nth_node is not None:
            nth_node.prev = last_node

        # we also have to ensure that when we rotate first group
        # we update the head node of the dll
        if first_group:
            ans_dll = new_head

        # here print the dll to see how it looks and if it works as it should

        # update pointers to make them ready for next iteration
        prev_node = last_node
        curr_head = n1thnode
        nth_node = nth_node_or_end(curr_head, k)
        n1thnode = nth_node.next

    return ans_dll


# main function
if __name__ == "__main__":

    dll = DllNode('a')
    tem = DllNode('b', dll)
    tem1 = DllNode('c', tem)
    tem2 = DllNode('d', tem1)
    tem3 = DllNode('e', tem2)
    tem4 = DllNode('f', tem3)
    tem5 = DllNode('g', tem4)
    tem6 = DllNode('h', tem5)
    # assigning next values to them
    dll.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    tem3.next = tem4
    tem4.next = tem5
    tem5.next = tem6

    print("befor n node rotation")
    print_dll(dll)
    rdll = rotate_dll_in_groups_of_k(dll, 3)
    print_dll(rdll)

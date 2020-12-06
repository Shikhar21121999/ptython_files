class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def print_linked_list(head):
    # a while loop to print the linked list
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print()


def give_length(head):
    # utility function to calculate length or number of nodes in the linked list

    if head is None:
        return 0
    curr = head
    length = 0
    while(curr is not None):
        length += 1
        curr = curr.next
    return length


def copy_ll1_ll2_length(head, L, R, n):
    # A function to copy first n nodes of linked list head
    # to create n nodes of L linked list
    # and rest nodes to create R linked list

    curr_h = head.next
    curr_L = L
    L.data = head.data

    # for loop to copy data of first n nodes of linked list head to L linked list
    for _ in range(1, n):
        new_node = Node(curr_h.data)
        curr_L.next = new_node
        curr_L = new_node
        curr_h = curr_h.next

    # print_linked_list(L)

    R.data = curr_h.data
    curr_R = R
    curr_h = curr_h.next

    while(curr_h is not None):
        new_node = Node(curr_h.data)
        curr_R.next = new_node
        curr_R = new_node
        curr_h = curr_h.next

    # print_linked_list(R)
    # print_linked_list(head)


def merge_sort_for_ll(head):
    length = give_length(head)
    if length > 1:
        firs_len = length//2
        if(length % 2 == 1):
            firs_len += 1

        # make first linked list of first_len nodes and other one consisting of removing elements

        L = Node(-2)
        R = Node(-4)

        copy_ll1_ll2_length(head, L, R, firs_len)
        # print_linked_list(head)
        # print_linked_list(L)
        # print_linked_list(R)

        # now we call merge_sort_for_ll on the list L and R
        merge_sort_for_ll(L)
        merge_sort_for_ll(R)

        # after this stemp L and R would be sorted individually
        # now we have to merge them so that merged linked list is also sorted

        c1 = L    # points to the first node or head of L
        c2 = R    # points to the first node or head of R
        c_h = head  # points to the head of first linked list or head itself

        while c1 is not None and c2 is not None and c_h is not None:
            # modify the data in head node with the smaller of the two linked list

            if(c1.data <= c2.data):
                c_h.data = c1.data
                c1 = c1.next

            else:
                c_h.data = c2.data
                c2 = c2.next
            c_h = c_h.next

        # we will come out of the prev while loop if either of the linked list gets finished
        # print("after while loop c1,c2 and ch are :", c1, c2, c_h)

        # fill the rest of the list with elements of L if all the elements of R are taken
        if(c1 is not None):
            # print("taking elements in L remaining")
            while(c1 is not None and c_h is not None):
                c_h.data = c1.data
                c1 = c1.next
                c_h = c_h.next

        # fill the rest of the list with elements of R if all the elements of L are taken
        if(c2 is not None):
            # print("taking elements in R remaining")
            while(c2 is not None and c_h is not None):
                c_h.data = c2.data
                c2 = c2.next
                c_h = c_h.next

        # print_linked_list(head)


# main function
if __name__ == '__main__':

    fir_head = Node(7)
    tem = Node(6)
    tem1 = Node(5)
    tem2 = Node(4)
    tem3 = Node(3)
    tem4 = Node(2)
    tem5 = Node(1)
    fir_head.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    tem3.next = tem4
    tem4.next = tem5
    # print_linked_list(fir_head)
    merge_sort_for_ll(fir_head)
    print_linked_list(fir_head)

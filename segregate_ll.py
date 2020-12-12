class Node():
    def __init__(self, val=-9999999999999999999):
        self.data = val
        self.next = None


def print_linked_list(head):
    # a while loop to print the linked list
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print("linked list finished")


def remove_duplicates(head):
    if(head == None):
        return head
    prev = head
    curr = head.next
    if(head.next == None):
        return head
    while(curr):
        if(curr.data != prev.data):
            prev.next = curr
            prev = curr
        curr = curr.next
    # print("while loop ke baad")
    prev.next = None
    return head


def gv_intersection(first, second):
    f_c = first
    s_c = second
    hs_lis = [0]*1005
    while(f_c):
        hs_lis[f_c.data] = 1
        f_c = f_c.next
    # print("common in both are : ")
    while(s_c):
        if(hs_lis[s_c.data] == 1):
            hs_lis[s_c.data] = 2
            # print(s_c.data, end=" ")
        s_c = s_c.next
    # print()
    # print(hs_lis[3])
    ans_head = Node(-45)
    curr_ans = ans_head
    f_c = first
    while(f_c):
        # print(f_c.data, hs_lis[f_c.data])
        if(hs_lis[f_c.data] == 2):
            # print("found commoan ", f_c.data)
            if(ans_head.data == -45):
                ans_head.data = f_c.data
            else:
                new_node = Node(f_c.data)
                curr_ans.next = new_node
                curr_ans = new_node
        f_c = f_c.next
    # print_linked_list(ans_head)
    return ans_head


def segregate(head):

    # this function segregate the linked list
    # such that all the 0 comes at beginning 2 at end and 1 int themiddle

    zero_head, zero_tail, one_head, one_tail, two_head, two_tail = None, None, None, None, None, None

    # whenever we encounter first of a particular number we
    # assign that node as the first
    curr = head
    while(curr is not None):

        if curr.data == 0:

            # two possibilites
            if zero_head is None:
                # this occurs when 1 is encountered for the first time
                zero_head = zero_tail = curr

            elif zero_head is not None:
                zero_tail.next = curr
                zero_tail = curr

        elif curr.data == 1:

            # two possibilites
            if one_head is None:
                # this occurs when 1 is encountered for the first time
                one_head = one_tail = curr

            elif one_head is not None:
                one_tail.next = curr
                one_tail = curr

        elif curr.data == 2:

            # two possibilites
            if two_head is None:
                # this occurs when 1 is encountered for the first time
                two_head = two_tail = curr

            elif two_head is not None:
                two_tail.next = curr
                two_tail = curr
        curr = curr.next

    zero_tail.next = one_tail.next = two_tail.next = None

    if zero_head is None and one_head is None:
        return two_head

    if zero_head is None:
        # implies that zeros are not present
        # but ones are definitely present
        one_tail.next = two_head
        return one_head

    if one_head is None:
        # implies that one is not present
        # but zero is presnent also its possible that two may or may not be present
        zero_tail.next = two_head
        return zero_head

    if one_head is not None and zero_head is not None and two_head is not None:
        # all are presnent
        # so we connect all the smaller linked list together
        zero_tail.next = one_head
        one_tail.next = two_head
        return zero_head


# print("prgrea")
# main function
if __name__ == '__main__':

    print("inside main function")
    fir_head = Node(1)
    tem = Node(1)
    tem1 = Node(2)
    tem2 = Node(2)
    tem3 = Node(0)
    fir_head.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    print_linked_list(fir_head)
    p = segregate(fir_head)
    print_linked_list(p)

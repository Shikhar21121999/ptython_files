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


if __name__ == '__main__':

    fir_head = Node(1)
    tem = Node(2)
    tem1 = Node(3)
    tem2 = Node(4)
    tem3 = Node(5)
    fir_head.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    print_linked_list(fir_head)

    sec_head = Node(8)
    stem = Node(6)
    stem1 = Node(7)
    sec_head.next = stem
    stem.next = stem1
    print_linked_list(sec_head)

    p = gv_intersection(fir_head, sec_head)
    print_linked_list(p)

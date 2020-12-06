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


def find_middle_node(head):
    # middle node is such that
    # if odd nodes then give the middle linked list
    # if even give the second node

    length = give_length(head)

    mid_node_no = length//2
    mid_node_no += 1

    curr = head
    i = 1
    while curr is not None:
        if(i == mid_node_no):
            return curr
        curr = curr.next
        i += 1
    return Node(69)


def check_if_circular(head):

    # empty linked list is considered circular
    if head is None:
        return True

    # linked list with single node is not considered circular
    if head.next is None:
        return False

    if head.next is head:
        return True

    # traverse the whole linked list to either reach Null or reach the head again from second node
    curr = head.next
    while curr is not None:
        if(curr is head):
            return True
        curr = curr.next
    return False


# main function
if __name__ == '__main__':

    fir_head = Node(7)
    tem = Node(6)
    tem1 = Node(5)
    tem2 = Node(4)
    tem3 = Node(3)
    tem4 = Node(2)
    fir_head.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    tem3.next = tem4
    # print_linked_list(fir_head)
    print_linked_list(fir_head)
    print(find_middle_node(fir_head).data)
    print(check_if_circular(fir_head))

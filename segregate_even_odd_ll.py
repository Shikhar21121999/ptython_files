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


def segregate_even_odd_ll(head):

    # base case if linked list has only one node
    if head.next is None:
        # return the ll
        return head

    # now we first or segregate the linked list into two linked lists
    odd_head, odd_last, even_head, even_last = None, None, None, None

    curr = head

    while curr is not None:

        # two possiblities either data at curr is odd or even

        if curr.data % 2 == 1:

            # two possiblities either it is the first element for the even ll
            # or not

            if odd_head is None:
                # first element to be put in linked list
                odd_head = curr
                odd_last = curr

            elif odd_head is not None:
                odd_last.next = curr
                odd_last = curr

        if curr.data % 2 == 0:

            # two possiblities either it is the first element for the even ll
            # or not

            if even_head is None:
                # first element to be put in linked list
                even_head = curr
                even_last = curr

            elif even_head is not None:
                even_last.next = curr
                even_last = curr
        curr = curr.next

    if even_last is not None:
        even_last.next = odd_head
        if odd_last is not None:
            odd_last.next = None
        head = even_head

    else:
        head = odd_head

    return head


def create_ll(head, arr):
    curr = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        curr = new_node

    return head


# main function
if __name__ == '__main__':

    test = int(input())

    while test > 0:
        n = int(input())
        arr = list(map(int, input().split(' ')))
        head = Node(arr[0])
        fir_head = create_ll(head, arr)
        # print_linked_list(fir_head)
        p = segregate_even_odd_ll(fir_head)
        print_linked_list(p)
        test -= 1

    # fir_head = Node(12)
    # tem = Node(15)
    # tem1 = Node(10)
    # tem2 = Node(11)
    # tem3 = Node(5)
    # tem4 = Node(6)
    # tem5 = Node(2)
    # tem6 = Node(3)
    # fir_head.next = tem
    # tem.next = tem1
    # tem1.next = tem2
    # tem2.next = tem3
    # tem3.next = tem4
    # tem4.next = tem5
    # tem5.next = tem6
    # print_linked_list(fir_head)
    # p = segregate_even_odd_ll(fir_head)
    # print_linked_list(fir_head)

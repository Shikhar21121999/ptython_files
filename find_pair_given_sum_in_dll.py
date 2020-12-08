class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


def pair_sum(head, x):

    # this function checks if there exist pairs
    # in linked list head whoose sum equals x

    # set two pointers,first to the
    # beginning of dll
    # and other to the end
    first = head
    second = head

    # put second pointer to equal to the last node
    while second.next is not None:
        second = second.next

    # now first points to head and second points to the last node or tail
    ans_lis = []
    while(first.data < second.data):
        if(second.data == x-first.data):
            ans_lis.append([second.data, first.data])

        if(second.data < x-first.data):
            first = first.next

        if(second.data > x-first.data):
            second = second.prev

    return ans_lis

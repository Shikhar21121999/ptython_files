class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


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
            first = first.next
            second = second.next

        if(second.data < x-first.data):
            first = first.next

        if(second.data > x-first.data):
            second = second.prev

    return ans_lis


if __name__ == "__main__":
    print("Hello world!")

    dll = DllNode(1)
    tem = DllNode(2, dll)
    tem1 = DllNode(3, tem)
    tem2 = DllNode(4, tem1)
    tem3 = DllNode(5, tem2)
    tem4 = DllNode(6, tem3)
    tem5 = DllNode(7, tem4)
    tem6 = DllNode(8, tem5)
    tem7 = DllNode(9, tem6)
    # assigning next values to them
    dll.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    tem3.next = tem4
    tem4.next = tem5
    tem5.next = tem6
    tem6.next = tem7

    print("Dll is :", end=" ")
    print_dll(dll)
    lis = pair_sum(dll, 7)
    print(lis)

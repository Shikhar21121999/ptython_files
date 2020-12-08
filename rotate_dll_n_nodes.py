# Given a doubly linked list, rotate the linked list counter-clockwise by N nodes.
# Here N is a given positive integer and is smaller than the count of nodes in linked list.


class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


def rotate_by_n(head, n):
    nth_nodes = head
    cnt = 1
    last = head

    # traverse through last and when cnt==n store that node as nth node
    while last.next is not None:
        if cnt == n:
            nth_nodes = last
        last = last.next
        cnt += 1

    # now we first connect last node with the current head
    last.next = head
    head.prev = last

    # new head of the linked list will be n+1th node
    new_head = nth_nodes.next

    # nth node will become the last node
    nth_nodes.next = None

    # make new_head.prev None
    # and put head as new head
    new_head.prev = None
    head = new_head

    return head


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
    rdll = rotate_by_n(dll, 4)
    print_dll(rdll)

import pdb


class Node:
    def __init__(self, data=-5001551):
        self.data = data
        self.next = None

# function that prints the data in the linked list


def print_ll(head):
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print()


# functino to return length or number of nodes in the linked list
def get_len(head):
    num = 0
    curr = head
    while curr is not None:
        num += 1
        curr = curr.next
    return num

# function to reverse a linked list of nodes


def reverse(head):
    prev = None
    current = head
    while(current is not None):
        next_el = current.next
        current.next = prev
        prev = current
        current = next_el
    head = prev
    return head


def push_ll(head, value):
    if(head.data == 5001551):
        head.data = value
        return

    # traverse till the lasst nodes of linked list
    curr = head
    while curr.next is not None:
        curr = curr.next

    # add a new node to the end of the linked list and point it to None
    new_node = Node(value)
    curr.next = new_node


def is_equal(ll1, ll2):
    curr1 = ll1
    curr2 = ll2

    # data in each node of both the linked list must be same
    while(curr1 is not None and curr2 is not None):
        if(curr1.data != curr2.data):
            return False
        curr1 = curr1.next
        curr2 = curr2.next

    # both linked list must have same length
    # that is both curr1 and curr2 should be pointing to None after while loop

    if curr1 is None and curr2 is None:
        # both have same length also
        return True

    return False


def is_pallindrome_ll(ll1):
    # we split the linked list into two smaller halves
    # we reverse the second half and then compare the two linked lists
    # to see if they are equal and form a pallindrome or not

    # we first see if the linked list is odd or even
    no_nodes = get_len(ll1)

    # making first list of n//2 nodes
    node_in_one = no_nodes//2
    # print(no_nodes, node_in_one)

    curr = ll1

    for _ in range(1, node_in_one):
        curr = curr.next

    # here curr must be the last node in the firs half of the linked list
    sec = curr.next
    curr.next = None

    # sec represent the head or the second linked list

    if(no_nodes % 2 == 1):
        # if odd skip a node
        # as centre node is equal to itself
        sec = sec.next

    # print_ll(sec)
    sec = reverse(sec)
    # print_ll(ll1)
    # print_ll(sec)

    if is_equal(ll1, sec):
        return True
    else:
        return False


def create_a_ll():
    ll.data = 1
    tem = Node(2)
    tem1 = Node(3)
    tem2 = Node(2)
    tem3 = Node(1)
    # tem4 = Node(1)
    ll.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    # tem3.next = tem4


ll = Node()
create_a_ll()
# print_ll(ll)
print(is_pallindrome_ll(ll))

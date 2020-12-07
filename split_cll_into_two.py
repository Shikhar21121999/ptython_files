class Node:
    def __init__(self, data=-5):
        self.data = data
        self.next = None

# takes the head of the circular linked list and returns its length


def find_len_cll(head):
    lenght = 0
    curr = head
    while curr.next is not head:
        lenght += 1
        curr = curr.next
    lenght += 1
    return lenght


def push_cll(head, value):

    # this function takes in head node of a cll and a value
    # to which last node is appended to make a new cll with one additional node

    if(head.data == -5):
        head.data = value
        head.next = head
        return

    # if head is not none then we have to go to the last node
    # that is the one that points to this head
    # put an extra node and make that point to head

    if head.next is head:
        # create new node
        new_node = Node(value)
        head.next = new_node
        new_node.next = head
        return

    # if we reach here it means cll has more than one node
    # so we traverse the last node that is the one that points to head itself
    # and add one more node to it there

    curr = head.next
    while curr.next is not head:
        curr.next = curr

    # when we reach here the curr is the last node
    # that points to head
    new_node = Node(value)
    curr.next = new_node
    new_node.next = head


def print_cll(head):

    # if an empty circular linked list
    if head is None:
        print("empty list")

    curr = head
    while curr.next is not head:
        print(curr.data, end=" ")
        curr = curr.next
    print(curr.data, end=" ")
    print()

# function to split a parent circular into two children circular linked list


def split_cll_into_two(p_head, ll_h1, ll_h2):
    # p_head is the head of the parent linked list
    # ll_h1 is the head of the first child linked list that will be formed
    # ll_h2 is the head of the second child linked list that will be formed

    # first we find the length of the circular linked list
    # in order to determine how many nodes to put in the first child circular linked list

    cll_len = find_len_cll(p_head)
    print("length of parent list is :", cll_len)
    fir_length = cll_len//2
    print("half or length is :")

    # if odd then first circular linked list shoud have one extra
    if cll_len % 2 == 1:
        fir_length += 1

    print("nodes to be put in first linked list is ", fir_length)

    # now we know we have to put fir_length nodes in first circular linked list
    # and rest into second circular linked list

    # length of parent circular linked list is more than two

    curr_phead, curr_ll1, curr_ll2 = p_head.next, ll_h1, ll_h2

    # fill the first circular linked list
    ll_h1.data = p_head.data
    ll_h1.next = ll_h1    # insureing that child ll remains a circular linked list

    for _ in range(1, fir_length):
        new_node = Node(curr_phead.data)
        new_node.next = ll_h1
        curr_ll1.next = new_node
        curr_ll1 = new_node
        curr_phead = curr_phead.next

    print_cll(ll_h1)
    print(curr_phead.data)

    # make cll2 for the remaining nodes
    ll_h2.data = curr_phead.data
    ll_h2.next = ll_h2
    curr_phead = curr_phead.next
    while curr_phead is not p_head:
        new_node = Node(curr_phead.data)
        new_node.next = ll_h2
        curr_ll2.next = new_node
        curr_ll2 = new_node
        curr_phead = curr_phead.next

    print_cll(ll_h2)


# main function
if __name__ == '__main__':
    # firs test the insertion function for circular linked list
    # no_nodes = int(input("Enter number of nodes to be insterted"))
    # cll1 = Node()
    # for _ in range(no_nodes):
    #     data_node = int(input())
    #     push_cll(cll1, data_node)
    cll1 = Node(1)
    tem = Node(2)
    tem1 = Node(3)
    tem2 = Node(4)
    tem3 = Node(5)
    tem4 = Node(6)
    cll1.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    tem3.next = tem4
    tem4.next = cll1
    print_cll(cll1)
    ll_h1 = Node()
    ll_h2 = Node()
    split_cll_into_two(cll1, ll_h1, ll_h2)
    print_cll(cll1)
    print_cll(ll_h1)
    print_cll(ll_h2)

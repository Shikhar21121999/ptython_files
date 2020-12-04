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
    hash_lis = [0]*(10**5)
    hash_lis[prev.data] = 1
    while(curr):
        if(hash_lis[curr.data] == 0):
            prev.next = curr
            prev = curr
            hash_lis[curr.data] = 1
        curr = curr.next
    prev.next = None
    return head


def last_to_first(head):
    if(head == None or head.next == None):
        return head

    prev = curr = head
    while(curr.next):
        prev = curr
        curr = curr.next
    # curr is the last node
    # prev is the second last node
    prev.next = None
    curr.next = head
    head = curr
    return head


def addOne(head):

    # if thre is only one node
    if(head.next == None):
        if(head.data < 9):
            head.data += 1
        else:
            new_node = Node(1)
            head.next = new_node
            head.data = 0
        p = reverse(head)
        return p
    # first we reverse the current linked list using reverse()
    p = reverse(head)
    # implies there are more than one nodes in the linked list

    if(p.data < 9):
        # if first node or reversed linked list is less than 9
        # we can just increment the first node by 1
        # and return the reversed liked list
        p.data += 1
        return reverse(p)
    curr = p
    curr.data += 1
    while(curr.data > 9 and curr):
        # the data in the current node is 9 or greater than 1
        # in this case the current node data has to be made 0
        # and next nodes data will be incremented by 1
        curr.data = 0
        if(curr.next):
            # if next node exist
            curr.next.data += 1
        elif(curr.next == None):
            # if next node does not exist
            # that is current node is the last node of the linked list
            # then we add a new node with value equal to 1
            new_node = Node(1)
            curr.next = new_node
        curr = curr.next
    # now we reverse the linked list
    return reverse(p)


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


head = Node(9)
tem1 = Node(9)
tem2 = Node(9)
# tem3 = Node(5)
# tem4 = Node(6)
# tem5 = Node(7)
head.next = tem1
tem1.next = tem2
# tem2.next = tem3
# tem3.next = tem4
# tem4.next = tem5
print_linked_list(head)
q = addOne(head)
print_linked_list(q)

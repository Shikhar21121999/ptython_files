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


def linked_list_to_number(head):
    if(head == None):
        return 0
    num = head.data
    curr = head.next
    while(curr):
        num = num*10+curr.data
        curr = curr.next
    return num


def add_two_num(first, second):
    first_no = linked_list_to_number(first)
    second_no = linked_list_to_number(second)
    sum_no = first_no+second_no
    print(sum_no)

    # now we need to make a linked list for this number
    ans = Node(sum_no % 10)
    sum_no = int(sum_no/10)
    curr = ans
    while(sum_no > 0):
        last_dig = sum_no % 10

        # make a node with data equal to last digit
        new_node = Node(last_dig)
        curr.next = new_node
        curr = new_node
        sum_no = int(sum_no/10)
    # print_linked_list(ans)

    # reverse the linked list to get the right order
    return reverse(ans)


def addTwoLists(first, second):
    prev = None
    temp = None
    carry = 0

    # While both list exists
    while(first is not None or second is not None):

        # Calculate the value of next digit in
        # resultant list
        # The next digit is sum of following things
        # (i) Carry
        # (ii) Next digit of first list (if ther is a
        # next digit)
        # (iii) Next digit of second list ( if there
        # is a next digit)
        fdata = 0 if first is None else first.data
        sdata = 0 if second is None else second.data
        Sum = carry + fdata + sdata

        # update carry for next calculation
        carry = 1 if Sum >= 10 else 0

        # update sum if it is greater than 10
        Sum = Sum if Sum < 10 else Sum % 10

        # Create a new node with sum as data
        temp = Node(Sum)

        # if this is the first node then set it as head
        # of resultant list
        ans = Node(-12)
        if ans.data == -12:
            ans = temp
        else:
            prev.next = temp

        # Set prev for next insertion
        prev = temp

        # Move first and second pointers to next nodes
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next

    if carry > 0:
        temp.next = Node(carry)
    print_linked_list(ans)
    return reverse(ans)


# first linked list representing number 256
fir_head = Node(9)
tem1 = Node(4)
tem2 = Node(6)
fir_head.next = tem1
tem1.next = tem2
print_linked_list(fir_head)


sec_head = Node(5)
stem1 = Node(7)
stem2 = Node(1)
sec_head.next = stem1
stem1.next = stem2
print_linked_list(sec_head)

# q = add_two_num(fir_head, sec_head)
print_linked_list(addTwoLists(fir_head, sec_head))

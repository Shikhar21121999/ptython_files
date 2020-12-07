class Node:
    def __init__(self, data=-5):
        self.data = data
        self.next = None


def print_cll(head):

    # if an empty circular linked list
    if head is None:
        print("empty list")

    curr = head
    while curr.next is not head:
        print(curr.data, end=" ")
        curr = curr.next
    print(curr.data, end=" ")
    print(curr.next.data)


def delet_node_incll(cll, del_data):
    # cll is the head of the circular linked list cll
    # del_data represent the data
    # function deletes the first node that has data equal to del_data

    # if cll is empty
    if cll is None:
        print("Nothing in the circular linked list cll")
        return cll

    if cll.data == del_data:
        # we have to remove the first or the head node

        # make a new_head node
        new_head = cll.next

        # traverse to reach the end node
        curr = cll.next
        while curr.next is not cll:
            curr = curr.next

        # curr is the last node
        # we make it to point to the new_head node
        curr.next = new_head
        return new_head

    # in other cases it is safe to assume that
    # either node which has data to be deleted in the middle of the ll
    # or it does not exist at all

    prev = cll
    curr = cll.next
    while curr.data != del_data and curr.next is not cll:
        curr = curr.next
        prev = prev.next

    # we reach here either if cll got over
    if(curr.data != del_data and curr.next is cll):
        # del data does not exist in the ll
        print("Element not found in the ll")
        return cll

    # we found a node that has data equal to del_data
    if(curr.data == del_data):
        # we have to delete this node
        prev.next = curr.next
        # this way we skip the current node there by in essence removing it from the linked list
    return cll


# make a circular linked list
llc = Node(1)
tem = Node(2)
tem1 = Node(3)
tem2 = Node(4)
tem3 = Node(5)
tem4 = Node(6)

# connect to make a circular linked list
llc.next = tem
tem.next = tem1
tem1.next = tem2
tem2.next = tem3
tem3.next = tem4
tem4.next = llc

print_cll(llc)
n_cll = delet_node_incll(llc, 5)
print_cll(n_cll)

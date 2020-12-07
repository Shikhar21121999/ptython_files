class Node:
    def __init__(self, data=-5001551):
        self.data = data
        self.next = None

# function that prints the data in the linked list


def reverse(head):
    prev = None
    current = head
    while(current is not None):
        next_el = current.next
        current.next = prev
        prev = current
        current = next_el
    head = prev


def reverse_returns(head):
    prev = None
    current = head
    while(current is not None):
        next_el = current.next
        current.next = prev
        prev = current
        current = next_el
    head = prev
    return head


def create_a_ll():
    ll.data = 1
    tem = Node(2)
    tem1 = Node(3)
    tem2 = Node(4)
    tem3 = Node(5)
    # tem4 = Node(1)
    ll.next = tem
    tem.next = tem1
    tem1.next = tem2
    tem2.next = tem3
    # tem3.next = tem4


def print_ll(head):
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print()


ll = Node()
create_a_ll()
# reverse(ll)
print_ll(ll)
ll = reverse_returns(ll)
print_ll(ll)

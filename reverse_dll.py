# doubly linked list node
class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# utility function to print Doubly linked list


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


def reverse_dll(head):

    # if empty or linked list with single node is passed
    if head is None or head.next is None:
        return head

    curr_node = head
    next_node = head.next

    while(next_node is not None):
        # flipping previous and next
        curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
        curr_node = next_node
        next_node = next_node.next

    # when we reach here next_node is none
    # that is node next to curr_node is none
    # which implies curr_node is the last node in the dll

    # flip for last node that is current_node
    # also put head as current_node
    curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
    head = curr_node
    return head


dll = DllNode(1)
tem = DllNode(2, dll)
tem1 = DllNode(3, tem)
tem2 = DllNode(4, tem1)
tem3 = DllNode(5, tem2)
tem4 = DllNode(6, tem3)

# assigning next values to them
dll.next = tem
tem.next = tem1
tem1.next = tem2
tem2.next = tem3
tem3.next = tem4
print_dll(dll)
rdll = reverse_dll(dll)
print_dll(rdll)

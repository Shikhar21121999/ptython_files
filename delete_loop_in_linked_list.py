from collections import defaultdict
# node class


class Node():
    def __init__(self, val=-9999999999999999999):
        self.data = val
        self.next = None


def push_node_in_linked_list(head, value):
    # here head denotes the beginning node of a linked list

    # base case if head does not have a value
    if(head.data == -9999999999999999999):
        head.data = value

    else:
        new_node = Node(value)
        # put this node at the end of the linked list
        curr = head
        while(curr.next != None):
            curr = curr.next
        curr.next = new_node


# # create an example linked list
# head = Node()
# first = Node(5)
# second = Node(6)
# third = Node(7)
# head.next = first
# first.next = second
# second.next = third


def print_linked_list(head):
    # a while loop to print the linked list
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print("linked list finished")


def detect_and_Delete(head):
    node_map = defaultdict(int)
    curr = head
    prev = head
    print("trying to delete node")
    while(curr and node_map[curr] < 1):
        prev = curr
        node_map[curr] = 1
        curr = curr.next

    # if curr is not none then it means curr is the starting node or the first repeated node in the linked list
    if(curr is not None):
        print("loop exist between : ", prev.data, " and ", curr.data)
        # hence to remove the loop
        # we point prev to None
        prev.next = None


head = Node(1)
tem1 = Node(2)
tem2 = Node(3)
tem3 = Node(4)
tem4 = Node(5)
tem5 = Node(6)
head.next = tem1
tem1.next = tem2
tem2.next = tem3
tem3.next = tem4
tem4.next = tem5

detect_and_Delete(head)
print_linked_list(head)

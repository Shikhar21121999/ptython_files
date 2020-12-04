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
    while(curr):
        if(curr.data != prev.data):
            prev.next = curr
            prev = curr
        curr = curr.next
    # print("while loop ke baad")
    prev.next = None
    return head


head = Node(1)
tem1 = Node(2)
tem2 = Node(2)
tem3 = Node(4)
tem4 = Node(4)
tem5 = Node(6)
head.next = tem1
tem1.next = tem2
tem2.next = tem3
tem3.next = tem4
tem4.next = tem5
print_linked_list(head)
p = remove_duplicates(head)
print_linked_list(p)

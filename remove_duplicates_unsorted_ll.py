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


head = Node(2)
tem1 = Node(2)
tem2 = Node(2)
tem3 = Node(2)
tem4 = Node(2)
tem5 = Node(2)
head.next = tem1
tem1.next = tem2
tem2.next = tem3
tem3.next = tem4
tem4.next = tem5
print_linked_list(head)
p = remove_duplicates(head)
print_linked_list(p)

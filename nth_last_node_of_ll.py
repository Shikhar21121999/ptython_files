class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def print_linked_list(head):
    # a while loop to print the linked list
    curr = head
    while(curr):
        print(curr.data, end=" ")
        curr = curr.next
    print()


def give_length(head):
    # utility function to calculate length or number of nodes in the linked list

    if head is None:
        return 0
    curr = head
    length = 0
    while(curr is not None):
        length += 1
        curr = curr.next
    return length


def create_ll(head, arr):
    curr = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        curr = new_node

    return head

# main function
if __name__ == '__main__':

    test = int(input())

    while test > 0:
        arr = list(map(int, input().split(' ')))
        n = int(input())
        head = Node(arr[0])
        fir_head = create_ll(head, arr)
        # print_linked_list(fir_head)
        p = nth_last_node(fir_head, n)
        print(p)
        test -= 1

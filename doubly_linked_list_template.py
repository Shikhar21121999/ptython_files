class DllNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def DoublyLinkedList(self,node=None):
    self.head = node
    self.tail = node
    self.length=1 if node is None else 0

def push_ind_dll(self,value):
    # if linked list is none
    if(self.head is None):
        self.head.data = value
        self.tail.data = value
        return

    # if linked list has one or more node
    # 

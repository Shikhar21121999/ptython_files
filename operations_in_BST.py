class BTnode:
    '''
    class to create an object of binary tree node
    '''

    def __init__(self, data):
        '''
        constructor to initialize fields
        such as data
        left pointer
        and right pointer
        '''
        self.data = data
        self.left = None
        self.right = None

def search(root,key):
    '''
    Utility function to search 
    element in the Binary tree
    '''

    # base case
    # either key is not present in whole Tree
    # or it is the current node

    if root is None or root.data==key:
        return root

    if key<root.data:
        # recurse in left subtree
        search(root.left,key)

    if key>root.data:
        # recurse in right subtree
        search(root.right,key)

def min(root):
    '''
    Utility function to find min
    and min value in Binary Search Tree
    '''

    # base case
    if root is None:
        return -1

    # make a que to recurse through left subtree
    q=[]
    q.append(root)

    while(len(q)>0):
        node=q.pop(0)
        if node.left is None:
            return node.data
        q.append(node.left)


if __name__ == '__main__':
    '''
    Main function to declare a binary tree
    and call relevant function
    '''
    root = BTnode(1)
    root.left = BTnode(2)
    root.left.left = BTnode(4)
    root.left.right = BTnode(5)
    root.right = BTnode(3)
    root.right.left = BTnode(6)
    root.right.right = BTnode(7)

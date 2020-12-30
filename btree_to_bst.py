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


def Inorder_iterative(root):
    '''
    utility fuction to perform inorder traversal
    of binary tree and return list
    '''
    # Left Node Right

    ans = []
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            ans.append(node.data)
            node = node.right
    return ans

def inorder_copy(root,arr):
    '''
    utility function to copy contents of arr
    to binary tree inorder traversal
    '''

    ind=0       # storing index of current element of the list
    ans = []
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            # update the value of node data
            node.data = arr[ind]
            ind+=1
            node = node.right
    return root

def binaryTreeToBST(root):
    '''
    main function to convert a binary tree to BST
    inplace where root represent the head of the binary tree
    '''

    # first we get the inorder traversal of binary tree
    # and store it in a list
    temp=Inorder_iterative(root)

    # sort the list
    temp.sort()

    # now we perform inorder traversal of the binary tree
    # and copy content of the array into the tree
    return inorder_copy(root, temp)

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
    Utility function to to return
    inorder traversal of the
    binary tree
    '''

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



def kth_smallest(root, k):
    '''
    Utility function to find kth smallest
    element in the bst
    we perform inorder traversal
    which in turn gives us a sorted list
    of elements of the tree
    '''

    lis=Inorder_iterative(root)

    # as it gives no clear boundation for k
    # we have to set them ourselves
    # return : lis[k-1]  1<=k<n
    #        : -1         otherwise
    if 1<=k and k<len(lis):
        return lis[k-1]

    return -1


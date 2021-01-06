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


def kth_smallest(root, k):
    '''
    Utility function to find kth smallest
    element in the bst
    we perform inorder traversal 
    '''

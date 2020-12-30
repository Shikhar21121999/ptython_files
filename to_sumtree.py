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


def to_sumtree(root):
    '''
    recursive function to convert binary tree to sum tree
    it is a type of tree where each node of the tree
    contains sum of left and right subtree of the original tree
    '''

    # base case
    if root is None:
        return 0

    # calculating sum of left and right subtree
    left_sum = to_sumtree(root.left)
    right_sum = to_sumtree(root.right)

    # store prev val of current node
    prev_val = root.data

    # update val of current node data to sum of left and right subtree
    root.data = left_sum+right_sum

    # return sum of original left and right subtree
    # which means left_sum + right_sum + prev_val
    return root.data+prev_val


# Driver Code
if __name__ == '__main__':
    root = BTnode(10)
    root.left = BTnode(12)
    root.right = BTnode(15)
    root.left.left = BTnode(25)
    root.left.right = BTnode(30)
    root.right.left = BTnode(36)

    to_sumtree(root)
    print("sucess")

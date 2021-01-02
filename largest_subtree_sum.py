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

def largest_subtree_sum(root):
    '''
    Function to find largest subtree sum
    Tree can have negative values also
    '''

    # base case
    if root is None:
        return 0

    #recursive case
    lef_sum=largest_subtree_sum(root.left)
    ryt_sum=largest_subtree_sum(root.right)

    greater_lef_ryt=max(lef_sum,ryt_sum)

    return max(greater_lef_ryt,greater_lef_ryt+root.data)
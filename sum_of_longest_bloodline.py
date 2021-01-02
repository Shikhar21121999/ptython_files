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


def is_leaf(root):
    '''
    utility function to check
    if node is leaf node
    '''

    # handeling if node is None
    if root is None:
        return False

    if root.left is None and root.right is None:
        return True

    return False

def sumOfLongRootToLeafPath(root):
    '''
    Function to call long_blood_util(root)
    '''
    
    ans=long_blood_util(root)

    # here ans is a tuple and we need only sum
    return ans[1]


def long_blood_util(root):
    '''
    Utility function to find sum of nodes
    in the longest bloodline of tree
    Condition are as follows:
        choose the one with greater path
        if length of path same, choose the one with greater sum
    here we asuume that all the data is greater than 1
    '''

    # base case
    if root is None:
        return (0,0)

    # base case leaf node
    if is_leaf(root):
        return (1,root.data)

    # recursive case
    
    # recurse for subtrees
    lef_tup=long_blood_util(root.left)
    ryt_tup = long_blood_util(root.right)

    # choosing the path based on conditions
    
    # if length of path is same
    if lef_tup[0]==ryt_tup[0]:
        
        # path length same hence choose greater sum
        if lef_tup[1]>=ryt_tup[1]:
            return (lef_tup[0]+1,lef_tup[1]+root.data)

        return (ryt_tup[0]+1,ryt_tup[1]+root.data)

    # if path length different
    # choose the one with greater length

    if lef_tup[0]>ryt_tup[0]:
        return (lef_tup[0]+1,lef_tup[1]+root.data)
    
    return (ryt_tup[0]+1,ryt_tup[1]+root.data)



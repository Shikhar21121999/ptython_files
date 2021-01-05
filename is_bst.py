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


INT_MAX = 4294967296
INT_MIN = -4294967296


def isBST(root):
    return isBSTutil(root, INT_MIN, INT_MAX)


def isBSTutil(root, mini, maxi):
    '''
    Utility function to check if BST
    '''

    # empty tree is binary search tree
    if root is None:
        return True

    # check if data in current node
    # are valid that is they satisfy the condition
    if root.data <= mini or root.data >= maxi:
        return False

    return (isBSTutil(root.left, mini, root.data) and isBSTutil(root.right, root.data, maxi))


if __name__ == '__main__':
    '''
    Main function to declare a binary tree
    and call relevant function
    '''
    root = BTnode(8)
    root.left = BTnode(5)
    root.left.left = BTnode(4)
    root.left.right = BTnode(6)
    root.right = BTnode(10)
    root.right.left = BTnode(3)
    root.right.right = BTnode(12)
    print(isBST(root))

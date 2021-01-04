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


def isIsomorphic(root1, root2):
    '''
    Utility function to check if two trees are isomorphic
    '''

    # base case
    if root1 is None and root2 is None:
        return True

    # recursive case
    if root1 is not None and root2 is not None:

        if (root1.data == root2.data) and ((isIsomorphic(root1.left, root2.left) and isIsomorphic(
            root1.right, root2.right)) or (isIsomorphic(root1.right, root2.left) and isIsomorphic(
                root1.left, root2.right))):
            return True

    return False


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

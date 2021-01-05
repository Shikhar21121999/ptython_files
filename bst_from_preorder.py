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


def create_bst(preorder_str):
    '''
    Utility function to create bst
    from preorder
    '''

    # if preorder list is empty
    if len(preorder_str) == 0:
        return None

    # make root node out of first character
    # of string
    root = BTnode(preorder_str[0])

    # all the elements that are less
    # root or first element
    # belong to left subtree
    i = 1
    while i < len(preorder_str):
        if preorder_str[i] > preorder_str[0]:
            break
        i += 1

    lef_stree = create_bst(preorder_str[1:i])
    ryt_stree = create_bst(preorder_str[i:])

    root.left = lef_stree
    root.right = ryt_stree

    return root


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
    # print(isBST(root))

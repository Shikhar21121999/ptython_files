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


def buildtree(inorder, preorder, n):
    '''
    recursive function to build binary tree
    from inorder and preorder traversal
    given in the form of list
    and size of the tree (not actually required)
    inorder=[Left,Root,Right]
    preorder=[Root,Left,Right]
    '''

    # base case
    if len(inorder) == 0 or len(preorder) == 0:
        return None

    # first element of the preorder list
    # is the root element for current level
    root = BTnode(preorder[0])

    # get the index at which first element
    # of preorder is present in the inorder list
    index = inorder.index(preorder[0])

    # check if left subtree exists
    lef_subtree = None
    if index > 0:

        # create inorder list for left subtree
        inord_lef = inorder[0:index]
        # create preorder list for right subtree
        preord_lef = preorder[1:index+1]

        # resursive call for left subtree
        lef_subtree = buildtree(inord_lef, preord_lef, n-1)

    # check if right subtree exists
    right_subtree = None
    if index+1 <= (len(inorder)-1):

        # get inorder list for right subtree
        inord_right = inorder[index+1:]
        # get preorder list for right subtree
        preord_right = preorder[index+1:]

        # recursive call for right subtree
        right_subtree = buildtree(inord_right, preord_right, n-1)

    # now we connect root with left and right subtree
    root.left = lef_subtree
    root.right = right_subtree

    # return root
    return root


# Driver Code
if __name__ == '__main__':
    inorder = [10, 1, 30, 40, 20]
    preorder = [1, 10, 20, 30, 40]
    n = 7
    buildtree(inorder, preorder, n)

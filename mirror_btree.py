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


def to_mirror(root):
    '''
    Function to convert binary tree
    to its mirror image
    To convert mirror image
    make mirror image of left subtree the mirror image of right subtree
    and mirror image of right subtree the mirror image of left subtree
    '''

    # if root is leaf node return node
    if is_leaf(root):
        return root

    if root is None:
        return root

    # else we have to make changes
    lef_subtre = to_mirror(root.left)
    ryt_subtre = to_mirror(root.right)

    # swap subtrees
    root.left = ryt_subtre
    root.right = lef_subtre

    return root


def are_mirror(root1, root2):
    '''
    Function to check if two tree are mirror
    image of each other
    root1 represents first tree
    root2 represents second tree
    '''

    # if both trees are not None
    if root1 is not None and root2 is not None:
        if root1.data == root2.data and are_mirror(root1.left, root2.right) and are_mirror(root1.right, root2.left):
            return True
        else:
            return False

    # else it implies
    # either one of the root is not None
    # or both of the root are None
    if root1 is None and root2 is None:
        return True

    else:
        # this is the case when the structue of the tree
        # is not same
        return False


if __name__ == '__main__':
    root = BTnode('1')
    root.left = BTnode('2')
    root.right = BTnode('3')
    root.left.left = BTnode('4')
    root.left.right = BTnode('5')
    root.right.right = BTnode('2')
    root.right.right.left = BTnode('6')
    root.right.right.right = BTnode('5')
    new_root = to_mirror(root)
    print("sucess")

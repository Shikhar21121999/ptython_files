class BTnode:
    '''
    Class to create a node for Binary Tree
    '''

    def __init__(self, data):
        '''
        constructor for initializing various parameters of node
        '''
        self.data = data
        self.left = None
        self.right = None


def btree_to_dll_util(root):
    '''
    Utility function to convert binary tree to dll
    '''

    if root.left is not None:
        # recurse for left subtree

        left_stree = btree_to_dll_util(root.left)     # left subtree

        # find the inorder predecessor for root
        # which is the rightmost node of left subtree
        while left_stree.right is not None:
            left_stree = left_stree.right

        # make root as next of inorder predecssor
        left_stree.right = root

        # make predecessor as previous of root
        root.left = left_stree

    if root.right is not None:
        # recurse for right subtrees

        right_stree = btree_to_dll_util(root.right)

        # find in order sucessor for the root
        # which is the leftmost node in the right subtree
        # of root
        while right_stree.left is not None:
            right_stree = right_stree.left

        # make root as previous of sucessor
        right_stree.left = root

        root.right = right_stree

    return root


def btree_to_dll(root):

    if root is None:
        return root

    # convert btree to dll using utility function
    root = btree_to_dll_util(root)

    # now we need a pointer to the left most node of the doubly linked list
    while root.left is not None:
        root = root.left

    return root


def print_list(head):
    """
    Function to print the given 
    doubly linked list
    """
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right


# Driver Code
if __name__ == '__main__':
    root = BTnode(10)
    root.left = BTnode(12)
    root.right = BTnode(15)
    root.left.left = BTnode(25)
    root.left.right = BTnode(30)
    root.right.left = BTnode(36)

    head = btree_to_dll(root)
    print_list(head)

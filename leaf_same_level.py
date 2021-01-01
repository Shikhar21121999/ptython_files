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

    if root.left is None and root.right is None:
        return True

    return False


def same_level(root, level, store):
    '''
    Utility function to check
    if current root is a leaf node
    and store the level for it
    then call recursively for left and right
    store is a set that stores the level
    of leaf nodes found
    '''

    if root is None:
        return

    # check if leaf node
    # if a leaf node then it will not have
    # any child nodes
    if(is_leaf(root)):
        store.add(level)
        return

    # call for left and right
    same_level(root.left, level+1, store)
    same_level(root.right, level+1, store)

    return


def check(node):
    '''
    main function which calls other 
    '''

    # initialze a set to store values
    store={}

    # call function same_level to fill values in store
    same_level(node,0,store)

    # if store has only one elemnt
    # implies that all the leaf nodes
    # are at same level
    if len(store) == 1:
        return True
    
    return False

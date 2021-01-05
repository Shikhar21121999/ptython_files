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
    Utility function to check if root
    is a leaf node
    '''

    if root.left is None and root.right is None:
        return True

    return False


def is_parentone(root):
    '''
    Utility function to check if root
    has only one child
    '''
    if (not is_leaf(root)) and (not is_parenttwo(root)):
        return True
    return False


def is_parenttwo(root):
    '''
    Utilty function to check if 
    node has two children
    '''
    if root.left is not None and root.right is not None:
        return True
    return False


def search_nodes(parent, root, key):
    '''
    Utility function to search n1 node
    in Binary Search Tree
    It returns searched node and its parent
    '''

    # base case
    # either key is not present in whole Tree
    # or it is the current node

    if root is None or root.data == key:
        return (parent, root)

    if key < root.data:
        # recurse in left subtree
        return search_nodes(root, root.left, key)

    if key > root.data:
        # recurse in right subtree
        return search_nodes(root, root.right, key)


def min_intree(root):
    '''
    Utility function to find 
    smallest node in the BST
    '''

    # base case
    if root is None:
        return -1

    # make a que to recurse through left subtree
    q = []
    q.append(root)

    while(len(q) > 0):
        node = q.pop(0)
        if node.left is None:
            return node
        q.append(node.left)


def is_left(parent, child):
    '''
    Utility function to check if 
    child is the left child of the parent
    '''
    if parent.left is child:
        return True
    return False


def delete_node(root, n1):
    '''
    utility function to delete 
    node from a Binary Search Tree
    '''

    # first we search for the node
    # and get a pointer to parent and child node
    par, child = search_nodes(None, root, n1)

    if is_leaf(child):
        # if node to be deleted is leaf node
        # we just have to make parent of the child
        # point to None

        # find if the child is left or right child
        if is_left(par, child):
            par.left = None
            return
        par.right = None
        return

    if is_parentone(child):
        # if node to be deleted has only one child tree

        # we need to find which if child has left
        # child or right child

        # get a pointer to g_child tree
        g_tree = None
        if child.left is not None:
            g_tree = child.left
        elif child.right is not None:
            g_tree = child.right

        # now we need to point parent to g_tree
        # depending on wether child was left or right

        if is_left(par, child):
            # is child was on left
            par.left = g_tree
            return

        par.right = g_tree
        return

    # if child has two subtree
    if is_parenttwo(child):

        # we find the smallest element in the right subtree
        # store its value
        # delete that node
        # put child value equal to the min

        min_node = min_intree(child.right)
        child.data = min_node.data

        # delete min_node
        delete_node(child.right, min_node.data)
        return


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
    root.right.left = BTnode(9)
    root.right.right = BTnode(12)
    delete_node(root, 8)
    print("sucess")

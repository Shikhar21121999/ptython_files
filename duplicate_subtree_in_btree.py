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


def is_siz_2(root):
    '''
    utility function to check
    if size of tree is 2
    '''

    # size of the tree is 2
    # if either left node is a leaf node
    # or right node is a leaf node
    if is_leaf(root.left) or is_leaf(root.right):
        return True

    return False


def inorder_iterative(root):
    '''
    Utility function to find 
    and return inorder traversal of tree
    Inorder = [Left,Root,Right]
    '''

    ans = ""
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            ans += node.data
            node = node.right
    return ans


def preorder_iterative(root):
    '''
    Utility function to return preorder traversal
    Preorder=[Root,Left,Right]
    '''
    if root is None:
        return

    st = []
    ans = ""
    st.append(root)

    while(len(st) > 0):
        node = st.pop()
        ans += node.data
        if node.right is not None:
            st.append(node.right)

        if node.left is not None:
            st.append(node.left)

    return ans


def dupsub(root, store):
    '''
    Function to find if duplicate subtree of size
    greater than or equal to 2 exist
    Only If a duplicate tree of size 2 exists
    A duplicate subtree of size greater than 2 can exist
    So we just find if a duplicate subtree of size 2 exists
    else we return False
    '''

    if root is None:
        return

    # check if size of tree is 2
    if is_siz_2(root):

        # store the inorder and preorder traversal
        # of the binary tree
        in_ord = inorder_iterative(root)
        pre_ord = preorder_iterative(root)

        key = in_ord+pre_ord

        # store it in the hash dictionary
        if key in store:
            store[key] = store[key]+1
        else:
            store[key] = 1

    # calling on left and right subtree if they exist
    if root.left is not None:
        dupsub(root.left, store)

    if root.right is not None:
        dupsub(root.right, store)


def dubup_util(root):
    '''
    Utility function to call dupsup and get value
    '''
    store = dict()
    dupsub(root, store)

    # check if value for any key is greater than 2
    val = store.values()

    # iterate through val list to see
    # if it has any val greater than or equal to 2
    ans = False
    for i in val:
        if i >= 2:
            ans = True

    return ans


if __name__ == '__main__':
    root = BTnode('1')
    root.left = BTnode('2')
    root.right = BTnode('3')
    root.left.left = BTnode('4')
    root.left.right = BTnode('5')
    root.right.right = BTnode('2')
    root.right.right.left = BTnode('6')
    root.right.right.right = BTnode('5')
    print(dubup_util(root))

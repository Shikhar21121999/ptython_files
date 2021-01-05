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


def search(root, key):
    '''
    Utility function to search 
    element in the Binary tree
    '''

    # base case
    # either key is not present in whole Tree
    # or it is the current node

    if root is None or root.data == key:
        return root

    if key < root.data:
        # recurse in left subtree
        search(root.left, key)

    if key > root.data:
        # recurse in right subtree
        search(root.right, key)


def pred_sucessor(root, pred, sucessor, key):
    '''
    Utility function to find the predecessor
    and sucessor of the binary search tree
    This function sets the value of pred and sucessor
    to the predecessor and sucessor of the given tree
    '''

    # search for the node with given data
    curr_node = search(root, key)

    # predecessor is the right most element in the left subtree
    # or the highest element in the left subtree
    if root.left is not None:
        tmp = root.left
        while(tmp.right is not None):
            tmp = tmp.right
        pred = tmp

    # inorder sucessor is the left most element
    # in the right subtree
    # or the minimum element in the right subtree
    if root.right is not None:
        temp = root.right
        while(temp.left is not None):
            temp = temp.left
        sucessor = temp


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

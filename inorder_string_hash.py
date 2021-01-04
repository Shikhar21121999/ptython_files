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


def inorder_string_hash(root, recd):
    '''
    Utility function to print dublicate_subtrees
    First we hash trees in inorder form
    then we check if they are repeated
    if they are we print node
    '''

    if root is None:
        return ""

    # recursive function to hash tree in inorder form
    inord_tree = "("
    inord_tree += inorder_string_hash(root.left, recd)
    inord_tree += str(root.data)
    inord_tree += inorder_string_hash(root.right, recd)
    inord_tree += ")"

    # check if current inorder string already present in hash
    if inord_tree in recd:

        # if it occurs for second time
        if recd[inord_tree] == 1:
            print(root.data, end=" ")

        else:
            recd[inord_tree] += 1

    # if not present in recd that is first occurence
    recd[inord_tree] = 1

    return inord_tree


def printAllDups(root):
    '''
    Wrapper function to call inorder string hash
    '''
    recd = dict()
    inorder_string_hash(root, recd)


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
    printAllDups(root)

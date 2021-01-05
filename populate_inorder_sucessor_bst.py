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
        self.next = None


def populateNext(root):
    '''
    Utility function to populate 
    inorder sucessor in bst
    point next to the inorder sucessor
    for each node
    '''

    # ans = []
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    pred = None
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            if pred is None:
                pred = node
            elif pred is not None:
                pred.next = node
                pred = node
            node = node.right


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

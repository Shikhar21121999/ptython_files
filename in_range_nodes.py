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


def Inorder_iterative(root):
    '''
    Utility function to to return
    inorder traversal of the
    binary tree
    '''

    ans = []
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            ans.append(node.data)
            node = node.right
    return ans


def getCount(root, low, high):
    '''
    utility function to count no of nodes
    that are present in bst which lie in the
    range [low,high] both inclusive
    '''
    cnt = 0
    s = []
    # It returns a list containing inorder traversal of Btree
    node = root
    while(node != None or len(s) > 0):
        if node is not None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            if node.data >= low and node.data <= high:
                count += =1
            node = node.right
    return cnt

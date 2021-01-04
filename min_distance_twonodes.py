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


def get_path(root, path, n1):
    '''
    Utility function to find path from root node to n1
    returns true if it exists else true
    modifies path to store path from root to n1
    '''

    # base case
    if root is None:
        return False

    # add this node to the path
    # and check if it if n1 can be found

    path.append(root)

    # current node is n1
    if root.data == n1:
        return True

    # check if n1 can be found in
    # left and right subtree

    if ((root.left is not None and get_path(root.left, path, n1)) or (root.right is not None and get_path(root.right, path, n1))):
        return True

    # n1 does not exist in this path
    # hence we remove nodes from the path
    path.pop()
    return False


def min_distance(root, n1, n2):
    '''
    Utility function to find min_distance
    btween n1 and n2 in the given tree
    '''

    # base case
    if root is None:
        return None

    # get the nodes in the path from root to n1
    n1_path = []
    n2_path = []

    n_1 = get_path(root, n1_path, n1)
    n_2 = get_path(root, n2_path, n2)

    min_distance=-1
    # if both are found
    if n_1 and n_2:

        # traverse n1_path and n2_path to find lca
        i = 0
        while i < len(n1_path) and i < len(n2_path):
            if n1_path[i] != n2_path[i]:
                break
            i += 1

        min_distance=len(n1_path)+len(n2_path)-2*(i+1)
    return min_distance


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

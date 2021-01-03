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


def get_grandchild(root):
    '''
    Utility function to return grand child
    for the current node
    '''
    ans = []
    if root.left is not None:
        if root.left.left is not None:
            ans.append(root.left.left)
        if root.left.right is not None:
            ans.append(root.left.right)

    if root.right is not None:
        if root.right.right is not None:
            ans.append(root.right.right)
        if root.right.left is not None:
            ans.append(root.right.left)

    return ans


def max_sum_no_adj(root):
    '''
    Function to return max sum of nodes
    such that no two nodes are adjacent
    here adjacent means parent child
    that is left and right nodes are not considered adjacent
    '''

    # we take current node and grand-child nodes
    sum1 = 0
    # get max_sum_adj grand-child nodes

    g_lis = get_grandchild(root)
    for node in g_lis:
        sum1 += max_sum_no_adj(node)

    # add the current node
    sum1 += root.data

    # we don't take current node
    # that is we call on child nodes

    sum2 = 0
    if root.left is not None:
        sum2 += max_sum_no_adj(root.left)
    if root.right is not None:
        sum2 += max_sum_no_adj(root.right)

    return max(sum1, sum2)


if __name__ == '__main__':
    root = BTnode(1)
    root.left = BTnode(2)
    root.right = BTnode(3)
    root.left.left = BTnode(1)
    root.right.right = BTnode(5)
    root.right.left = BTnode(4)
    print(max_sum_no_adj(root))

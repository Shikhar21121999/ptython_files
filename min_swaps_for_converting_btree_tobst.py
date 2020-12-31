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
    utility fuction to perform inorder traversal
    of binary tree and return list
    '''
    # Left Node Right

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


def min_swap_1(arr):
    '''
    Straight forward approach
    we iterate from forward to backward
    and swap elements that are not in place greedily
    and count the swaps done
    time complexity O(N*N)
    space complexity O(N)
    '''

    # make a sorted copy of the array
    arr_cpy = arr[0:]
    arr_cpy.sort()

    min_swap_cnter = 0
    for i in range(0, len(arr)):

        # check if not in right place
        if arr[i] != arr_cpy[i]:
            min_swap_cnter += 1
            index = arr.index(arr_cpy[i])
            arr[i], arr[index] = arr[index], arr[i]

    return min_swap_cnter


def min_swap_for_btree_to_bst(root):
    '''
    Function to find min_swaps to convert btree to bst
    In this we find inorder traversal of tree
    and then calculate min_swaps to sort that list
    '''

    # first we get the inorder traversal of binary tree
    # and store it in a list
    temp = Inorder_iterative(root)

    # now find min_swaps to sort this list
    ans = min_swap_1(temp)

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


def print_lis(arr, j):
    '''
    Utility function to print a list
    from some element to the last element
    '''

    for i in range(j, len(arr)):
        print(arr[i], end=" ")
    print()


def check_k_sum(arr, k):
    '''
    Utility function to check
    if it is possble to get sum k
    by adding a window of of elemnts
    of the list
    window is from some beginning to last
    '''
    curr_sum = 0
    for i in range(len(arr)-1, -1, -1):
        curr_sum += arr[i]
        if(curr_sum == k):
            # print path from current element of the list
            # to the last element
            print_lis(arr, i)


def printKPathUtil(root, path, k):

    # base case
    if root is None:
        return

    # inlude current root in the path
    path.append(root.data)

    # and check if it is possbile
    # to get a path with k sum including current node
    check_k_sum(path, k)

    llis = path[:]
    rlis = path[:]

    # call for left and right subtree
    printKPathUtil(root.left, llis, k)
    printKPathUtil(root.right, rlis, k)

    # remove the current node
    # path.pop(-1)

    return


if __name__ == '__main__':
    '''
    Main function to declare a binary tree
    and call relevant function
    '''
    root = BTnode(1)
    root.left = BTnode(3)
    root.left.left = BTnode(2)
    root.left.right = BTnode(1)
    root.left.right.left = BTnode(1)
    root.right = BTnode(-1)
    root.right.left = BTnode(4)
    root.right.left.left = BTnode(1)
    root.right.left.right = BTnode(2)
    root.right.right = BTnode(5)
    root.right.right.right = BTnode(2)
    k = 5
    path = []
    printKPathUtil(root, path, 5)

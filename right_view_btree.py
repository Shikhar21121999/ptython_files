class BTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hieght(root):
    if(root is None):
        return 0

    else:
        return max(hieght(root.left), hieght(root.right))+1


def right_view_btree(root, n):
    # if root is none nothing can be printed
    if root is None:
        return []

    # if level we are looking for is the current level
    # that is current node or root belongs to this level
    # we print the data in this node or root
    if n == 1:
        return [root.data]

    # root does not belong to this level and we need to go deper into the tree
    # to get the desired level
    elif n > 1:

        # as we want to print left view we only get right if len(l) is zero
        r = right_view_btree(root.right, n-1)
        if(len(r) > 0):
            # r = print_level_btree(root.right, n-1)
            return r
        return right_view_btree(root.left, n-1)


def level_order_traversal(root):
    # find the hieght of the tree
    high = hieght(root)

    # iterate throug a for loop to print ith level of the tree
    ans = []
    for i in range(1, high+1):
        ans += right_view_btree(root, i)
    return ans


# main function
if __name__ == "__main__":
    # create a Btree
    root = BTnode(1)
    root.left = BTnode(2)
    root.right = BTnode(3)
    root.left.left = BTnode(4)
    root.left.right = BTnode(5)

    # ans = levelOrder(root)
    # print(ans)
    print(level_order_traversal(root))

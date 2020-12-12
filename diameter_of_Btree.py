class BTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A utiility function to print level order traversal of the BTree iteratively


def levelOrder(root):

    ans = []
    # An empty tree
    if(root is None):
        return ans
    # Else we print the root.data and add its children to a queue
    # print(root.data, end=" ")
    que = []
    que.append(root)

    # while there is no root left in the queue
    while(len(que) > 0):
        curr_node = que.pop(0)
        ans.append(curr_node.data)

        # append child node to queue if they are not none
        left_child = curr_node.left
        right_child = curr_node.right
        if(left_child is not None):
            que.append(left_child)
        if(right_child is not None):
            que.append(right_child)

    return ans

# utility function to print nth level of the tree


def print_level_btree(root, n):
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

        # we first call for left node as it will ensure that nodes are printed from left
        # n-1 as when we go down we need find 1 less level
        l = print_level_btree(root.left, n-1)
        r = print_level_btree(root.right, n-1)
        return l+r


# utility funciton to print level order traversal of the tree recursively
def lever_order_recursive(root):

    # find the hieght of the tree
    high = hieght(root)

    # iterate throug a for loop to print ith level of the tree
    for i in range(1, high+1):
        print_level_btree(root, i)


def reverse_level_traversal(root):
    # find the hieght of the tree
    high = hieght(root)

    # iterate throug a for loop to print ith level of the tree
    ans = []
    for i in range(high, 0, -1):
        ans += print_level_btree(root, i)
    return ans

# utility functin to find hieght of the tree


def hieght(root):
    if(root is None):
        return 0

    else:
        return max(hieght(root.left), hieght(root.right))+1


#  modified hieght function that returns hieght and also modifies ans at the same time


def hieght_ans(root, ans):

    if root is None:
        return 0

    left_hieght = hieght_ans(root.left, ans)
    right_hieght = hieght_ans(root.right, ans)

    ans[0] = max(ans, left_hieght+right_hieght+1)

    # hieght of current tree
    return max(left_hieght, right_hieght)+1


def diameter(root):
    if root is None:
        return 0

    ans = [-99999999999]
    hieght_of_tree = hieght_ans(root, ans)
    return ans[0]


def make_mirror_image(root):
    if root is None:
        return

    # make mirror image of left_subtree
    make_mirror_image(root.left)

    # make mirror image of right_subtree
    make_mirror_image(root.right)

    # swap left and right subtree to make mirro image of root
    root.left, root.right = root.right, root.left


# main function
if __name__ == "__main__":
    # create a Btree
    root = BTnode(1)
    root.left = BTnode(2)
    root.right = BTnode(3)
    root.left.left = BTnode(4)
    root.left.right = BTnode(5)

    ans = levelOrder(root)
    print(ans)
    make_mirror_image(root)
    print(levelOrder(root))

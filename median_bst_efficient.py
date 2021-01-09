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


def inorder_morris(root):
    '''
    Utility function to perfrom
    morris's inorder traversal
    it is a type of inorder traversal
    which requires has O(1) space complexity
    '''
    current = root
    while current is not None:
        if current.left is not None:
            # we can get here for two possbilites
            # either left subtree is already traversed
            # or left subtree is yet to be traversed
            # we decide that on the fact
            # wether last node is linked back to current node on right

            # get inorder predecessor
            # or node whose right child is current(set earlier)
            pred = current.left
            while(pred.right is not None and pred.right is not current):
                pred = pred.right

            # here either pred is equal to current(which implies left subtree is visited)
            # or it is something else in that case we have to visit left subtree
            if pred.right is current:
                # we break the link we put
                # visit current node
                # traverse the right subtree
                pred.right = None
                print(current.data, end=" ")
                current = current.right

            elif pred.right is None:
                # implies that left subtree is yet to be visited
                # we make a temporary link from perd to current
                # so that we can get back to root after traversing left subtree
                pred.right = current
                # traverse left subtrees
                current = current.left

        else:
            # when left subtree does not exist
            # visit the current node
            # traverse the right subtree
            print(current.data, end=" ")
            current = current.right


def inorder_morris_cnter(root):
    '''
    Utility function to perfrom
    morris's inorder traversal and count no of nodes in tree
    it is a type of inorder traversal
    which requires has O(1) space complexity
    '''
    cnt = 0
    current = root
    while current is not None:
        if current.left is not None:
            # we can get here for two possbilites
            # either left subtree is already traversed
            # or left subtree is yet to be traversed
            # we decide that on the fact
            # wether last node is linked back to current node on right

            # get inorder predecessor
            # or node whose right child is current(set earlier)
            pred = current.left
            while(pred.right is not None and pred.right is not current):
                pred = pred.right

            # here either pred is equal to current(which implies left subtree is visited)
            # or it is something else in that case we have to visit left subtree
            if pred.right is current:
                # we break the link we put
                # visit current node
                # traverse the right subtree
                pred.right = None
                cnt += 1
                current = current.right

            elif pred.right is None:
                # implies that left subtree is yet to be visited
                # we make a temporary link from perd to current
                # so that we can get back to root after traversing left subtree
                pred.right = current
                # traverse left subtrees
                current = current.left

        else:
            # when left subtree does not exist
            # visit the current node
            # traverse the right subtree
            cnt += 1
            current = current.right

    return cnt


def inorder_morris_get_nth(root, n):
    '''
    Utility function to get nth node in tree
    using morris's inorder traversal
    it is a type of inorder traversal
    which requires has O(1) space complexity
    '''
    cnt = 0
    current = root
    while current is not None:
        if current.left is not None:
            # we can get here for two possbilites
            # either left subtree is already traversed
            # or left subtree is yet to be traversed
            # we decide that on the fact
            # wether last node is linked back to current node on right

            # get inorder predecessor
            # or node whose right child is current(set earlier)
            pred = current.left
            while(pred.right is not None and pred.right is not current):
                pred = pred.right

            # here either pred is equal to current(which implies left subtree is visited)
            # or it is something else in that case we have to visit left subtree
            if pred.right is current:
                # we break the link we put
                # visit current node
                # traverse the right subtree
                pred.right = None
                if cnt == n:
                    return current.data
                cnt += 1
                current = current.right

            elif pred.right is None:
                # implies that left subtree is yet to be visited
                # we make a temporary link from perd to current
                # so that we can get back to root after traversing left subtree
                pred.right = current
                # traverse left subtrees
                current = current.left

        else:
            # when left subtree does not exist
            # visit the current node
            # traverse the right subtree
            if cnt == n:
                return current.data
            cnt += 1
            current = current.right


def median_bst_eff(root):
    '''
    Wrapper function to get median
    of bst using inorder morris traversal
    '''

    # first we get the no of nodes in the bst
    n = inorder_morris_cnter(root)

    # if odd nodes
    if n % 2 == 1:
        return inorder_morris_get_nth(root, n//2)

    # if even nodes
    if n % 2 == 0:
        return (inorder_morris_get_nth(root, n//2)+inorder_morris_get_nth(root, (n//2)-1))/2


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
    inorder_morris(root)
    print()
    print(median_bst_eff(root))

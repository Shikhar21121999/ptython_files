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

def kth_ancestor(root,node,k):
    '''
    Utility function to calculate kth ancestor
    We recurse all the way to find the node
    when we find the node we start back tracking
    and returning node to represent that node will be found
    below in subtree
    and decreasing value at k[0]
    when we hit k[0]=0 we get the kth ancestor
    from that point onwards we return None
    to signify that we dont need further traversal
    '''

    # Base case
    if root is None:
        return None
    
    # recursive case
    if (root.data==node or kth_ancestor(root.left,node,k) or kth_ancestor(root.right,node,k)):
        
        if k[0]>0:
            k[0]-=1
        
        elif k[0]==0:
            # this is the kth ancestor of the node
            print("kth ancestor is : "+root.data)

            # start returning to stop further backtracking
            return None

        return None
    
    


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

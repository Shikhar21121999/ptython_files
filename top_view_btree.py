class BTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def store_top_view(root, recd, curr_dis, level):
    ''' 
    utility function to store horizontal distance
    of current node(root) from head of the tree
    root->curr_node
    curr_dis->horizontal distance of current node(root) from head of the tree
    recd->dictionary to store nodes at a particular distance
    '''

    # base case
    if root is None:
        return

    # first we check if we already have data 
    # alreday saved corrosponding to curr_dis
    if curr_dis in recd:

        # we check if level of current node is lesser than previous node
        if level<recd[curr_dis][1]:
            # update the data in the dicitonary
            recd[curr_dis] = [root.data,level]

    else:
        recd[curr_dis] = [root.data,level]

    # recurse for left subtree
    store_top_view(root.left, recd, curr_dis-1,level+1)

    # recurse for right subtree
    store_top_view(root.right, recd,curr_dis+1,level+1)


def print_top_view(recd):
    '''
    Function to print top_view of the tree
    It first calls storeverticalorder() to store values in recd
    Then we acess first element for each vertical order
    to get top view of the tree
    '''
    recd = dict()

    # store values in recd
    store_top_view(root, recd, 0,0)

    ans=[]
    for value in sorted(recd):
        ans.append(value[0])
    
    return ans


# main function
if __name__ == "__main__":
    # create a Btree
    root = BTnode(1)
    root.left = BTnode(2)
    root.right = BTnode(3)
    root.left.left = BTnode(4)
    root.left.right = BTnode(5)
    print_top_view(root)

    # ans = levelOrder(root)
    # print(ans)

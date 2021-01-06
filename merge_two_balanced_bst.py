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

def btree_to_bst(root):
    '''
    Wrapper function ot convert
    a binary tree into a
    binary search tree
    '''

    # get inorder traversal of the tree
    # and sort it 
    inord_trav=Inorder_iterative(root)
    inord_sorted=sorted(inord_trav)

    # make a balanced bst out of it
    root=create_balanced_bst(inord_sorted)

    return root

def sort_and_merge(arr1,arr2):
    '''
    Utility function to merge two list
    in sorted way when both list are sorted
    '''
    lis3=[]

    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        # find the smaller of two
        # merge the element to the list
        if arr1[i]<arr2[j]:
            lis3.append(arr1[i])
            i+=1
        else:
            lis3.append(arr2[j])
            j+=1

    # append the remainig elements of lis1
    # to the arr
    if i<len(arr1)-1:
        while(i<len(arr1):
            lis3.append(arr1[i])
            i+=1

    elif j<len(arr2)-1:
        while(j<len(arr2):
            lis3.append(arr2[j])
            j+=1

    return lis3

def merge_two_bst(root1,root2):
    '''
    Wrapper function to merge two bst
    For this we get inorder traversals of both tree
    then we join the two list together
    and create a new bst out of it
    '''

    lis1=Inorder_iterative(root1)
    lis2=Inorder_iterative(root2)

    # merging the two list together and sorting the list
    lis1=sort_and_merge(lis1,lis2)

    # create a bst with this list
    return create_balanced_bst(lis1)



def create_balanced_bst(arr):
    '''
    Utility function to create a balanced bst
    it takes in a list of sortd elements
    out of which a balanced bst
    can be constructed
    We simply split the list in the middle
    put root as middle element
    left substring to left subtree
    and right substring to right subtree
    '''

    mid_ind=len(arr)//2

    # make root out of the middle element
    root=BTnode(arr[mid_ind])

    # create left and right subtree
    # out of left and right subtring
    lef_subtree=create_balanced_bst(arr[0:mid_ind])
    ryt_subtree=None
    if mid_ind+1<len(arr):
        ryt_subtree=create_balanced_bst(arr[mid_ind+1:])

    # connect root with left and right subtree
    root.left =lef_subtree
    root.right =ryt_subtree

    return root





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
    # print(isBST(root))

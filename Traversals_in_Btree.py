class BTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Traversals in binary tree

# Inorder Recursive traversal of Btree
def Inorder_recursive(root, arr):
    if root is None:
        return

    # call the inorder on left subtree
    Inorder_recursive(root.left, arr)

    arr.append(root.data)

    # call inorder on right subtree
    Inorder_recursive(root.right, arr)


# Inorder Iterative traversal of Btree
def Inorder_iterative(root):
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


# preorder Recursive traversal of binary tree

def predorder_recursive(root, arr):
    if root is None:
        return
    arr.append(root.data)
    predorder_recursive(root.left, arr)
    predorder_recursive(root.right, arr)

# preorder iterative traversal of binary tree


def preorder_iterative(root):
    if root is None:
        return

    st = []
    arr = []
    st.append(root)
    arr = []
    while(len(st) > 0):
        node = st.pop()
        arr.append(node.data)
        if node.right is not None:
            st.append(node.right)

        if node.left is not None:
            st.append(node.left)

    return arr

# postorder recursive


def postorder_recursive(root, arr):
    if root is None:
        return

    postorder_recursive(root.left, arr)
    postorder_recursive(root.right, arr)
    arr.append(root.data)

# postorder iterative traversal of Btree


def postorder_iterative(root):
    st = []
    t = []
    st.append(root)
    while(len(st) > 0):
        node = st.pop()
        t.append(node)
        if(node.left is not None):
            st.append(node.left)
        if(node.right is not None):
            st.append(node.right)

    ans = []
    while(len(t) > 0):
        ans.append(t.pop().data)

    return ans


# main function
if __name__ == "__main__":
    # create a Btree
    root = BTnode(1)
    root.left = BTnode(2)
    root.right = BTnode(3)
    root.left.left = BTnode(4)
    root.left.right = BTnode(5)

    inorder_lis = []
    preorder_lis = []
    Inorder_recursive(root, inorder_lis)
    print(inorder_lis)
    print("inorder iterative", Inorder_iterative(root))
    predorder_recursive(root, preorder_lis)
    print("pre recursive", preorder_lis)
    print(preorder_iterative(root))
    postorder_lis = []
    postorder_recursive(root, postorder_lis)
    print("post recursive", postorder_lis)
    print("post order iterative", postorder_iterative(root))

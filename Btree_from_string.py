class BTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def word_split_inde(word):
    '''
    utility function which returns the index of word split
    '''

    i = 2
    open_brack_cnt = 1
    close_brack_cnt = 0
    while(i < len(word)):
        if(word[i] == '('):
            open_brack_cnt += 1
        elif(word[i] == ')'):
            close_brack_cnt += 1
        if(open_brack_cnt == close_brack_cnt):
            break
        # scan the current character and increement counter
        # for open and close bracket accordingly

        i += 1

    # at the end of this loop value of i
    # will be the index at which bracket became balanced
    # or we can say a subtree was found
    return i


def tree_from_string(word):
    '''
    This is a function that is used to create tree
    from bracket representation of the string
    '''

    # base case empty string
    if word == "":
        return None

    if len(word) == 1:
        # make a single node with data of word
        curr_node = BTnode(word[0])

        return curr_node

    if len(word) > 1:
        # it is implied that this node of tree will in turn have 1 or more subtree

        # make node with data equal to first character of node
        curr_node = BTnode(word[0])

        # we split the string into two substrings
        # which inturn represent two subtrees
        index = word_split_inde(word)

        # first substring for subtree is from word[2:index]
        fir_substr = word[2:index]

        # second substring for subtree is from word[index+2:]
        # check if second substring word hence second subtree exists
        sec_substr = ""
        if index+2 < len(word):
            sec_substr = word[index+2:]

        # recurse to create lef_node and rig_node
        lef_node = tree_from_string(fir_substr)
        rig_node = tree_from_string(sec_substr)

        # make connections from current_node to left and right subtree
        curr_node.left = lef_node

        curr_node.right = rig_node

        # return current_node
        return curr_node


# main function
if __name__ == "__main__":
    # take a word as input and create a string for it
    word = input()
    root = tree_from_string(word)
    print("sucess")

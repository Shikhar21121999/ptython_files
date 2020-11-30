
def quer_poss(inp, l, r):

    # inp reprsent a string indexed from 0
    # l is the beginning index for the pattern
    # r is the ending index for the pattern to be searched
    # l,r both are inclusive and are in 1 based inedexing

    c_chr_i, l_chr_i_mch, is_conti = l-1, -5, True
    ans_found = False

    # print(c_chr_i, l_chr_i_mch, is_conti, ans_found)
    # print("loop starts")
    for i in range(0, len(inp)):
        # print(c_chr_i, i, is_conti, l_chr_i_mch)
        # case 1 first character of pattern and ith character of string matches
        if(inp[c_chr_i] == inp[i] and c_chr_i == l-1):
            # print("we came here also")
            # we need to initialize the last character matched index
            l_chr_i_mch = i

            # update the current character index to look for next character in the pattern
            c_chr_i += 1
            continue

        # if we current character we are lookoing for is the last character in the pattern
        elif(c_chr_i == r-1):

            # character matches and subsequence found is non-contiguous

            # we need to check will the subsequence remain contiguous if we include this element or will it not be
            if(i-l_chr_i_mch > 1 and is_conti):
                # no longer contiguous
                is_conti = False

            if(inp[c_chr_i] == inp[i] and not is_conti):
                # this is the required answer
                ans_found = True
                return "Yes"

            # character matches but sequence is not contiguous
            # we try to look for some other index that has same last character
            elif(inp[c_chr_i] == inp[i] and is_conti):
                is_conti = False      # as now the next character wont be contiguous
                # look for last character again

        # current character matches
        elif(inp[c_chr_i] == inp[i]):
            # print("character matches", end="\t")
            # print(l_chr_i_mch, i, is_conti)

            # check if subsequence is no longer contiguous
            if(i-l_chr_i_mch > 1 and is_conti):
                # no longer contiguous
                is_conti = False

            # update last character and next character to look for
            c_chr_i += 1
            l_chr_i_mch = i

    # if ans not found already then return no
    if(not ans_found):
        return "No"


# main function
if __name__ == '__main__':
    # binary string

    # test cases
    test = int(input())

    while(test > 0):

        # length of the string and no of queries
        n, q = map(int, input().split(' '))

        # input the string
        inp = input()

        for _ in range(q):

            # input the queries
            l, r = map(int, input().split(' '))
            # call the query_poss function q times
            print(quer_poss(inp, l, r))

        test -= 1

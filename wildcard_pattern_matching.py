

def recur(i, j, str1, str2):

    # print(i, j)
    n = len(str1)
    m = len(str2)

    # exception case when one string finishes befor other one
    if(i >= n or j >= m):
        return False

    # end case when both string ends at the same time
    if(i == n-1 and j == m-1):
        return True

    # current character matches
    if(str1[i] == str2[j]):
        # call for the next characters in both
        return recur(i+1, j+1, str1, str2)

    # first character is wildcard '?'
    if(str1[i] == '?'):
        # consider the current characters as matched
        return recur(i+1, j+1, str1, str2)

    # first character is wildcard '*'
    if(str1[i] == '*'):
        # there are two possibilities we ignore *
        # or we take * to represent current character in the second string
        return (recur(i+1, j, str1, str2) or recur(i, j+1, str1, str2))

    return False


# main function
if __name__ == '__main__':
    test = int(input())
    while(test > 0):
        s1 = input()
        s2 = input()
        if recur(0, 0, s1, s2):
            print("YES")
        else:
            print("NO")
        test -= 1

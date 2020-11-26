def recur(i, j):
    global str1
    global str2
    global dp

    # base case if we reached the end of the sttring
    if(i == 0 or j == 0):
        return 0

    # construct a key for the given indices
    key = (i, j)

    # if key is not found in the dictionary we assign value to it
    if key not in dp:

        # last characters match
        if(str1[i-1] == str2[j-1]):
            dp[key] = recur(i-1, j-1)+1

        else:
            dp[key] = max(recur(i-1, j), recur(i, j-1))

    return dp[key]


# main function
if __name__ == "__main__":
    str1 = input()
    str2 = input()

    # create a dictionary to store the dp values
    dp = {}
    print(recur(len(str1), len(str2)))

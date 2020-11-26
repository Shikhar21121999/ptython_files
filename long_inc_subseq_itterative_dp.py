# this program uses top down itterative approach


# main function
if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(str1, str2)
    n = len(str1)
    m = len(str2)
    print(n, m)

    # this time we make a list of list for storing dp values
    # initialzes a matrix with n rows and m columns with zero
    dp = [[0 for x in range(0, m+1)]for y in range(0, n+1)]
    # column comes first and row comes later in the above statement

    print(dp)

    for i in range(1, n+1):
        for j in range(1, m+1):

            # if current character matches
            if(str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    print(dp)
    print(dp[n][m])

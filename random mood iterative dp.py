# iterative dp solution for random mood
# we will use top down approach
# time complexity: O(N)

# main function
if __name__ == "__main__":
    n, p = input().split()
    n = int(n)
    p = float(p)
    # p = float(input())

    # make a dp to store answeres
    dp = [[-0.01 for i in range(2)]for j in range(n+1)]
    # initial value is taken as negative

    dp[0][1] = 1
    dp[0][0] = 0

    for i in range(1, n+1):

        # filling the dp for state after ith min
        dp[i][1] = dp[i-1][0]*p+dp[i-1][1]*(1-p)
        dp[i][0] = 1-dp[i][1]

    # print(dp)
    print(dp[n][1])

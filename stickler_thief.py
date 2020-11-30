# this code is giveing error
# will debug or see later
def solve():

    n = int(input())

    a = list(map(int, input().split(' ')))

    print(a)

    # if length < 3

    if(n == 1):
        # print("size : ", n)
        return a[0]

    if(n == 2):
        # print("size : ", n)
        return max(a[0], a[1])

    if(n == 3):
        # print("size : ", n)
        return max(a[0]+a[2], a[1])

    # make a dp of size n+1
    dp = [0]*(n+1)

    dp[0] = a[0]
    dp[1] = a[1]
    dp[2] = a[0]+a[2]

    for i in range(3, n):

        # dp[i]=max(dp[i-2],dp[1-3])
        dp[i] = max(dp[i-2], dp[1-3])+a[i]

    return max(dp[n-1], dp[n-2])


# main function
if __name__ == '__main__':
    test = int(input())

    while(test > 0):
        print(solve())
        test -= 1

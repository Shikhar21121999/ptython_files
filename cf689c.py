
def solve():
    n, k = map(int, input().split())
    # print(n, k)
    a = list(map(int, input().split()))
    b = list(range(1, n+1))

    # print(a, b)

    # min_val of ri required to make desirable changes
    min_reqd = n
    for i in range(n-1, -1, -1):
        if(a[i] == b[i]):
            min_reqd -= 1
        if(a[i] != b[i]):
            break

    # print("min_recd is ", min_reqd)

    ans_probab = 0.0000000000

    # if whole of the permutation is already sorted
    if(min_reqd == 0):
        ans_probab = 1

    # while loop to input ri,pi
    # and make changes to the probablity

    while(k > 0):
        tem_lis = input().split()
        curr_r, curr_p = int(tem_lis[0]), float(tem_lis[1])
        # print(curr_r, curr_p)

        # this experiment will make changes to the ans probablity only
        # curr_r is greater or equal to min_reqd

        if(curr_r >= min_reqd):
            ans_probab = ans_probab*curr_p+ans_probab *
                (1-curr_p)+(1-ans_probab)*curr_p
        k -= 1

    print(ans_probab)


# main function
if __name__ == '__main__':
    test = int(input())
    while(test > 0):
        solve()
        test -= 1



def find_subarray(arr, n):

    # arr is a list of integers
    # n is the length of the lis

    # find no of subarrays such that there  sum is  zero
    dp_sum = [0]*n
    zero_sum_cnt = 0

    for x in range(n):
        # this is the current number that gets added
        for y in range(0, x+1):
            dp_sum[y] += arr[x]
            # check if new sum is zero
            if(dp_sum[y] == 0):
                zero_sum_cnt += 1

    print(zero_sum_cnt)


# main function
if __name__ == '__main__':
    lis = list(map(int, input().split()))
    # print(lis)
    find_subarray(lis, len(lis))

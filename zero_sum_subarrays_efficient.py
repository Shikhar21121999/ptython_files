from collections import defaultdict


def findSubArrays(arr, n):

    # arr is a list of integers
    # n is the number of elements in the array

    hash_sum = defaultdict(int)

    zero_cnt = 0
    curr_sum = 0

    for i in range(n):

        curr_sum += arr[i]

        if(curr_sum == 0 and arr[i] == 0):
            zero_cnt += 1

        hash_sum[curr_sum] += 1
        zero_cnt += hash_sum[curr_sum]-1

    return zero_cnt


# main function
if __name__ == '__main__':
    lis = list(map(int, input().split()))
    # print(lis)
    print(findSubArrays(lis, len(lis)))

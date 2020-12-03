
def print_kth_smallest(range_lis, k):

    # traverse over range_lis and print kth smallest for the range
    for lis in range_lis:
        first = lis[0]
        last = lis[1]
        if(k > last):
            print(-1)
        else:
            print(first+k-1)


# main function
if __name__ == '__main__':

    # test cases
    test = int(input())

    while(test > 0):
        n, q = map(int, input().split())
        test -= 1
        # now we have to store n lines of x and y
        # which represent the range in which we have to find kth smallest
        lis_range = []
        for _ in range(n):
            lis_range.append(list(map(int, input().split())))
        for _ in range(q):
            q = int(input())
            print_kth_smallest(lis_range, q)

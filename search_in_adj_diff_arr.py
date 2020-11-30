
def find_ind(arr, x, k):
    # arr is a list of integers
    # x is the element whose index to be searched
    # k is the difference between adjacent indices

    # printing inputs

    # print(arr)
    # print(x)
    # print(k)
    ans_found = False
    curr_ind = 0
    while(curr_ind < len(arr)):
        # print(curr_ind, arr[curr_ind])
        # search the element at curr inedex
        if(arr[curr_ind] == x):
            print(curr_ind)
            ans_found = True
            break
        else:
            # we calculate next index at which we look for
            jump = abs(arr[curr_ind]-x)//k
            if(jump < 1):
                curr_ind += 1
            else:
                curr_ind += jump

    if(not ans_found):
        print(-1)


# main function
if __name__ == '__main__':
    n = int(input())  # size of the array
    lis = list(map(int, input().split()))  # array of integers
    x = int(input())  # element to be searched
    k = int(input())  # atmost difference between adjacent elements
    find_ind(lis, k, x)

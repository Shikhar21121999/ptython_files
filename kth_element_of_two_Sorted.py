
def kth_smallest(A, B, k):
    curr_ind = 0
    curr_ele = -1
    # we traverse both the list at the same time using whie loop
    i = 0
    j = 0
    while(i < len(A) or j < len(B)):
        # we find the smallest elment for the current index or the curr_indth smallest elmeent
        if(A[i] <= B[j]):
            curr_ele = A[i]
            i += 1
        elif(A[i] > B[j]):
            curr_ele = B[j]
            j += 1
        # print(i, j, curr_ind, curr_ele)

        if(curr_ind == k-1):
            return curr_ele
        curr_ind = curr_ind + 1
    print("hum toh bahar aa gye")


# main function
if __name__ == '__main__':
    test = int(input())
    while(test > 0):
        n, m, k = map(int, input().split(' '))
        print(n, m, k)
        A = list(map(int, input().split(' ')))
        A.append(10**7)
        B = list(map(int, input().split(' ')))
        B.append(10**7)
        # print(kth_smallest(A, B, k))
        test -= 1

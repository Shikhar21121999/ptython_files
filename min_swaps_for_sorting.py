'''
This file contains various functions
to calculate min number of swaps required
for sorting an array
'''


def min_swap_1(arr):
    '''
    Straight forward approach
    we iterate from forward to backward
    and swap elements that are not in place greedily
    and count the swaps done
    time complexity O(N*N)
    space complexity O(N)
    '''

    # make a sorted copy of the array
    arr_cpy = arr[0:]
    arr_cpy.sort()

    min_swap_cnter = 0
    for i in range(0, len(arr)):

        # check if not in right place
        if arr[i] != arr_cpy[i]:
            min_swap_cnter += 1
            index = arr.index(arr_cpy[i])
            arr[i], arr[index] = arr[index], arr[i]

    return min_swap_cnter


# main function
if __name__ == '__main__':
    arr = [2, 4, 5, 1, 3]
    print(min_swap_1(arr))

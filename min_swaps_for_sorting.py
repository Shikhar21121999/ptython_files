
from collections import defaultdict


def min_swaps_reqd(a, n):

    # make a copy of the list a and sort it
    p = a[0:]
    p.sort()

    # make a default dict and initialize it to -1
    # in this we store pair of a[i] to p[i] if they are not equal

    hash_map = defaultdict(lambda: -1)
    print(a)
    print(p)

    pair_cnt, total_diff, swap_cnt = 0, 0, 0
    for i in range(0, n):
        # print(a[i], p[i])
        if (a[i] != p[i]):
            total_diff += 1

            if(hash_map[a[i]] == -1):
                # there does not exist a pair which is reverse with which current can be swapped
                # we add this to the hash map in reverse for finding the reverse in future

                hash_map[p[i]] = a[i]

            elif(hash_map[a[i]] == p[i]):
                pair_cnt += 1
    print(total_diff, pair_cnt)
    swap_cnt = pair_cnt
    total_diff -= 2*pair_cnt
    if(total_diff > 2):
        swap_cnt += total_diff-1

    return swap_cnt


# main function
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(arr)
    print(min_swaps_reqd(arr, len(arr)))

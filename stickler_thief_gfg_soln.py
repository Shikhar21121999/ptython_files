# gfg solution for stickeler problem.

def solve():
    n = int(input())

    a = list(map(int, input().split()))

    incl = a[0]
    excl = 0

    for i in range(1, n):

        # current max excluding current one
        new_excl = max(incl, excl)

        # current max including current one
        incl = excl+a[i]

        # update excl
        excl = new_excl

    return max(incl, excl)


# main function
if __name__ == '__main__':
    test = int(input())

    while(test > 0):
        print(solve())
        test -= 1

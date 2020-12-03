
def check_if_possible_square(p, q, r, s, length):
    global n, m, x, y
    if(p+length > n or q+length > m or r+length > x or s+length > y):
        # implies that for the square the index will go out of bounds
        return False
    return True


def check_if_square_length(p, q, r, s, length):

    global A, B

    # to check if square of lenght 'length' can be selected from given coordinates in A and B
    if not check_if_possible_square(p, q, r, s, length):
        # print("fit hi nhi ho sakta")
        return False

    # we initially say that square of length l exists
    # print("fit toh ho rha hai")
    ans = True
    for i, k in zip(range(p, p+length), range(r, r+length)):
        for j, l in zip(range(q, q+length), range(s, s+length)):
            if(A[i][j] != B[k][l]):
                # print("yhan maamla bigda", i, j, k, l)
                ans = False

    # if ans is still True it implies that a square of length l is equal in a and b
    return ans


# main function
if __name__ == '__main__':

    # n row and m columns of first kheshtaks
    n, m = map(int, input().split(' '))

    # input first kheshtaks
    A = [list(map(int, input().split()))for y in range(m)]
    # print(A)

    # x row and y columns of first kheshtaks
    x, y = map(int, input().split(' '))

    # input first kheshtaks
    B = [list(map(int, input().split()))for y in range(y)]
    # print(B)

    # now we iterate over all the possible indices and check if a square of length 1 is possible
    ans = 0
    # print(n, m, x, y)
    for i in range(n):
        for j in range(m):
            for k in range(x):
                for l in range(y):
                    # print(i, j, k, l, end="\t")
                    # print(A[i][j], B[k][l])
                    if(A[i][j] == B[k][l]):
                        for leng in range(1, min(n, m, x, y)):
                            # we iteratively look for the highest BCS achivable for current coordinates
                            if(check_if_square_length(i, j, k, l, leng)):
                                ans = max(ans, leng)
                            else:
                                break

    # n, m = 3, 3
    # x, y = 3, 3
    # A = [[0, 1, 2], [1, 1, 2], [3, 1, 2]]
    # B = [[1, 2, 0], [1, 2, 1], [1, 2, 3]]
    # print(A)
    # print(B)
    # print(check_if_square_length(0, 1, 1, 0, 2))
    print(ans)

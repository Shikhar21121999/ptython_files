

# main function
if __name__ == '__main__':
    test = int(input())
    while (test > 0):
        n, m, k = map(int, input().split(' '))
        A = list(map(int, input().split(' ')))
        B = list(map(int, input().split(' ')))
        C = A+B
        C.sort()
        print(C[k-1])
        test -= 1

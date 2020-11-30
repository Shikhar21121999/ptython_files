
def solve():
    n = int(input())
    if(n == 1):
        return 0

    if(n == 2):
        return 1

    if(n == 3):
        return 2

    # if n is even then there are two steps required
    if(n % 2 == 0):
        return 2

    # if n is odd then there are three steps required
    if(n % 2 == 1):
        return 3


# main function
if __name__ == '__main__':
    test = int(input())
    while(test != 0):
        test -= 1
        print(solve())

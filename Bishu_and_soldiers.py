

def soldier_killed(power):
    global a, n

    # creating prefix sum array of a
    d = [0]*n
    d[0] = a[0]
    for i in range(1, n):
        d[i] = a[i]+d[i-1]

    # print(d)

    # seearch for the index which is just less than or equal to power in a[i]
    index = -1
    for i in range(n):
        if(a[i] <= power):
            index = i

        else:
            break

    if(index < 0):
        print(0, 0)
    else:
        print(index+1, d[index])


# main function
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    no_round = int(input())
    while(no_round > 0):
        power = int(input())
        soldier_killed(power)
        no_round -= 1

def count_bits(a):

    # function to count number of bits in a number

    k = 1
    active_bits = 0
    while(k <= a):
        if(k & a):
            active_bits += 1
        k <<= 1
    return active_bits


def myfunc(e):
    return count_bits(e)


# main function
if __name__ == "__main__":
    lis = list(map(int, input().split()))
    lis.sort(key=lambda e: count_bits(e), reverse=True)
    print(lis)

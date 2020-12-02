def count_bits(a):

    # function to count number of bits in a number

    k = 1
    active_bits = 0
    while(k <= a):
        if(k & a):
            active_bits += 1
        k <<= 1
    return active_bits


# main function
if __name__ == "__main__":
    p = int(input())
    print(count_bits(p))

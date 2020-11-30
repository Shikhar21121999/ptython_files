# main function
def func(inp):
    p_c_i = 0
    print(inp[0], end="")

    for c_c_i in range(1, len(inp)):
        if(inp[c_c_i] != inp[p_c_i]):
            print(inp[c_c_i], end="")
            p_c_i = c_c_i
    print()


if __name__ == '__main__':
    test = int(input())
    # print(test)
    while(test > 0):
        a = input()
        func(a)
        test -= 1

def append(klis):
    print(id(klis))
    for i in range(10, 15):
        klis.append(i)
    print(id(klis))
    return klis


def reasign(lis):
    print(id(lis))
    lis = [4, 5, 6]
    print(id(lis))


def copy(lis):
    print(id(lis))
    klis = lis[:]
    klis[0] = 100
    print(id(klis))


# main function
if __name__ == '__main__':
    lis = [4, 5, 6]
    print(id(lis))
    print(reasign(lis))
    print(lis)
    copy(lis)
    print(lis)

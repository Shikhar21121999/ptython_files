def exp1(arr):
    arr.append(5)


def base(arr):
    print(arr)

    # copy arr
    arr1 = arr[:]

    exp1(arr1)
    print(arr)
    print(arr1)
    arr = arr1
    print(arr)


ini_arr = [1, 2]
base(ini_arr)
print(ini_arr)


def mergeSort(arr):
    # this function makes changes on the same variable or object refrence

    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        # two new objects are created and new variables are created as label for them
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        # call merge sort on newly created variables
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        # after the merge sort L and R get modified such that now L and R are sorted

        i = j = k = 0

        # here we once again modify contents of array as an object
        # as we make changes to the object and not make new object
        # hence changes are made to the object passed (kind of like pass by value)

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    # at the end the passed object or original variable is changed


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [4, 3, 1, 2]
    print("Given array is", end="\n")
    printList(arr)
    # print(id(arr))
    mergeSort(arr)
    # print(id(arr))
    print("Sorted array is: ", end="\n")
    printList(arr)

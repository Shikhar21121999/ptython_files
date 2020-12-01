A = input()
B = input()

# first we check if the occurence of all the characters is same
hash1 = [0]*256
hash2 = [0]*256

# fill the first hash list
for i in A:
    hash1[ord(i)] += 1

# fill the second hash list
for i in B:
    hash2[ord(i)] += 1

# compare the two hash list to see if they are equal

are_equal = True
for i in range(0, 256):
    if(hash1[i] != hash2[i]):
        are_equal = False
        break

if not are_equal:
    print("Not possible")

else:

    i = len(A)-1
    j = len(B)-1
    result = 0
    while(i >= 0):

        # if there is a mismatch then we increement to make character at i == j
        while(A[i] != B[j]):
            i -= 1
            result += 1

        if(A[i] == B[j]):
            i -= 1
            j -= 1

print(result)

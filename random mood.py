# recursive solution for random mood
# time complexity : O(a^n)
def recur(i, j):
    # i,j represent probability of having mood j after ith minutes
    # j has only two values 0 or 1
    global p

    # base case at i==0 and j==1
    if(i == 0 and j == 1):
        return 1

    # recursive case

    # if happy
    if(j == 1):
        return recur(i-1, 1)*(1-p)+recur(i-1, 0)*p

    # if sad
    if(j == 0):
        # probability of sad is 1-probablity of happy
        return 1-recur(i, 1)


# main function
if __name__ == "__main__":
    n = int(input())
    p = float(input())
    print(recur(n, 1))

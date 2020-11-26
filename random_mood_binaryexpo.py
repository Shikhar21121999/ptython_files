

# main function
if __name__ == "__main__":
    n, p = input().split()
    n = int(n)
    p = float(p)
    prob_happy = 1.0

    # we try to find the probability of mood change after n seconds
    # using binary exponentiation
    prob_happy = 1
    while(n > 0):
        if(n & 1):
            prob_happy = prob_happy*(1-p)+(1-prob_happy)*p
        p = p*(1-p)+(1-p)*p
        n = int(n/2)
    print(prob_happy)

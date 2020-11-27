# binary exponenttation solution for string mood
# incorrect solution

# main function
if __name__ == "__main__":
    n = int(input())

    happy = int(1)
    sad = int(0)
    mod = int(10**9+7)
    H_H = 19
    S_H = 6
    H_S = 7
    S_S = 20
    a = 1
    b = 0
    c = 0
    d = 1
    while(n > 0):
        if(n & 1):
            # # we need a temp int to store so that changes are not reflected in sad
            # temp_happy = ((happy*H_H) % mod+(sad*S_H) % mod) % mod
            # temp_sad = ((sad*S_S) % mod+(happy*H_S) % mod) % mod
            # happy = temp_happy
            # sad = temp_sad
            n_a = a*H_H+b*S_H
            n_b = a*H_S+b*S_S
            n_c = c*H_H+d*S_H
            n_d = c*H_S+d*S_S
            a = n_a
            b = n_b
            c = n_c
            d = n_d
        H_H = H_H*H_H+H_S*S_H
        H_S = H_H*H_S+H_S*S_S
        S_H = S_S*S_H+S_H*H_H
        S_S = S_S*S_S+S_H*H_S
        n = int(n/2)

    print(a % mod)

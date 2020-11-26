# iterative solution for string mood

# main function
if __name__ == "__main__":
    n = int(input())

    happy = int(1)
    sad = int(0)
    mod = int(10**9+7)
    for x in range(1, n+1):
        n_h = ((happy*19) % mod+(sad*6) % mod) % mod
        n_s = ((happy*7) % mod+(sad*20) % mod) % mod
        happy = n_h
        sad = n_s

    print(happy)

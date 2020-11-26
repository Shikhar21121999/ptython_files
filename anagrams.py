from collections import defaultdict


# function to print vector of string
def print_vec_str(a):
    for x in a:
        for i in x:
            print(i, end=" ")
        print()


# function to make a vector of string such that each vector of string contains all anagrams
def give_anagrams(strlis):
    # strlis is a list of string

    # we use defaultdict to store list of string corrosponding to a string
    store = defaultdict(lambda: list)

    for curr_str in strlis:
        key_str = ''.join(sorted(curr_str))

        # case if no vector exist corrosponding to this string
        if(key_str not in store):
            # make a vector and link it to this key
            temp_vec = []
            temp_vec.append(curr_str)
            store[key_str] = temp_vec

        else:
            # Push new string to
            # already existing key
            temp_vec = store[key_str]
            temp_vec.append(curr_str)
            store[key_str] = temp_vec

    # we make a vector of vector and put all the anagrams linked to a key string into it
    lis_of_lis = [[]]
    for k, v in store.items():
        lis_of_lis.append(v)

    print(lis_of_lis)


lis_str = ["cat", "dog", "tac", "god", "act"]
give_anagrams(lis_str)

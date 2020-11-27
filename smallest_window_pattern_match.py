def min_length_pattern_match(string, pattern):
    # takes complete string and find the smallest window in which pattern can be found
    n = int(len(string))
    m = int(len(pattern))

    if n < m:
        print("No such window exists")
        return ""

    # first we create a hash map to store the occurences of characters in pattern and string
    hash_str = [0]*256
    hash_pat = [0]*256

    # fill the map for patern
    for i in pattern:
        hash_pat[ord(i)] += 1

    # traverse through the string to get a window
    min_len = 50000000
    start = 0
    start_ind = -1
    count = 0

    # print(string, pattern)

    for i in range(0, n):

        # add the current character to the hash_str
        hash_str[ord(string[i])] += 1

        # if string's character matches with
        # pattern character then increment count
        if(hash_pat[ord(string[i])] != 0 and hash_str[ord(string[i])] <= hash_pat[ord(string[i])]):
            count += 1

        if(count == m):

            # Try to minimize the window i.e., check if
            # any character is occurring more no. of times
            # than its occurrence in pattern, if yes
            # then remove it from starting and also remove
            # the useless characters.

            while(hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):

                if(hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1

            # update window size
            len_window = i-start+1
            if min_len > len_window:

                min_len = len_window
                start_ind = start

    if start_ind == -1:
        print("No such window exists")
        return ""

    # return substring starting from
    # start_ind and length min_len
    return string[start_ind:start_ind + min_len]


# main function
if __name__ == "__main__":

    com_str = input()
    patter_find = input()
    print(min_length_pattern_match(com_str, patter_find))

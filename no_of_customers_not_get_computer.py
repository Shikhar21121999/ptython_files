

# main function
if __name__ == '__main__':

    # number of computers in cafe
    n = int(input())

    # a sequence of upper case characters
    seq = input()

    # hash map to store customers
    recd = [0]*256
    # number of customers currently inside cafe
    curr_cust = 0

    max_cust_went_empty = 0
    for i in seq:
        # print("strt ", curr_cust, recd[ord(i)])

        # case 1 the customer i enters
        if(recd[ord(i)] % 2 == 0):
            curr_cust += 1
            recd[ord(i)] += 1

        elif(recd[ord(i)] % 2 == 1):
            curr_cust -= 1
            recd[ord(i)] -= 1

        # check if curr_customers > n
        if(curr_cust > n):
            max_cust_went_empty = max(curr_cust-n, max_cust_went_empty)

        # print("end", curr_cust, recd[ord(i)])

    if(max_cust_went_empty > 0):
        print(max_cust_went_empty)
    else:
        print(0)

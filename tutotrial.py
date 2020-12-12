# check how to achieve results simmilar to pass by refrence in python

def pass_by_refrence(arr):

    # here arr is an array
    arr.append(5)


arr = [75]
pass_by_refrence(arr)
print(arr)

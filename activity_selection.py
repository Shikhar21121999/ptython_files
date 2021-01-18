'''
Activity selection Problem
'''


# class pair:
#     '''
#     Class to make a pair
#     '''

#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def __repr__(self):
#         return 'Pair(%s, %s)' % (self.first, self.second)

#     # For call to str(). Prints readable form
#     def __str__(self):
#         return '%s + i%s' % (self.first, self.second)


# p1 = pair(4, 5)
# p2 = pair(8, 7)
# print(p1.first+p2.second)

# # make a list of pairs
# lis1 = [1, 2, 3, 4, 5, 6]
# lis2 = [7, 8, 9, 5, 6, 4]
# pair_lis = []
# normal_lis = []
# for i in range(0, len(lis1)):
#     pair_lis.append(pair(lis1[i], lis2[i]))
#     normal_lis.append([lis1[i], lis2[i]])

# print(normal_lis)
# print(pair_lis)
# print(sorted(pair_lis, key=lambda x: x.second, reverse=True))
# print(sorted(normal_lis, key=lambda x: x[1], reverse=True))

# User function Template for python3
def maximumMeetings(n, start, end):
    '''
    Utility funciton to find
    max no of meethings that can be scheduled
    '''
    cnt = 0
    # maka vector of pair representing the start
    # and end time for the meetings

    pl = []
    for i in range(0, len(start)):
        pl.append([start[i], end[i]])

    # sort the pl according to the end time
    pl = sorted(pl, key=lambda x: x[1])

    # now we traverse the sorted vector of pair
    # now count the no of meething that can be picked up
    # one after the other
    last_met_end = -1
    for i in pl:
        if i[0] > last_met_end:
            cnt += 1
            last_met_end = i[1]

    return cnt


# main function
if __name__ == "__main__":
    start_arr = [75250, 50074, 43659, 8931, 11273,
                 27545, 50879, 77924]
    end_arr = [112960, 114515, 81825, 93424, 54316,
               35533, 73383, 160252]
    n = 8
    print(maximumMeetings(n, start_arr, end_arr))

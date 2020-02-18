"""
- start by choosing a pivot (could be first, last, middle, random etc)
- move all of the elements smaller than the pivot to LHS
- move all of the elements larger than the pivot to RHS
- invoke a recursive call to quick sort on LHS and RHS until base case 
    (a side only contains a single element)

[8, 3, 6, 4, 7, 9, 5, 2, 1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

pivot = [8] 
[3, 6, 4, 7, 9, 5, 2, 1]
lhs = [3, 6, 4, 7, 5, 2, 1]
rhs = [9]

[lhs call]
pivot [3] 
[6, 4, 7, 5, 2, 1]
lhs = [2, 1]
rhs = [6, 4, 7, 5]

[lhs2 call]
[2] [1]
lhs = [1]
rhs = []

[rhs2 call]
pivot = [6] 
[4, 7, 5]
lhs = [4,5]
rhs = [7]





[pivot call]
[8]

[rhs call]
[9]





"""

def partition(data):
    # make a new empty list for LHS
    # make a pivot
    # make a new empty list for RHS

    # loop over the data 
        # if lower than or equal to pivot
            # append to LHS list
        # otherwise
            # append to RHS list
    
    # return a tuple containing the LHS list, the pivot, and the RHS list

    pass

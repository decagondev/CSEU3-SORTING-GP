"""
Algorithm
Start with current index = 0

For all indices EXCEPT the last index:

a. Loop through elements on right-hand-side of current index and find the smallest element

b. Swap the element at current index with the smallest element found in above loop
"""

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # set sorted item index to i
        cur_index = i

        # give smallest a sentinal value
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # loop over elements at right hand side of current index (current index + 1)
        # our ranege is the current index to the len of array - 1
        # loop here
        for j in range(cur_index + 1, len(arr)):
            # check if the number current iteration index is smaller than 
            # the number at the smallest index
            # if condition here
            if arr[j] < arr[smallest_index]:
                # if true then set smallest index to iteration index
                smallest_index = j
        
        # swap number at current index for number at smallest index
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # arr[smallest_index], arr[cur_index] = 5, 3


        # arr[smallest_index] = 5
        # arr[cur_index] = 3

        # a, b = 5, 3

    # return the array
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr